import sys
import os


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        # base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        # base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
