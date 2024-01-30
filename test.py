import random 

def sumNum(number):
    return number//10+number%10

def luna(cardNumber):
    evenNumbers = cardNumber[::2]
    oddNumbers = list(cardNumber[1::2])
    sumOddNumbers = 0
    for i in oddNumbers:
        sumOddNumbers+=int(i)
    k = 0
    summ = 0
    for i in evenNumbers:
        k = int(i)*2
        summ+=sumNum(k)
    return(summ+sumOddNumbers)%10 

def generateCardNumber(prefix=None):
    if prefix == None:
        result = '4'
    else:
        result = str(prefix)
    for i in range(len(result)+1,16):
        random.seed()
        result+=str(random.randint(1,9))
        # if(i%4 == 0):
        #     result+=' '
    #print(result)
    for i in range(0,9):
        if(luna((result+str(i)).replace(" ",'')) == 0):
            result+=str(i)
            return result