import random

cubeLines={150: {"legendary": { "%str" : ("STR: +12%", 3, [0]),
                                "%dex" : ("DEX: +12%", 3, [0]),
                                "%int" : ("INT: +12%", 3, [0]),
                                "%luk" : ("LUK: +12%", 3, [0]),
                                "%hp" : ("MaxHP: +12%", 3, [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17]),
                                "%mp" : ("MaxMP: +12%", 3, [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17]),
                                "%def": ("DEF: +12%", 4, [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17]), #5 to 4
                                "%atk": ("ATT: +12%", 3, [3,16,18]), 
                                "%matk": ("Magic ATT: +12%", 3, [3,16,18]),
                                "%damage": ("Damage: +12%", 3, [3,16,18]),
                                "%crit": ("Critical Rate: +12%", 3, [3,16,18]),
                                "%allstat": ("All Stats: 9%", 2, [0]),
                                "%critdmg": ("Critical Damage: +8%", 3, [13]),
                                "allskill3": ("All Skills: +3 (except 5th Job skills, and certain skills which only go up to the skill's master level)",2, [7]),
                                "allskill2": ("All Skills: +2 (except 5th Job skills, and certain skills which only go up to the skill's master level)",2, [7]),
                                "elementalresist": ("Elemental Resist: +10%", 3, [8]),
                                "abnormalstatus": ("Abnormal Status Resistance: +10", 3, [9]),
                                "35ied": ("Ignore Monster DEF: +35%", 3, [3,16,18]),
                                "40ied": ("Ignore Monster DEF: +40%", 3, [3,16,18]),
                                "ignoredamagedealt1": ("10% chance to ignore 20% of monster damage dealt", 5, [7,8,9,10,12,13,15,16]),
                                "ignoredamagedealt2": ("10% chance to ignore 40% of monster damage dealt", 5, [7,8,9,10,12,13,15,16]),
                                "iframe": ("Invincible for +3 more sec. when hit", 5, [8]),
                                "iframe2": ("4% chance to become invincible for 7 seconds when attacked", 5, [8]),
                                "reflect": ("30% chance to reflect 50% damage", 5, [9]),
                                "reflect2": ("30% chance to reflect 70% damage", 5, [9]),
                                "mpcost": ("Skill MP Cost: -15%", 5,  [1,2,5,6,11]),
                                "mpcost2": ("Skill MP Cost: -30%", 5, [1,2,5,6,11]),
                                "cd1": ("Skill Cooldown: -1 sec (-5% for under 10 sec, minimum cooldown of 10 sec)",3, [7]),
                                "cd2": ("Skill Cooldown: -2 sec (-5% for under 10 sec, minimum cooldown of 10 sec)",3, [7]),
                                "30boss": ("Boss Monster Damage: +30%",2, [3,16]),
                                "35boss": ("Boss Monster Damage: +35%",2, [3,16]),
                                "40boss": ("Boss Monster Damage: +40%",2, [3,16]),
                                "meso": ("Meso Obtained: +20%",3,[1,2,5,6,11]), #reduced to 3 from 5 based on data
                                "item": ("Item Drop Rate: +20%",3,[1,2,5,6,11]), #reduced to 3 from 5 based on data
                                "dco": ("Enables the <Decent Combat Orders> skill", 5, [10]),
                                "dab": ("Enables the <Decent Advanced Blessing> skill",5, [7]),
                                "dsi": ("Enables the <Decent Speed Infusion> skill", 5, [13]),
                                "atkperlevel":("Weapon ATT +1 per 10 Character Levels",3, [3,16,18]),
                                "matkperlevel":("Magic ATT +1 per 10 Character Levels",3, [3,16,18])},
                    "unique": { "%str" : ("STR: +9%", 3, [0]),
                                "%dex" : ("DEX: +9%", 3, [0]),
                                "%int" : ("INT: +9%", 3, [0]),
                                "%luk" : ("LUK: +9%", 3, [0]),
                                "%hp" : ("MaxHP: +9%", 3, [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17]),
                                "%mp" : ("MaxMP: +9%", 3, [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17]),
                                "%def": ("DEF: +9%", 5, [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17]),
                                "%atk": ("ATT: +9%", 3, [3,16,18]),
                                "%matk": ("Magic ATT: +9%", 3, [3,16,18]),
                                "%damage": ("Damage: +9%", 3, [3,16,18]),
                                "%crit": ("Critical Rate: +9%", 3, [3,16,18]),
                                "%allstat": ("All Stats: 6%", 2, [0]),
                                "allskill3": ("All Skills: +1 (except 5th Job skills, and certain skills which only go up to the skill's master level)",2, [7]),
                                "allskill2": ("All Skills: +2 (except 5th Job skills, and certain skills which only go up to the skill's master level)",2, [7]),
                                # "elementalresist": ("Elemental Resist: +10%", 3, [8]),
                                # "abnormalstatus": ("Abnormal Status Resistance: +10", 3, [9]),
                                "30ied": ("Ignore Monster DEF: +30%", 3, [3,16,18]),
                                "ignoredamagedealt1": ("5% chance to ignore 20% of monster damage dealt", 5, [7,8,9,10,12,13,15,16]),
                                "ignoredamagedealt2": ("5% chance to ignore 40% of monster damage dealt", 5, [7,8,9,10,12,13,15,16]),
                                "iframe": ("Invincible for +2 more sec. when hit", 5, [8]),
                                "iframe2": ("2% chance to become invincible for 7 seconds when attacked", 5, [8]),
                                "reflect": ("30% chance to reflect 50% damage", 5, [9]),
                                "reflect2": ("30% chance to reflect 70% damage", 5, [9]),
                                "hprecov": ("HP Recovery Items and Skills: +30%", 5,  [1,2,4,5,6,7,8,9,10,11,12,13,14,15,17]),
                                "30boss": ("Boss Monster Damage: +30%",2, [3,16]),
                                "20boss": ("Boss Monster Damage: +20%",2, [3,16]),
                                "dhaste": ("Enables the <Decent Haste> skill", 5, [10]),
                                "dse": ("Enables the <Decent Sharp Eyes> skill",5, [13]),
                                "dhb": ("Enables the <Decent Hyper Body> skill", 5, [9]),
                                "ddoor": ("Enables the <Decent Mystic Door> skill", 5, [7]),
                                "dexperlevel":("DEX per 10 Character Levels +1",5, [13]),
                                "intperlevel":("INT per 10 Character Levels +1",5, [13]),
                                "lukperlevel":("LUK per 10 Character Levels +1",5, [13]),
                                "strperlevel":("STR per 10 Character Levels +1",5, [13])}
                    }
}
nonwepbpot=[1,2,4,5,6,7,8,9,10,11,12,13,14,15,17]
wepbpot=[3,16,18]
bonuscubeLines={150: {"legendary": {"%str" : ("STR: +7%", 2, nonwepbpot),
                                "%dex" : ("DEX: +7%", 2, nonwepbpot),
                                "%int" : ("INT: +7%", 2, nonwepbpot),
                                "%luk" : ("LUK: +7%", 2, nonwepbpot),
                                "str" : ("STR: +18", 3, nonwepbpot),
                                "dex" : ("DEX: +18", 3, nonwepbpot),
                                "int" : ("INT: +18", 3, nonwepbpot),
                                "luk" : ("LUK: +18", 3, nonwepbpot),
                                "atk" : ("ATT: +14", 2, nonwepbpot),
                                "atk" : ("Magic ATT: +14", 2, nonwepbpot),
                                "def" : ("DEF: +200", 5, nonwepbpot),
                                "hp" : ("MaxHP: +300", 3, nonwepbpot),
                                "mp" : ("MaxMP: +300", 3, nonwepbpot),
                                "%hp" : ("MaxHP: +10%", 3, nonwepbpot),
                                "%mp" : ("MaxMP: +10%", 3, nonwepbpot),
                                "%critdmg1": ("Critical Damage: +3%", 2, [13]),
                                "%critdmg2": ("Critical Damage: +1%", 2, nonwepbpot),
                                "%allstat1": ("All Stats: 5%", 2, nonwepbpot),
                                "elementalresist": ("Elemental Resist: +5%", 1, nonwepbpot),
                                "abnormalstatus": ("Abnormal Status Resistance: +5", 1, nonwepbpot),
                                "dexperlevel":("DEX per 10 Character Levels +2",3, nonwepbpot),
                                "intperlevel":("INT per 10 Character Levels +2",3, nonwepbpot),
                                "lukperlevel":("LUK per 10 Character Levels +2",3, nonwepbpot),
                                "strperlevel":("STR per 10 Character Levels +2",3, nonwepbpot),
                                "%def": ("DEF: +10%", 5, nonwepbpot), #5 to 4
                                "cd1": ("Skill Cooldown: -1 sec (-5% for under 10 sec, minimum cooldown of 10 sec)",3, [7]),
                                "meso": ("Meso Obtained: +5%",3,nonwepbpot), #reduced to 3 from 5 based on data
                                "item": ("Item Drop Rate: +5%",3,nonwepbpot), #reduced to 3 from 5 based on data
                                "allskill2": ("All Skills: +2 (except 5th Job skills, and certain skills which only go up to the skill's master level)",5, [7]),
                                "hprecov": ("HP Recovery Items and Skills: +30%", 3,  nonwepbpot),         
                                "%str2" : ("STR: +12%", 12, wepbpot),
                                "%dex2" : ("DEX: +12%", 12, wepbpot),
                                "%int2" : ("INT: +12%", 12, wepbpot),
                                "%luk2" : ("LUK: +12%", 12, wepbpot),
                                "%allstat2": ("All Stats: 9%", 8, wepbpot),
                                "%atk2": ("ATT: +12%", 16, wepbpot), 
                                "%matk2": ("Magic ATT: +12%", 16, wepbpot),
                                "%damage2": ("Damage: +12%", 12, wepbpot),
                                "%crit2": ("Critical Rate: +12%", 12, wepbpot),
                                "%hp2" : ("MaxHP: +10%", 16, wepbpot),
                                "%mp2" : ("MaxMP: +10%", 8, wepbpot),
                                "abnormalstatus2": ("Abnormal Status Resistance: +5", 6, wepbpot),
                                "18boss": ("Boss Monster Damage: +18%",4, wepbpot),
                                "5ied": ("Ignore Monster DEF: +5%", 1, wepbpot),
                                "dexperlevel2":("DEX per 10 Character Levels +2",12, wepbpot),
                                "intperlevel2":("INT per 10 Character Levels +2",12, wepbpot),
                                "lukperlevel2":("LUK per 10 Character Levels +2",12, wepbpot),
                                "strperlevel2":("STR per 10 Character Levels +2",12, wepbpot),
                                "atkperlevel2":("Weapon ATT +1 per 10 Character Levels",6, wepbpot),
                                "matkperlevel2":("Magic ATT +1 per 10 Character Levels",6, wepbpot)},
                    "unique": { "%str" : ("STR: +5%", 2, nonwepbpot),
                                "%dex" : ("DEX: +5%", 2, nonwepbpot),
                                "%int" : ("INT: +5%", 2, nonwepbpot),
                                "%luk" : ("LUK: +5%", 2, nonwepbpot),
                                "str" : ("STR: +16", 3, nonwepbpot),
                                "dex" : ("DEX: +16", 3, nonwepbpot),
                                "int" : ("INT: +16", 3, nonwepbpot),
                                "luk" : ("LUK: +16", 3, nonwepbpot),
                                "atk" : ("ATT: +12", 2, nonwepbpot),
                                "atk" : ("Magic ATT: +12", 2, nonwepbpot),
                                "def" : ("DEF: +150", 5, nonwepbpot),
                                "hp" : ("MaxHP: +240", 3, nonwepbpot),
                                "mp" : ("MaxMP: +240", 3, nonwepbpot),
                                "%hp" : ("MaxHP: +7%", 3, nonwepbpot),
                                "%mp" : ("MaxMP: +7%", 3, nonwepbpot),
                                "%allstat1": ("All Stats: 4%", 2, nonwepbpot),
                                "elementalresist": ("Elemental Resist: +4%", 1, nonwepbpot),
                                "abnormalstatus": ("Abnormal Status Resistance: +4", 1, nonwepbpot),
                                "dexperlevel":("DEX per 10 Character Levels +1",3, nonwepbpot),
                                "intperlevel":("INT per 10 Character Levels +1",3, nonwepbpot),
                                "lukperlevel":("LUK per 10 Character Levels +1",3, nonwepbpot),
                                "strperlevel":("STR per 10 Character Levels +1",3, nonwepbpot),
                                "%def": ("DEF: +7%", 5, nonwepbpot), #5 to 4
                                "%str2" : ("STR: +9%", 12, wepbpot),
                                "%dex2" : ("DEX: +9%", 12, wepbpot),
                                "%int2" : ("INT: +9%", 12, wepbpot),
                                "%luk2" : ("LUK: +9%", 12, wepbpot),
                                "%allstat2": ("All Stats: 6%", 6, wepbpot),
                                "%atk2": ("ATT: +9%", 6, wepbpot), 
                                "%matk2": ("Magic ATT: +9%", 6, wepbpot),
                                "%damage2": ("Damage: +9%", 6, wepbpot),
                                "%crit2": ("Critical Rate: +9%", 6, wepbpot),
                                "%hp2" : ("MaxHP: +7%", 6, wepbpot),
                                "%mp2" : ("MaxMP: +7%", 6, wepbpot),
                                "12boss": ("Boss Monster Damage: +12%",4, wepbpot),
                                "4ied": ("Ignore Monster DEF: +4%", 1, wepbpot),
                                "dexperlevel2":("DEX per 10 Character Levels +1",6, wepbpot),
                                "intperlevel2":("INT per 10 Character Levels +1",6, wepbpot),
                                "lukperlevel2":("LUK per 10 Character Levels +1",6, wepbpot),
                                "strperlevel2":("STR per 10 Character Levels +1",6, wepbpot),
                                "hprecovdamagedealt1": ("15% chance to recover 95 HP when attacking.", 10, wepbpot),
                                "mprecovdamagedealt2": ("15% chance to recover 95 MP when attacking.", 10, wepbpot)}
                            

                        }
}
#
itemType = {"ring": 1,
            "pendant": 2,
            "weapon": 3,
            "belt": 4,
            "face": 5,
            "eye": 6,
            "hat": 7,
            "top": 8,
            "bottom": 9,
            "shoes": 10,
            "earrings": 11,
            "shoulder": 12,
            "gloves": 13,
            "cape": 15,
            "heart": 14,
            "secondary": 16,
            "badge": 17,
            "emblem": 18
}


