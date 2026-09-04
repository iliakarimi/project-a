import os
import json
import dotenv
# from amemory.jobmap import JobMap
# from amemory.shortmemory import ShortMem
from configs.model_sys_text import system_text
from openai import OpenAI, APIConnectionError, RateLimitError, APITimeoutError


dotenv.load_dotenv()
key=str(os.getenv("OPENAI_API_KEY"))
client = OpenAI(
    api_key=key
    )


with open("configs/models.json", "r") as mc:
    model_conf = json.load(mc)

model_name = model_conf["GPT"]


def openai_response(chat_input="", model_name = model_name, stream=False):

    response = client.responses.create(
        model=model_name,
        input=chat_input,
        stream=stream
        )

    model_reply = response.output_text

    with open("logs/response.json", "w") as wr:
        wr.write(model_reply)
