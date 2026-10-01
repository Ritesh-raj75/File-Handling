from pathlib import Path
import os

def createfile():
    try:
        name = input("please tell your file name:- ")
        path = Path(name)
        if not path.exists():
            with open(path, 'w') as f:
                data = input("what you want to write in your file:- ")
                f.write(data)
            print(f"File '{name}' created successfully.")
        else:
            print("Error file name already exists")
    except Exception as err:
        print(f"an error as ocuured {err}")

def readfile():
    try:
        name = input("please tell your file name:- ")
        path = Path(name)
        if path.exists():
            with open(path ,"r") as f:
                content = f.read()
                print(f"Content of the file '{name}':\n{content}")
                
        else:
            print(f"error no file such exist")
    except Exception as err:
        print(f"an error as ocuured {err}")
        

def updatefile():
    try:
        name = input("please tell your file name:- ")
        path = Path(name)
        
        if path.exists():
            print("operation you want to perform")
            print("1. Renaming the file")
            print("2. Appending data to the file")
            print("3. Overwriting the file")
            
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                newname = input("Enter the new file name: ")
                new_path = Path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print(f"File renamed to '{newname}' successfully.")
                else:
                    print("Error: A file with the new name already exists.")
                    
            elif choice == 2:
                with open(path, 'a') as f:
                    data = input("What you want to append: ")
                    f.write(" \n"+data)
                    print(f"Data appended to the file '{name}' successfully.")
            
            elif choice == 3:
                with open(path, 'w') as f:
                    data = input("What you want to overwrite: ")
                    f.write(" \n"+data)
                    print(f"File '{name}' overwritten successfully.")
    except Exception as err:
        print(f"an error as ocuured {err}")

def deletefile():
    try:
        name = input("please tell your file name:- ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print(f"File '{name}' deleted successfully.")
        
        else:
            print(f"error no file such exist")
    except Exception as err:
        print(f"an error as ocuured {err}")
    


print("press 1 for creating a new file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")



a = int(input("\nEnter your choice: "))

if a == 1:
    createfile()
if a == 2:
    readfile()
if a == 3:
    updatefile()
if a == 4:
    deletefile()