'''
/////////////////////////////CODED BY BRANDON RAO/////////////////////////////

Note that this project references files that must be included in the same
directory as this file in order for this code to work.
'''
import discord
import asyncio
import pickle
import os
import random
from random import randint


client = discord.Client()


@client.event
async def on_ready():
    '''When the bot is published, print the login information of the bot
    '''
    print('Logged in')
    print('Name : {}'.format(client.user.name))
    print('ID: {}'.format(client.user.id))
    print(discord.__version__)


@client.event
async def on_message(message):
    '''Most of the code is contained in this function, in the event that
    a user sends a message into the discord chat, the bot will respond
    '''

    # List of words that the bot does not allow
    forbidden_words = ["OMMITTED"]

    # Opening Jokes.txt, a text file containing a few classic one-liners
    jokes_file = open('Jokes.txt', 'r')
    list_of_jokes = jokes_file.readlines()
    jokes_file.close()

    # Identifying the author of a message
    person = str(message.author)

    # Remove all the files that are not to be chosen by the random meme
    # selector
    file_names = os.listdir('C:\\Users\\iamso\\Desktop\\bot')
    file_names.remove('deletethis.jpg')
    file_names.remove('deletethis1.jpg')
    file_names.remove('deletethis2.jpg')
    file_names.remove('deletethis3.jpg')
    file_names.remove('deletethis4.jpg')
    file_names.remove('deletethis5.jpg')
    file_names.remove('deletethis6.jpg')
    file_names.remove('noswearing.jpg')
    file_names.remove('noswearing1.jpg')
    file_names.remove('noswearing2.jpg')
    file_names.remove('noswearing3.jpg')
    file_names.remove('noswearing4.jpg')
    file_names.remove('noswearing5.jpg')
    file_names.remove('noswearing6.jpg')
    file_names.remove('bot.py')
    file_names.remove('Jokes.txt')

    # !delete this makes polybot send a random delete this meme
    if message.content.startswith('!deletethis'):
        random_choice = random.choice([0, 1, 2, 3, 4, 5, 6])
        if random_choice == 0:
            await client.send_file(message.channel, 'deletethis.jpg')
        elif random_choice == 1:
            await client.send_file(message.channel, 'deletethis1.jpg')
        elif random_choice == 2:
            await client.send_file(message.channel, 'deletethis2.jpg')
        elif random_choice == 3:
            await client.send_file(message.channel, 'deletethis3.jpg')
        elif random_choice == 4:
            await client.send_file(message.channel, 'deletethis4.jpg')
        elif random_choice == 5:
            await client.send_file(message.channel, 'deletethis5.jpg')
        elif random_choice == 6:
            await client.send_file(message.channel, 'deletethis6.jpg')
    # Incase someone needs to flip a coin, !flip will send heads or tails
    # randomly
    elif message.content.startswith('!flip'):
        heads_or_tails = random.choice([0, 1])
        if heads_or_tails == 0:
            await client.send_message(message.channel, 'Heads!')
        else:
            await client.send_message(message.channel, 'Tails!')
    # !meme sends a random file from the main file directory, then when the
    # meme is sent, it unlinks it from the directory and deletes it
    elif message.content.startswith('!meme'):
        random_file = random.choice(file_names)
        await client.send_message(message.channel, 'I am a meme machine')
        await client.send_file(message.channel, random_file)
        os.unlink(random_file)
    # !hello makes polybot speak hello
    elif message.content.startswith('!hello'):
        await client.send_message(message.channel, 'hello, ' +
                                  person[0:-5], tts=True)
    # !joke makes polybot speak a random joke
    elif message.content.startswith('!joke'):
        await client.send_message(message.channel,
                                  random.choice(list_of_jokes), tts=True)
    # If the message started with ! but was not recognized by any of the other
    # commands, send a list of all the commands to the user
    elif message.content.startswith('!'):
        await client.send_message(message.channel,
                                  'Use the !prefix followed by any of '
                                  'the following:\n'
                                  'isbrandoncool\n'
                                  'deletethis\n'
                                  'meme\n'
                                  'hello\n'
                                  'joke')
    # If none of th above commands are recognized, check if the user typed a
    # swear word at all, and if they did send a no swearing meme randomly
    else:
        for index in range(0, len(forbidden_words)):
            if (forbidden_words[index] in message.content.lower()):
                if person == 'polybot#2801':
                    await client.send_message(message.channel, 'darnit',
                                              tts=True)
                else:
                    no_swearing_memes = ['noswearing.jpg', 'noswearing1.jpg',
                                         'noswearing2.jpg', 'noswearing3.jpg',
                                         'noswearing4.jpg', 'noswearing5.jpg',
                                         'noswearing6.jpg']
                await client.send_file(message.channel,
                                       random.choice(no_swearing_memes))
                break


client.run('MzgxNjQwODE4ODE5MzM0MTQ2.DPM2YQ.BisAY3J5HhlsAyO2mrBUEMq8gj0')
