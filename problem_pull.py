import requests
import json
from prob_info_get import submit_problems_info_get

API_Head = "http://codeforces.com/api/"

def resolve_pid(api_text):
    """
    统计并返回problem list中所有题目的pid
    输出set(pid(str类型),...)
    """
    problems = set()
    print(len(api_text))
    for i in api_text:
        problems.add(i["pid"])
    return problems

def get_all_pid_with_tag(tag):
    """
    返回某类型算法tag的全部题目
    返回list(dict()) [apitext]
    """
    query = "problemset.problems?tags="+tag
    result = requests.get(API_Head + query)
    return json.loads(result.text)

def get_unsolved_pid(tag, username="SHU-19-PHH"):
    """
    返回username未完成的,给定算法tag的题目pid
    返回set(pid(str类型),...)
    """
    submit_result = submit_problems_info_get(username,-1)
    passed_pid = set()
    for i in submit_result:
        passed_pid.add(i["pid"])
    
    all_pid_by_tag = get_all_pid_with_tag(tag)
    all_problems_pid = set()
    for i in all_pid_by_tag["result"]["problems"]:
        all_problems_pid.add(str(i["contestId"])+"-"+str(i["index"]))

    return all_problems_pid-passed_pid

if __name__=="__main__":
    print(get_unsolved_pid("implementation"))
