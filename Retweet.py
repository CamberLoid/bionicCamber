# Bionic Camber Retweet 1.0

import logging, traceback
import pyrogram, tweepy
import json

with open("./auth.json","r") as f:
    auth = json.load(f)

# Pyrogram auth / Not worked yet
telebot = pyrogram.Client(
    session_name = ":memory:",
    bot_token = auth["telegram-bot-token"],
    api_id = auth["telegram-user"]["id"],
    api_hash = auth["telegram-user"]["hash"],
    )

# tweepy auth / Worked
tweetauth = tweepy.OAuthHandler(
    auth["twitter"]["consumer_key"], 
    auth["twitter"]["consumer_secret"])
tweetauth.set_access_token(
    auth["twitter"]["access_token"], 
    auth["twitter"]["access_secret"])
tweetapi = tweepy.API(tweetauth)

# Hardcoded properties
chatID = [-1001285340742,-1001300408563]
groupID = -1001300408563
twprofile = "https://twitter.com/libCamber/status/{id_str}"
botName = "Bionic Camber Retweet 0.1 dev"
TWFooter = "\n\n由仿生拱拱转发自 {fwd_link}"

def parser(message:pyrogram.Message): 
    #先实现纯文字转发
    _text = None
    _fwdLink = "https://t.me/{chatPreview}{msgID}"
    _medias = []
    if(message.text != None): 
        _text = message.text
    elif (message.caption != None):
        _text = message.caption
    if(_text != None):
        if(message.chat.username == None): 
            _fwdLink = _fwdLink.format(
                chatPreview="c/"+str(message.chat.id)[4:]+"/",
                msgID=message.message_id
            )
        else: 
            _fwdLink = _fwdLink.format(
                chatPreview="s/"+message.chat.username+"?before=",
                msgID=message.message_id
            )
        _text += TWFooter.format(fwd_link=_fwdLink)
    ret = tweetapi.update_status(
        tweet_mode = "extended",
        status = _text)
    return ret.id_str

# Handler
@telebot.on_message(pyrogram.Filters.command(["retweet", "retweet@atCambot"]))
def Forward_to_Twitter(client:pyrogram.Client, message:pyrogram.Message):
    logging.warn("Recieved message "+str(message.chat.id)+" "+str(message.message_id))
    fwd_id = None
    replyID = None
    messageToBeSend = {}
    if(message.chat.id not in chatID):
        print("ERROR")
        return
    if(message.reply_to_message != None):
        fwd_id = message.reply_to_message.message_id
        # Parsing and forwarding
        _id_str = parser(message.reply_to_message)
        # Delete command message
        telebot.delete_messages(message.chat.id,message.message_id)
        # Forward complete
        telebot.send_message(
            chat_id=groupID,
            text="转发完成喵~~\
                \nURL: {url}\
                \nFrom".format(url=twprofile.format(id_str=_id_str))
                + botName)
        pass
    if(message.reply_to_message == None):
        telebot.send_message(
            reply_to_message_id=message.message_id,
            chat_id=groupID, 
            text="拱拱(也有可能是猪猪)刚才对着空气回复了!\nTwitter不能转发空气!!!")
    pass

if(__name__=="__main__"):telebot.run()
else:telebot.start()