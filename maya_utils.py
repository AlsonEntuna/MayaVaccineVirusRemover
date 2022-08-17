import os

MAYA_PREFS_PATH = 'maya'

def get_maya_prefs_path():
    docs_path = os.path.expanduser('~')
    return os.path.join(os.path.realpath(docs_path), MAYA_PREFS_PATH)

def get_maya_scripts_path():
    docs_path = os.path.expanduser('~')
    return os.path.join(os.path.realpath(docs_path), 'maya', 'scripts')