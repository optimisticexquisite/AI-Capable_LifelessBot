import discord
import os
import requests
import json
import youtube_dl
import datetime
import csv
import boto3
from discord.ext import commands
from discord.utils import get
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from pytube import YouTube
#from youtube_search import YoutubeSearch
from youtubesearchpython import VideosSearch
import asyncio

client=discord.Client()
lifelessemoji='<a:lifeless:843039789405044757>'
mycandy='<:mycandy:843491792279961601>'
balbasaur='<:balbasaur:843491791658549258>'
pinkheart='<:pinkheart:843491791553953804>'
girlkiss='<a:girlkiss:843491799246962708>'
girlagree='<a:girlagree:843491797443412038>'
discogirl='<a:discogirl:843491796838252595>'
cute='<a:cute:843491796347912242>'
hoodie='<a:lifelesshoodie:843491795245334578>'
cutecat='<a:cutecat:842966553321275412>'

@client.event
#async def on_ready():
  #activity = discord.Activity(type=discord.ActivityType.listening, name="The Sweetness of Lifeless")
  #await client.change_presence(status=discord.Status.idle, activity=activity)
  #print('We have logged in as {0.user}'.format(client))

# Interactive Part of LifelessBot

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('lifelessHello'):
    await message.channel.send('Hello, Hello, Hello! This is LifelessBot reciprocating the Sweetness of Lifeless. :heart:')

  if message.content.startswith('lifelessKick'):
    await message.channel.send('Sorry! Lifeless is too sweet to kick/ban sweet people! <a:cutecat:842966553321275412>')

  if message.content.startswith('lifelessBan'):
    await message.channel.send('Sorry! Lifeless is too sweet to kick/ban sweet people! <a:cutecat:842966553321275412>')

  if message.content.startswith('lifelessInspire'):
    quote=get_quote()
    await message.channel.send('_Here is an inspirational quote from the sweetness factory of Lifeless_ :heart:'+'\n'+'\n'+quote)

  if message.content.startswith('lifelessSowiee'):
    quote=get_quote()
    await message.channel.send('<:Sowiee:837558958071611412>')

  if message.content.startswith('lifelessCutecat'):
    quote=get_quote()
    await message.channel.send('<a:cutecat:842966553321275412>')

  if message.content.startswith('lifelessAstonished'):
    quote=get_quote()
    await message.channel.send('<:OhhAisa:837558942262493195>')

  if message.content.startswith('lifelessInnocent'):
    quote=get_quote()
    await message.channel.send('<:Innocent:837676007779467325>')

  if message.content.endswith('lifelessCute'):
    quote=get_quote()
    await message.channel.send('<a:cutegirl:842992585378103296>')

  if message.content.startswith('Hi Lifeless!'):
    quote=get_quote()
    await message.channel.send(lifelessemoji+lifelessemoji+lifelessemoji)

 #Music Part of LifelessBot

client1=commands.Bot(command_prefix='lifeless2')
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " \n" +"- "+ json_data[0]['a']
  return(quote)
@client1.event
async def on_ready():
  activity = discord.Activity(type=discord.ActivityType.listening, name="The Sweetness of Lifeless")
  await client1.change_presence(status=discord.Status.idle, activity=activity)
  print('We have logged in as {0.user}'.format(client1))

@client1.command()
async def Cute(ctx):
  await ctx.send('<a:cutegirl:842992585378103296>')
@client1.command()
async def Hello(ctx):
  await ctx.send('Hello, Hello, Hello! This is LifelessBot2 reciprocating the Sweetness of Coordinate Bond. :heart:')
@client1.command()
async def Kick(ctx):
  await ctx.send('Sorry! SSAV is too sweet to kick/ban sweet people! <a:cutecat:842966553321275412>')
@client1.command()
async def Ban(ctx):
  await ctx.send('Sorry! SSAV is too sweet to kick/ban sweet people! <a:cutecat:842966553321275412>')
@client1.command()
async def Inspire(ctx):
  quote=get_quote()
  await ctx.send('_Here is an inspirational quote from the sweetness factory of us_ :heart:'+'\n'+'\n'+quote)
@client1.command()
async def Sowiee(ctx):
  await ctx.send('<:Sowiee:837558958071611412>')
@client1.command()
async def Cutecat(ctx):
  await ctx.send('<a:cutecat:842966553321275412>')
@client1.command()
async def Vibe(ctx):
  await ctx.send(lifelessemoji+lifelessemoji+lifelessemoji)
@client1.command()
async def Emotes(ctx):
  await ctx.send("_Here are our favourite emotes_"+'\n'+lifelessemoji+mycandy+balbasaur+girlkiss+girlagree+pinkheart+discogirl+cute+hoodie+'<a:cutecat:842966553321275412>')
@client1.command()
async def WishBirthdayChoti(ctx):
    await ctx.send("Happy birthday <@759116563159711814>! Missing you a lotttttttttttttttttttttttttttttttttttttttttttttt! Lots, lots and lots of loveeee for you... "+girlkiss+"-Opti Bhaiyya")
