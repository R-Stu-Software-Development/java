### Bot is under the license of MIT license 
### ©2021  R Stu Team │ All Right Reserved.

### change this code at your own risk


### requirement
# pip install discord
# pip install discord-ext-bot
# pip install wikipedia
# pip install googletrans


import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import datetime
import os
import asyncio
import wikipedia
import googletrans
from googletrans import Translator


###client = commands.Bot(command_prefix="~")

TOKEN = 'your token'

### prefix command
bot = commands.Bot(command_prefix='~')




@bot.command()
async def on_ready():
    print("im online")

@bot.command()
async def tr(ctx, lang, *, thing):
    translator = Translator()
    translation = translator.translate(thing, dest=lang)
    await ctx.send(translation.text)


@bot.command()
async def whatis(context, *, something):
    await context.send(wikipedia.summary(something, sentences=2))

### bot command
@bot.command()
async def hi(ctx):
    await ctx.reply(f"Hello!, {ctx.author.nick} a.k.a {ctx.author.name}")

@bot.command()
async def zoom(ctx):
    embed=discord.Embed(title="ZOOM Link", description="[7B](https://us02web.zoom.us/j/4715315440?pwd=bVR0cHZ0T2JQZHFwUXhEalJvMUJTQT09)\n[Ngaji](https://us02web.zoom.us/j/6310076461?pwd=R3BNZlN2eG8rc05lMHArUTJjTGdCUT09)", color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.command()
async def bc(ctx):
    embed=discord.Embed(title="Bot Source Code", url="https://github.com/R-Stu-Software-Development/java/blob/main/main.py", description="Because the bot is [Open Source](https://opensource.org/), You can download The source code too!", color=discord.Color.green())
    await ctx.send(embed=embed)    

@bot.command()
async def jadwalpts(ctx):
    embed=discord.Embed(title="Jadwal PTS", url="https://i.ibb.co/c6GWhzF/nice.jpg", description="untuk tanggal 20 sampai dengan 28", color=discord.Color.green())
    embed.set_image(url="https://i.ibb.co/c6GWhzF/nice.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def botinfo(ctx):
    embed=discord.Embed(title="Al Hikmah Bot Info", 
    description="A Bot that only for Al hikmah junior high school Server's.", 
    color=discord.Color.green())
    embed.add_field(name="Bot Created at :", value="16 Sep 2021", inline=True)
    embed.add_field(name="Author :", value="Radit - R Stu Team", inline=True)
    embed.add_field(name="Version :", value="V 1.90.160921", inline=True)
    embed.add_field(name="Bot License :", value="MIT lisence, Open Source \n [Read more about MIT License](https://github.com/rstusoftdev/discord-Bot/blob/main/LICENSE)", inline=False)
    embed.set_footer(text="Bot Info")
    await ctx.send(embed=embed)

@bot.command()
async def ahelp(ctx):
    embed=discord.Embed(title="~ahelp", 
    description="Al-Hikmah junior high school Server's Bot \n**Command Help**.", 
    color=discord.Color.green())
    embed.add_field(name="Commands", value="\n- Prefix = ``~`` \n \n**Greeting**\n- Hi = ``hi``\n \n**Tools**\n- Browsing and Searching = ``whatis``\n- Translate = ``tr [the language you want to translate]`` \n \n**Schedule and Link** \n - Zoom 7B = ``zoom``\n- Jadwal PTS = ``jadwalpts``\n \n**Fun Game(s)**\n- Tic Tac Toe = ``ttt [@yourname] [@yourfriend]`` \n - How to play Tic Tac Toe = ``ttthelp``\n \n**Information and About**\n- UserInfo = ``userinfo [@member-name]``\n- Bot Info = ``botinfo``\n- Bot Source Code = ``bc`` \n \n \n**More?** [Join Our server](https://discord.io/RStuTeamServer) now to **ask more!** ")

    embed.set_footer(text="Command Help")

    
    #Button(style=ButtonStyle.URL, label="Join Dev Server", url="https://discord.io/RStuTeamServer")
    
    
    await ctx.send(embed=embed)


@bot.command()
async def ttthelp(ctx):
    embed=discord.Embed(title="~ttthelp", 
    description="Al-Hikmah junior high school Server's Bot \n**Tic Tac Toe Multiplayer Game Command Help**.", 
    color=discord.Color.purple())
    embed.add_field(name="Commands", value="``~`` - prefix \n``ttt [@yourname] [@yourfriend]`` - start the game\n \n:one: :two: :three:\n:four: :five: :six:\n:seven: :eight: :nine:\n \n``place [number position]`` - locate your :o2: or :regional_indicator_x: at the number position like above")

    embed.set_footer(text="Tic Tac Toe Game Command Help")
    await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title=f"UserInfo {member.name}", color=0xFFFFFF)
    embed.add_field(name="Nickname:", value=f"{member.nick}")
    embed.add_field(name="ID:", value=f"{member.id}", inline=False)
    embed.add_field(name="Created at:", value=f"{member.created_at.strftime('%d.%m.%Y, %H:%M Uhr')}")
    embed.add_field(name="Joined at:", value=f"{member.joined_at.strftime('%d.%m.%Y, %H:%M Uhr')}")
    embed.add_field(name="Top Role:", value=f"{member.top_role}", inline=False)
    embed.add_field(name="Activity:", value=f"{member.activity}")
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text="Member Info")

    await ctx.send(embed=embed)

## game 
player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@bot.command()
async def ttt(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@ttt.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@849627159911465051>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

### Bot run Command 

bot.run(TOKEN)

