import os
from ..secret_key import open_api_key

os.environ["OPENAI_API_KEY"] = open_api_key
from langchain.llms import OpenAI

llm = OpenAI(temperature = 0.6)

name = "Who was the first Kenyan President Post independence?"

print (llm(name))