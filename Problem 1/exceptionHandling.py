#Name: Braden Stanfield  Lab: Fri 3
def exceptionHandling():
    # Split input into 2 parts: name and age
    parts = input().split()
    name = parts[0]
    while name != '-1':
        # FIXME: The following line will throw ValueError exception.
        #        Insert try/except blocks to catch the exception.
        try: 
            age = int(parts[1]) + 1
        except ValueError:
            print(f'{name} 0')
        else:

            age = int(parts[1]) + 1
            print(f'{name} {age}')

        
        # Get next line
        parts = input().split()
        name = parts[0]
        #"Huw 29","Jaspar 49","Melina Lynn 32","Quinta 13","Mina Ny 38","Hanna 28","-1"  
        #"Huw 30","Jaspar 50","Melina 0","Quinta 14","Mina 0","Hanna 29"

if __name__ == '__main__':
    exceptionHandling()