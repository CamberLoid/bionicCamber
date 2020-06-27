# bionicCamber/chatID.py | 0.9 pre-Stable
# 收到/chatid时回复
# 测试用途.

import pyrogram
import json, logging
import api

telebot = api.telebot

@telebot.on_message(pyrogram.Filters.command(["chatid", "chatid@"+telebot.get_me().username]))
def ChatIDHandler(client:pyrogram.Client, message:pyrogram.Message):
    logging.warn("/Chatid recieved at " + str(message.chat.id))
    replyText = "这里是拱拱的工具拱喵. 现在放送Chat相关信息: \
    \nChat ID= {chatID}\
    \nChat type= {chatType}\
    \nAdditional Properties= {additional}\
    \n本命令作为Debug用, 这说明了仿生拱拱的网络功能一切正常.\
    \nFrom bionicCamber/ChannelID 0.9 pre-stable"
    chatID=message.chat.id
    client.send_message(
        reply_to_message_id=message.message_id,
        text=replyText.format(chatID=chatID, chatType=message.chat.type, additional=None),
        chat_id=message.chat.id)
    pass

if(__name__=="__main__"):
    telebot.run()