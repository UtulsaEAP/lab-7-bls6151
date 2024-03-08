#Name: Braden Stanfield  Lab: Fri 3
def wordInRange():
    #Type your code here
    strung = input()
    top = input()
    bot = input()
    stuff = open(strung).read().split()
    i = 0

    while i < len(stuff):
        if top <= stuff[i]:
            if bot >= stuff[i]:
                print(stuff[i] + " - in range")
            else:
                print(stuff[i] + " - not in range")
        else:
            print(stuff[i] + " - not in range")
            
        i += 1
   # ./Problem 2/input1.txt
    #ammoniated
    #millennium
if __name__ == '__main__':
    wordInRange()