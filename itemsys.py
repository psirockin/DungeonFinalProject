import item 
import random
 
###Item System by Mitsunari-san###
 
def generate_item(): #limit 10 random items per floor unless special events occur.
        ID = random.randrange(len(item.catalog[0]))
        return item.catalog[0][ID]


#aka godmod, but we'll use this to make a Vulnerary.
def godmake(nameofitem):
        for i in range(len(item.catalog)):
            for j in range(len(item.catalog[i])):
                if item.catalog[i][j].name == nameofitem:
                    return item.itemwrapper(item.catalog[i][j],None,None,None)
        print("Warning! No such item exists.")
        return
