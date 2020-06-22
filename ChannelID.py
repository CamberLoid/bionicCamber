# 工具拱 - ChatID
# 收到/id时回复
# 测试用途.

import pyrogram
import json

with open("./auth.json","r") as f:
    auth = json.load(f)

telebot = pyrogram.Client(
    session_name = "atCambot",
    bot_token = auth["telegram-bot-token"],
    api_id = auth["telegram-user"]["id"],
    api_hash = auth["telegram-user"]["hash"]
    )

@telebot.on_message(pyrogram.Filters.command(["chatid", "chatid@atCambot"]))
def ChatIDHandler(client:pyrogram.Client, message:pyrogram.Message):
    replyText = "这里是拱拱的工具拱喵. 现在放送Chat相关信息: \nChat ID= {chatID}\nChat type= {chatType}\
        \nFly safely. Cambot out."
    chatID=message.chat.id
    client.send_message(
        reply_to_message_id=message.message_id,
        text=replyText.format(chatID=chatID, chatType=message.chat.type),
        chat_id=message.chat.id)
    pass

telebot.run()