cubetypes={ "equality": 1,
            "violet" : 2,
            "black" : 3,
            "red" : 4,
            "bonus": 5,
            "one": 6
        }


cubetypes2={ 1:"equality",
            2:"violet",
            3:"black",
            4:"red",
            5:"bonus",
            6:"one"
        }
cubedata={} #id:{cubesleft:int,
                #cubesused:int,
                #potential:[],
                #itemID:int,
                #item:string
                #}}
def savePotentialdata(user,cubesused,potential,itemID=3,itemname="weapon",cubetype="equality"):
    global cubedata
    if user not in cubedata.keys():
        cubedata[user]={"cubesleft":1000, "cubesused":0, "potential":potential, "itemID":itemID, "item":itemname, "cubetype": cubetypes[cubetype]}
    else:
        cubedata[user]["cubesleft"]-=cubesused
        cubedata[user]["cubesused"]+=cubesused
        cubedata[user]["potential"]=potential
        cubedata[user]["itemID"]=itemID
        cubedata[user]["item"]=itemname
        cubedata[user]["cubetype"]=cubetypes[cubetype]
        if cubesused==-1:
            cubedata[user]["cubesused"]=0


def rollPotentialfromDiscord(id,potential_line=None):
    global cubedata
    global cubetypes2
    if id not in cubedata.keys():
        return None, -1
    else:
        itemID=cubedata[id]["itemID"]
        oldpotential=cubedata[id]["potential"]
        index, potential=roll_potential(itemID,cubedata[id]["cubetype"],potential_line)
        savePotentialdata(id,1,potential,itemID,cubedata[id]["item"],cubetypes2[cubedata[id]["cubetype"]])
        return potential, index

