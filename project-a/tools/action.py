import pyautogui as pg



class ComputerControl():
    
    """
    ## Control Computer
    """

    @classmethod
    def keyboard_control(
                cls, key= "", key_times=1, write= "",
                firsthkey= "", sechkey= "", hotkey= "",
            ):

        if write != "None" or write != "":
            pg.write(write)

        if key != "None" or key != "":
            pg.press(key, presses=int(key_times) if key_times else 0)

        if hotkey != "None" or hotkey !="":
            keys = hotkey.split('+')
            pg.hotkey(*keys)

        if firsthkey and sechkey != "None" or firsthkey and sechkey != "":
            with pg.hold(firsthkey):
                pg.press(sechkey)



    @classmethod
    def mouse_control(
                cls, movex=None, movey=None, 
                click_button=None, click_times=0, scroll=0
            ):
        
        if movex or movey != None or movex or movey != 0:
            try:
                pg.moveTo(x=movex, y=movey)
                
            except Exception as e:
                return f"Error: {e}"

        if click_button:
            try:
                pg.click(button=click_button, clicks=click_times)

            except Exception as e:
                return f"Error: {e}"

        if scroll:
            try:
                pg.vscroll(clicks=scroll)

            except Exception as e:
                return f"Error: {e}"
