import os

ROFI_SCRIPT_DIR = os.path.expanduser('~/.config/rofi/scripts/')

def rofi_script(fname):
    """Get the path of a script in the scripts directory"""
    return os.path.expanduser(ROFI_SCRIPT_DIR + fname)
