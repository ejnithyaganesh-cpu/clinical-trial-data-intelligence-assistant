from pathlib import Path

from src.gemini_client import GeminiClient


class RAGAssistant:

    def __init__(self):

        self.docs_folder = Path("docs")

        self.documents = self.load_documents()

        self.gemini = GeminiClient()

    def load_documents(self):

        docs = []

        for file in self.docs_folder.glob("*.md"):

            try:

                content = file.read_text(
                    encoding="utf-8"
                )

                docs.append(
                    {
                        "file_name": file.name,
                        "content": content
                    }
                )

            except Exception:
                pass

        return docs

    def answer_question(
        self,
        question
    ):

        if not self.documents:

            return (
                "No documents found in docs folder."
            )

        question_words = set(
            question.lower().split()
        )

        best_match = None
        best_score = 0

        for doc in self.documents:

            content_words = set(
                doc["content"].lower().split()
            )

            score = len(
                question_words.intersection(
                    content_words
                )
            )

            if score > best_score:

                best_score = score

                best_match = doc

        if best_match is None:

            return (
                "No relevant document found."
            )

        prompt = f"""
You are a Clinical Trial Data Intelligence Assistant.

You have access to the following project document:

DOCUMENT:
{best_match['content']}

QUESTION:
{question}

Instructions:

1. Use the document information whenever relevant.
2. If the document does not contain enough information,
   use your own clinical trial and healthcare knowledge.
3. Prefer document information when available.
4. Give a professional and human-friendly answer.
5. Do not mention file names.
6. Keep answers concise but informative.
"""

        try:

            answer = self.gemini.generate(
                prompt
            )

            return answer

        except Exception as e:

            return f"Gemini Error: {e}"