def tag_count_default(submit_problem_info):
    tag_val = {}
    for i in submit_problem_info:
        for j in i["tags"]:
            if j in tag_val:
                tag_val[j]=tag_val[j]+1
            else:
                tag_val[j]=1
    return tag_val
