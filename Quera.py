import json
import pandas

excel_data_fragment = pandas.read_excel('records.xlsx', sheet_name='Sheet')

data = json.loads(excel_data_fragment.to_json())

problems_count = len(data) // 5

total_score = int(input())

result = {}
for i in range(1, len(data['Unnamed: 1'])):
    index = str(i)
    if data['Unnamed: 1'][index] is None or len(data['Unnamed: 1'][index]) != 10:
        continue
    result[data['Unnamed: 1'][index]] = {"problemResults": [], "total_points": 0}
    for j in range(5, len(data), 5):
        score = 0
        if data['Unnamed: ' + str(j)][index] is not None and data['Unnamed: ' + str(j)][index].isnumeric():
            score = int(data['Unnamed: ' + str(j)][index])
        result[data['Unnamed: 1'][index]]["problemResults"].append(score)
        result[data['Unnamed: 1'][index]]["total_points"] += score


output = {k: v for k, v in sorted(result.items(), key=lambda item: (-item[1]['total_points']))}

last_user = None
last_ans = 1
ans = 1
for user in output:
    if last_user is None or output[last_user]['total_points'] > output[user]['total_points']:
        last_ans = ans
    last_user = user
    output[user]['rank'] = last_ans
    ans += 1
print(output)
