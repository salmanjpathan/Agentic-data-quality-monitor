import subprocess
import sys

print("\nRunning Data Quality Checks...")

subprocess.run(
    [sys.executable, "quality_checks/generate_dq_results.py"],
    check=True
)

print("\nRunning AI Agent...")

subprocess.run(
    [sys.executable, "agents/langgraph_dq_agent.py"],
    check=True
)

print("\nPipeline Completed Successfully")