#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""=================================================
@PROJECT_NAME: agent_example
@File    : cli_main.py
@Author  : virgoo
@Date    : 2024/10/10 16:54
@Function: 
    从0到1实现agent
@Modify History:
         
@Copyright：Copyright(c) 2024-2026. All Rights Reserved
=================================================="""
import time

def agent_execute(query, max_request_time):
    cur_request_time = 0
    chat_history = []
    agent_scrath = ""
    while cur_request_time < max_request_time:
        cur_request_time += 1
        


def main():
    """支持用户的多次需要输入和交互"""
    max_request_time = 10
    while True:
        query = input("请输入您的目标:")
        if query == "exit":
            return
        agent_execute(query, max_request_time=max_request_time)


if __name__=='__main__':
    # input = "请为我制定一个理财计划"
    main()