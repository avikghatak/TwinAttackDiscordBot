import discord
import os
import string
from decouple import config

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



def func(s):  #q1
    primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109]
    temp=''
    n=len(s)
    # print(s)
    for i in range(n):
        if i+1 in primes:
            temp=''.join((temp,s[i]))
    temp=temp[::-1]
    return temp

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
        await message.channel.send('Q1. input format: a string s')
        await message.channel.send('Q2. input format: a string s')
        await message.channel.send('Input can be entered after placing iq1 or iq2 in the first line followed by the input in the following lines.')
    
    

    if msg.startswith('iq1'):      
        
        z = msg.splitlines()
        if (len(z) < 2) or (len(z) > 2):
          await message.channel.send("Not a valid input\n")
        else:
          s = str(z[1])
          ans = func(s)
          print(ans)
          await message.channel.send(ans)


    if msg.startswith('iq2'):      
        
        z = msg.splitlines()
        if (len(z) < 2) or (len(z) > 2):
            await message.channel.send("Not a valid input\n")
        else:
          s = str(z[1])
          n=len(s)
          l1=string.ascii_lowercase+string.ascii_uppercase
          arr=['a']*n
          for i in range(n):
              x=s[i]
              arr[i] = l1[(l1.index(x) + pow(2, n - i - 1, 52)) % 52]
          final = ''.join(arr)
          print(final)
          await message.channel.send("Output:")
          await message.channel.send(final)
          
        

client.run(config('TOKEN'))