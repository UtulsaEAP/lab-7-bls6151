#Name: Braden Stanfield  Lab: Fri 3
def courseGrade():
    
    # TODO: Declare any necessary variables here. 
      
      
    # TODO: Read a file name from the user and read the tsv file here. 
    bot =  input()
    stuff = open(bot).read().split()
    h = len(stuff)
    i = 0
    j = open("./Problem 3/report1.txt", "w")
    total = 0
    num = 0
    mid1 = 0
    mid2 = 0
    fin = 0
    stri = ""
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    while i < h:
        total += int(stuff[i +2]) + int(stuff[i + 3]) + int(stuff[i + 4])
        mid1 += int(stuff[i+2])
        mid2 += int(stuff[i+3])
        fin += int(stuff[i+4])
        grade = "F"
        if total/3 >= 90:
            grade = "A"
        elif total/3 >= 80:
            grade = "B"
        elif total/3 >= 70:
            grade = "C"
        elif total/3 >= 60:
            grade = "D"
        stri += stuff[i] + " " + stuff[i + 1] + " " + stuff[i + 2] + " " +stuff[i+3] + " " + stuff[i+4] + " " + grade + "\n" 
        
        total = 0
        i += 5
    stri += "Averages: midterm1: " + (str("%.2f"%(mid1/(h/5)))) + ", midterm2: " + (str("%.2f"%(mid2/(h/5)))) + ", final: " + (str("%.2f"%(fin/(h/5))))
    j.write(stri)
    j.close()
    return

if __name__ == "__main__":
    courseGrade()
    
    