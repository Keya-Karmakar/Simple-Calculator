import tkinter as tk
#Function To Handle Button Clicks
def buttonclick(value):
    if(value=="AC"):
        entry.delete(0,tk.END) #All Clear The Entry Field
    elif(value=="ANS"):
        try:
            expression=entry.get()
            result=eval(expression)#Evaluate Mathematical Expression
            entry.delete(0,tk.END)
            entry.insert(tk.END,str(result))
        except Exception:
            entry.delete(0,tk.END)
            entry.insert(tk.END,"Error")#When You Put Wrong Expression
    elif(value=="DEL"):
        entry.delete(0)#Delete One Element
    else:
        entry.insert(tk.END,value)#Insert The Clicked Value Into The Entry Field
#Main Application Window
root=tk.Tk()
root.title("Simple Calculator Used For Simple Operation")
root.geometry("495x510")
root.resizable(False,False)
root.configure(bg="black")
#Title Lavel For Calculator
titlelavel=tk.Label(root,text="CALCULATOR",font=("Times New Roman",30,"bold"),bg="darkred",fg="cyan")
titlelavel.grid(row=0,column=0,columnspan=6,pady=10,padx=50)
#Entry Field For User Input
entry=tk.Entry(root,font=("Arial black",27,"bold"),justify="right",borderwidth=4,relief="solid",fg="brown")
entry.grid(row=1,column=0,columnspan=5,ipadx=0,ipady=2,pady=10)
#Button's Configuaration
button=["7","8","9","DEL","AC","4","5","6","*","/","1","2","3","+","-",".","0","%","//","**","(",")","{","}","ANS"]
#Button Colouring
buttoncolor={"DEL":"red","AC":"darkblue","*":"grey","/":"grey","+":"grey","-":"grey",".":"pink","%":"grey","//":"grey","**":"grey","ANS":"purple","(":"yellowgreen",")":"yellowgreen","{":"yellowgreen","}":"yellowgreen"}
defaultcolor="green"
#Create Buttom And Place Them In The Grid
row=2
column_value=0
for buttons in button:
    button_s=tk.Button(root,text=buttons,font=("Algerian",20,"bold"),bg=buttoncolor.get(buttons,defaultcolor),fg="white",width=3,height=1,command=lambda n=buttons:buttonclick(n))
    button_s.grid(row=row,column=column_value,padx=2,pady=2)
    column_value+=1
    if(column_value>4):
        column_value=0
        row=row+1
#Name Of The Creator
creator=tk.Label(root,text="* Creator Name: Keya Karmakar *",font=("Cooper Black",19,"bold"),fg="magenta",bg="black")
creator.grid(row=7,column=0,columnspan=6,pady=30)
#Run The Application
root.mainloop()