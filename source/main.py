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
# config idea by bloody0
file = open('config.json')
data = json.load(file)

token = data['token']
prefix = data['prefix']

client = commands.Bot(command_prefix=prefix, self_bot=True, help_command=None)



# help message !!!!!!!!!!!!!!!!!!!
@client.command()
async def help(ctx):
    await delete(ctx)
    g = await ctx.send("```fix\nSuccesfully printed help message to console```")
    
    print("\nPrefix: \"" + prefix + "\"\n\n" +

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
                    
"ip: sends a fake ip4 along the text \"vastcast is comming for you\"" + '\n' +

"uninstallpop: Tries a program, should succesfully execute right?" + '\n' +

"mail: Sends a text in a format like a letter (usage: prefix mail user/id \"msg\"" + '\n' +

"ddox: generates fake info lol" + '\n' +

"dmspam: You know what it means. args: user, message, times" + '\n' +

"")
    
    time.sleep(5)
    await g.delete()

# lets u know if its started
@client.event
async def on_ready():
    print("Online!")
    print("ur id is " + str(base64.b64decode(token[:24]).decode()))
    print("if this doesnt print out ur correct id fix token[:24] by incrementing or maybe decreasing it")

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

# Will get cedo smartness
@client.command()
async def getcedo(ctx):
    await delete(ctx)
    await ctx.send(cedoQuotes[random.randint(0,5)])
    time.sleep(0.5)
    await ctx.send("successfully hacked into cedo desktop")

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

# will get random quote from the caster
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

# from config will determen if u choose to delete msgs
# credit nullswap
async def delete(ctx):
    if(data['deletecmds'] == True):
        await ctx.message.delete()

fake = Faker()

# will send fake ipv4 to user
# credit bloody0
@client.command()
async def ip(ctx, user: discord.User):
    await delete(ctx)
    await ctx.send("<@" + str(user.id) + "> Your ip address is " + fake.ipv4_private() + " behold... vastcast is visiting you")

@client.command()
async def ddox(ctx, user: discord.User):
    await delete(ctx)
    await ctx.send("GUYS " + user.name.upper() + " LIVES AT " + fake.address().upper() + " AND HIS REAL LIFE NAME IS " + fake.name().upper() + " TRUST ME SOURCE IS VASTCAST")

@client.command()
async def dmspam(ctx, user: discord.User, msg: str, times: int):
    await delete(ctx)
    if(user.dm_channel == None):
        user.create_dm()
    for i in range(0,times):
        await user.dm_channel.send(msg)
        time.sleep(0.15)

# idk funny fake program with vastcast as virus
@client.command()
async def uninstallpop(ctx):
    await delete(ctx)
    await ctx.send("Trying uninstall-pop.exe")
    for i in range(0,3):
        await ctx.send("FAILED!")
    
    await ctx.send("bojaxhiu virus deployed")
    await ctx.send(vastFaces[random.randint(0, 2)])
    await ctx.send("Enjoy swatted!")

# makes a mail on desired user
@client.command()
async def mail(ctx, user: discord.User, msg):
    await delete(ctx)
    await ctx.send("Hi <@" + str(user.id) + ">," + '\n\n' +
                    msg + '\n\n' +
                    signatures[random.randint(0, 3)] + '\n' +
                    "-<@" + base64.b64decode(token[:24]).decode() + ">")


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