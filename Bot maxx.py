import discord
import random
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "!")



Bank = []
Ids = []
CashFlow = []
#secs = time.localtime(time.time())
#sec = secs[5]

print(time)
def CheckSec(sec):
    if sec == 0:
        print(sec)
        counter = 0
        max_index = len(CashFlow) - 1
        while counter <= max_index:
            CashFlow[counter] = 0
            counter += 1

def peps(user):
    Ids.append(user)
    Bank.append(50)
    CashFlow.append(0)

def Gain(user):
    print("flow " + "%s" % (CashFlow[user]))
    if CashFlow[user] == 0:
        Bank[user] += random.randint(5,10)
        CashFlow[user] = 1
    else:
        return



@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(msg):
    secs = time.localtime(time.time())
    sec = secs[5]
    CheckSec(sec)
    if not msg.author.id == '433370993273208864':
        if msg.author.id not in Ids:
            user = msg.author.id
            peps(user)
        else:
            Gain(Ids.index('%s' % (msg.author.id)))
        
        if msg.content == "+cookie":
            await client.send_message(msg.channel,":cookie:" )

        if msg.content == "+me":
            await client.send_message(msg.channel,"Hi! I'm Maxxbot" )

        if msg.content == "+money":
            userID = msg.author.id
            await client.send_message(msg.channel,"<@%s> You have :" % (userID))
            await client.send_message(msg.channel,"%s$" % (Bank[Ids.index('%s' % (msg.author.id))]))

        if msg.content == "+help":
            await client.send_message(msg.channel,"Commands : " )
            await client.send_message(msg.channel,"+me" )
            await client.send_message(msg.channel,"+cookie" )

        if msg.content == "+debug":
            await client.send_message(msg.channel,sec )
            await client.send_message(msg.channel,secs )
            await client.send_message(msg.channel,CashFlow )
            await client.send_message(msg.channel,time.localtime(time.time()) )


        if msg.content == "+role" and msg.author.id == '360089991587692546':
            await client.send_message(msg.channel,"HI!!" )
        #else:
           # await client.send_message(msg.channel,"NO!!" )

client.run("NDMzMzcwOTkzMjczMjA4ODY0.Da64Aw.T7u633mk_KqDDmLM-KQW7_OeyPk")