def resetCubes(cubes):
    global cubedata
    for user in cubedata.keys():
        cubedata[user]["cubesleft"]=cubes
        





    



initializedweightedlist=False
def getLines():
    global initializedweightedlist
    if not initializedweightedlist:
        initialize_weighted_list()
        initialize_weighted_bonus_list()
        initializedweightedlist=True

weighted_potential_dict={}
def initialize_weighted_list():
    global itemType
    global cubeLines
    global weighted_potential_dict
    weighted_potential_dict["legendary"]={}
    weighted_potential_dict["unique"]={}
    for item in itemType.values():
        potential_list = []
        for line in cubeLines[150]["legendary"].values():
            if item in line[2] or 0 in line[2]:
                for weight in range(line[1]):
                    potential_list.append(line[0])
        weighted_potential_dict["legendary"][item]=potential_list
        potential_list=[]
        for line in cubeLines[150]["unique"].values():
            if item in line[2] or 0 in line[2]:
                for weight in range(line[1]):
                    potential_list.append(line[0])
        weighted_potential_dict["unique"][item]=potential_list

weighted_bonus_potential_dict={}
def initialize_weighted_bonus_list():
    global itemType
    global cubeLines
    global weighted_bonus_potential_dict
    weighted_bonus_potential_dict["legendary"]={}
    weighted_bonus_potential_dict["unique"]={}
    for item in itemType.values():
        bonus_potential_list = []
        for line in bonuscubeLines[150]["legendary"].values():
            if item in line[2] or 0 in line[2]:
                for weight in range(line[1]):
                    bonus_potential_list.append(line[0])
        weighted_bonus_potential_dict["legendary"][item]=bonus_potential_list
        bonus_potential_list=[]
        for line in bonuscubeLines[150]["unique"].values():
            if item in line[2] or 0 in line[2]:
                for weight in range(line[1]):
                    bonus_potential_list.append(line[0])
        weighted_bonus_potential_dict["unique"][item]=bonus_potential_list

