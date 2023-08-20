import os
from dotenv import load_dotenv
from langchain import OpenAI  # langchain/llms/openai.py
from utils import get_prompt, output_text

load_dotenv()


def main():
    # pdfのpath
    pdf_path = input("Please input pdf path")

    # pdfのテキストを読み込む
    text = output_text(pdf_path, 1)

    # promptの入力
    your_prompt = input("Enter your prompt:")
    prompt = get_prompt(your_prompt, text)

    # llm(default="text-davinci-003")
    llm = OpenAI(temperature=1, openai_api_key=os.getenv("API_KEY"))
    output = llm(prompt)

    print("output:")
    print(output)


if __name__ == "__main__":
    main()
