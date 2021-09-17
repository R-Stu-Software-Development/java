### Bot is under the license of MIT license 
### ©2021  R Stu Team │ All Right Reserved.

### change this code at your own risk


### requirement
# pip install discord
# pip install discord-ext-bot

import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot


###client = commands.Bot(command_prefix="~")

TOKEN = 'token'

### prefix command
bot = commands.Bot(command_prefix='~')


### nothing
@bot.command()
async def on_ready():
    print("im online")

### bot command
@bot.command()
async def hi(ctx):
    await ctx.reply('Hello!',)

@bot.command()
async def linkzoom(ctx):
    embed=discord.Embed(title="Zoom 7B", url="https://us02web.zoom.us/j/4715315440?pwd=bVR0cHZ0T2JQZHFwUXhEalJvMUJTQT09", description="link untuk pelajaran di kelas 7B", color=discord.Color.blue())
    await ctx.send(embed=embed)


@bot.command()
async def jadwalpts(ctx):
    embed=discord.Embed(title="Jadwal Pts", url="https://i.ibb.co/c6GWhzF/nice.jpg", description="untuk tanggal 20 sampai dengan 28", color=discord.Color.green())
    embed.set_image(url="https://i.ibb.co/c6GWhzF/nice.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def a_hbotinfo(ctx):
    embed=discord.Embed(title="Al Hikmah Moderator Bot Info", 
    description="A Bot that only for Al hikmah junior high school Server's.", 
    color=discord.Color.green())
    embed.add_field(name="Bot Created at :", value="16 Sep 2021", inline=True)
    embed.add_field(name="Author :", value="Radit - R Stu Team", inline=True)
    embed.add_field(name="Version :", value="V 1.90.160921", inline=True)
    embed.add_field(name="Bot License :", value="MIT lisence, Open Source \n [Read more about MIT License](https://github.com/rstusoftdev/discord-Bot/blob/main/LICENSE)", inline=False)
    embed.set_footer(text="note: Bot is NOT OFFICIALLY from Al Hikmah")
    await ctx.send(embed=embed)

@bot.command()
async def ahelp(ctx):
    embed=discord.Embed(title="~Help", 
    description="Al-Hikmah junior high school Server's Bot \n**Command Help**.", 
    color=discord.Color.green())
    embed.add_field(name="Prefix", value="``~`` \n \n============ ")
    
    embed.add_field(name="Greeting", value="- Hi \n``~hi`` \n \n============ ", inline=False)

    embed.add_field(name="Schedule and Link", value="- Zoom 7B \n``~linkzoom`` \n \n- Jadwal PTS \n``~jadwalpts`` \n \n============ ", inline=False)

    embed.add_field(name="Information and About", value="- Bot Info \n``~a_hbotinfo`` \n \n============ ", inline=False)

    
    embed.set_footer(text="Command Help")
    await ctx.send(embed=embed)




bot.run(TOKEN)

