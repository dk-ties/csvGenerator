#Imports############################
import csv
import time

#Global variable#######################
NUMBEROFCOL = ""
INTERVALDRECORD = 0.5
STOPSETPOINT = 5
FILELOCATION = ""
FILENAME = "test"

#Get input #####################

#NUMBEROFCOL = input()
#INTERVALDRECORD = input()


randomList = [
        ["Name", "English", "Math", "Science", "Social Science"],
        ["Varun", "91", "90", "74", "80"],
        ["Rahul", "89", "94", "81", "86"],
        ["Kabir", "80", "93", "88", "82"],
        ["Suman", "80", "75", "98", "85"],
    ]

#Function declaration###################
#newFile
def newFile():
    with open(FILENAME, 'w', newline= '') as f:
        writer = csv.writer(f)
        
        x = 0
        while x < STOPSETPOINT:
            print(x)
            writer.writerows(randomList)
            print("Time to get the first sleep")
            time.sleep(INTERVALDRECORD)
            x += 1
            
print("lets starrt")
newFile()         
print("Now its time to finish")












 
            
"""   write first line (Header)
        input to first header
            for each num in NUMBEROFCOL:
                write 'col' + num
    close file
    save file at newFilepath()
#locateFile
#open filelocater
    newFilepath = open_file() """



""" #Loops#########################
#Generator loop
input(NUMBEROFCOL)
input(INTERVALDRECORD)
input(STOPSETPOINT)
create new file()
    setup everything
ask for confirmation to start generate
log information to terminal for each generation
 """
