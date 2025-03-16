from m6rclib import MetaphorParser, format_ast
from langchain_core.messages import HumanMessage
from langchain.chat_models import init_chat_model
from langchain.document_loaders import PyPDFLoader

import getpass
import os
import argparse
import tempfile

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using PyPDFLoader.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        str: The extracted text.
    """
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    text = " ".join([doc.page_content for doc in documents])
    return text

def extract_texts_from_directory(extract_text_dir):
    """
    Extracts text from all files in a directory.

    Args:
        extract_text_dir (str): The path to the directory.

    Returns:
        dict: A dictionary with filenames as keys and extracted text as values.
    """
    texts = {}
    for filename in os.listdir(extract_text_dir):
        file_path = os.path.join(extract_text_dir, filename)
        if os.path.isfile(file_path):
            if filename.lower().endswith('.pdf'):
                texts[filename] = extract_text_from_pdf(file_path)
            else:
                with open(file_path, 'r') as file:
                    texts[filename] = file.read()
    return texts

def main():
    # Create a parser instance
    arg_parser = argparse.ArgumentParser(description="Process a Metaphor file.")
    arg_parser.add_argument("-m6r", dest="file_path", required=True, help="Path to the .m6r file")
    arg_parser.add_argument("-i", "--includePath", dest="include_path", required=False, help="Path to include files", default=".")
    arg_parser.add_argument("-e", "--embedPath", dest="embed_path", required=False, help="Path to embed files", default=".")
    arg_parser.add_argument("-d", "--extractTextDir", dest="extract_text_dir", required=False, help="Path to directory containing files to extract text from")
    arg_parser.add_argument("-b", "--buildDir", dest="build_dir", required=False, help="Path to build directory", default="build")
    args = arg_parser.parse_args()

    includePath = args.include_path
    embedPath = args.embed_path
    file_path = args.file_path
    extract_text_dir = args.extract_text_dir
    build_dir = args.build_dir

    # Create build directory if it doesn't exist
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    # Create a temporary directory inside the build directory
    temp_dir = tempfile.mkdtemp(dir=build_dir)

    # Setup OpenAI
    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

    # model = init_chat_model("gpt-4o-mini", model_provider="openai")
    model = init_chat_model("o3-mini-high", model_provider="openai")


    # if extract_text_dir:
    #     texts = extract_texts_from_directory(extract_text_dir)
    #     for filename, text in texts.items():
    #         print(f"\n\nExtracted text from {filename}:\n{text}\n")

    #         # Write the extracted text to a file
    #         extracted_file_path = os.path.join(temp_dir, f"extracted_{filename}.txt")
    #         with open(extracted_file_path, "w") as f:
    #             f.write(text)


    parser = MetaphorParser()

    syntax_tree = parser.parse_file(file_path, search_paths=[includePath], embed_path=embedPath)
    
    prompt = format_ast(syntax_tree)

    # Write the prompt to a file
    prompt_file_path = os.path.join(temp_dir, "final_prompt.txt")
    print(f"final promt {prompt_file_path}")
    with open(prompt_file_path, "w") as f:
        f.write(prompt)



    # messages = [
    #     HumanMessage(prompt),
    # ]

    # # model.invoke(messages)

    # for token in model.stream(messages):
    #     print(token.content, end="")



if __name__ == "__main__":
    main()