from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_role
import discord
import asyncio
from nexonlib.magicwagondata import magicwagondata
import random
# from discord import Intents

class MagicWagon():
    '''
    MagicWagon object that holds the information on user's MagicWagon status
    '''
    
    def __init__(self,id,used=0, left=250):
        self.id=id
        self.restockused=used
        self.restockleft=left
        
    def buyrestocks(self,amount):
        '''
        Input: integer number of restocks to purchase and add to current total
        Output: Outputs new remainint restocks left
        '''
        self.restockleft+=amount
        return self.restockleft

    def restock(self):
        '''
        Perform a full restock/reroll of MagicWagon. Returns a list of 6 new items.
        '''
        if self.restockleft>0:
            self.restockused+=1
            self.restockleft-=1
            return self.getitems()
        else:
            return []

    def getitems(self):
        '''
        Helper function that returns a list of 6 items based on user's current restock count
        '''
        global magicwagondata
        weightedmagicwagon=[item for item in magicwagondata for _ in range(item[3]) if item[2]<=self.restockused]
        itemlist=[]
        while len(itemlist) != 6:
            candidate=random.choice(weightedmagicwagon)
            if candidate in itemlist:
                continue
            else:
                itemlist.append(candidate)
        return itemlist

    def getrestocks(self):
        '''
        Returns a tuple (restocked used, restocks remaining)
        '''

        return (self.restockused,self.restockleft)
    def resetrestocks(self):
        '''
        Resets user back to initial state
        '''
        self.restockused=0
        self.restockleft=250

