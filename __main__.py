# Bootstraper | bionicCamber/__main__.py
# ~~~~~~~~(0 - 0) = False

import api
import os,sys,asyncio
import pyrogram, tweepy

activeBots = ["chatID", "Retweet"]

# Pyrogram auth
telebot = api.telebot
# tweepy auth
tweetapi = api.tweetapi

if __name__ == "__main__":
    telebot.start()
    
for module in activeBots:
    __import__(module)

if __name__ == "__main__":
    telebot.idle()

