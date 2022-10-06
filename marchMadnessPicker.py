import random

def pickBracket():

    def gameWinner(seedA,seedB):
        if seedA==1 and seedB==16:
            odds=.993
        elif seedA==2 and seedB==15:
            odds=.938
        else:
            odds=.91*max(seedA,seedB)/(seedA+seedB)
        if odds>random.uniform(0,1):
            return min(seedA,seedB)
        else:
            return max(seedA,seedB)

    def getRegionalChamp():
        field=[1,16,8,9,5,12,4,13,6,11,3,14,7,10,2,15]
        roundOf32=[]
        sweet16=[]
        elite8=[]

        for index in range(16)[::2]:
            roundOf32.append(gameWinner(field[index],field[index+1]))
        print('Round of 32:',tuple(roundOf32))

        for index in range(8)[::2]:
            sweet16.append(gameWinner(roundOf32[index],roundOf32[index+1]))
        print('Sweet 16:',tuple(sweet16))

        for index in range(4)[::2]:
            elite8.append(gameWinner(sweet16[index],sweet16[index+1]))
        print('Elite 8:',tuple(elite8))

        regionalChamp=gameWinner(elite8[0],elite8[1])
        print('Regional Champ: ('+str(regionalChamp)+')')
        return regionalChamp


    print('\nTOP LEFT REGION')
    topLeft=getRegionalChamp()

    print('\nBOTTOM LEFT REGION')
    bottomLeft=getRegionalChamp()

    print('\nTOP RIGHT REGION')
    topRight=getRegionalChamp()

    print('\nBOTTOM RIGHT REGION')
    bottomRight=getRegionalChamp()

    leftChamp=gameWinner(topLeft,bottomLeft)
    if topLeft==bottomLeft:
        if random.uniform(0,1)>.5:
            leftChampName='Top Left'
        else:
            leftChampName='Bottom Left'
    else:
        if leftChamp==topLeft:
            leftChampName='Top Left'
        else:
            leftChampName='Bottom Left'

    rightChamp=gameWinner(topRight,bottomRight)
    if topRight==bottomRight:
        if random.uniform(0,1)>.5:
            rightChampName='Top Right'
        else:
            rightChampName='Bottom Right'
    else:
        if rightChamp==topRight:
            rightChampName='Top Right'
        else:
            rightChampName='Bottom Right'

    nationalChamp=gameWinner(leftChamp,rightChamp)
    if leftChamp==rightChamp:
        if random.uniform(0,1)>.5:
            nationalChampName=leftChampName
            nationalChampNum=leftChamp
        else:
            nationalChampName=rightChampName
            nationalChampNum=rightChamp
    else:
        if nationalChamp==leftChamp:
            nationalChampName=leftChampName
            nationalChampNum=leftChamp
        else:
            nationalChampName=rightChampName
            nationalChampNum=rightChamp

    print('\nFINAL FOUR WINNERS: '+str(leftChampName)+' ('+str(leftChamp)+')  &  '+str(rightChampName)+' ('+str(rightChamp)+')')
    print('\nNATIONAL CHAMPION: '+str(nationalChampName)+' ('+str(nationalChampNum)+')\n\n')

pickBracket()