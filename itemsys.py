import item
 
import random
 
###Item System by Mitsunari-san###
 
#rarity chart
rarechart = ["C","U","R","RR","RRR"]
 
def generate_item(): #limit 10 random items per floor unless special events occur.
        getlist = 0
        rID = random.randrange(115) #50 common, 30 uncommon, 20 rare, 10 super rare, 5 ultra rare
                                   
        if 50 <= rID and rID <= 79:
                getlist = 1
        elif 80 <= rID and rID <= 99:
                getlist = 2
        elif 100 <= rID and rID <= 109:
                getlist = 3
        elif rID >= 110:
                getlist = 4
        ID = random.randrange(len(item.catalog[getlist]))
        return item.catalog[getlist][ID]


#aka godmod, but we'll use this to make a Vulnerary.
def make_item(nameofitem):
        for i in range(len(item.catalog)):
            for j in range(len(item.catalog[i])):
                if item.catalog[i][j].name == nameofitem:
                    return item.catalog[i][j]
        print("Warning! No such item exists.")
        return