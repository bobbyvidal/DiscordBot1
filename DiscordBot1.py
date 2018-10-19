import discord
from discord.ext import commands
import time
import datetime
import requests
import asyncio
from bs4 import BeautifulSoup

bot = commands.Bot(command_prefix='!', description='A bot that greets the user back.')


@bot.event
async def on_ready():
    
    # sends message to terminal indicating login
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(' ^ _ ^ ')
    print('~~~~~~~~')
       
# command that asks if we are playing games
@bot.command()
async def ask(ctx):
    
    # gets server/channel data and compiles members into a list
    server = bot.get_guild(478044952920588288)
    channel = server.get_channel(478044952920588291)
    teamLst = []
    for i in ctx.guild.members:
        if str(i.status) == 'online':
            teamLst.append(i)
        elif str(i.status) == 'idle':
            teamLst.append(i)

    # sends the message to the channel 
    await channel.send('When do you guys want to play games tonight? ' + teamLst[0].mention + ' ' +teamLst[1].mention + ' ' +teamLst[2].mention + ' ' +teamLst[3].mention + ' ' + teamLst[4].mention + ' ' + teamLst[5].mention+ ' ' + teamLst[6].mention)

# greets user with timestamp log
@bot.command()
async def greet(ctx):
   
    author = ctx.author
    print (str(author) + ' greeted')
    print ('-----Timestamp: {:%Y-%m-%d %H:%M:%S}-----'.format(datetime.datetime.now()))
    commandMessage = ctx.message
    await commandMessage.delete()
    await ctx.send("Hello, there!")

# parses data from weather.com
@bot.command()
async def weather(ctx):
    
    # scraping weather.com for temp, feels like, and cloud coverage
    page = requests.get('https://weather.com/weather/today/l/USTX0617:1:US')
    soup = BeautifulSoup(page.content, 'html.parser')
    todayStuff = soup.find(class_= 'today_nowcard-section today_nowcard-condition')
    nowTemp = todayStuff.find(class_='today_nowcard-temp').get_text()
    nowFeels = todayStuff.find(class_='deg-feels').get_text()
    nowDescription = todayStuff.find(class_= 'today_nowcard-phrase').get_text()

    # printing to the server w/ scraped data
    await ctx.send("The temperature is: " + nowTemp)
    await ctx.send("The temperature feels like: " + nowFeels)
    await ctx.send("It looks __" + nowDescription + "__ outside.")
    print ('-----Timestamp: {:%Y-%m-%d %H:%M:%S}-----'.format(datetime.datetime.now()))

# prints the latest fortnite news
@bot.command()
async def topPost(ctx):

     #starts scraping
    page = requests.get('https://www.epicgames.com/fortnite/en-US/news')
    soup = BeautifulSoup(page.content, 'html.parser')
    nowActivity = soup.find(class_= 'top-featured-activity')
    aNow = nowActivity.find('a')
    aUrl = aNow['href']
    #combines epicgames url with the 'a' extension
    await ctx.send('Lastest news on fortnite coming right up!')
    await ctx.send('https://www.epicgames.com' + aUrl)

# prints the latest three fortnite posts    
@bot.command()
async def topPosts(ctx):
    
    hrefLst = []
    # begin scraping
    page = requests.get('https://www.epicgames.com/fortnite/en-US/news')
    soup = BeautifulSoup(page.content, 'html.parser')
    nowActivity = soup.find(class_= 'top-featured-activity')
    aNow = nowActivity.find('a')
    hrefLst.append(aNow['href'])
    # past two activities 
    pastActivity = soup.find(class_ = 'grid-layout container-fluid')
    aPastLst = pastActivity.find_all('a')
    for activity in aPastLst:
        hrefLst.append(activity['href'])
        if len(hrefLst) == 3:
            break
    for item in hrefLst:
        await ctx.send('https://www.epicgames.com' + item)

@bot.command()
async def commands(ctx):
    
    # gives a list of the commands possible
    commandList = ['topPosts', 'topPost', 'weather', 'ask', 'greet']
    await ctx.send('These are some of the commands I can perfom: ' 
    + '!' + commandList[0] + ' ' + '!' + commandList[1] + ' ' + '!' + commandList[2] + ' ' + '!' 
    + commandList[3] + ' ' + '!' + commandList[4] + ' ')


@bot.command()
async def getWord(ctx):

    page = requests.get('https://www.dictionary.com/wordoftheday/')
    soup = BeautifulSoup(page.content, 'html.parser')
    randWord = soup.find(class_= 'tile-image')
    randImg = randWord.find('img')
    imgURL = randImg['src']
    await ctx.send(imgURL)
    












bot.run('NDcwNjQ1MTY5MDEyODY3MTEy.DmEMZw.hL8fDUoWR135FuB7E7w_oKygn2c')



# fn team ids 131100075945492480, 232609309467344896, 134874474087579648, 135959846565445632
# test server number = 470644476340338690, channel number = 470644476340338696
# main server number = 478044952920588288 , channel number = 478044952920588291


















