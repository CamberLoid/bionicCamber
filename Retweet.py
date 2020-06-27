# bionicCamber/Retweet.py | Retweet 0.11 dev
__botName__ = "bionicCamber/Retweet 0.11 Canary"
# Canary -> 跑在本地上
# Canary以外的 -> 跑在云上
# 下一步: 140字 剪切[80-100切一次?], 媒体转发 

import logging, traceback, json
import pyrogram, tweepy
import api

if __name__ == "__main__":
    with open("./auth.json","r") as f:
        auth = json.load(f)
# Pyrogram auth
telebot = api.telebot
# tweepy auth
tweetapi = api.tweetapi

# Hardcoded properties
chatID = [
    -1001285340742, # Camber's Logistics
    -1001300408563, # Camber's Chatroom
    -1001162197620, # Piggy's Recycle Bin
    -1001171419126  # Piggy's Chatroom
    ]
groupID = -1001300408563 # Camber's Chatroom
# Todo: 自动判断向哪里转发
twprofile = "https://twitter.com/libCamber/status/{id_str}"
botName = __botName__
TWFooter = "\n\n转发自 {fwd_link} | {botName}"

def parser(message:pyrogram.Message, tweetapi:tweepy.API): 
    # 先实现纯文字转发 - 已经实现了
    # 切割
    # 媒体
    _text = None
    _fwdLink = "https://t.me/{chatPreview}{msgID}"
    _medias = []
    # 返回->list. 为了之后的剪切功能而变更
    ret = []
    if(message.text != None): 
        _text = message.text
    elif (message.caption != None):
        _text = message.caption
    if(_text != None):
        if(message.chat.username == None): 
        # _fwdLink/引用链接生成
            # 有用户名的情况
            _fwdLink = _fwdLink.format(
                chatPreview="c/"+str(message.chat.id)[4:]+"/",
                msgID=message.message_id
            )
        else: 
            # 没有用户名的情况
            _fwdLink = _fwdLink.format(
                chatPreview="s/"+message.chat.username+"?before=",
                msgID=message.message_id
            )
        _text += TWFooter.format(fwd_link=_fwdLink, botName=botName)
    ret.append(tweetapi.update_status(
        tweet_mode = "extended",
        status = _text).id_str)
    return ret

# Handler
@telebot.on_message(pyrogram.Filters.command(["retweet", "retweet@atCambot"]))
def Forward_to_Twitter(client:pyrogram.Client, message:pyrogram.Message):
    logging.warn("Recieved message "+str(message.chat.id)+" "+str(message.message_id))
    fwd_id = None
    replyID = None
    messageToBeSend = {}
    _completeMessage = "转发完成喵~~\nURL:\n{urls}\nFrom {botName}"
    _urls = []
    if(message.chat.id not in chatID):
        logging.warn(botName + " 接收到非法请求")
        message.reply("400 Bad Request\nFrom " + botName,
            reply_to_message_id=message.message_id)
        return
    if(message.reply_to_message != None):
        fwd_id = message.reply_to_message.message_id
        # Parsing and forwarding
        _id_str = parser(message=message.reply_to_message,tweetapi=tweetapi)
        # Delete command message
        message.delete()
        #telebot.delete_messages(message.chat.id,message.message_id)
        # Forward complete message
        telebot.send_message(
            chat_id=groupID,
            text=_completeMessage.format(
                urls=twprofile.format(id_str=_id_str[0]), 
                botName=botName))
        pass
    if(message.reply_to_message == None):
        telebot.send_message(
            reply_to_message_id=message.message_id,
            chat_id=groupID, 
            text="拱拱(也有可能是猪猪)刚才对着空气回复了!\nTwitter不能转发空气!!!")
    pass

if(__name__=="__main__"):
    telebot.run()
