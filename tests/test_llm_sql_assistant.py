import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from src.llm_sql_assistant import (
    LLMSQLAssistant
)

assistant = LLMSQLAssistant()

response = assistant.ask(
    "show me risk scores"
)

print("\nRESULT")
print(response["result"])

print("\nEXPLANATION")
print(response["explanation"])