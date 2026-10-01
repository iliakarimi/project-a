import pyautogui as pyagui


def _correct_resolution():
    '''
    This function get real resolution:\n
    (x-1)(y-1)=CR
    '''
    swidth = pyagui.resolution().width
    sheight = pyagui.resolution().height

    return f"{swidth-1}" + "*" + f"{sheight-1}"
