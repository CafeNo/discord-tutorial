import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='-',help_command=None)

@bot.event
async def on_ready():
    print(f'{bot.user} has Logged')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Couupe Ai"))

@bot.command()
async def help(ctx):
    await ctx.channel.send('ไม่มีคำสั่ง ขี้เกียจทำ')

@bot.command()
async def test1(ctx):
    await ctx.channel.send('TEST เฉยๆไม่มีอะไร')


@bot.event
async def on_message(message):
    if message.content == '123':
        print(message.channel)
        print('HELLO FUNCTION')
        await message.channel.send('HELLO!')
    elif message.content == '789654123564':
        await bot.logout
    await bot.process_commands(message)

bot.run(token)