def roll_random_line(itemID, tier):
    global weighted_potential_dict
    potential_list = weighted_potential_dict[tier][itemID]
    return potential_list[random.randrange(len(potential_list))]

def roll_random_bonus_line(itemID, tier):
    global weighted_bonus_potential_dict
    bonus_potential_list = weighted_bonus_potential_dict[tier][itemID]
    return bonus_potential_list[random.randrange(len(bonus_potential_list))]


def roll_potential(itemID,cubeID, potential_list=None):
    potential_list=potential_list[0:3]
    if cubeID==cubetypes["equality"]:
        result=roll_equality(itemID)
        return -1, result
    if cubeID==cubetypes["violet"]:
        result=roll_violet(itemID)
        return -1, result
    if cubeID==cubetypes["red"]:
        result=roll_red(itemID)
        return -1, result
    if cubeID==cubetypes["black"]:
        result=roll_black(itemID)
        return -1, result
    if cubeID==cubetypes["bonus"]:
        result=roll_bonus(itemID)
        return -1, result
    if cubeID==cubetypes["one"]:
        index, result=roll_one(itemID,potential_list)
        return index, result


def roll_bonus(itemID):
    tier="legendary"
    getLines()
    bonus_potential_list=[]
    bonus_potential_list.append(roll_random_bonus_line(itemID,tier))
    while len(bonus_potential_list) != 3:
        if random.randint(1,10)==1:
            tier="legendary"
        else:
            tier="unique"
        pot=roll_random_bonus_line(itemID,tier)
        if len([bonus_potential for bonus_potential in bonus_potential_list if "Boss" in bonus_potential]) == 2:
            while "Boss" in pot:
                pot=roll_random_bonus_line(itemID,tier)
        if len([bonus_potential for bonus_potential in bonus_potential_list if "Invincibility for +3 more sec. when hit" in bonus_potential]) == 1:
            while "Invincibility for +" in pot:
                pot=roll_random_bonus_line(itemID,tier)
        if len([bonus_potential for bonus_potential in bonus_potential_list if "Ignore Monster" in bonus_potential]) == 2:
            while "Ignore Monster" in pot:
                pot=roll_random_bonus_line(itemID,tier)
        bonus_potential_list.append(pot)
    return bonus_potential_list

