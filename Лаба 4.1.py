# TODO решите задачу
import json
def calculate_weighted_sum(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    total = 0.0
    for item in data:
        score = item.get("score", 0.0)
        weight = item.get("weight", 0.0)
        total += score * weight

    return round(total, 3)

result = calculate_weighted_sum('input.json')
print(result)