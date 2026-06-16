import json

dq_results = {
    "Null Names": 1,
    "Duplicate Records": 1,
    "Invalid Ages": 2
}

with open("data/dq_results.json", "w") as f:
    json.dump(dq_results, f, indent=4)

print("DQ Results Generated")