@client1.command(pass_context=True)
async def Connect(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client1.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
@client1.command(pass_context=True)
async def Disconnect(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        await server.disconnect()


@client1.command(pass_context=True)
async def join(ctx):
  channel=ctx.message.author.voice.voice_channel
  await client1.join_voice_channel(channel)

  LIFELESSTOKEN='ODQyOTM5MjExNTA5OTIzODYy.YJ8mUQ.JR73ff4u4cdi4eXWcb3SH00MDo8'
#my_secret = os.environ['LIFELESSTOKEN']

#Start of youtube_dl
players = {}

#Code Snippet is not running - START
@client1.command(pass_context=True)
async def ServerPlayDev1(ctx, search):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client1.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    guild = ctx.message.guild
    voice_client = guild.voice_client
    player = await voice_client.create_ytdl_player(video)
    players[server.id] = player
    player.start()
#Code Snippet is not running - STOP

@client1.command()
async def Play(ctx,*, url1 : str):
    await ctx.send("Please wait! Searching for your sweetness... "+cutecat)
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Please wait for the current playing music to end or use the 'lifelessStop' command. Love Love <a:cutegirl:842992585378103296>")
        return

    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client1.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    #voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': '249',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    url=""
    videosSearch = VideosSearch(url1, limit = 1)

    obj1=json.dumps(videosSearch.result())
    obj2=json.loads(obj1)
    for i in obj2['result']:
        url="https://www.youtube.com/watch?v="+(i['id'])
        title=i['title']

    #asyncio.run(search())






    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    await ctx.send("Let's vibe with the song!"+lifelessemoji)
    await ctx.send("Now Playing - ```"+title+"```")

@client1.command()
async def Replay(ctx):
    voice = get(client1.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    await ctx.send('I love to play the same song twice!.<a:cutecat:842966553321275412>')

@client1.command()
async def Stop(ctx):

    voice = get(client1.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send('I guess you cannot hear the sweetness anymore.<a:cutecat:842966553321275412>')




@client1.command()
async def DM(ctx, user: discord.User, *, message=None):
    message = message or "EVENT-1 '\n'Hello Hello <a:girlkiss:843491799246962708> '\n'Type **lifelessParticipate** to participate. "
    await user.send(message)


event_1_usernames_list=[]

@client1.command()
async def Participate(ctx):
    await ctx.send(f'Hi {ctx.author.mention}, thanks for your participation. Looking forward to your performance! {lifelessemoji}')
    event_1_usernames_list.append(ctx.message.author.display_name)

@client1.command()
async def ListEvent1(ctx):
    await ctx.send('This is the list of participants : {}'.format(', '.join(event_1_usernames_list)))

#Participate()
#event1=event1+username+'\n'



@client1.command()
async def Help(ctx):
  await ctx.send("```\nLifelessBot#7585 v1.1\nOpen Source Code, Link to repository: https://github.com/optimisticexquisite/LifelessBot\n...............................................\nPrefix: lifeless\nThe prefix of this bot is preset and cannot be changed.\n..................\nCommands to chill with this bot:\nlifelessCute\nlifelessHello\nlifelessKick\nlifelessBan\nlifelessSowiee\nlifelessCutecat\nlifelessVibe\nlifelessEmotes\nlifelessInspire : LifelessBot \n...................\nVoice commands:\nlifelessConnect : Connects LifelessBot to the same VC user is in.\nlifelessDisconnect : Disconnects LifelessBot from the VC.\nlifelessPlay <YouTube URL> : LifelessBot connects to VC and plays the music. (Limited to music duration - 30 mins)\nlifelessStop : LifelessBot stops the currently playing music.\nlifelessReplay : LifelessBot repeats the last song.\n...................\nEvent Management System :\nlifelessDM @USER : LifelessBot DMs the USER using the preset message.\nlifelessDM @USER <message> : LifelessBot DMs the USER the content written in <message>.\nlifelessParticipate : LifelessBot confirms the participation of the user in the event.\nlifelessListEvent1 : LifelessBot shows the list of participants seperated by ','.\n...................\nThis is as of now, all about the simple LifelessBot. The bot is getting updated continuosly.\nPlease note that the bot is a single instance bot. i.e. The voice activity cannot run at more than one VC at the same time.\n...................\nLifelessBot is hosted live on AMAZON WEB SERVICES server, located at Seattle, US which runs 24/7 at 1Gbps Internet Upload Speed.\nIf the bot stops working, please try pinging \"us-east-2.compute.amazonaws.com\" to check if the server is working properly.\nTo report bug, please DM OptimisticExquisite#8666 or email at sgtracer@gmail.com\nDevelopers are welcome to change the code and ask for a pull request at Github.\n...................\nThanks and Regards,\nOptimisticExquisite\n```")

#.............................................................................
#AI CAPABLE LIFELESSBOT2
@client1.command()
async def ImageAI1(ctx):

    await ctx.send("Please wait till I try to analyze the photo. Love, love! "+":heart:")
    with open('lifelessCred.csv','r') as input:
        next(input)
        reader = csv.reader(input)
        for line in reader:
            access_key_id = line[2]
            secret_access_key = line[3]
    global imageurl
    photo='image1.jpg'
    awsclient = boto3.client('rekognition',region_name='us-east-2',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)

    with open(photo,'rb') as source_image:
        source_bytes=source_image.read()

    response = awsclient.detect_labels(Image={'Bytes':source_bytes},MaxLabels=3,MinConfidence=95)
    await ctx.send("These are the possibilities Lifeless thinks, are present in your image. "+cutecat)
    #print(response)
    obj1=json.dumps(response)
    #result.json=response
    obj2=json.loads(obj1)
    for i in obj2['Labels']:
        await ctx.send("```"+i['Name']+"```")
    await ctx.send("Lifeless thanks you for using the LifelessBot AI. "+lifelessemoji)




imageurl=""
@client1.command()
async def Image1(ctx):
    global imageurl
    imageurl=ctx.message.attachments[0].url
    await ctx.send("Yayy! Lifeless received your image! "+girlagree+" Please go ahead and type **lifelessImageAI1** for analysis!")
    #import requests

    print('Beginning file download with requests')

    url = imageurl
    r = requests.get(url)

    with open('image1.jpg', 'wb') as f:
      f.write(r.content)

















#client.run(LIFELESSTOKEN)
client1.run(TOKEN)
