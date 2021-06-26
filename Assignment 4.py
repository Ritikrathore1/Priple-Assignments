myUniqueList = []
myLeftovers = []

def addToList(thing):
    if thing in myUniqueList:
        addtoLeftovers(thing)
        return False
    else:
        myUniqueList.append(thing)
        return True
    
def addtoLeftovers(thing):
    myLeftovers.append(thing)
    
print(myUniqueList) 
print(addToList("dog")) 
print(myUniqueList)
print(myLeftovers) 

print(addToList("dog")) 
print(myUniqueList) 
print(myLeftovers) 

print(addToList("cat")) 
print(myUniqueList) 
print(myLeftovers)  