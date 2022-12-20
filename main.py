# Part 1
def arrangeList(aList):
    tempList=[]

    for each in aList:
        if(type(each) == list):
            tempList.extend(arrangeList(each))
        else:
            tempList.append(each)

    return tempList


# Part 2
def reverseList(aList):
    tempList = []

    aList = aList[::-1]

    for each in aList:
        if(type(each) == list):
            tempList.append(reverseList(each))
        else:
            tempList.append(each)

    return tempList



print("For Part 1: ")
print(arrangeList([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))
print()
print("For Part 2: ")
print(reverseList([[1, 2], [3, 4], [5, 6, 7]]))