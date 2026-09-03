import os
import json
import dotenv
# from amemory.jobmap import JobMap
from utils.encode import encode_image
# from amemory.shortmemory import ShortMem
from utils.snapshot import _screen_picture
from configs.model_sys_text import system_text
from openai import OpenAI, APIConnectionError, RateLimitError, APITimeoutError




dotenv.load_dotenv()
key=str(os.getenv("OPENAI_API_KEY"))
client = OpenAI(
    api_key=key
    )
# sm = ShortMem()



with open("configs/models.json", "r") as mc:
    model_conf = json.load(mc)

model_name = model_conf["GPT"]





def openai_response(chat_input="", model_name = model_name, stream=False):
    
    _screen_picture()
    image_f = "logs/snapshot.png"
    base64_image = encode_image(image_f)



    response = client.responses.create(
        model=model_name,
        input=[
            {
                "role": "developer",
                "content": system_text
            },


            # Put short term memory here


            {
                "role": "user",
                "content": [
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}"
                    }
                ]
            },
            {"role":"user","content":chat_input}
        ],
        stream=stream
        )




    model_reply = response.output_text

    with open("logs/response.json", "w") as wr:
        wr.write(model_reply)
