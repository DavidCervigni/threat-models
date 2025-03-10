import unittest
from langchain_openai import OpenAIEmbeddings

class TestOpenAIEmbeddings(unittest.TestCase):

    def setUp(self):
        self.embeddings_model = OpenAIEmbeddings()

    def test_embed_documents(self):
        documents = [
            "Hi there!",
            "Oh, hello!",
            "What's your name?",
            "My friends call me World",
            "Hello World!"
        ]
        embeddings = self.embeddings_model.embed_documents(documents)
        self.assertEqual(len(embeddings), 5)
        self.assertEqual(len(embeddings[0]), 1536)

    def test_embed_query(self):
        query_embedding = self.embeddings_model.embed_query("What is the meaning of life?")
        self.assertEqual(len(query_embedding), 1536)

if __name__ == '__main__':
    unittest.main()