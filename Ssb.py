from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_role
import discord
import asyncio
from nexonlib.ssbdata import pssbdata
import random
# from discord import Intents

# class PSSB():
#     def __init__(self,id):
#         self.id=id
#         self.restockused=0
#         self.restockleft=250
        
#     def buyrestocks(self,amount):
#         self.restockleft+=amount

#     def restock(self):
#         if self.restockleft>0:
#             self.restockused+=1
#             self.restockleft-=1
#             return self.getitems()
#         else:
#             return []

#     def getitems(self):
#         global magicwagondata
#         weightedmagicwagon=[item for item in magicwagondata for _ in range(item[3]) if item[2]<=self.restockused]
#         itemlist=[]
#         while len(itemlist) != 6:
#             candidate=random.choice(weightedmagicwagon)
#             if candidate in itemlist:
#                 continue
#             else:
#                 itemlist.append(candidate)
#         return itemlist

#     def getrestocks(self):
#         return (self.restockused,self.restockleft)
#     def resetrestocks(self):
#         self.restockused=0
#         self.restockleft=10000

class SsbCog(commands.Cog):
    
    def __init__(self,bot):
        self.client=bot
        self.boxcount={}
        self.reroll_processing={}
        self.totalbox=0

    @commands.command(pass_context=True)    
    async def pssb(self,ctx,*args):
        if ctx.author.id not in self.boxcount.keys():
            self.boxcount[ctx.author.id]=[22,0]
        self.boxcount[ctx.author.id][0]-=1
        self.boxcount[ctx.author.id][1]+=1
        e=discord.Embed(title="Premium Surprise Style Box",color=0x9d3077)
        reward=random.choice(pssbdata)
        e.add_field(name="Remaining", value=str("N/A"),inline=True)#self.boxcount[ctx.author.id][0]
        e.add_field(name="Used", value=str(self.boxcount[ctx.author.id][1]),inline=True)
        e.add_field(name="Item", value=reward[0]+" ("+str(reward[2])+")",inline=False)

        e.set_image(url=reward[3])
        self.totalbox+=1
        roll_message=await ctx.send(content=ctx.author.mention ,embed=e)
        self.reroll_processing[ctx.author.id]={"message": roll_message, "context":ctx}
        await roll_message.add_reaction(emoji=self.client.get_emoji(798358884078977074))
        f = open("aliciapluspssb.txt", "a")
        f.write("Discord name = "+str(ctx.author.name)+" "+ str(ctx.author.id))
        f.write("\t")
        f.write("Boxes used = "+str(self.boxcount[ctx.author.id][1]))
        f.write("\t")
        f.write("Server name = "+str(ctx.guild.name))
        f.write("\t")
        f.write("Channel name = "+str(ctx.channel.name))
        f.write("\n")
        print(str(self.totalbox)+" PSSB Discord name = "+str(ctx.author.name)+" "+ str(ctx.author.id),"Server name = "+str(ctx.guild.name),"Channel name = "+str(ctx.channel.name))

        



    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.id == self.client.user.id:
            return
        if reaction.emoji==self.client.get_emoji(798358884078977074): #pssb
            if reaction.message.author.id !=self.client.user.id:
                return
            await self.pssb(self.reroll_processing[user.id]["context"])
        #await self.process_add_violet_line(reaction, user)




    async def process_add_violet_line(self, reaction, user):

        if user.id in self.violet_cube_processing.keys() and reaction.emoji in self.violet_cube_reactions.keys() and reaction.message.id==self.violet_cube_processing[user.id]["message"].id:
            self.violet_cube_processing[user.id]["selected_lines"].add(self.violet_cube_reactions[reaction.emoji])
            #print(self.violet_cube_processing[user.id]["selected_lines"])
            if len(self.violet_cube_processing[user.id]["selected_lines"])==3:
                await self.violet_cube_processing[user.id]["message"].add_reaction("✅")
            elif len(self.violet_cube_processing[user.id]["selected_lines"])>3:
                await self.violet_cube_processing[user.id]["message"].remove_reaction("✅", self.client.user)
        if user.id in self.violet_cube_processing.keys() and reaction.message.id==self.violet_cube_processing[user.id]["message"].id:
            if reaction.emoji=="✅" and len(self.violet_cube_processing[user.id]["selected_lines"])==3:
                potential=select_violet_potential_from_discord(self.violet_cube_processing[user.id]["selected_lines"], user.id)
                await self.update_potential(user.id, potential)
                await self.violet_cube_processing[user.id]["message"].add_reaction(emoji=self.client.get_emoji(796233177273466931))
            if reaction.emoji==self.client.get_emoji(796233177273466931):
                await self.cube(self.violet_cube_processing[user.id]["context"])




        
def setup(client):
    client.add_cog(SsbCog(client))