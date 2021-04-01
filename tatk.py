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
        await message.channel.send('Hello! Welcome to Twin-Attack Round 3!\nTo ask for help enter --help')

    if msg.startswith('--help'):
        await message.channel.send('Twin-Attack Bot Help---\nThere are 2 questions in this challenge:\n')
        await message.channel.send('Q1. input format: a string s')
        await message.channel.send('Q2. input format: a string s')
        await message.channel.send('Input can be entered after placing iq1 or iq2 in the first line followed by the input in the following lines. Each of the strings should contain all lowercase english alphabets only, and greater than 1 characters. i.e, a-z')
        await message.channel.send('For example to send the string "abcd" for the first question, enter:\niq1\nabcd\n\nFor any more queries ask in the General channel.')
    
    

    if msg.startswith('iq1'):      
        
        z = msg.splitlines()
        if (len(z) < 2) or (len(z) > 2):
          await message.channel.send("Not a valid input\nInput must contain 2 lines only")
        else:
            s = str(z[1])
            n = len(s)
            ok = 1
            if n <= 1:
                await message.channel.send("Not a valid input\nString must contain atleast 2 characters.")
                ok = 0
            for i in range(n):
                if (s[i] > 'z' or s[i] < 'a'):
                    await message.channel.send("Not a valid input\nString must contain only english alphabets")
                    ok = 0
            if ok == 0:
                return         
            ans = func(s)
            print(ans)
            await message.channel.send("Output:")
            await message.channel.send(ans)


    if msg.startswith('iq2'):      
        
        z = msg.splitlines()
        if (len(z) < 2) or (len(z) > 2):
            await message.channel.send("Not a valid input\nInput must contain 2 lines only")
        else:            
            s = str(z[1])
            n=len(s)
            ok = 1
            if n <= 1:
                await message.channel.send("Not a valid input\nString must contain atleast 2 characters.")
                ok = 0
            for i in range(n):
                if (s[i] > 'z' or s[i] < 'a'):
                    await message.channel.send("Not a valid input\nString must contain only english alphabets")
                    print('not ok')
                    ok = 0
                    break
            if ok == 0:
                return
            s=s.lower()
            l1=string.ascii_lowercase
            arr=['a']*n
            for i in range(n):
                x=s[i]
                arr[i]=l1[(l1.index(x)+pow(2,n-i-1,26))%26]
            final = ''.join(arr)
            print(final)
            await message.channel.send("Output:")
            await message.channel.send(final)          
          
        

client.run(config('TOKEN'))