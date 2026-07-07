import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.rag_assistant import (
    RAGAssistant
)

rag = RAGAssistant()

response = rag.answer_question(
    "What is an enrollment KPI?"
)

print(response)