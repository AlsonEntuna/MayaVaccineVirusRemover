import sys
import maya.OpenMayaUI as omui
import shiboken2
from PySide2 import QtWidgets

def get_maya_main_window():
    """
    Get the main Maya window as a QtGui.QMainWindow instance
    @return: QtGui.QMainWindow instance of the top level Maya windows
    """

    pointer = omui.MQtUtil.mainWindow()
    if pointer is not None:
        if sys.version_info.major >= 3:
            shiboken2.wrapInstance(int(pointer), QtWidgets.QWidget)
        else:
            return shiboken2.wrapInstance(long(pointer), QtWidgets.QWidget)