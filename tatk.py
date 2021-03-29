import discord
import os
from decouple import config

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    msg = message.content

    if message.author == client.user:
        return
    msg = message.content
    msg = msg.lower()

    if msg.startswith('hi'):
        await message.channel.send('Hello! Welcome to Twin-Attack!\nTo ask for help enter --help')

    if msg.startswith('--help'):
        await message.channel.send('Twin-Attack Bot Help---\nThere are 2 questions in this challenge:\n')
        await message.channel.send('Q1. input format: n\nn spaced integers')
        await message.channel.send('Q2. input format: n\nn spaced integers')
        await message.channel.send('Input can be entered after placing iq1 or iq2 in the first line followed by the input in the following lines.')
    
    

    if msg.startswith('iq1'):      
        
        z = msg.splitlines()
        if len(z) < 3:
            await message.channel.send("Not a valid input\n")
        else:
            n=int(z[1])
            print(n)
            l=[]
            l.extend(map(int,z[2].split()))
            c=0
            if len(l) != n:
                await message.channel.send("Not a valid input\n")
            else:
                for i in l:
                    c+= i
                
                print(c)
                await message.channel.send("Output:\n")
                await message.channel.send(c)


    if msg.startswith('iq2'):      
        
        z = msg.splitlines()
        
       
        await message.channel.send("Question not set yet\n")

client.run(config('TOKEN'))