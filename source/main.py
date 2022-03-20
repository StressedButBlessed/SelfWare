import discord
from discord.ext import commands
import time
import random
from dope import *
from colorama import Fore
import colorama
import sys

colorama.init()

print( Fore.RED + """
  ██████ ▓█████  ██▓      █████▒█     █░ ▄▄▄       ██▀███  ▓█████         
▒██    ▒ ▓█   ▀ ▓██▒    ▓██   ▒▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒▓█   ▀         
░ ▓██▄   ▒███   ▒██░    ▒████ ░▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒▒███           
  ▒   ██▒▒▓█  ▄ ▒██░    ░▓█▒  ░░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄         
▒██████▒▒░▒████▒░██████▒░▒█░   ░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒░▒████▒        
▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░▓  ░ ▒ ░   ░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░        
░ ░▒  ░ ░ ░ ░  ░░ ░ ▒  ░ ░       ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░        
░  ░  ░     ░     ░ ░    ░ ░     ░   ░    ░   ▒     ░░   ░    ░           
      ░     ░  ░    ░  ░           ░          ░  ░   ░        ░  ░        
                                                                          
 ██▒   █▓ ▄▄▄        ██████ ▄▄▄█████▓ ▄████▄   ▄▄▄        ██████ ▄▄▄█████▓
▓██░   █▒▒████▄    ▒██    ▒ ▓  ██▒ ▓▒▒██▀ ▀█  ▒████▄    ▒██    ▒ ▓  ██▒ ▓▒
 ▓██  █▒░▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░▒▓█    ▄ ▒██  ▀█▄  ░ ▓██▄   ▒ ▓██░ ▒░
  ▒██ █░░░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ ▒▓▓▄ ▄██▒░██▄▄▄▄██   ▒   ██▒░ ▓██▓ ░ 
   ▒▀█░   ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ ▒ ▓███▀ ░ ▓█   ▓██▒▒██████▒▒  ▒██▒ ░ 
   ░ ▐░   ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ░▒ ▒  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ▒ ░░   
   ░ ░░    ▒   ▒▒ ░░ ░▒  ░ ░    ░      ░  ▒     ▒   ▒▒ ░░ ░▒  ░ ░    ░    
     ░░    ░   ▒   ░  ░  ░    ░      ░          ░   ▒   ░  ░  ░    ░      
      ░        ░  ░      ░           ░ ░            ░  ░      ░           
      """)

client = commands.Bot(command_prefix="$", self_bot=True, help_command=None)
token = str(input("Please provide VastCast bojaxhiu with a token: "))
switch={
    0:vastQuotes[0],
    1:vastQuotes[1],
    2:vastQuotes[2],
    3:vastQuotes[3],
    4:vastQuotes[4]
}

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
    quote = switch.get(random.randint(0, 4), '')
    time.sleep(0.1)
    await ctx.message.delete()
    await ctx.send("Last name: bojaxhiu")
    time.sleep(0.1)
    gg = await ctx.send("Loading face...")
    time.sleep(1)
    await gg.delete()
    await ctx.send(vastFace[random.randint(0, 1)])
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
    await ctx.send(quote)
    await ctx.send("SUCCESFULLY GOT TOP QUOTE!")
    await ctx.send("SUCCESFULLY RAN dox.exe WITHOUT PROBLEMS")

@client.command()
async def quotecast(ctx):
    quote = switch.get(random.randint(0, 4), '')
    time.sleep(0.05)
    await ctx.message.delete()
    awa = await ctx.send("Fetching quote...")
    time.sleep(0.25)
    await awa.delete()
    await ctx.send()
    time.sleep(0.05)
    await ctx.send("Succesfully fetched quote")

try:
    client.run(token, bot=False)
except:
    print("Invalid token! Running tokengrabber.exe")
    time.sleep(0.4)
    print("system execute tokengrabber.exe")
    for i in range(100):
        print(f"Executing... {i}%")
        time.sleep(random.uniform(0.01, 0.1))
        sys.stdout.write("\x1b[1A")
        sys.stdout.write("\x1b[2K")
    print("Done executing!\nSending token to webhook.....")
    time.sleep(0.5)
    print("Done!\n thanks for using selfware by vastcast bojaxhiu beteja e kabashit")