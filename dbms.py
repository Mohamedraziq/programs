from tkinter import*

w=Tk()
w.geometry("1330x680+10+10")
w.title("student mark details")
w.config(bg="white")

lbl=Label(w,text="STUDENT MARK DETAILS",font=('times',20,'bold'),bg='blue',fg='black')
lbl.pack(fill=X,pady=20)

lfrm=LabelFrame(w,text="student details",font=('times',14,'bold'),width=600,height=550,highlightthickness=2,highlightbackground="blue")  
lfrm.place(x=50,y=80)

Label(lfrm,text="student roll number",font=('times',14,'bold'),fg="green").place(x=30,y=50)
rtxt=Entry(lfrm,font=('times',14,'bold'),width=20,bd=2)
rtxt.place(x=300,y=50)

Label(lfrm,text="student name",font=('times',14,'bold'),fg="green").place(x=30,y=100)
ntxt=Entry(lfrm,font=('times',14,'bold'),width=20,bd=2)
ntxt.place(x=300,y=100)

Label(lfrm,text="tamil mark",font=('times',14,'bold'),fg="green").place(x=30,y=150)
m1txt=Entry(lfrm,font=('times',14,'bold'),width=20,bd=2)
m1txt.place(x=300,y=150)

Label(lfrm,text="english mark",font=('times',14,'bold'),fg="green").place(x=30,y=200)
m2txt=Entry(lfrm,font=('times',14,'bold'),width=20,bd=2)
m2txt.place(x=300,y=200)

Label(lfrm,text="maths mark",font=('times',14,'bold'),fg="green").place(x=30,y=250)
m3txt=Entry(lfrm,font=('times',14,'bold'),width=20,bd=2)
m3txt.place(x=300,y=250)

Label(lfrm,text="science mark",font=('times',14,'bold'),fg="green").place(x=30,y=300)
m4txt=Entry(lfrm,font=('times',14,'bold'),width=20,bd=2)
m4txt.place(x=300,y=300)

Label(lfrm,text="social mark",font=('times',14,'bold'),fg="green").place(x=30,y=350)
m5txt=Entry(lfrm,font=('times',14,'bold'),width=20,bd=2)
m5txt.place(x=300,y=350)

cfrm=LabelFrame(w,text="calculate details",font=('times',14,'bold'),width=600,height=350,highlightthickness=2,highlightbackground="blue")  
cfrm.place(x=700,y=80)

Label(cfrm,text="total mark",font=('times',14,'bold'),fg="green").place(x=30,y=50)
tttxt=Entry(cfrm,font=('times',14,'bold'),width=20,bd=2)
tttxt.place(x=300,y=50)

Label(cfrm,text="average",font=('times',14,'bold'),fg="green").place(x=30,y=100)
atxt=Entry(cfrm,font=('times',14,'bold'),width=20,bd=2)
atxt.place(x=300,y=100)

Label(cfrm,text="grade",font=('times',14,'bold'),fg="green").place(x=30,y=150)
gtxt=Entry(cfrm,font=('times',14,'bold'),width=20,bd=2)
gtxt.place(x=300,y=150)

Label(cfrm,text="result",font=('times',14,'bold'),fg="green").place(x=30,y=200)
retxt=Entry(cfrm,font=('times',14,'bold'),width=20,bd=2)
retxt.place(x=300,y=200)

frm=Frame(w,width=600,height=180,highlightthickness=2,highlightbackground="green")
frm.place(x=700,y=450)

def calculation():
    tttxt.delete(0,'end')
    m1=int(m1txt.get())
    m2=int(m2txt.get())
    m3=int(m3txt.get())
    m4=int(m4txt.get())
    m5=int(m5txt.get())
    tot=m1+m2+m3+m4+m5
    tttxt.insert(END,str(tot))
    atxt.delete(0,'end')
    avg=tot/5
    atxt.insert(END,str(avg))
    retxt.delete(0,'end')
    gtxt.delete(0,'end')
    
    if m1>=40 and m2>=40 and m3>=40 and m4>=40 and m5>=40:
        re="pass"

        if avg>=90:
            grade="A"
        elif avg>=80:
            grade="B"
        elif avg>=60:
            grade="C"
        elif avg>=40:
            grade="D"
    else:
        re="fail"
        grade="nill"
    retxt.insert(END,(re))
    gtxt.insert(END,(grade))
    
calbtn=Button(frm,text="calculation",width=14,bg="green",fg="white",font=('times',14,'bold'),command=calculation)
calbtn.place(x=20,y=50)

def clear():
     rtxt.delete(0,'end')
     ntxt.delete(0,'end')
     m1txt.delete(0,'end')
     m2txt.delete(0,'end')
     m3txt.delete(0,'end')
     m4txt.delete(0,'end')
     m5txt.delete(0,'end')
     tttxt.delete(0,'end')
     atxt.delete(0,'end')
     retxt.delete(0,'end')
     gtxt.delete(0,'end')
       
    
clbtn=Button(frm,text="clear",width=14,bg="green",fg="white",font=('times',14,'bold'),command=clear)
clbtn.place(x=200,y=50)

def exit():
         
    w.destroy()

ebtn=Button(frm,text="exit",width=14,bg="green",fg="white",font=('times',14,'bold'),command=exit)
ebtn.place(x=380,y=50)




w.mainloop()



