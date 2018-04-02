# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    一个微信机器人程序

    微信客户端itchat:
        http://itchat.readthedocs.io/
    机器人聚合API：
        ## params
        - info 发给机器人的信息
        - dtype json|xml
        - loc 地点
        - userid 1-32位，可以用于上下文关联

        http://op.juhe.cn/robot/index?info=%E5%8C%97%E4%BA%AC&dtype=&loc=&userid=1&key=978f281744b2cda30642dbbaf3eb8349

"""

import itchat
import requests

applyMsg = {
    'eat': 'an apple',
    'sleep': 'hoo,hoo'
}
def xiao_ai(say, user_id):
    '''调用聚合机器人接口实现自动回复，逻辑层次可以在这里面加'''
    if applyMsg.get(say, None):
        return applyMsg[say]
    url = 'http://www.tuling123.com/openapi/api'
    params = {
        'info' : say,
        'userid' : user_id,
        'key' : '978f281744b2cda30642dbbaf3eb8349'
    }
    config = {
        'key': '621547baa4ea4080bfd4e0ce655ea62f',
        'info': say,
        'userid': user_id
    }
    r = requests.post(url, data=config)
    data = r.json()
    # print data
    if data['code'] != 100000:
        return 'xiaoai病了，过会再问吧'

    # result = data['result']
    text = data['text']
    # url = result.get('url', '')

    # recv = text + url
    # print text
    return text

@itchat.msg_register(itchat.content.TEXT)
def recv_content(msg):
    say = msg['Text']
    user_id = msg.get('FromUserName', '@0') # 获取用户ID
    print say, user_id;
    result = xiao_ai(say, user_id);
    print result
    return result
    itchat.send(result) # call xiaoai

if __name__ == '__main__':
    # itchat.auto_login(enableCmdQR=2) # hotReload=True
    itchat.auto_login(hotReload=True)
    itchat.run()