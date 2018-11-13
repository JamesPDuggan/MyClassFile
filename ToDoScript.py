
#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   James Duggan, 11/10/2018, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# fileObj = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------

objFileName = "C:\_PythonClass\Todo.txt"
strData = ""
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"
fileObj = open(objFileName, "r")
for item in fileObj: #Read each row of text data in the text file
     strData = item.split(",") #Split the row of text data at the comma
     #Create a dictionary row of the two elements
     dicRow = {"Task":strData[0].strip(), "Priority":strData[1].strip()}
     lstTable.append(dicRow) #Add each row to the table 
fileObj.close()  

# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options:
    1) Show current data.
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File.
    5) Exit Program.    """)
    strChoice = str(input("Enter the option would you like to perform? [1 to 4]: "))
    strChoice = strChoice.strip()
    print()#adding a new line

# Step 3 -Show the current items in the table
    if (strChoice == '1'):
        print("The current items in your ToDo list are:")
        for item in lstTable:
            print("\t" + item["Task"] + "--" + item["Priority"])
        
# Step 4 - Add a new item to the list/Table
    elif(strChoice == '2'):
        strTask = input("Enter the new task: ")
        strTask = strTask.strip()
        strPriority = input("Enter the priority: ")
        strPriority = strPriority.strip()
        dicRow = {"Task":strTask, "Priority": strPriority} #Create new row
        lstTable.append(dicRow) #Add the new row to lstTable
        print("\n" + strTask + " has been added.")
        
# Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        strDelete = input("Enter the task would you like to delete: ")
        strDelete = strDelete.strip()
       
        for item in lstTable: #Look at each row in lstTable
            if strDelete in item.values(): #Identify the right row
                lstTable.remove(item) #Delete the row
        print("\n"+ strDelete + " has been deleted.")  
        
# Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        fileObj = open(objFileName, "w")
        for dicRow in lstTable: #Write the two elements, separated by a comma
            fileObj.write(dicRow["Task"] + "," + dicRow["Priority"] +"\n")
        fileObj.close()
        print("Your data has been saved.")
        
 #Step 7 - Program exits     
    elif (strChoice == '5'):
        print("Goodbye!")
        break #and Exit the program
