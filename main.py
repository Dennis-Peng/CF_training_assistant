import prob_info_get
import problem_pull
import tag_count

user_name = "SHU-19-PHH"

recent_passed_problems = prob_info_get.submit_problems_info_get(user_name)

print(recent_passed_problems)

tags = tag_count.tag_count_default(recent_passed_problems)

print(tags)

topic_tag = max(tags, key=tags.get)
unsolved = problem_pull.get_unsolved_pid(topic_tag, user_name)
print(topic_tag,len(unsolved))

# for i in unsolved:
#     print(i)
