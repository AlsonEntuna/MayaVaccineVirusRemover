import os
import sys
from imp import reload
from PySide2 import QtWidgets, QtCore
from virusremover.virus_defs import VIRUS_PYTHON_FILES

dir_path = os.path.dirname(os.path.realpath(__file__))
if dir_path not in sys.path:
    sys.path.append(dir_path)

import maya_window
import maya_utils
import const
import virus_defs
import maya.cmds as cmds
import ui.virus_remover_ui as window

# Reload the modules
reload(maya_window)
reload(maya_utils)
reload(const)
reload(virus_defs)

SCRIPTS_PATH = maya_utils.get_maya_scripts_path()
MAYA_PREFS_PATH = maya_utils.get_maya_prefs_path()

class VirusRemoverWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(VirusRemoverWindow, self).__init__(parent, QtCore.Qt.Window.WindowStaysOnTopHint)

        self.ui = window.Ui_MainWindow()
        self.ui.setupUi(self)

        # Members
        self._maya_version = ''
        self._virus_detected = False
        self._maya_ver_path = ''
        self._virus_files = []

        # Bindings...
        self.ui.btn_scan.clicked.connect(self.scan)
        self.ui.btn_remove_virus.clicked.connect(self.remove_virus)

        # Initializations
        self.init_modules()

    def init_modules(self):
        self._maya_version = cmds.about(version=True)
        self.ui.txtb_results.append('Maya version: %s' % self._maya_version)
        self._maya_ver_path = os.path.join(MAYA_PREFS_PATH, self._maya_version)

    def closeEvent(self, event):
        pass

    @QtCore.Slot()
    def scan(self):
        self._virus_detected = False
        self.ui.txtb_results.clear()
        self.ui.txtb_results.append('Scanning...')

        self.ui.txtb_results.append('<b>Scripts path:</b> %s' % SCRIPTS_PATH)
        user_setup_file = os.path.join(SCRIPTS_PATH, 'userSetup.py')
        self.ui.txtb_results.append('<b>Scanning file</b> >> %s' % user_setup_file)
        
        # Generic userSetup.py
        if os.path.isfile(user_setup_file):
            with open(user_setup_file, 'r') as user_file:
                lines = user_file.readlines()
                for line in lines:
                    self.ui.txtb_results.append('<b>Scanning line</b> >> %s' % line)
                    if line.strip('\n') in virus_defs.VIRUS_LINE_DEFS:
                        self.ui.txtb_results.append('<b style="color:red">Virus found at line:</b> %s' % line)
                        self._virus_detected = True

        # Maya env userSetup.py
        user_maya_file = os.path.join(self._maya_ver_path, 'scripts', 'userSetup.py')
        self.ui.txtb_results.append('<b>Scanning path: </b> >> %s' % user_maya_file)
        if os.path.isfile(user_maya_file):
            with open(user_maya_file, 'r') as user_maya_file:
                lines = user_maya_file.readlines()
                for line in lines:
                    self.ui.txtb_results.append('<b>Scanning line</b> >> %s' % line)
                    if line.strip('\n') in virus_defs.VIRUS_LINE_DEFS:
                        self.ui.txtb_results.append('<b style="color:red">Virus found at line:</b> %s' % line)
                        self._virus_detected = True
                    
        # Check for the virus files even if we don't have the python code in userSetup.py
        
        has_virus_file = self._has_virus_files()
        if not self._virus_detected:
            self._virus_detected = has_virus_file

        self.ui.btn_remove_virus.setEnabled(self._virus_detected)

        if self._virus_detected:
            self.ui.txtb_results.append('<b style="color:red"> Scan complete... VIRUS DETECTED!</b>')
        else:
            self.ui.txtb_results.append('<b style="color:green">Scan complete... ALL CLEARED!</b>')
    
    @QtCore.Slot()
    def remove_virus(self):
        self._remove_virus_code()
        self._delete_virus_files()
        self.ui.txtb_results.append('<b style="color:green">DONE! Your PC is safe!</b>')

    def _remove_virus_code(self):
        user_setup_generic = os.path.join(SCRIPTS_PATH, 'userSetup.py')

        # Generic userSetup.py
        if not os.path.isfile(user_setup_generic):
            return

        with open(user_setup_generic, 'r+') as user_generic_file:
            lines = user_generic_file.readlines()
            user_generic_file.seek(0)
            for line in lines:
                self.ui.txtb_results.append('<b style="color:orange">Removing line</b> >> %s' % line)
                if not line.strip('\n') in virus_defs.VIRUS_LINE_DEFS:
                    user_generic_file.write(line)

            user_generic_file.truncate()
        
        # Maya Version of userSetup.py
        user_setup_cur_maya_env = os.path.join(self._maya_ver_path, 'scripts', 'userSetup.py')
        if not os.path.isfile(user_setup_cur_maya_env):
            return

        with open(user_setup_cur_maya_env, 'r+') as user_file:
            lines = user_file.readlines()
            user_file.seek(0)
            for line in lines:
                self.ui.txtb_results.append('<b style="color:orange"> Removing line </b> >> %s' % line)
                if not line.strip('\n') in virus_defs.VIRUS_LINE_DEFS:
                    user_file.write(line)

            user_file.truncate()

    def _has_virus_files(self):
        # Maya main prefs
        for paths, path_names, file_names in os.walk(SCRIPTS_PATH):
            for f in file_names:
                if f in VIRUS_PYTHON_FILES:
                    self._virus_files.append(os.path.join(SCRIPTS_PATH, f))

        # Maya ver prefs
        maya_ver_scripts_path = os.path.join(self._maya_ver_path, 'scripts')
        for paths, path_names, file_names in os.walk(maya_ver_scripts_path):
            for f in file_names:
                if f in VIRUS_PYTHON_FILES:
                    self.ui.txtb_results.append('<b style="color:red">Virus File Detected</b>: %s' % f)
                    self._virus_files.append(os.path.join(maya_ver_scripts_path, f))

        return len(self._virus_files) > 0

    def _delete_virus_files(self):
        for v in self._virus_files:
            if not os.path.isfile(v):
                continue
            self.ui.txtb_results.append('<b style="color:orange">Deleting Virus File</b>: %s' % v)
            os.remove(v)

        # Clear the list once done
        self._virus_files.clear()

def main():
    window = VirusRemoverWindow(maya_window.get_maya_main_window())
    window.show()
    return window