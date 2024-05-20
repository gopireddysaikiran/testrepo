import tkinter as tk
import re
root = tk.Tk()
root.title("Employee Registration Form")
root.geometry("1920x1080")
	
	
    
def sub():
    l1=v1.get()
    l2=v2.get()
    l3=v3.get()
    l4=v4.get()
    l5=v5.get()
    l6=v6.get()


    if(len(l1)==0):
        tk.Label(root,text="Enter First Name",width="15",font=("arial",15),fg="red").place(x=950,y=100)
    elif(re.search("^[A-z]+$",l1)):
        tk.Label(root,text="",width="15",font=("arial",15),fg="red").place(x=950,y=100)
    else:
        tk.Label(root,text="Enter valid data",width="15",font=("arial",15),fg="red").place(x=950,y=100)
    
    if(len(l2)==0):
        tk.Label(root,text="Enter Last Name",width="15",font=("arial",15),fg="red").place(x=950,y=150)
    elif(re.search("^[A-z]+$",l2)):
        tk.Label(root,text="",width="15",font=("arial",15),fg="red").place(x=950,y=150)
    else:
        tk.Label(root,text="Enter valid data",width="15",font=("arial",15),fg="red").place(x=950,y=150)
    
    if(len(l3)==0):
        tk.Label(root,text="Enter Password",width="15",font=("arial",15),fg="red").place(x=950,y=200)
    else:
        tk.Label(root,text="",width="15",font=("arial",15),fg="red").place(x=950,y=200)
        
    if(len(l4)==0):
        tk.Label(root,text="Re-Enter Password",width="15",font=("arial",15),fg="red").place(x=950,y=250)
    elif(l3!=l4):
        tk.Label(root,text="Password doesn't matched",width="23",font=("arial",15),fg="red").place(x=950,y=250)
    else:
        tk.Label(root,text="",width="23",font=("arial",15),fg="red").place(x=950,y=250)
        
    if(len(l5)==0):
        tk.Label(root,text="Enter Email",width="15",font=("arial",15),fg="red").place(x=950,y=300)
    elif(re.search("^[A-z0-9.]+\@[a-zA-Z.]+\.[A-z]+$",l5)):
        tk.Label(root,text="",width="15",font=("arial",15),fg="red").place(x=950,y=300)
    else:
        tk.Label(root,text="Enter valid data",width="15",font=("arial",15),fg="red").place(x=950,y=300)
    
    if(l6==0):
        tk.Label(root,text="Select Gender",width="15",font=("arial",15),fg="red").place(x=950,y=350)
    else:
        tk.Label(root,text="",width="15",font=("arial",15),fg="red").place(x=950,y=350)


r = tk.Label(root, text="Employee Registration Form", font=("arial",15)).place(x=630,y=50)
f1 = tk.Label(root, text="First Name:", font=("arial",15)).place(x=500,y=100)
f2 = tk.Label(root, text="Last Name:", font=("arial",15)).place(x=500,y=150)
f3 = tk.Label(root, text="Password:", font=("arial",15)).place(x=500,y=200)
f4 = tk.Label(root, text="Re-Enter Password:", font=("arial",15)).place(x=500,y=250)
f5 = tk.Label(root, text="Email:", font=("arial",15)).place(x=500,y=300)
f6 = tk.Label(root, text="Gender:", font=("arial",15)).place(x=500,y=350)
f7 = tk.Label(root, text="Qualification:", font=("arial",15)).place(x=500,y=400)
f8 = tk.Label(root, text="Country:", font=("arial",15)).place(x=500,y=450)

v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()
v4 = tk.StringVar()
v5 = tk.StringVar()

e1 = tk.Entry(root, font=("arial",15),textvariable=v1)
e1.place(x=700,y=100)
e2 = tk.Entry(root, font=("arial",15),textvariable=v2)
e2.place(x=700,y=150)
e3 = tk.Entry(root, font=("arial",15), show="*",textvariable=v3)
e3.place(x=700,y=200)
e4 = tk.Entry(root, font=("arial",15), show="*",textvariable=v4)
e4.place(x=700,y=250)
e5 = tk.Entry(root, font=("arial",15),textvariable=v5)
e5.place(x=700,y=300)

v6=tk.IntVar()
tk.Radiobutton(root,text="Male",value=1,variable=v6, font=("arial",15)).place(x=700,y=350)
tk.Radiobutton(root,text="Female",value=2,variable=v6, font=("arial",15)).place(x=800,y=350)

tk.Checkbutton(root,text="SSC",font=("arial",15)).place(x=700,y=400)
tk.Checkbutton(root,text="INTER", font=("arial",15)).place(x=800,y=400)
tk.Checkbutton(root,text="BTECH",font=("arial",15)).place(x=900,y=400)

list=["INDIA","USA","UK","OTHER"]
v8=tk.StringVar()
tk.OptionMenu(root,v8,*list).place(x=700,y=450)

clear = tk.Button(root, text="Clear", font=("arial",15)).place(x=560,y=500)
submit = tk.Button(root, text="Submit", font=("arial",15), command=sub).place(x=760,y=500)

root.mainloop()
