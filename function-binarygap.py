def ConvertToBinary(num):
    mybin = []
    divider = num / 2
    remainder = num % 2
    mybin.append(remainder)

    while divider != 0:
    #print ("before ", divider)
    #print(divider)
    #print (divider)
        remainder = divider % 2
        mybin.append(remainder)
        divider = divider/2
        #mybin.reverse()
    return mybin[::-1]
#result = ConvertToBinary(32)

#print result
#d = [0,1,0,0,0,0.0]
def BinaryGap(d):
    countOfZeros = 0
    sumOfZerosB = 0
    lastsum = 0
    #print a[0]
    for i in range(len(d)):
        if d[i] == 0:
            countOfZeros= countOfZeros + 1
        else:
            sumOfZerosB = countOfZeros
            countOfZeros = 0
        if sumOfZerosB > lastsum:
            lastsum = sumOfZerosB
    return lastsum

def solution(n):
    print (BinaryGap(ConvertToBinary(n)))

solution(1041)

