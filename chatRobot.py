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
import random
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

applyMsg = {
    'doutu': 'pictures\{}.jpg'.format(random.randint(0, 50)),
    'sleep': 'hoo,hoo'
}


def next_topic():
    """
        聊天机器人无法获取回复时的备用回复
        """

    return random.choice((
        '换个话题吧',
        '聊点别的吧',
        '下一个话题吧',
        '无言以对呢',
        '这话我接不了呢'
    ))


def xiao_ai(say, user_id):
    '''调用聚合机器人接口实现自动回复，逻辑层次可以在这里面加'''
    if applyMsg.get(say, None):
        return applyMsg[say]
    url = 'http://www.tuling123.com/openapi/api'
    config = {
        'key': '621547baa4ea4080bfd4e0ce655ea62f',
        'info': say,
        'userid': user_id
    }
    r = requests.post(url, data=config)
    data = r.json()
    ret = str()
    print data
    # """ 文本类 """
    if data.get('code') >= 100000:
        text = data.get('text')
        if not text or (text == say and len(text) > 3):
            text = next_topic()
        url = data.get('url')
        items = data.get('list', list())

        ret += str(text)
        if url:
            ret += '\n{}'.format(url)
        for item in items:
            ret += '\n\n{}\n{}'.format(
                item.get('article') or item.get('name'),
                item.get('detailurl')
            )
    else:
        ret += next_topic()
    print ret
    # text = data['text']
    return ret

# 群聊@后，回应
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def recv_content(msg):
    say = msg['Content']
    user_id = msg.get('FromUserName', '@0')  # 获取用户ID
    print msg
    if (msg.isAt):
        result = xiao_ai(say, user_id);
        itchat.send(u'@%s\u2005: %s' % (msg['ActualNickName'], result), msg['FromUserName'])
        user = itchat.search_chatrooms(userName=user_id)
        print user
        print result

# 好友回应
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def friend_content(msg):
    say = msg['Content']
    user_id = msg.get('FromUserName', '@0')
    print say, user_id
    result = xiao_ai(say, user_id)
    if msg.get('MsgType') == 3:
        print msg.get('MsgId')
        itchat.send_image('pictures\{}.jpg'.format(random.randint(0, 30)), msg['FromUserName'])
    itchat.send(result, msg['FromUserName'])

#日常斗图，群聊和好友
@itchat.msg_register(itchat.content.PICTURE, isFriendChat=True, isGroupChat=True)
def friend_content(msg):
    print msg
    print msg.get('MsgId')
    img = 'pictures{}.jpg'.format(random.randint(0, 30))
    itchat.send_image(img, msg['FromUserName'])


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2,hotReload=True) # hotReload=True
    itchat.run()
