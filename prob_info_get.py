import requests
import json
import time
import datetime

API_Head = "http://codeforces.com/api/"

def get_api_by_name(usr_name="SHU-19-PHH", count=100):
    """
    根据用户名得到其最近的count条提交记录
    输入: usr_name: 用户名, count: 查询记录数(<=0为全部查询)
    输出: 提交记录api_text
    """
    query = "user.status?handle=" + usr_name + "&from=1"
    if count >= 0:
        query = query + "&count=" + str(count)
    result = requests.get(API_Head + query)
    return json.loads(result.text)

def resolve_api(api):
    """
    解析user.status下返回的过题记录[只返回过题的记录]
    输入: request.get得到的返回内容(输入保证status=="OK")
    输出: list of dict, {"pid":比赛id+题号, "tags":该题的算法tag , "rating":该题的难度分数,不存在为-1}
    """
    info = []
    for i in api['result']:
        if i["verdict"] == "OK":
            pid = str(i["problem"]["contestId"])+"-"+str(i["problem"]["index"])
            tags = i["problem"]["tags"]
            if "rating" in i["problem"]:
                rating = i["problem"]["rating"]
            else:
                rating = -1

            submit_time_str = time.localtime(i["creationTimeSeconds"])
            time_submit = datetime.datetime(submit_time_str.tm_year, submit_time_str.tm_mon, submit_time_str.tm_mday)
            time_now = datetime.datetime.now()
            day_count_from_submit = (time_now-time_submit).days

            info.append({"pid": pid,
                         "tags": tags,
                         "rating": rating,
                         "daypassed": day_count_from_submit})
    return info


def submit_problems_info_get(username="SHU-19-PHH", tracecount=100):
    api_text = get_api_by_name(username,tracecount)
    if api_text["status"]=="OK":
        result = resolve_api(api_text)
        return result

if __name__ == "__main__":
    print(submit_problems_info_get())
