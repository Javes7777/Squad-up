from tkinter import *
import os 

def registerUser():
    usernameInfo = username.get()
    passwordInfo = password.get()
    file = open(usernameInfo+".txt", "w")
    file.write(usernameInfo)
    file.write(passwordInfo)
    file.close()

    usernameE.delete(0,END)
    passwordE.delete(0,END)

    Label(screen1, text = "Thank you for registering!", fg = "green", font = ("calibri",11)).pack()
    
def register():
    global screen1
    screen1  = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x340")

    global username 
    global password
    global usernameE
    global passwordE

    username = StringVar()
    password = StringVar()
    
    Label(screen1, text = "Please enter the following").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username ").pack()
    usernameE = Entry(screen1, textvariable = username)
    usernameE.pack()
    Label(screen1, text = "Password ").pack()
    passwordE = Entry(screen1, textvariable = password)
    passwordE.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 2, command = registerUser).pack()

def loginVerify():
    username1 = usernameCheck.get()
    password1 = passwordCheck.get()


    usernameEntry1.delete(0,END)
    passwordEntry1.delete(0,END)

    listFiles = os.listdir()
    if username1+'.txt' in listFiles:
        file1 = open(username1+'.txt', 'r')
        verify = file1.read().splitlines()
        print(verify)
        if password1 in verify:
            print("login success")
        else:
            print("password isn't right")
    else:
        print("not found")

        

        

    

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x400")
    Label(screen2, text = "Please enter the following").pack()
    Label(screen2, text = "").pack()

    global usernameCheck
    global passwordCheck

    usernameCheck = StringVar()
    passwordCheck = StringVar()

    global usernameEntry1
    global passwordEntry1
    
    Label(screen2, text = "Username").pack()
    usernameEntry1 = Entry(screen2, textvariable = usernameCheck)
    usernameEntry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password").pack()
    passwordEntry1  = Entry(screen2, textvariable = passwordCheck)
    passwordEntry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 2, command = loginVerify).pack()
    

def main():
    global screen 
    screen = Tk()
    screen.geometry("400x450")
    screen.title("Squad-Up")
    Label(text = "Squad-Up", bg  = "orange", width = "500", height = "3", font = ("MS Serif",14)).pack()
    Label(text = "").pack()
    Button(text = "login", bg = "grey", width = "50" , height = "2", command = login).pack()
    Label(text = "").pack()
    Button(text = "register", bg = "grey", width = "50" , height = "2", command = register).pack()

    
    

    
main()
