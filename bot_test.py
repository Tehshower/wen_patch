#TODO: Add help commands
#
import random
import discord
from discord.ext import commands
from datetime import datetime
import re

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.command()
async def vibecheck(ctx, member: discord.Member):
    if member == None:
        member = ctx.author
    #TODO: Add error handling for when the user doesn't exist
    #TODO: 
    guild = ctx.guild
    guild_members = []
    for item in guild.members:
        guild_members.append(item)
    if member not in guild_members:
        await ctx.send('I don\'t know who that is!')
    else:
        temp_list = []  
        async for message in ctx.channel.history(limit=5000):
            if message.author.name == member.name and message.content.startswith('!') == False:
                temp_list.append(message)
        print(f' Length of list: {len(temp_list)}')
        my_message = random.choice(temp_list).content
        await ctx.send(f'<@{member.id}> sent "{my_message}" on {datetime.strftime(message.created_at, "%m/%d/%Y")}.')
    #await ctx.send(f'{ctx.author} is a receipt!')

@bot.command()
async def ghorvas(ctx):
    await ctx.send('I shoot.')

@bot.command()
async def wordcount(ctx, member: discord.Member, arg):
    lookback = 5000
    guild = ctx.guild
    guild_members = []
    for item in guild.members:
        guild_members.append(item)
    print(member.display_name)
    if member not in guild_members:
        await ctx.send('I don\'t know who that is!')
    else:
        temp_list = []  
        async for message in ctx.channel.history(limit=lookback):
            if message.author.name == member.name:
                temp_list.append(message)
        print(f' Length of list: {len(temp_list)}')
        word_count = 0
        for message in temp_list:
            words = message.content.split()
            for word in words:
                if word.lower() == arg.lower():
                    word_count += 1
        await ctx.send(f'<@{member.id}> has written {arg} {word_count} times in the last {lookback} messages!')

@bot.command()
async def goodbot(ctx):
    print('I am here!')
    await ctx.send(f'\`\`\`Thanks, {ctx.author.display_name}! <:peepoCheer:690742015339790457>\`\`\`')

async def check_twitter(message):
    twitter_pattern = r'.*https:\/\/twitter.com\/(\w+\/status\/\d+).*'
    x_pattern = r'.*https:\/\/x.com\/(\w+\/status\/\d+).*'

    if re.match(twitter_pattern, message.content):
        twitter_link = re.match(twitter_pattern, message.content).group(1)
        # Do something with the twitter link
        await message.channel.send(f"I made a better link!: https://fxtwitter.com/{twitter_link}")
    
    elif re.match(x_pattern, message.content):
        x_link = re.match(x_pattern, message.content).group(1)
        # Do something with the x link
        await message.channel.send(f"I made a better link!: https://fxtwitter.com/{x_link}")
@bot.event
async def on_message(message):
    bot.loop.create_task(check_twitter(message))
    await bot.process_commands(message)



bot.run('MTI0OTg5Mzg2ODE4MzIyODU1Nw.G045-u.Hx0JYa9twltIl8Ic611GNzW08VSgJMoP_mIZl0')