from math import trunc
import discord
from discord.ext import commands
import time
import random
from vars import *
from colorama import Fore
import colorama
import sys
import json
import base64
from faker import Faker
colorama.init()
# op intruduction credit by bloody0

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

# import config & get token + prefix
file = open('config.json')
data = json.load(file)

token = data['token']
prefix = data['prefix']

client = commands.Bot(command_prefix=prefix, self_bot=True, help_command=None)



# help message !!!!!!!!!!!!!!!!!!!
@client.command()
async def help(ctx):
    await delete(ctx)
    await ctx.send("```\nPrefix: \"" + prefix + "\"\n" + '\n' +

                   "help: Displays this message" + '\n' +

                   "mario: sends \"MARIO!\" 5 times" + '\n' +

                   "botnet: same as above but sends \"Boptnet just hijacked u\" instead" + '\n' +

                   "getvast: will get vastcast face (randomness of 3 faces)" + '\n' +

                   "say: send desired message x amount of times (prefix say \"hi bojaxhiu\" 5)" + '\n' +

                   "farmer: sends vastcast in farmer cosplay" + '\n' +

                   "dox: Will succesfully run vastcasts details on the discord client" + '\n' +

                   "quotecast: 10$ will get vastcasts best coping msgs" + '\n' +

                   "hack: sends user first part of token usage [prefix hack @user/id]" + '\n' +

                   "getbeloved: gets vastcast in love locker being beloved ❤️" + '\n' +

                   "\n```")


# lets u know if its started
@client.event
async def on_ready():
    print("Online!")

# sends mario 5 times
@client.command()
async def mario(ctx):
    await delete(ctx)
    for i in range(0,5):
        await ctx.send("MARIO!")

# same thing here except (Boptnet just hijacked u)
@client.command()
async def botnet(ctx):
    await delete(ctx)
    for i in range(0,5):
        await ctx.send("Boptnet just hijacked u")

# Will get vastcast face status has a randomness of 3 faces
@client.command()
async def getvast(ctx):
    await delete(ctx)
    await ctx.send(vastFaces[random.randint(0, 2)])
    await ctx.send("success")

# basic say command will say desired message and the amount of times with delay
@client.command()
async def say(ctx, arg, amount: int):
    await delete(ctx)
    for i in range(0 , amount):
        await ctx.send(arg)
        time.sleep(0.5)

# Will get status of vastcast in a farmer cosplay 
@client.command()
async def farmer(ctx):
    await delete(ctx)
    await ctx.send("bojaxhiu status: at beteja e kabashit")
    await ctx.send(farmerURI)
    await ctx.send("success")

# Will auto dox vastcast [Most funniest command]
@client.command()
async def dox(ctx):
    #quote = vastQuotes[random.randint(0, 4)] Bloody0 fixed this $$
    time.sleep(0.1)
    await delete(ctx)
    await ctx.send("Last name: bojaxhiu")
    time.sleep(0.1)
    gg = await ctx.send("Loading face...")
    time.sleep(1)
    await gg.delete()
    await ctx.send(vastFaces[random.randint(0, 2)])
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
    await ctx.send(vastQuotes[random.randint(0, 4)])
    await ctx.send("SUCCESFULLY GOT TOP QUOTE!")
    await ctx.send("SUCCESFULLY RAN dox.exe WITHOUT PROBLEMS")

# will get random quqte from the caster
@client.command()
async def quotecast(ctx):
    #quote = vastQuotes[random.randint(0, 4)]
    time.sleep(0.05)
    await delete(ctx)
    awa = await ctx.send("Fetching quote...")
    time.sleep(0.25)
    await awa.delete()
    await ctx.send(vastQuotes[random.randint(0, 4)])
    time.sleep(0.05)
    await ctx.send("Succesfully fetched quote")

# gets desired users first part of token credit null-swap
@client.command()
async def hack(ctx, user: discord.User):
    await delete(ctx)
    await ctx.send("<@" + str(user.id) + ">" + " your token starts with " + base64.b64encode(str(user.id).encode()).decode() + " get scared.")

# send love locket meme about vastcast
@client.command()
async def getbeloved(ctx):
    await delete(ctx)
    await ctx.send(beloved)
    await ctx.send("Bojaxhiu my beloved :heart:")

@client.command()
async def delete(ctx):
    if(data['deletecmds'] == True):
        await ctx.message.delete()

fake = Faker()

@client.command()
async def ip(ctx, user):
    await ctx.send(user + " Your ip address is " + fake.ipv4_private() + " behold... vastcast is visiting you")

# will try running the self bot on the token in config.json
# otherwise it will print fake token logger :troll: credit bloody0
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