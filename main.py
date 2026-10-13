import gradio as gr
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

prompt = ChatPromptTemplate.from_template(
    "Translate the text '{word}' from Telugu language to German language. "
    "Reply with only the German translation."
)

parser = StrOutputParser()

chain = prompt | model | parser


def translate(text):
    if not text.strip():
        return "Please enter some Telugu text."
    return chain.invoke({"word": text})


demo = gr.Interface(
    fn=translate,
    inputs=gr.Textbox(label="Telugu text", lines=2),
    outputs=gr.Textbox(label="German translation"),
    title="Telugu to German Translator",
    description="Type Telugu text and get the German translation.",
)

if __name__ == "__main__":
    demo.launch()