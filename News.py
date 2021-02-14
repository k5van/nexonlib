from nexonlib.NexonCheck import *
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_role
from datetime import datetime
#from discordbots.coronalib.coronadb import *
import discord
import asyncio
import yaml
# from discord import Intents
class News(commands.Cog):
    
    def __init__(self,bot):
        self.client=bot
        self.configsetting={}
        self.configfilename="nexonlib/newsconfig.yaml"
        self.prevnews=0
        self.load()
        

    @commands.Cog.listener()
    async def on_ready(self):
        timecounter=1
        while True:
            try:
                await self.newsupdate(10100)
            except Exception:
                print("Failed to retrieve news")
            await asyncio.sleep(60)
    @commands.Cog.listener()
    async def newsupdate(self,ID):
        channel = self.client.get_channel(450813020470247426)
        news=latestNews(10100)
        if news["Id"]==-1 or int(news["Id"])==self.prevnews:
            return
        else:
            if news["Category"] in ["general","sale", "update", "maintenance"] or "Memo" in news["Title"]:
                e=discord.Embed(title=news["Title"]+" | Maplestory", description=news["Summary"],url=news["url"])
                e.set_author(name="Maplestory | "+news["Category"][0].upper()+news["Category"][1:])
                e.set_thumbnail(url=news["ImageThumbnail2"])
                await channel.send(embed=e)
                self.prevnews=int(news["Id"])
        self.save()

    def load(self):
        with open(self.configfilename,"r") as self.configfile:
            self.configsetting = yaml.full_load(self.configfile)
            self.prevnews=self.configsetting["prevnews"]
    
    def save(self):
        with open(self.configfilename,"w") as self.configfile:
            self.configsetting["prevnews"]=self.prevnews
            yaml.dump(self.configsetting, self.configfile)
            



        


def setup(client):
    client.add_cog(News(client))