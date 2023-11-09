import os

os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI

llm = OpenAI(temperature = 0.6)

name = "Who was the first Kenyan President Post independence?"

print (llm(name))