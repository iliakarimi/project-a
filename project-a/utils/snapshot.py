import Xlib
from termcolor import colored
import pyautogui
import subprocess


def _screen_picture():
    """
    This function just Take an ScreenShot from the Screen
    """

    try:
        pyautogui.screenshot('logs/snapshot.png')
    except Xlib.error.DisplayConnectionError:
        subprocess.call(["xhost", "+"])
        pyautogui.screenshot('logs/snapshot.png')
    except Exception as e:
        raise RuntimeError(f"An Error Happend: {e};\n {colored("------>", "red")} Change to {colored("X11", "blue")} Protocol.")