class MagicWagonCog(commands.Cog):
    '''
    MagicWagonCog that has all the MagicWagon functionality for discord.py
    '''
    def __init__(self,bot):
        self.client=bot
        self.restockcount={}
        self.reroll_processing={}
        self.totalrestocks=0
        
    @commands.command(pass_context=True)
    async def buyrestock(self, ctx, amount:int):
        '''
        Description: Increases and prints current restock amount.
        Input: command context, integer amount to increase restock by
        Output: None
        '''
        if ctx.author.id not in self.restockcount.keys():
            self.restockcount[ctx.author.id]=MagicWagon(ctx.author.id,0,amount)
        else:
            self.restockcount[ctx.author.id].buyrestocks(amount)
        e=discord.Embed(title="Magic Wagon",color=0x9966cc)
        e.add_field(name="Remaining", value=str(self.restockcount[ctx.author.id].getrestocks()[1]),inline=True)
        e.add_field(name="Used", value=str(self.restockcount[ctx.author.id].getrestocks()[0]),inline=True)
        roll_message=await ctx.send(content=ctx.author.mention ,embed=e)

    @commands.command(pass_context=True)
    async def resetmagicwagon(self, ctx):
        '''
        Description: Resets Magic Wagon to initial state for user who invokes it.
        Input: command context
        Output: None
        '''
        self.restockcount[ctx.author.id]=MagicWagon(ctx.author.id,0,250)

    @commands.command(pass_context=True)
    async def magicwagonuntil(self,ctx, *searchitems):
        '''
        Description: Runs Magic Wagon until item matches one of the items being searched for then responds to user 
                     with number it took to get as well as the full Magic Wagon set that got the prize.
        Input: command context, args of items to search for
        Output: None
        '''
        self.restockcount[ctx.author.id]=MagicWagon(ctx.author.id,0,2000)
        items=[]
        while len([item for item in items for searchitem in searchitems if searchitem.lower() in item[0].lower()])==0:
            items=self.restockcount[ctx.author.id].restock()    
            if len(items)==0:
                await ctx.send("Could not get within 2000 restocks")
                return
        e=discord.Embed(title="Magic Wagon Search", description=str(searchitems),color=0x9966cc)
        e.add_field(name="Used", value=str(self.restockcount[ctx.author.id].getrestocks()[0]),inline=True)
        e.add_field(name="Items", value='\n'.join([str(item[0])+" ("+item[1]+")" for item in items]),inline=False)
        roll_message=await ctx.send(content=ctx.author.mention ,embed=e)
        print("MWSearch "+str(searchitems)+" "+str(self.restockcount[ctx.author.id].getrestocks()[0])+" MagicWagon Discord name = "+str(ctx.author.name)+" "+ str(ctx.author.id),"Server name = "+str(ctx.guild.name),"Channel name = "+str(ctx.channel.name))
        self.restockcount[ctx.author.id].resetrestocks()

    @commands.command(pass_context=True)
    async def magicwagonuntilallof(self,ctx, *searchitems):
        '''
        Description: Runs Magic Wagon until item matches one of the items being searched for then responds to user 
                     with number it took to get as well as the full Magic Wagon set that got the prize.
        Input: command context, args of items to search for
        Output: None
        '''
        searchitems=list(searchitems)
        self.restockcount[ctx.author.id]=MagicWagon(ctx.author.id,0,2000)
        items=[]
        finalitems=set()
        finallength=len(searchitems)
        while len(finalitems)!=finallength:
            results=self.restockcount[ctx.author.id].restock()
            for result in results:
                for item in searchitems:
                    if item.lower() in result[0].lower():
                        items.append((result,self.restockcount[ctx.author.id].getrestocks()[0]))
                        finalitems.add(result[0])
                        #searchitems.remove(item)

            #print("items %d, searchitems %d" % (len(items), len(searchitems)))
            if len(results)==0:
                await ctx.send("Could not get all within 2000 restocks")
                if len(items)==0:
                    return
                else:
                    break
        e=discord.Embed(title="Magic Wagon Search",color=0x9966cc)
        e.add_field(name="Items", value='\n'.join([str(item[0][0])+" ("+item[0][1]+")" for item in items]),inline=True)
        e.add_field(name="Used", value='\n'.join([str(item[1]) for item in items]),inline=True)

        roll_message=await ctx.send(content=ctx.author.mention ,embed=e)
        print("MWSearch "+str(searchitems)+" "+str(self.restockcount[ctx.author.id].getrestocks()[0])+" MagicWagon Discord name = "+str(ctx.author.name)+" "+ str(ctx.author.id),"Server name = "+str(ctx.guild.name),"Channel name = "+str(ctx.channel.name))
        self.restockcount[ctx.author.id].resetrestocks()
        

    @commands.command(pass_context=True)
    async def magicwagon(self,ctx,*args):
        '''
        Description: Rerolls magicwagon for user who invokes this command. Sends embed/message containing 
                     information from MagicWagon object and adds reaction to give user to continue rerolling with single click
        Input: command context
        Output: None
        '''
        if ctx.author.id not in self.restockcount.keys():
            self.restockcount[ctx.author.id]=MagicWagon(ctx.author.id)
        items=self.restockcount[ctx.author.id].restock()
        if len(items)==0:
            await ctx.send("You don't have any restocks, use `buyrestock` command to purchase more restocks")
            return
        self.totalrestocks+=1
        e=discord.Embed(title="Magic Wagon",color=0x9966cc)
        e.add_field(name="Remaining", value=str(self.restockcount[ctx.author.id].getrestocks()[1]),inline=True)
        e.add_field(name="Used", value=str(self.restockcount[ctx.author.id].getrestocks()[0]),inline=True)
        e.add_field(name="Items", value='\n'.join([str(item[0])+" ("+item[1]+")" for item in items]),inline=False)
        roll_message=await ctx.send(content=ctx.author.mention ,embed=e)
        self.reroll_processing[ctx.author.id]={"message": roll_message, "context":ctx}
        await roll_message.add_reaction(emoji=self.client.get_emoji(798358941301080074))

        f = open("aliciaplusmw.txt", "a")
        f.write("Discord name = "+str(ctx.author.name)+" "+ str(ctx.author.id))
        f.write("\t")
        f.write("Restocks left = "+str(self.restockcount[ctx.author.id].getrestocks()[0]))
        f.write("\t")
        f.write("Server name = "+str(ctx.guild.name))
        f.write("\t")
        f.write("Channel name = "+str(ctx.channel.name))
        f.write("\n")
        print(str(self.totalrestocks)+" MagicWagon Discord name = "+str(ctx.author.name)+" "+ str(ctx.author.id),"Server name = "+str(ctx.guild.name),"Channel name = "+str(ctx.channel.name))



    @commands.command(pass_context=True)
    async def magicwagonreset(self,ctx,*args):
        pass
        #resetCubes(int(args[0]))

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.id == self.client.user.id: 
            return

        if reaction.emoji==self.client.get_emoji(798358941301080074): #magicwagon reroll reactions
            if reaction.message.author.id !=self.client.user.id:
                return
            await self.magicwagon(self.reroll_processing[user.id]["context"]) #invoke magicwagon command on reaction
        #await self.process_add_violet_line(reaction, user)




        
def setup(client):
    client.add_cog(MagicWagonCog(client))