def roll_violet(itemID):
    tier="legendary"
    getLines()
    potential_list=[]
    potential_list.append(roll_random_line(itemID,tier))
    while len(potential_list) != 6:
        if random.randint(1,10)==1:
            tier="legendary"
        else:
            tier="unique"
        pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Boss" in potential]) == 2:
            while "Boss" in pot:
                pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Invincibility for +3 more sec. when hit" in potential]) == 1:
            while "Invincibility for +" in pot:
                pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Ignore Monster" in potential]) == 2:
            while "Ignore Monster" in pot:
                pot=roll_random_line(itemID,tier)
        potential_list.append(pot)
    return potential_list


def roll_equality(itemID):

    tier="legendary"
    getLines()
    potential_list=[]
    potential_list.append(roll_random_line(itemID,tier))
    while len(potential_list) != 3:
        pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Boss" in potential]) == 2:
            while "Boss" in pot:
                pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Invincibility for +3 more sec. when hit" in potential]) == 1:
            while "Invincibility for +" in pot:
                pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Ignore Monster" in potential]) == 2:
            while "Ignore Monster" in pot:
                pot=roll_random_line(itemID,tier)
        potential_list.append(pot)
    return potential_list
    # tier="legendary"
    # getLines()
    # potential_list=[]
    # potential_list.append(roll_random_line(itemID,tier))
    # potential_list.append(roll_random_line(itemID,tier))
    # potential_list.append(roll_random_line(itemID,tier))
    # if "Boss" in potential_list[0] and "Boss" in potential_list[1]:
    #     while "Boss" in potential_list[2]:
    #         potential_list[2]=roll_random_line(itemID)
    # if "Ignore Monster" in potential_list[0] and "Ignore Monster" in potential_list[1]:
    #     while "Ignore Monster" in potential_list[2]:
    #         potential_list[2]=roll_random_line(itemID)
    
    # while len([potential for potential in potential_list if "Invincibility for +3 more sec. when hit" in potential]) > 1:
    #         pot=roll_random_line(itemID,tier)
    # return potential_list

