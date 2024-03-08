#Name: Braden Stanfield  Lab: Fri 3
def courseGrade():
    
    # TODO: Declare any necessary variables here. 
      
      
    # TODO: Read a file name from the user and read the tsv file here. 
    bot = "./Problem 3/" + input()
    stuff = open(bot).read().split()
    h = len(stuff)
    i = 0
    j = open("report.txt", "w+")
    total = 0
    num = 0
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    while i < h:
        total += int(stuff[i +2]) + int(stuff[i + 3]) + int(stuff[i + 4])
        grade = "F"
        if total/3 >= 90:
            grade = "A"
        elif total/3 >= 80:
            grade = "B"
        elif total/3 >= 70:
            grade = "C"
        elif total/3 >= 60:
            grade = "D"
        j.write(str(stuff[i]))
        total = 0
        i += 5
    j.close()
    return
# + " " + stuff[i + 1] + " " stuff[i + 2] + " " +stuff[i] + " " + stuff[i] + " " + grade
if __name__ == "__main__":
    courseGrade()
    
    