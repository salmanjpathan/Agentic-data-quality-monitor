import json
from langchain_ollama import OllamaLLM

# Load DQ Results
with open("data/dq_results.json", "r") as f:
    dq_results = json.load(f)

# Convert JSON to text
report_text = "\n".join(
    [f"{key}: {value}" for key, value in dq_results.items()]
)

# Load LLM
llm = OllamaLLM(model="llama3.2")

prompt = f"""
You are a Senior Data Quality Analyst.

Analyze these data quality issues:

{report_text}

Provide:

1. Executive Summary
2. Business Impact
3. Recommended Actions

Keep response professional.
"""

response = llm.invoke(prompt)

print("\n")
print("=" * 60)
print("AI DATA QUALITY REPORT")
print("=" * 60)
print(response)