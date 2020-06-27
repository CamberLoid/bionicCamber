# Bootstraper | bionicCamber/__main__.py
# ~~~~~~~~(0 - 0) = False

import api
import os,sys,asyncio
import pyrogram, tweepy

activeBots = ["ChannelID", "Retweet"]

# Pyrogram auth
telebot = api.telebot
# tweepy auth
tweetapi = api.tweetapi

for module in activeBots:
    __import__(module)

telebot.run()
