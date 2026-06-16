import json
from typing import TypedDict

from langchain_ollama import OllamaLLM
from langgraph.graph import StateGraph, END

# Load LLM
llm = OllamaLLM(model="llama3.2")


# Agent State
class DQState(TypedDict):
    dq_data: str
    severity: str
    report: str
    alert: str


# Node 1 - Severity Detection
def classify_severity(state):

    dq_text = state["dq_data"]

    total_issues = 0

    for line in dq_text.split("\n"):
        count = int(line.split(":")[1].strip())
        total_issues += count

    if total_issues >= 3:
        severity = "HIGH"
    elif total_issues >= 1:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    return {
        **state,
        "severity": severity
    }


# Node 2 - AI Report Generation
def generate_report(state):

    prompt = f"""
    You are a Senior Data Quality Analyst.

    Severity Level: {state['severity']}

    Analyze:

    {state['dq_data']}

    Provide:
    - Executive Summary
    - Business Impact
    - Recommended Actions
    """

    response = llm.invoke(prompt)

    return {
        **state,
        "report": response
    }
def generate_alert(state):

    if state["severity"] == "HIGH":

        alert = """
ALERT STATUS: TRIGGERED

High severity data quality issues detected.

Immediate investigation required.
"""

    else:

        alert = """
ALERT STATUS: NORMAL

No critical data quality issues detected.
"""

    return {
        **state,
        "alert": alert
    }

# Build Workflow
graph = StateGraph(DQState)

graph.add_node("classify", classify_severity)
graph.add_node("generate_report", generate_report)
graph.add_node("alert", generate_alert)

graph.set_entry_point("classify")

graph.add_edge("classify", "generate_report")
graph.add_edge("generate_report", "alert")
graph.add_edge("alert", END)
app = graph.compile()

# Read DQ Results
with open("data/dq_results.json") as f:
    dq = json.load(f)

dq_text = "\n".join(
    [f"{k}: {v}" for k, v in dq.items()]
)

result = app.invoke({
    "dq_data": dq_text,
    "severity": "",
    "report": "",
    "alert": ""
})

print("\n")
print("=" * 60)
print("SEVERITY:", result["severity"])
print("=" * 60)
print(result["report"])

print("\n")
print("=" * 60)
print("ALERT")
print("=" * 60)
print(result["alert"])