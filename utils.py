from PyPDF2 import PdfReader
from langchain.prompts import PromptTemplate


def output_text(file_PATH, page_number):
    """
    Args:
        file_PATH (str): Path to the PDF file.
        page_number (int): Page number from which to extract text, starting from 0.

    Returns:
        str: The extracted text from the specified page. Returns None if no text could be extracted or if the page doesn't exist.
    """
    with open(file_PATH, "rb") as input:
        reader = PdfReader(input)
        page = reader.pages[page_number]
        text = page.extract_text()

    return text


def output_text_v2(file_PATH):
    """
    Args:
        file_PATH (str): Path to the PDF file.

    Returns:
        str: The concatenated text content from all pages of the PDF.
    """
    output_sum = str()

    with open(file_PATH, "rb") as input:
        reader = PdfReader(input)

        for i in range(len(reader.pages)):
            page = reader.pages[i]
            text = page.extract_text()
            output_sum = output_sum + text

    return output_sum


# prompt_template
def get_prompt(your_prompt, pdf_text):
    """

    Args:
        your_prompt (str): Prompt to enter in LLM
        pdf_text (str): text extracted from pdf

    Returns:
        str: PromptTemplate
    """

    input_prompt = PromptTemplate(
        input_variables=["your_prompt", "pdf_text"],
        template="{your_prompt}\nTEXT:\n{pdf_text}",
    )
    prompt = input_prompt.format(your_prompt=your_prompt, pdf_text=pdf_text)
    print("prompt:")
    print(prompt)
    return prompt
