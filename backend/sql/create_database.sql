CREATE DATABASE IF NOT EXISTS cf_assistant;

/*
用户基本信息
主键：用户id
*/
CREATE TABLE IF NOT EXISTS database.users(
    uid     SERIAL      NOT NULL,   --系统内用户id
    name    TEXT        NOT NULL,   --系统内用户名
    passwd  char(16)    NOT NULL,   --用户密码的md5值
    cf_name TEXT        NOT NULL,   --用户绑定的codeforces用户名
    PRIMARY KEY (uid)
);

/*
用户做题的偏好
推荐题目需要的信息
上次生成推荐题时选择的tag，和Rating区间
主键：用户id(外键->user.id)
*/
CREATE TABLE IF NOT EXISTS IF NOT EXISTS database.preferences(
    uid     INT         NOT NULL,   --用户id
    rating  INT,                    --用户当前的rating
    lb_rt   INT,                    --用户偏好的rating区间下限
    ub_rt   INT,                    --用户偏好的rating区间上限
    tags    BIT(40),                --用户喜好的codeforces上题目的tag
    PRIMARY KEY (uid),
    CONSTRAINT fk_users
        FOREIGN KEY (uid)
            REFERENCES users(uid)
);

/*
用户做题偏好中tags各bit位(id)和算法tag的对应关系
系统初始化/安装时更新一次
之后每2天更新一次(拉取所有的题目，扫描一遍所有的tag，更新不存在的tag的tid)
当用户发现找不到tag时更新一次(?具体逻辑还未想清楚)
*/
CREATE TABLE database.tags(
    tagid   SERIAL      NOT NULL,   --codeforces上题目算法tag的id
    tag     TEXT        NOT NULL,   --codeforces上题目算法的tag
    PRIMARY KEY (tagid)
);