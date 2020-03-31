from tkinter import *
    from tkinter.messagebox import showerror
    root = Tk()
    root.geometry('500x500')
    root.title("Loging Page")
    

    label_0 = Label(root, text="Loging",width=20,font=("bold", 20))
    label_0.place(x=100,y=53)


    label_1 = Label(root, text="User Name",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)

    entry_1 = Entry(root)
    entry_1.place(x=240,y=130)

    label_2 = Label(root, text="Password",width=20,font=("bold", 10))
    label_2.place(x=68,y=180)

    entry_2 = Entry(root,show='*')
    entry_2.place(x=240,y=180)

    Button(root, text='Login Now',width=20,bg='red',fg='black',command = validatecr).place(x=180,y=280)
    Button(root, text='New User',width=20,bg='red',fg='black').place(x=180,y=330)

    
    def validatecr():
        a = entry_1.get()
        b = entry_2.get()
        if a =='Admin' and b =='Admin':
            
            showerror(title = "Logged in ", message = "You are logged in")
        else:
            showerror(title = "Error", message = "Something bad happened")
    root.mainloop()
        