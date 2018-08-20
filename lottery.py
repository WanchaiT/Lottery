from random import randint
import time

def showStatIfWin(cost ,countBuyLottery ,myNumber ,currentRound ,currentYear ,randomNumber ,month):
    print(" ====================================")
    print("Count buy = " ,countBuyLottery)
    print("My Number = " ,myNumber)
    print("Jackpot   = " ,randomNumber)
    print("Round     = " ,currentRound)
    print("Month     = " ,month)
    print("Year      = " ,currentYear)
    print("Money     = " ,6000000 - cost)

def showStat(cost ,countBuyLottery ,myNumber ,currentRound ,currentYear ,randomNumber ,month):
    print(countBuyLottery ," : " ,myNumber ," : " ,randomNumber ," : " ,currentRound ," : " ,month ," : " ,currentYear ," : " ,cost)

def checkLottery(myNumber ,numRandom):
    if(myNumber == numRandom):
        return True
    else:
        return False

def randomNum():
    return randint(0,999999)

def nextYear(currentMonth ,currentYear):
    if(currentMonth == 11):
        currentYear += 1
        return currentYear
    else:
        return currentYear

def nextMonth(currentMonth):
    if(currentMonth == 11):
        return 0
    else:
        currentMonth += 1
        return currentMonth

def totalCost(cost):
    cost += 80
    return cost

def totalBuyLottery(count):
    count += 1
    return count

def totalRound(currentRound):
    if(currentRound == 1):
        return 2
    else:
        return 1

def main():
    t0 = time.time()
    cost = 0
    countBuyLottery = 0
    myNumber = int(input())
    month = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    currentRound = 2
    currentMonth = 7
    currentYear = 2018
    checkWin = False
    randomNumber = 0

    while(not checkWin):
        randomNumber = randomNum()
        checkWin = checkLottery(myNumber ,randomNumber)
        cost = totalCost(cost)
        countBuyLottery = totalBuyLottery(countBuyLottery)

        showStat(cost ,countBuyLottery ,myNumber ,currentRound ,currentYear ,randomNumber ,month[currentMonth])
        #print(countBuyLottery ," : " ,myNumber ," : " ,randomNumber ," : " ,currentRound ," : " ,month[currentMonth] ," : " ,currentYear ," : " ,cost)
        if(checkWin):
            showStatIfWin(cost ,countBuyLottery ,myNumber ,currentRound ,currentYear ,randomNumber ,month[currentMonth])
            break

        currentRound = totalRound(currentRound)
        currentYear = nextYear(currentMonth ,currentYear)
        currentMonth = nextMonth(currentMonth)

    print(time.time() - t0)

main()