def roll_one(itemID,potential_list:list):
    tier="legendary"
    getLines()
    if len(potential_list)<3:
        return -1, None
    index=random.randint(0,2)
    potential_list.pop(index)
    while len(potential_list) != 3:
        if random.randint(1,10)==1:
            tier="legendary"
        else:
            tier="unique"
        pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Boss" in potential]) == 2:
            while "Boss" in pot:
                pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Invincibility for +3 more sec. when hit" in potential]) == 1:
            while "Invincibility for +" in pot:
                pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Ignore Monster" in potential]) == 2:
            while "Ignore Monster" in pot:
                pot=roll_random_line(itemID,tier)
        potential_list.insert(index,pot)
    return index,potential_list

def roll_red(itemID):
    tier="legendary"
    getLines()
    potential_list=[]
    potential_list.append(roll_random_line(itemID,tier))
    while len(potential_list) != 3:
        if random.randint(1,10)==1:
            tier="legendary"
        else:
            tier="unique"
        pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Boss" in potential]) == 2:
            while "Boss" in pot:
                pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Invincibility for +3 more sec. when hit" in potential]) == 1:
            while "Invincibility for +" in pot:
                pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Ignore Monster" in potential]) == 2:
            while "Ignore Monster" in pot:
                pot=roll_random_line(itemID,tier)
        potential_list.append(pot)
    return potential_list

def roll_black(itemID):
    tier="legendary"
    getLines()
    potential_list=[]
    potential_list.append(roll_random_line(itemID,tier))
    while len(potential_list) != 3:
        if random.randint(1,100)<24:
            tier="legendary"
        else:
            tier="unique"
        pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Boss" in potential]) == 2:
            while "Boss" in pot:
                pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Invincibility for +3 more sec. when hit" in potential]) == 1:
            while "Invincibility for +" in pot:
                pot=roll_random_line(itemID,tier)
        if len([potential for potential in potential_list if "Ignore Monster" in potential]) == 2:
            while "Ignore Monster" in pot:
                pot=roll_random_line(itemID,tier)
        potential_list.append(pot)
    return potential_list

