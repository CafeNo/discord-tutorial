import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-',help_command=None) 

# doing when client has started
@bot.event
async def on_ready():
    print(f'{bot.user} has Logged')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Couupe Ai"))

# doing with profix
@bot.command()
async def help(ctx):
    await ctx.channel.send('All variable commands')

@bot.command()
async def test1(ctx):
    await ctx.channel.send('JUST TEST')

# doing without prefix
@bot.event
async def on_message(message):
    if message.content == 'Hello':
        print(message.channel)
        print('HELLO FUNCTION')
        await message.channel.send('HELLO!')
    elif message.content == '789654123564':
        await bot.logout
    await bot.process_commands(message)


bot.run(token)
