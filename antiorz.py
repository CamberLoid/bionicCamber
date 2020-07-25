# bionicCamber/antiOrz.py Nightly 20200714
# 反ORZ机器人, 使用Userbot

import api
import logging, sched, re

pyrogram = api.pyrogram
telebot = api.telebot
teleuser = api.teleuser

scheduler = api.scheduler

# 对猪猪Bot和柠檬Bot优化
userID = str(teleuser.get_me().id)
isMoRegexString = r'膜.{9,15}tg://user\?id=' + userID
replyToMo = "被膜了好害羞喵...拱拱也要膜!\
    \n[{camberUserName}](tg://user?id={camberID}) 膜了 [{toMoUserName}](tg://user?id={toMoID}) "

userInfo = None

@teleuser.on_message(pyrogram.Filters.mentioned)
def antiOrzHandler(client: pyrogram.client, message: pyrogram.Message) -> bool:
    # 如果不是Bot在膜
    if (not message.from_user.is_bot): 
        return False

    # 判断是否是真的膜
    if (re.search(pattern=isMoRegexString, string=message.text.html) == None): 
        return False

    # 获取膜人的用户信息
    toMoUser = None
    for entity in message.entities:
        if(entity.user != None and entity.user.id != 713137548):
            toMoUser = entity.user
            break
    if (toMoUser == None): return False
    
    # 反膜
    try:
        telebot.send_message(
            chat_id = message.chat.id, 
            parse_mode = "md", 
            reply_to_message_id = message.message_id,
            text = replyToMo.format(
                camberUserName = userInfo.first_name,
                camberID = userInfo.id,
                toMoUserName = toMoUser.first_name,
                toMoID = toMoUser.id))
                
    # 如果没成, 就用Userbot膜
    except:
        message.reply(
            parse_mode = "md", 
            text = replyToMo.format(
                camberUserName = userInfo.first_name,
                camberID = userInfo.id,
                toMoUserName = toMoUser.first_name,
                toMoID = toMoUser.id)
        )
    return True

# 更新
def updateUserInfo():
    userInfo = telebot.get_users(user_ids=userID)
    scheduler.enter(delay=600, priority=1, action=updateUserInfo)

scheduler.enter(delay=1, priority=1, action=updateUserInfo)