def getItemID(id,itemname):
    global cubetypes
    global cubedata
    if itemname in itemType.keys():
        if id in cubedata.keys():
            savePotentialdata(id,-1,[],itemType[itemname], itemname,cubetypes2[cubedata[id]["cubetype"]] )
        else:            
            savePotentialdata(id,-1,[],itemType[itemname], itemname)
        return itemType[itemname]
    else:
        return None
        
def select_violet_potential(potentials_index:set,potentials):
    new_potential=[]
    if(len(potentials_index)!=3):
        return None
    for index in potentials_index:
        new_potential.append(potentials[index])
    return new_potential

def select_violet_potential_from_discord(potentials_index:set,id):
    if id not in cubedata.keys():
        return None
    cubedata[id]["potential"]=select_violet_potential(potentials_index,cubedata[id]["potential"])
    return cubedata[id]["potential"]


def getCubeID(id,itemname):
    global cubetypes
    global cubedata
    if itemname in cubetypes.keys():
        if id in cubedata.keys():
            savePotentialdata(id,0,[],cubedata[id]["itemID"],cubedata[id]["item"],cubetype=itemname)
        else:            
            savePotentialdata(id,0,[],cubetype=itemname)
        return cubetypes[itemname]
    else:
        return None
# def getTrials(lines, itemID, lineRequirement):
#     trials=[]
#     for _ in range(1000):

#         desiredLines=0
#         count=0
#         while desiredLines<lineRequirement:
#             potentials=roll_potential(itemID)
#             count+=1
#             desiredLines=checkPotential(lines, potentials)
#             if count>1000000:
#                 return None #impossible lines
#         trials.append(count)
    
# def checkPotential(lines, potential):
#     pass

# def check1LPotential(lines, potential):
#     count=3-len(lines)
#     for i in range(3):
#         for line in lines:
#             if line.upper() in potential[i]:
#                 count+=1
#     return count



# def check2LPotential(lines, potential):
#     count=3-len(lines)
#     for i in range(3):
#         for line in lines:
#             pool=getMatchingPotentialLines(line)
#             for p in pool:
#                count+=potential.count(p)
        


# def check3LPotential(lines,potential):
#     count=3-len(lines)

# def getMatchingPotentialLines(line):
#     linestrings=[]
#     for key in cubeLines.keys():
#         if line.upper() in key.upper():
#             linestrings.append(cubeLines[key][0])
#     return linestrings

# accessoryType=[1,2,4,5,6,11]
# armorType=[7,8,9,10,12,13,15]


# count=1
# itemID=7
# # potentials=roll_potential(itemID)

# critdmglines=0
# secondaryline=0
# searchline="Cooldown: -2"
# searchline2=["Cooldown: -1"]
# triallist=[]
# for _ in range(5000):
#     potentials=roll_potential(itemID)
#     count=1
#     critdmglines=0
#     secondaryline=0
#     while  (critdmglines<2 or secondaryline<0):
#         potentials=roll_potential(itemID)
#         count+=1
#         critdmglines=0
#         secondaryline=0
#         for i in range(3):
#             if searchline.upper() in potentials[i].upper():
#                 critdmglines+=1
#         for i in range(3):
#             for secondline in searchline2:
#                 if secondline.upper() in potentials[i].upper():
#                     secondaryline+=1
#     # print(potentials)
#     # print(count)
#     triallist.append(count)
# import statistics
# print("AVG:")
# print(sum(triallist)/len(triallist))
# print("Median:")
# print(statistics.median(triallist))
# print("P(x<=30")
# print(len([x for x in triallist if x<=30])/len(triallist))
# print("P(x<=100")
# print(len([x for x in triallist if x<=100])/len(triallist))
# print("P(x<=300")
# print(len([x for x in triallist if x<=300])/len(triallist))
# print("P(x<=51")
# print(len([x for x in triallist if x<=51])/len(triallist))


# itemType = {"ring": 1,
#             "pendant": 2,
#             "weapon": 3,
#             "belt": 4,
#             "face": 5,
#             "eye": 6,
#             "hat": 7,
#             "top": 8,
#             "bottom": 9,
#             "shoes": 10,
#             "earrings": 11,
#             "shoulder": 12,
#             "gloves": 13,
#             "cape": 15,
#             "heart": 14,
#             "secondary": 16,
#             "badge": 17,
#             "emblem": 18
# }