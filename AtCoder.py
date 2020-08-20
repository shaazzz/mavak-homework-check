# sample input:
# RuinerWorm null_nerd
# 80 120
'''
mikaeel RuinerWorm null_nerd reza
abc080_a abc090_a abc095_a abc090_a abc096_a
100
'''
import urllib.parse
import urllib.request
from os import system, name

users = input().split()
problem_ids = input().split()
total_score = int(input())
problem_score = total_score / len(problem_ids)
output = {}

total_pages = len(problem_ids) * len(users)
page_id = 0


def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


for user in users:
    output[user] = {"problemResult": []}
    sum_score = 0
    for problem_id in problem_ids:
        clear_screen()
        page_id += 1
        print(str(page_id * 100 / total_pages) + "%")
        contest_id = problem_id.split('_')[0]
        url = 'https://atcoder.jp/contests/' + contest_id + '/submissions?f.Task=' + problem_id + '&f.Language=&f.Status=AC&f.User=' + user
        response = urllib.request.urlopen(url)
        webContent = response.read()
        result = webContent.decode("utf-8").find('class="text-right submission-score"')
        if result != -1:
            sum_score += problem_score
            output[user]["problemResult"].append(problem_score)
        else:
            output[user]["problemResult"].append(0)
    output[user]["total_points"] = sum_score

output = {k: v for k, v in sorted(output.items(), key=lambda item: (-item[1]['total_points']))}

last_user = None
last_ans = 1
ans = 1
for user in output:
    if last_user is None or output[last_user]['total_points'] > output[user]['total_points']:
        last_ans = ans
    last_user = user
    output[user]['rank'] = last_ans
    ans += 1
clear_screen()
print(output)
