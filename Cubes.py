from nexonlib.cubelines import *
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_role
import discord
import asyncio
# from discord import Intents
class Cubes(commands.Cog):
    
    def __init__(self,bot):
        self.client=bot
        self.cubecount=28000
        self.violet_cube_reactions={"1️⃣":0, "2️⃣":1, "3️⃣": 2, "4️⃣": 3, "5️⃣": 4, "6️⃣": 5}
        self.black_cube_reactions={"1️⃣":0, "2️⃣":1}
        self.violet_cube_processing={}#id:{"potential": potential, "message": cube_message, "selected_lines": set(), "context":ctx}
        intents = discord.Intents.default()
        intents.members = True
        intents.reactions = True
    # @commands.command(pass_context=True)
    # async def setItem(self,ctx,*args):
    #     itemID=getItemID(ctx.author.id,args[0].lower())
    #     if ctx.author.id in self.violet_cube_processing.keys():
    #         self.violet_cube_processing.pop(ctx.author.id)
    #     if itemID is None:
    #         e=discord.Embed(title="Available items", color=0xbbdbb4,description='\n!setcube '.join([""]+list(itemType.keys())))
    #         await ctx.send(embed=e)
    #     else:
    #         await ctx.send("Your "+cubedata[ctx.author.id]["item"]+" is ready to be "+cubetypes2[cubedata[ctx.author.id]["cubetype"]] +" cubed")

    @commands.command(pass_context=True, aliases=["setItem"])
    async def setitem(self,ctx,*args):
        if len(args)==0:
            e=discord.Embed(title="Available items", color=0xbbdbb4 , description='\n!setitem '.join([""]+list(itemType.keys())))
            await ctx.send(embed=e)
            return
        itemID=getItemID(ctx.author.id,args[0].lower())
        if ctx.author.id in self.violet_cube_processing.keys():
            self.violet_cube_processing.pop(ctx.author.id)
        if itemID is None:
            e=discord.Embed(title="Available items", color=0xbbdbb4 , description='\n!setitem '.join([""]+list(itemType.keys())))
            await ctx.send(embed=e)
        else:
            await ctx.send("Your "+cubedata[ctx.author.id]["item"]+" is ready to be "+cubetypes2[cubedata[ctx.author.id]["cubetype"]] +" cubed")

    @commands.command(pass_context=True)
    async def setcube(self,ctx,*args):
        # if ctx.author.id in self.violet_cube_processing.keys():
        #     self.violet_cube_processing.pop(ctx.author.id)
        if len(args)==0:
            e=discord.Embed(title="Available cubes", color=0xb4bbdb, description='\n!setcube '.join([""]+list(cubetypes.keys())))
            await ctx.send(embed=e)
            return
        # if args[0].lower()=="one" and ctx.author.id not in self.violet_cube_processing.keys() or len(self.violet_cube_processing[ctx.author.id]["potential"])<3:
        #     await ctx.send("You do not have an existing potential to use combining cube on--set and use a different cube first before using this")
        #     return
        cubeID=getCubeID(ctx.author.id,args[0].lower())
        if cubeID is None:
            e=discord.Embed(title="Available cubes", color=0xb4bbdb, description='\n!setcube '.join([""]+list(cubetypes.keys())))
            await ctx.send(embed=e)
        else:
            if ctx.author.id in self.violet_cube_processing.keys():
                self.violet_cube_processing[ctx.author.id]["cubetype"]=cubeID
            await ctx.send("Your "+cubedata[ctx.author.id]["item"]+" is ready to be "+cubetypes2[cubedata[ctx.author.id]["cubetype"]] +" cubed")

    @commands.command(pass_context=True)
    async def cube(self,ctx):
        global cubedata
        # if ctx.author.id not in self.violet_cube_processing.keys():
        #     self.violet_cube_processing[ctx.author.id]={"potential": potential, "message": cube_message, "selected_lines": set(), "context":ctx, "cubetype":  cubedata[ctx.author.id]["cubetype"] }
        if ctx.author.id in cubedata.keys() and cubedata[ctx.author.id]["cubesleft"]==0:
            await ctx.send("You have no more cubes")
            return
        if cubedata[ctx.author.id]["cubetype"]==6 and (ctx.author.id not in self.violet_cube_processing.keys() or len(self.violet_cube_processing[ctx.author.id]["potential"])<3):
             await ctx.send("You do not have an existing potential to use combining cube on--set and use a different cube first before using this")
             return
        if ctx.author.id in self.violet_cube_processing.keys():
            copyofpot=self.violet_cube_processing[ctx.author.id]["potential"].copy()
            potential, index=rollPotentialfromDiscord(ctx.author.id,copyofpot)
        else:
            potential, index=rollPotentialfromDiscord(ctx.author.id,[])

        if potential is None and cubedata[ctx.author.id]["cubetype"]==6:
            await ctx.send("You do not have an existing potential to use combining cube on--set and use a different cube first before using this")
            return
        elif potential is None:
            await ctx.send("An error has occurred. (set item to fix? `!info` for commands)")
            return
        self.cubecount+=1
        temp=[]
        cubename="N/A"
        cube_reaction_id=0
        if cubedata[ctx.author.id]["cubetype"]==1:
            cubename="Cube of Equality"
            cube_reaction_id=798358977247051846
        elif cubedata[ctx.author.id]["cubetype"]==2:
            cubename="Violet Cube - Select 3 potentials"
        elif cubedata[ctx.author.id]["cubetype"]==3:
            cubename="Black Cube"
            cube_reaction_id=798358999589191710
        elif cubedata[ctx.author.id]["cubetype"]==4:
            cubename="Red Cube"
            cube_reaction_id=798359023442460693
        elif cubedata[ctx.author.id]["cubetype"]==5:
            cubename="Bonus Potential Cube"
            cube_reaction_id=799466785593360405
        elif cubedata[ctx.author.id]["cubetype"]==6:
            cubename="Combining Cube"
            cube_reaction_id=806334002352488538
            if ctx.author.id not in self.violet_cube_processing.keys() or len(self.violet_cube_processing[ctx.author.id]["potential"])<3:
                await ctx.send("2. You do not have an existing potential to use combining cube on--set and use a different cube first before using this")
                return
        e=discord.Embed(title=str(cubename),description=cubedata[ctx.author.id]["item"],color=0x009933)
        if cubename=="Black Cube":
            if ctx.author.id not in self.violet_cube_processing.keys() or len(self.violet_cube_processing[ctx.author.id]["potential"])<3:
                e.add_field(name="Before", value="N/A", inline=False) 
            else:
                e.add_field(name="Before", value='\n'.join(self.violet_cube_processing[ctx.author.id]["potential"][0:3]), inline=False)
                
            e.add_field(name="After", value='\n'.join(potential), inline=False)
        elif cubedata[ctx.author.id]["cubetype"]==2:
            e.add_field(name="Legendary", value='\n'.join([list(self.violet_cube_reactions)[i]+" "+potential[i] for i in range(len(potential))]),inline=False)
        elif index != -1: #combining cube
            temp=potential.copy() #temp is new pot, potential is old
            potential=self.violet_cube_processing[ctx.author.id]["potential"][0:3].copy()
            potential2=potential.copy()
            potential2[index]="[**"+potential2[index]+"**]"
            e.add_field(name="Legendary", value='\n'.join(potential2), inline=False)

            
        else:
            e.add_field(name="Legendary", value='\n'.join(potential), inline=False)
        e.add_field(name="Cubes left", value=cubedata[ctx.author.id]["cubesleft"],inline=True)
        e.add_field(name="Cubes used", value=cubedata[ctx.author.id]["cubesused"], inline=True)
        cube_message=await ctx.send(content=ctx.author.mention ,embed=e)



        if cubedata[ctx.author.id]["cubetype"]==2: #violet
            self.violet_cube_processing[ctx.author.id]={"potential": potential, "message": cube_message, "selected_lines": set(), "context":ctx, "cubetype":  cubedata[ctx.author.id]["cubetype"] }
            for reaction in self.violet_cube_reactions.keys():
                await cube_message.add_reaction(reaction)
        elif cubedata[ctx.author.id]["cubetype"]==3: #black
            if ctx.author.id in self.violet_cube_processing.keys():
                prevpot=self.violet_cube_processing[ctx.author.id]["potential"][0:3]  
            else:
                prevpot=[]
            self.violet_cube_processing[ctx.author.id]={"potential": prevpot+potential, "message": cube_message, "selected_lines": set(), "context":ctx, "cubetype":  cubedata[ctx.author.id]["cubetype"] }
            for reaction in self.black_cube_reactions.keys():
                await cube_message.add_reaction(reaction)
            await cube_message.add_reaction(emoji=self.client.get_emoji(cube_reaction_id))
        elif cubedata[ctx.author.id]["cubetype"]==6: #combining
            await cube_message.add_reaction("✅")
            await cube_message.add_reaction("❌")
            await cube_message.add_reaction(emoji=self.client.get_emoji(cube_reaction_id))
        else:
            self.violet_cube_processing[ctx.author.id]={"potential": potential, "message": cube_message, "selected_lines": set(), "context":ctx, "cubetype":  cubedata[ctx.author.id]["cubetype"]}
            await cube_message.add_reaction(emoji=self.client.get_emoji(cube_reaction_id))

        if index != -1:
            self.violet_cube_processing[ctx.author.id]={"potential": potential, "message": cube_message, "selected_lines": set(), "context":ctx, "cubetype":  cubedata[ctx.author.id]["cubetype"]}
            def startcheck(reaction,user):
                return ((reaction.emoji =="✅" or reaction.emoji=="❌") and user.id==ctx.author.id and reaction.message.id==cube_message.id)
            startreaction,user=await self.client.wait_for('reaction_add', check=startcheck)
            if cube_message.id != self.violet_cube_processing[ctx.author.id]["message"].id:
                return
            e=discord.Embed(title=str(cubename),description=cubedata[ctx.author.id]["item"],color=0x009933)


            if startreaction.emoji=="✅":
                potential=temp
            #elif startreaction.emoji==self.client.get_emoji(806334002352488538):
            e.add_field(name="Legendary", value='\n'.join(potential), inline=False)
            e.add_field(name="Cubes left", value=cubedata[ctx.author.id]["cubesleft"])
            e.add_field(name="Cubes used", value=cubedata[ctx.author.id]["cubesused"])
            await cube_message.edit(embed=e)

                
            self.violet_cube_processing[ctx.author.id]={"potential": potential, "message": cube_message, "selected_lines": set(), "context":ctx, "cubetype":  cubedata[ctx.author.id]["cubetype"]}
            

        f = open("aliciaplus.txt", "a")
        f.write("Total cubes used = "+str(self.cubecount))
        f.write("\t")
        f.write("Discord name = "+str(ctx.author.name)+" "+ str(ctx.author.id))
        f.write("\t")
        f.write("Cubes left = "+str(cubedata[ctx.author.id]["cubesleft"]))
        f.write("\t")
        f.write("Server name = "+str(ctx.guild.name))
        f.write("\t")
        f.write("Item = "+str(cubedata[ctx.author.id]["item"]))
        f.write("\t")
        f.write("Cube = "+str(cubetypes2[cubedata[ctx.author.id]["cubetype"]]))
        f.write("\t")
        f.write("Channel name = "+str(ctx.channel.name))
        f.write("\n")
        print(str(self.cubecount)+" "+str(cubetypes2[cubedata[ctx.author.id]["cubetype"]])+" Discord name = "+str(ctx.author.name)+" "+ str(ctx.author.id),"Server name = "+str(ctx.guild.name),"Channel name = "+str(ctx.channel.name),"Cubes left = "+str(cubedata[ctx.author.id]["cubesleft"]),"Item = "+str(cubedata[ctx.author.id]["item"]))
    

    @commands.command(pass_context=True)
    async def smega(self,ctx):
        global cubedata
        channel=self.client.get_channel(789802273723121704)
        e=discord.Embed(title="Cube of Equality",description=cubedata[ctx.author.id]["item"],color=0x009933)
        e.add_field(name="Legendary", value='\n'.join(cubedata[ctx.author.id]["potential"]))
        e.add_field(name="Cubes left", value=cubedata[ctx.author.id]["cubesleft"])
        e.add_field(name="Cubes used", value=cubedata[ctx.author.id]["cubesused"])
        await channel.send(embed=e, content=ctx.author.mention)

    @commands.command(pass_context=True)
    @has_role("Alicia")
    async def cubereset1(self,ctx,*args):
        resetCubes(int(args[0]))

    @commands.Cog.listener()
    async def on_message(self, message):
        pass
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.id == self.client.user.id:
            return
        if user.id in self.violet_cube_processing.keys():
            await self.process_add_violet_line(reaction, user)
            await self.process_add_black_line(reaction, user)
        await self.process_cube_reaction(reaction,user)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if user.id == self.client.user.id:
            return
        if user.id in self.violet_cube_processing.keys():
            await self.process_remove_violet_line(reaction, user)

    
    async def update_potential(self,userid, potential):
        global cube
        msg=self.violet_cube_processing[userid]["message"]
        if self.violet_cube_processing[userid]["cubetype"]==2:
            e=discord.Embed(title=str("Violet Cube"),description=cubedata[userid]["item"],color=0x009933)
        elif self.violet_cube_processing[userid]["cubetype"]==3:
            e=discord.Embed(title=str("Black Cube"),description=cubedata[userid]["item"],color=0x009933)
        e.add_field(name="Legendary", value='\n'.join(potential))
        e.add_field(name="Cubes left", value=cubedata[userid]["cubesleft"])
        e.add_field(name="Cubes used", value=cubedata[userid]["cubesused"])
        await msg.edit(embed=e)

    async def process_cube_reaction(self, reaction, user):
        if reaction.message.author.id !=self.client.user.id:
            return
        if reaction.emoji==self.client.get_emoji(798358977247051846): #equality
            if self.violet_cube_processing[user.id]["cubetype"] !=1:
                self.violet_cube_processing[user.id]["cubetype"]=getCubeID(user.id,"equality")
            await self.cube(self.violet_cube_processing[user.id]["context"])
        elif reaction.emoji==self.client.get_emoji(798358999589191710): #black
            if self.violet_cube_processing[user.id]["cubetype"] !=3:
                self.violet_cube_processing[user.id]["cubetype"]=getCubeID(user.id,"black")
            await self.cube(self.violet_cube_processing[user.id]["context"])
        elif reaction.emoji==self.client.get_emoji(798359023442460693): #red
            if self.violet_cube_processing[user.id]["cubetype"] !=4:
                self.violet_cube_processing[user.id]["cubetype"]=getCubeID(user.id,"red")
            await self.cube(self.violet_cube_processing[user.id]["context"])
        elif reaction.emoji==self.client.get_emoji(796233177273466931): #violet
            if self.violet_cube_processing[user.id]["cubetype"] !=2:
                self.violet_cube_processing[user.id]["cubetype"]=getCubeID(user.id,"violet")
            await self.cube(self.violet_cube_processing[user.id]["context"])
        elif reaction.emoji==self.client.get_emoji(799466785593360405): #bonus
            if self.violet_cube_processing[user.id]["cubetype"] !=5:
                self.violet_cube_processing[user.id]["cubetype"]=getCubeID(user.id,"bonus")
            await self.cube(self.violet_cube_processing[user.id]["context"])
        elif reaction.emoji==self.client.get_emoji(806334002352488538): #combining           
            if self.violet_cube_processing[user.id]["cubetype"] !=6:
                self.violet_cube_processing[user.id]["cubetype"]=getCubeID(user.id,"one")
            await self.cube(self.violet_cube_processing[user.id]["context"])
    async def process_add_black_line(self, reaction, user):
        if self.violet_cube_processing[user.id]["cubetype"] != 3:
            return
        if user.id in self.violet_cube_processing.keys() and reaction.emoji in self.black_cube_reactions.keys() and self.violet_cube_processing[user.id]["message"] != None and reaction.message.id==self.violet_cube_processing[user.id]["message"].id:
            if self.black_cube_reactions[reaction.emoji]==0 or (self.black_cube_reactions[reaction.emoji]==1 and len(self.violet_cube_processing[user.id]["potential"])==3):
                self.violet_cube_processing[user.id]["potential"]=self.violet_cube_processing[user.id]["potential"][0:3]
                await self.update_potential(user.id, self.violet_cube_processing[user.id]["potential"])
                self.violet_cube_processing[user.id]["message"]=None
            elif self.black_cube_reactions[reaction.emoji]==1:
                self.violet_cube_processing[user.id]["potential"]=self.violet_cube_processing[user.id]["potential"][3:]
                await self.update_potential(user.id, self.violet_cube_processing[user.id]["potential"])
                self.violet_cube_processing[user.id]["message"]=None
    async def process_add_violet_line(self, reaction, user):
        if reaction.message.author.id !=self.client.user.id:
            return
        if self.violet_cube_processing[user.id]["cubetype"] != 2:
            return
        if user.id in self.violet_cube_processing.keys() and reaction.emoji in self.violet_cube_reactions.keys() and self.violet_cube_processing[user.id]["message"] != None  and reaction.message.id==self.violet_cube_processing[user.id]["message"].id:
            self.violet_cube_processing[user.id]["selected_lines"].add(self.violet_cube_reactions[reaction.emoji])
            #print(self.violet_cube_processing[user.id]["selected_lines"])
            if len(self.violet_cube_processing[user.id]["selected_lines"])==3:
                await self.violet_cube_processing[user.id]["message"].add_reaction("✅")
            elif len(self.violet_cube_processing[user.id]["selected_lines"])>3:
                await self.violet_cube_processing[user.id]["message"].remove_reaction("✅", self.client.user)
        if user.id in self.violet_cube_processing.keys() and self.violet_cube_processing[user.id]["message"] != None and reaction.message.id==self.violet_cube_processing[user.id]["message"].id:
            if reaction.emoji=="✅" and len(self.violet_cube_processing[user.id]["selected_lines"])==3:
                potential=select_violet_potential_from_discord(self.violet_cube_processing[user.id]["selected_lines"], user.id)
                await self.update_potential(user.id, potential)
                await self.violet_cube_processing[user.id]["message"].add_reaction(emoji=self.client.get_emoji(796233177273466931))
                self.violet_cube_processing[user.id]["message"]=None



    async def process_remove_violet_line(self, reaction, user):
        if self.violet_cube_processing[user.id]["cubetype"] != 2:
            return
        if user.id in self.violet_cube_processing.keys() and reaction.emoji in self.violet_cube_reactions.keys() and reaction.message.id==self.violet_cube_processing[user.id]["message"].id:
            self.violet_cube_processing[user.id]["selected_lines"].remove(self.violet_cube_reactions[reaction.emoji])
            if len(self.violet_cube_processing[user.id]["selected_lines"])==3:
                await self.violet_cube_processing[user.id]["message"].add_reaction("✅")
            elif len(self.violet_cube_processing[user.id]["selected_lines"])<3:
                try:
                    await self.violet_cube_processing[user.id]["message"].remove_reaction("✅",self.client.user)
                except Exception:
                    print("Failed to remove reaction")




        
def setup(client):
    client.add_cog(Cubes(client))