# Bootstraper | bionicCamber/__main__.py
# ~~~~~~~~(0 - 0) = False

import api
import os, sys, asyncio, re
import pyrogram, tweepy

activeBots = ["chatID", "Retweet", "antiorz"]

# Pyrogram auth
telebot = api.telebot
# tweepy auth
tweetapi = api.tweetapi

if __name__ == "__main__":
    telebot.start()
    
# <TODO>  
# 基于当前文件夹的模块加载
# Regex (.*)\.py\Z
# re.search(toImport).group(1)

for module in activeBots:
    __import__(module)

if __name__ == "__main__":
    telebot.idle()

