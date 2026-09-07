#Configure User information and Operating System Platform
import json
import readline
import platform
import termcolor
from utils.correct_resolution import _correct_resolution
from textfx import typeeffect
from utils.clear import cleart


cleart()


with open("configs/user_config.json", "r") as l:
    user_conf = json.load(l)

get_os = platform.system()


def main():
    if user_conf["user_name"] == "None" and user_conf["os"] == "None" and user_conf["agent_name"] == "None":
        
        typeeffect("Welcome To Viora Configuration\n", delay=0.06)
        typeeffect("Please enter your name: ", delay=0.06)
        get_name = str(input())
        user_conf["user_name"] = get_name

        typeeffect("Please enter your Agent name: ", delay=0.06)
        get_agent_name = str(input())
        user_conf["agent_name"] = get_agent_name

        print("Get OS Platform...")

        user_conf["os"] = get_os
        user_conf["screen_size"] = _correct_resolution()

        with open("configs/user_config.json", "w") as w:
            json.dump(user_conf, w)

    elif user_conf["user_name"] is not None and user_conf["os"] is not None:    
        typeeffect("You already have Configured your Information.\n", delay=0.06)
        typeeffect("Do you Want to change your information (y / yes, n / no): ", delay=0.06)
        
        user_awnser = str(input())

        loop_t = True
        while loop_t:
            if user_awnser.lower() in ("y", "Y", "yes"):
                typeeffect("Please Enter your new Name: ", delay=0.06)
                get_new_name = str(input())
                user_conf["user_name"] = get_new_name

                typeeffect("Please Enter your new Name: ", delay=0.06)
                get_new_agent_name = str(input())
                user_conf["agent_name"] = get_new_agent_name

                user_conf["os"] = get_os
                user_conf["screen_size"] = _correct_resolution()

                with open("configs/user_config.json", "w") as wn:
                    json.dump(user_conf, wn)
                loop_t = False

            elif user_awnser.lower() in ("n", "N", "no"):
                print("OK!")
                loop_t = False            
            else:
                user_awnser = str(input("Type (y / yes , n / no): "))



if __name__ == "__main__":
    try:
        main()
        typeeffect("You can Now Using Viora by Typing:\n\n")
        print(termcolor.colored("python chat.py", color="yellow"))
        
    except Exception as e:
        print("\nAn unexpected error occurred. Please try again. If the problem persists, open issue on GitHub.")
        print(e)
