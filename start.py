import discord
from discord.ext import commands


from strikedb import StrikeDB
from strikedbhelper import *




bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as' + " " + bot.user.name)
    print()
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="YoServer", description="台灣高品質1.8 PvP Practice伺服器", color=0x228B22)
    embed.add_field(name="IP", value="yoserver.cc")
    embed.add_field(name="版本", value="1.8~1.8.X")
    await ctx.send(embed=embed)
        


@bot.command()
async def user(ctx, username: str):
    db = StrikeDB()

    results = db.getStatByUsername(username)

    if results is None:
        await ctx.send("資料庫錯誤！")

    if len(results.all()) == 0:
        await ctx.send("用戶不存在！")
    json = ""
    # json = "YoServer玩家資料\n"
    for stat in results:
        json += str('用戶名：') + str(stat.username) + "\n"
        json += str('UUID：') + str(stat.uuid) + "\n"
        json += "\n"
        
        
    await ctx.send(json)
    await ctx.send('https://media.mojang.com/blog-image/2c34ca1217c7d95e76a6f8d646adf9208f78145a/blogmcnet.png')



@bot.command()
async def rank(ctx, username: str):
    db = StrikeDB()

    results = db.getStatByUsername(username)

    if results is None:
        await ctx.send("資料庫錯誤！")

    if len(results.all()) == 0:
        await ctx.send("用戶不存在！")

    json = ""
    # json = "YoServer玩家資料\n"
    for stat in results:
        json += str('用戶名 username：') + str(stat.username) + "\n"
        json += str('UUID：') + str(stat.uuid) + "\n" + "\n"
        json += str('總排名：') + str(stat.global_elo) + "\n"
        json += str('競技場排名：') + str(stat.elo_builduhcelo) + "\n"
        json += str('魔水排名：') + str(stat.elo_debuffelo) + "\n"
        json += str('藥水排名：') + str(stat.elo_nodebuffelo) + "\n"
        json += str('連擊排名：') + str(stat.elo_comboelo) + "\n"
        json += str('金蘋果排名：') + str(stat.elo_gappleelo) + "\n"
        json += str('大補湯排名：') + str(stat.elo_soupelo) + "\n"
        json += str('相撲排名：') + str(stat.elo_sumoelo) + "\n"
        json += str('相撲(三戰)排名：') + str(stat.elo_sumobestof3elo) + "\n"
        json += str('斧頭戰排名：') + str(stat.elo_axepvpelo) + "\n"
        json += str('極限團體戰：') + str(stat.elo_hcfelo) + "\n"
        json += "\n"

    await ctx.send(json)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    
    embed = discord.Embed(title="Yoserver Discord Bot Command", description="Yoserver 伺服器官方Discord機器人指令", color=0x228B22)
    embed.add_field(name="查詢伺服器資訊", value="!info", inline=False)
    embed.add_field(name="查詢玩家資料", value="!user", inline=False)
    embed.add_field(name="查詢玩家排名積分", value="!rank", inline=False)

    

    await ctx.send(embed=embed)

bot.run('Njc0OTkzNjIyNTM3NzMyMTA2.Xkty-A.5XsnRPT7lzjVgZhM25VwV0RwjZc')