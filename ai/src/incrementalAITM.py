from m6rclib import MetaphorParser, format_ast
from langchain_core.messages import HumanMessage
from langchain.chat_models import init_chat_model

import getpass
import os
import argparse

def main():
    # Create a parser instance
 

    # Parse the input with search paths for Include: directives
    arg_parser = argparse.ArgumentParser(description="Process a Metaphor file.")
    arg_parser.add_argument("-m6r", dest="file_path", required=True, help="Path to the .m6r file")
    

    arg_parser.add_argument("-i", "--includePath", dest="include_path", required=False, help="Path to include files", default=".")
    arg_parser.add_argument("-e", "--embedPath", dest="embed_path", required=False, help="Path to embed files", default=".")
    args = arg_parser.parse_args()

    includePath = args.include_path
    embedPath = args.embed_path
    file_path = args.file_path


    # Setup openAI

    if not os.environ.get("OPENAI_API_KEY"):
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

    model = init_chat_model("gpt-4o-mini", model_provider="openai")

    parser = MetaphorParser()

    syntax_tree = parser.parse_file(file_path, search_paths=[includePath], embed_path=embedPath)
    
    prompt = format_ast(syntax_tree)

    messages = [
        HumanMessage(prompt),
    ]

    # model.invoke(messages)

    for token in model.stream(messages):
        print(token.content, end="")



if __name__ == "__main__":
    main()