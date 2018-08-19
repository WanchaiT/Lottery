from random import randint

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

def randomNum2():
    return randint(0,99)

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
    cost = 0
    countBuyLottery = 0
    myNumber = int(input())
    month = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    currentRound = 2
    currentMonth = 7
    currentYear = 2018
    checkWin = False
    randomNumber = 0
    amountFrom2 = 0
    myNumber2 = int(str(myNumber)[4] + str(myNumber)[5])
    count2 = 0
    check2 = False

    while(not checkWin):
        randomNumber = randomNum()
        randomNumber2 = randomNum2()
        print(myNumber2 , randomNumber2 , myNumber2 == randomNumber2)
        if(myNumber2 == randomNumber2):
            count2 += 1
            check2 = True
            amountFrom2 += 2000

        checkWin = checkLottery(myNumber ,randomNumber)
        cost = totalCost(cost)
        countBuyLottery = totalBuyLottery(countBuyLottery)

        #showStat(cost ,countBuyLottery ,myNumber ,currentRound ,currentYear ,randomNumber ,month[currentMonth])
        #print(countBuyLottery ," : " ,myNumber ," : " ,randomNumber ," : " ,currentRound ," : " ,month[currentMonth] ," : " ,currentYear ," : " ,cost)
        if(checkWin or check2):
            print()
            print(count2)
            print(cost)
            print(amountFrom2)
            print(amountFrom2 - cost)
            showStatIfWin(cost ,countBuyLottery ,myNumber ,currentRound ,currentYear ,randomNumber ,month[currentMonth])
            break

        currentRound = totalRound(currentRound)
        currentYear = nextYear(currentMonth ,currentYear)
        currentMonth = nextMonth(currentMonth)

main()
