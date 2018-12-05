import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'hi and welcome to arrow music show and here are the roles. you may not talk unless you have been promoted and given permission to do it, To become a fan you must agree by joining me in a voice call when you do that if I think you are worthy you will become a fan, after you become a fan you can join in activities respond to my talking subscribe and that will rank you up faster by giving you points and no talking about love on the channel thanks')
    print('Sent message to ' + member.name)
    
@client.event
async def on_ready():
    await client.change_presence(game=Game(name='you live', type = 3))
    print('Bot Online.') 

client.run(os.getenv('TOKEN'))
