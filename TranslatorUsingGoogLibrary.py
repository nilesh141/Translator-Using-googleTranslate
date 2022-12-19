from tkinter import *
from tkinter import ttk 
from googletrans import Translator,LANGUAGES

def translt(text="type",frm="English",to="Hindi"):
    text1=text 
    frm1=frm 
    to1=to 
    trans=Translator()
    trans1=trans.translate(text,dest=to1,src=frm1)#Not working showing error here
    return trans1.text 
def getData():
    f=comboInputL.get()
    t=comboOutputL.get()
    masg=inputTxt.get(1.0,END)
    textget=translt(text=masg,frm=f,to=t)
    outputTxt.delete(1.0,END)
    outputTxt.insert(END,textget)

root=Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='aqua')

labTxt=Label(root,text="Translator", font=("Times New Roman",40,"bold"))
labTxt.place(x=100,y=40,height=50,width=300)

frame=Frame(root).pack(side=BOTTOM)

labTxt=Label(root,text="Input Text", font=("Times New Roman",20,"bold"))
labTxt.place(x=100,y=100,height=30,width=300)

inputTxt=Text(frame,font=("Times New Roman",12,"bold"),wrap=WORD)
inputTxt.place(x=10,y=130,height=150,width=480)

langList=list(LANGUAGES.values())

comboInputL=ttk.Combobox(frame,value=langList)
comboInputL.place(x=10,y=300,height=40,width=100)
comboInputL.set("english")

buttonTrans=Button(frame,text="Translate",relief=RAISED,command=getData)
buttonTrans.place(x=170,y=300,height=40,width=150)

comboOutputL=ttk.Combobox(frame,value=langList)
comboOutputL.place(x=330,y=300,height=40,width=150)
comboOutputL.set("english")

labTxt=Label(root,text="Translated Text", font=("Times New Roman",20,"bold"))
labTxt.place(x=100,y=360,height=30,width=300)
outputTxt=Text(frame,font=("Times New Roman",12,"bold"),wrap=WORD)
outputTxt.place(x=10,y=400,height=150,width=480)

root.mainloop()

