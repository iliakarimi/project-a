import json
import readline
from utils.clear import cleart
from gpt import openai_response
# from speech.tts import main_tts
from utils.encode import encode_image
from utils.snapshot import _screen_picture
from tools.action import ComputerControl as cc
from configs.model_sys_text import system_text
from amemory.shortmemory import ShortMem, GoalsMem


sm = ShortMem()
gm = GoalsMem()


def run_agent():

    sm.store_messages(role="developer", message=system_text)

    while True:
        user_input = str(input("You: "))
        sm.store_messages(role="user", message=user_input)

        _screen_picture()
        image_f = "logs/snapshot.png"
        base64_image = encode_image(image_f)
        sm.add_image(image=f"data:image/jpeg;base64,{base64_image}")


        res = openai_response(
            chat_input=sm.remind_messages(),
            stream=False
        )

        res
        

        with open("logs/response.json", "r") as rr:
            response_data = json.load(rr)

        final_response = f"{json.dumps(response_data["response"])}"

        sm.store_messages(role="assistant", message=final_response)

        with open("logs/memorylog.json", "w") as f:
            f.write(json.dumps(sm.remind_messages()))

        print(sm.remind_messages())
        print(len(sm.remind_messages()))
        print(f"Viora: {final_response}")
        # main_tts(final_response)

        action = False
        if response_data["control_action"] == "True":

            action = True

            while action:

                openai_response()

                print(f"Viora: {final_response}")
                # main_tts(final_response)
                
                key_word = response_data.get("key", "")
                times_word = response_data.get("times", "")
                write_key = response_data.get("write", "")
                firsthkey_word = response_data.get("firsthkey", "")
                sechkey_word = response_data.get("sechkey", "")
                hotkey_word = response_data.get("hotkey", "")
                movex_mouse = response_data.get("movex", "")
                movey_mouse = response_data.get("movey", "")
                click_button_mouse = response_data.get("click_button", "")
                click_times_mouse = response_data.get("click_times", "")
                scroll_mouse = response_data.get("scroll", "")

                cc.keyboard_control(
                    key= key_word,
                    key_times= times_word,
                    write= write_key,
                    firsthkey= firsthkey_word,
                    sechkey= sechkey_word,
                    hotkey= hotkey_word
                )
                cc.mouse_control(
                    movex=movex_mouse,
                    movey=movey_mouse,
                    click_button=click_button_mouse,
                    click_times=click_times_mouse,
                    scroll=scroll_mouse
                )

        else:
            action = False


def main():
    # try:
    run_agent()
    if Exception:
        with open("logs/memorylog.json", "w") as f:
            f.write(json.dumps(sm.remind_messages()))


if __name__ == "__main__":
    try:
        cleart()

        print("════════════════════════════════════════")
        print("       |  Project-A Alpha 0.1  |        ")
        print("════════════════════════════════════════")
        print("        For Quit press Ctrl+C         \n")

        main()
    
    except KeyboardInterrupt:
        print("\nQuiting Project-A.")

    # except Exception:
    #     with open("logs/memorylog.json", "w") as f:
    #         f.write(json.dumps(sm.remind_messages()))
