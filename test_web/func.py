# #!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time   :2020/12/21 5:45 下午
# @Author :Amaris
# @File   :func.py
import random
import string


def username():
    username = "".join(random.sample(string.ascii_letters, 8))
    username = "测试"+username
    return username

def memberAdd_acctid():
    memberAdd_acctid = "".join(random.sample(string.ascii_letters, 8))
    memberAdd_acctid = "test"+memberAdd_acctid
    return memberAdd_acctid

def memberAdd_phone():
    memberAdd_phone = "".join(random.sample(string.digits, 10))
    memberAdd_phone = "1"+memberAdd_phone
    return memberAdd_phone


if __name__ == '__main__':
    username = username()
    print(username)
    memberAdd_acctid = memberAdd_acctid()
    print(memberAdd_acctid)
    memberAdd_phone = memberAdd_phone()
    print(memberAdd_phone)

