import discord
from discord.ext import commands
import time
import random
from dope import *

client = commands.Bot(command_prefix="$", self_bot=True, help_command=None)
token = ""
random = random.randrange(0,5)
def quote(num):
    switch={
        0:vastQuotes[0],
        1:vastQuotes[1],
        2:vastQuotes[2],
        3:vastQuotes[3],
        4:vastQuotes[4]
    }
    return switch.get(num, "Broke")

@client.event
async def on_ready():
    print("Online!")

@client.command()
async def mario(ctx):
    for i in range(0,5):
        await ctx.send("Wwwwww")
    
@client.command()
async def botnet(ctx):
    for i in range(0,5):
        await ctx.send("Boptnet just hijacked u")

@client.command()
async def getvast(ctx):
    await ctx.send(vastURI)
    await ctx.send("success")

@client.command()
async def say(ctx, arg, amount: int):
    await ctx.message.delete()
    for i in range(0 , amount):
        await ctx.send(arg)
        time.sleep(0.5)

@client.command()
async def farmer(ctx):
    await ctx.message.delete()
    await ctx.send("bojaxhiu status: at beteja e kabashit")
    await ctx.send(farmerURI)
    await ctx.send("success")

@client.command()
async def dox(ctx):
    time.sleep(0.1)
    await ctx.message.delete()
    await ctx.send("Last name: bojaxhiu")
    time.sleep(0.1)
    gg = await ctx.send("Loading face...")
    time.sleep(1)
    await gg.delete()
    await ctx.send(vastJEW)
    await ctx.send("FACE LOADED SUCCESFULLY!")
    time.sleep(0.1)
    poop = await ctx.send("Getting current cordinates...")
    time.sleep(0.5)
    await poop.delete()
    await ctx.send(vastCORDS)
    await ctx.send("CORDS LOADED SUCCESFULLY!")
    time.sleep(0.1)
    mayonas = await ctx.send("Fetching top quotes...")
    time.sleep(1)
    await mayonas.delete()
    await ctx.send(quote(random))
    await ctx.send("SUCCESFULLY GOT TOP QUOTE!")
    await ctx.send("SUCCESFULLY RAN dox.exe WITHOUT PROBLEMS")

@client.command()
async def quotecast(ctx):
    time.sleep(0.05)
    await ctx.message.delete()
    awa = await ctx.send("Fetching quote...")
    time.sleep(0.25)
    await awa.delete()
    await ctx.send(quote(random))
    time.sleep(0.05)
    await ctx.send("Succesfully fetched quote")

client.run(token, bot=False)
