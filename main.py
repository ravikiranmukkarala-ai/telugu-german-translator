from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

prompt = ChatPromptTemplate.from_template(
    "Translate the word '{word}' from Telugu langage to German langage. "
    "Reply with only the German translation."
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"word": "నేను నిన్ను ప్రేమిస్తున్నా"})
print(result)