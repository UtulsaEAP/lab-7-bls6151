#Name: Braden Stanfield  Lab: Fri 3
def fileNameChange():
    #type your code here
    text = input()
    stuff = open(text).read().split()
    i = 0
    und = 0
    spilt = ""
    new = ""
    while i < len(stuff):
        und = stuff[i].find("_")
        spilt = stuff[i].split("_")
        new += spilt[0] + "_info.txt\n"
        i += 1
    
    print(new)
    return

if __name__ == '__main__':
    fileNameChange()