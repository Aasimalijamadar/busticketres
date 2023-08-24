from tkinter import *
from tkinter import messagebox
class page:
    def __init__(self,master):
        self.master=master
        self.master.geometry("1600x800")
        self.login()
        self.i=1
        self.h=80
    def bill(self):
        self.newWindow7=Toplevel(self.master)
        self.newWindow7.title("bill")
        self.newWindow7.geometry("1600x900")
        self.photo6=PhotoImage(file="Screenshot (154).png")
        self.img9=Label(self.newWindow7,image=self.photo6)
        self.img9.pack(fill=BOTH, expand=100)
        xyz=self.ceckvar1.get()
        sdsl=Label(self.newWindow7,text="your bill",width=45,height=2,bg="cornsilk2",fg="black",font="Algerian 16 bold").place(x=470,y=10)
        startjrny=self.startjrny.get()
        destjrny=self.destjrny.get()
        bsn=self.busnumb.get()
        slpr1=""
        stpr1=""
        with open("1.txt","r") as file:
            m1=0
            n1=0
            w1=0
            content=file.readlines()
            for i in content[(bsn*4)-4].split():
                if(i=="->"):
                    m1+=1
                if(i==startjrny):
                    break
            for k in content[(bsn*4)-4].split():
                if(k=="->"):
                    n1+=1
                if(k==destjrny):
                    break
            for j in content[(bsn*4)-3].split():
                    if(w1==1):
                        slpr1=int(j)
                    if(w1==3):
                        stpr1=int(j)
                    if(w1==4):
                        day=j
                    if(w1==5):
                        month=j
                    if(w1==6):
                        time=j
                    w1+=1
            stpr=int(stpr1)       
            slpr=int(slpr1)
        with open("1.txt","r") as file:
            strt=0
            dest=0
            cont=file.readlines()
            for i in cont[(bsn*4)-4].split():
                if(i=="->"):
                    strt+=1
                if(strt==m1):
                    strt1=i
            for k in cont[(bsn*4)-4].split():
                if(k=="->"):
                    dest+=1
                if(dest==n1):
                    dest1=k
            f=open("bill.txt","w")
            f.write("From : "+strt1+"\t "+"To : "+dest1)
            f.write("\nDate : "+day+"/"+month+"\t\tTime : "+time) 
            f.close()   
            nsl=0
        nst=0
        f=open("bill.txt","a")
        f.write("\nSL : ")
        f.close()
        f=open("bill.txt","a")
        if(bsn==1):
            fp=open("2.txt","a")
        if(bsn==2):
            fp=open("3.txt","a")
        if(bsn==3):
            fp=open("4.txt","a")
        if(bsn==4):
            fp=open("5.txt","a")
        if(bsn==5):
            fp=open("6.txt","a")
        if(bsn==6):
            fp=open("7.txt","a")
        if(bsn==7):
            fp=open("8.txt","a")
        if(bsn==8):
            fp=open("9.txt","a")
        if(self.ceckvar1.get()==1):
            nsl+=1
            f.write("01 ")
            fp.write("01 ")
        if(self.ceckvar2.get()==1):
            nsl+=1
            f.write("02 ")
            fp.write("02 ")
        if(self.ceckvar3.get()==1):
            nsl+=1
            f.write("03 ")
            fp.write("03 ")
        if(self.ceckvar4.get()==1):
            nsl+=1
            f.write("04 ")
            fp.write("04 ")
        if(self.ceckvar5.get()==1):
            nsl+=1
            f.write("05 ")
            fp.write("05 ")
        if(self.ceckvar6.get()==1):
            nsl+=1
            f.write("06 ")
            fp.write("06 ")
        if(self.ceckvar7.get()==1):
            nsl+=1
            f.write("07 ")
            fp.write("07 ")
        if(self.ceckvar8.get()==1):
            nsl+=1
            f.write("08 ")
            fp.write("08 ")
        if(self.ceckvar9.get()==1):
            nsl+=1
            f.write("09 ")
            fp.write("09 ")
        if(self.ceckvar10.get()==1):
            nsl+=1
            f.write("10 ")
            fp.write("10 ")
        if(self.ceckvar11.get()==1):
            nsl+=1
            f.write("11 ")
            fp.write("11 ")
        if(self.ceckvar12.get()==1):
            nsl+=1
            f.write("12 ")
            fp.write("12 ")
        if(self.ceckvar13.get()==1):
            nsl+=1
            f.write("13 ")
            fp.write("13 ")
        if(self.ceckvar14.get()==1):
            nsl+=1
            f.write("14 ")
            fp.write("14 ")
        if(self.ceckvar15.get()==1):
            nsl+=1
            f.write("15 ")
            fp.write("15 ")
        if(self.ceckvar16.get()==1):
            nsl+=1
            f.write("16 ")
            fp.write("16 ")
        if(self.ceckvar17.get()==1):
            nsl+=1
            f.write("17 ")
            fp.write("17 ")
        if(self.ceckvar18.get()==1):
            nsl+=1
            f.write("18 ")
            fp.write("18 ")
        if(self.ceckvar19.get()==1):
            nsl+=1
            f.write("19 ")
            fp.write("19 ")
        if(self.ceckvar20.get()==1):
            nsl+=1
            f.write("20 ")
            fp.write("20 ")
        if(self.ceckvar21.get()==1):
            nsl+=1
            f.write("21 ")
            fp.write("21 ")
        if(self.ceckvar22.get()==1):
            nsl+=1
            f.write("22 ")
            fp.write("22 ")
        if(self.ceckvar23.get()==1):
            nsl+=1
            f.write("23 ")
            fp.write("23 ")
        if(self.ceckvar24.get()==1):
            nsl+=1
            f.write("24 ")
            fp.write("24 ")
        f.write("\tST : ")
        fp.write("\n")
        if(self.ceckvar111.get()==1):
            nst+=1
            f.write("01 ")
            fp.write("01 ")
        if(self.ceckvar112.get()==1):
            nst+=1
            f.write("02 ")
            fp.write("02 ")
        if(self.ceckvar113.get()==1):
            nst+=1
            f.write("03 ")
            fp.write("03 ")
        if(self.ceckvar114.get()==1):
            nst+=1
            f.write("04 ")
            fp.write("04 ")
        if(self.ceckvar115.get()==1):
            nst+=1
            f.write("05 ")
            fp.write("05 ")
        if(self.ceckvar116.get()==1):
            nst+=1
            f.write("06 ")
            fp.write("06 ")
        if(self.ceckvar117.get()==1):
            nst+=1
            f.write("07 ")
            fp.write("07 ")
        if(self.ceckvar118.get()==1):
            nst+=1
            f.write("08 ")
            fp.write("08 ")
        if(self.ceckvar119.get()==1):
            nst+=1
            f.write("09 ")
            fp.write("09 ")
        if(self.ceckvar1110.get()==1):
            nst+=1
            f.write("10 ")
            fp.write("10 ")
        if(self.ceckvar1111.get()==1):
            nst+=1
            f.write("11 ")
            fp.write("11 ")
        if(self.ceckvar1112.get()==1):
            nst+=1
            f.write("12 ")
            fp.write("12 ")
        if(self.ceckvar1113.get()==1):
            nst+=1
            f.write("13 ")
            fp.write("13 ")
        if(self.ceckvar1114.get()==1):
            nst+=1
            f.write("14 ")
            fp.write("14 ")
        if(self.ceckvar1115.get()==1):
            nst+=1
            f.write("15 ")
            fp.write("15 ")
        if(self.ceckvar1116.get()==1):
            nst+=1
            f.write("16 ")
            fp.write("16 ")
        if(self.ceckvar1117.get()==1):
            nst+=1
            f.write("17 ")
            fp.write("17 ")
        if(self.ceckvar1118.get()==1):
            nst+=1
            f.write("18 ")
            fp.write("18 ")
        if(self.ceckvar1119.get()==1):
            nst+=1
            f.write("19 ")
            fp.write("19 ")
        if(self.ceckvar1120.get()==1):
            nst+=1
            f.write("20 ")
            fp.write("20 ")
        if(self.ceckvar1121.get()==1):
            nst+=1
            f.write("21 ")
            fp.write("21 ")
        if(self.ceckvar1122.get()==1):
            nst+=1
            f.write("22 ")
            fp.write("22 ")
        if(self.ceckvar1123.get()==1):
            nst+=1
            f.write("23 ")
            fp.write("23 ")
        if(self.ceckvar1124.get()==1):
            nst+=1
            f.write("24 ")
            fp.write("24 ")
        f.close()
        slpr1=slpr1/9
        stpr1=stpr1/9
        slttl=slpr1*(n1-m1)
        stttl=stpr1*(n1-m1)
        total=(nst*stttl)+(nsl*slttl) 
        f=open("bill.txt","a")
        f.write("\nRs : "+str(total))
        f.close()
        f=open("bill.txt","r")
        lines=f.read()
        asd=Label(self.newWindow7,text=lines,font="Algerian 16 bold",bg="cornflowerblue",fg="black",height=10,width=45,).place(x=470,y=100)
        self.photo9=PhotoImage(file="Screenshot_20221125_122542.png")
        self.img10=Label(self.newWindow7,image=self.photo9,height=254,width=254)
        cp=Label(self.newWindow7,text="complete payment using upi",font="Algerian 16 bold",bg="cornflowerblue",fg="black",height=3,width=45,).place(x=470,y=400)
        self.img10.place(x=650,y=550)
    def addjourney(self):
        flag=0
        if((self.day).get()>31):
            messagebox.showinfo("msg","Invalid Date")
            flag=1
        if((self.month).get()>12):
            messagebox.showinfo("msg","Invalid Month")
            flag=1
        if(flag==0):
            adjyfrom=self.from1.get()
            adjyto=self.to1.get()
            adjyday=self.day.get()
            adjymonth=self.month.get()
            adjytime=self.time.get()
            stpe1=self.stpe1.get()+" -> "
            stpe2=self.stpe2.get()+" -> "
            stpe3=self.stpe3.get()+" -> "
            stpe4=self.stpe4.get()+" -> "
            stpe5=self.stpe5.get()+" -> "
            stpe6=self.stpe6.get()+" -> "
            stpe7=self.stpe7.get()+" -> "
            stpe8=self.stpe8.get()+" -> "
            noslst=str(self.noslst.get())
            nostst=str(self.nostst.get())
            slpr=str(self.slpr.get())
            stpr=str(self.stpr.get())
            self.busnumber=StringVar()
            buno=self.busnumber.get()
            day=str(self.day.get())
            month=str(self.month.get())
            time=str(self.time.get())
            selectBus=Label(self.adjWindow,text="Select Bus",width=45,height=2,bg="cornsilk2",fg="black",font="Algerian 16 bold").place(x=470,y=10)
            butname="Bus Number = "+str(self.i)+" : "+adjyfrom+" -> "+stpe1+stpe2+stpe3+stpe4+stpe5+stpe6+stpe7+stpe8+adjyto+" |    Date: "+str(adjyday)+"/"+str(adjymonth)+"  "+adjytime+"  SL av/pice = "+noslst+"/"+slpr+" St av/price = "+nostst+"/"+stpr
            if(self.i==1):
                label1=Label(self.adjWindow,text=butname,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=self.h)
                fp=open("1.txt","w")
                fp.write(butname+"\n"+noslst+" "+slpr+" "+nostst+" "+stpr+" "+day+" "+month+" "+time+"\n")
                for i in range(1,int(noslst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                for i in range(1,int(nostst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                self.id=1 
            if(self.i==1):
                label1=Label(self.adjWindow,text=butname,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=self.h)
                fp=open("1.txt","w")
                fp.write(butname+"\n"+noslst+" "+slpr+" "+nostst+" "+stpr+" "+day+" "+month+" "+time+"\n")
                for i in range(1,int(noslst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                for i in range(1,int(nostst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                self.id=1 
            if(self.i==2):
                label2=Label(self.adjWindow,text=butname,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=self.h)
                fp=open("1.txt","a")
                fp.write(butname+"\n"+noslst+" "+slpr+" "+nostst+" "+stpr+" "+day+" "+month+" "+time+"\n")
                for i in range(1,int(noslst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                for i in range(1,int(nostst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                self.id=2
            if(self.i==3):
                label3=Label(self.adjWindow,text=butname,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=self.h)
                fp=open("1.txt","a")
                fp.write(butname+"\n"+noslst+" "+slpr+" "+nostst+" "+stpr+" "+day+" "+month+" "+time+"\n")
                for i in range(1,int(noslst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                for i in range(1,int(nostst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                self.id=3
            if(self.i==4):
                label4=Label(self.adjWindow,text=butname,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=self.h)
                fp=open("1.txt","a")
                fp.write(butname+"\n"+noslst+" "+slpr+" "+nostst+" "+stpr+" "+day+" "+month+" "+time+"\n")
                for i in range(1,int(noslst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                for i in range(1,int(nostst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n") 
                self.id=4
            if(self.i==5):
                label5=Label(self.adjWindow,text=butname,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=self.h)
                fp=open("1.txt","a")
                fp.write(butname+"\n"+noslst+" "+slpr+" "+nostst+" "+stpr+" "+day+" "+month+" "+time+"\n")
                for i in range(1,int(noslst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                for i in range(1,int(nostst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                self.id=5
            if(self.i==6):
                label6=Label(self.adjWindow,text=butname,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=self.h)
                fp=open("1.txt","a")
                fp.write(butname+"\n"+noslst+" "+slpr+" "+nostst+" "+stpr+" "+day+" "+month+" "+time+"\n")
                for i in range(1,int(noslst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                for i in range(1,int(nostst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                self.id=6
            if(self.i==7):
                label7=Label(self.adjWindow,text=butname,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=self.h)
                fp=open("1.txt","a")
                fp.write(butname+"\n"+noslst+" "+slpr+" "+nostst+" "+stpr+" "+day+" "+month+" "+time+"\n")
                for i in range(1,int(noslst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                for i in range(1,int(nostst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                self.id=7
            if(self.i==8):
                label8=Label(self.adjWindow,text=butname,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=self.h)
                fp=open("1.txt","a")
                fp.write(butname+"\n"+noslst+" "+slpr+" "+nostst+" "+stpr+" "+day+" "+month+" "+time+"\n")
                for i in range(1,int(noslst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                for i in range(1,int(nostst)+1):
                    if(i<10):
                        fp.write("0"+str(i)+" ")
                    else:
                        fp.write(str(i)+" ")
                fp.write(" -1\n")
                self.id=8
            if(self.i==9):
                messagebox.showinfo("message","No space available")
            self.i=self.i+1
            self.h=self.h+80
            busno=Entry(self.adjWindow,font="Algerian 14 bold",textvariable=self.busnumber).place(x=900,y=700,height=20)
            label11=Label(self.adjWindow,font="Algerian 14 bold",width=30,height=1,bg="cyan4",fg="black",text="Enter Bus Number").place(x=450,y=700,width=250)
            addbus=Button(self.adjWindow,text="Submit",font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=20).place(x=700,y=750)
    def add(self):
        self.newWindow3=Toplevel(self.master)
        self.newWindow3.title("Admin login")
        self.newWindow3.geometry("1600x900")  
        self.photo4=PhotoImage(file="Screenshot (29).png")
        self.img3=Label(self.newWindow3,image=self.photo4)
        self.img3.pack(fill=BOTH, expand=100)
        from1=Label(self.newWindow3,text="From",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=120,y=50)
        to1=Label(self.newWindow3,text="To",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=120,y=130)
        day=Label(self.newWindow3,text="Date",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=120,y=210)
        month=Label(self.newWindow3,text="Month",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=120,y=290)
        Time=Label(self.newWindow3,text="Time",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=120,y=370)
        noslst1=Label(self.newWindow3,text="Number of sleeper seats",width=20,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=120,y=450)
        nostst1=Label(self.newWindow3,text="Number of seater seats",width=20,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=120,y=530)
        slpr1=Label(self.newWindow3,text="Sleeper seat price",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=120,y=610)
        stpr1=Label(self.newWindow3,text="seater seat price",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=120,y=690)
        inbtstp=Label(self.newWindow3,text="select in between stops",width=45,height=2,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=800,y=50)
        stp1=Label(self.newWindow3,text="stop 1",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=800,y=160)
        stp2=Label(self.newWindow3,text="stop 2",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=800,y=220)
        stp3=Label(self.newWindow3,text="stop 3",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=800,y=280)
        stp4=Label(self.newWindow3,text="stop 4",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=800,y=340)
        stp5=Label(self.newWindow3,text="stop 5",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=800,y=400)
        stp6=Label(self.newWindow3,text="stop 6",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=800,y=460)
        stp7=Label(self.newWindow3,text="stop 7",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=800,y=520)
        stp8=Label(self.newWindow3,text="stop 8",width=15,height=1,bg="cyan4",fg="black",font="Algerian 14 bold").place(x=800,y=580)
        self.stpe1=StringVar()
        self.stpe2=StringVar()
        self.stpe3=StringVar()
        self.stpe4=StringVar()
        self.stpe5=StringVar()
        self.stpe6=StringVar()
        self.stpe7=StringVar()
        self.stpe8=StringVar()
        stpe1=Entry(self.newWindow3,font="Algerian 12 bold",textvariable=self.stpe1).place(x=1180,y=160,width=200)
        stpe2=Entry(self.newWindow3,font="Algerian 12 bold",textvariable=self.stpe2).place(x=1180,y=220,width=200)
        stpe3=Entry(self.newWindow3,font="Algerian 12 bold",textvariable=self.stpe3).place(x=1180,y=280,width=200)
        stpe4=Entry(self.newWindow3,font="Algerian 12 bold",textvariable=self.stpe4).place(x=1180,y=340,width=200)
        stpe5=Entry(self.newWindow3,font="Algerian 12 bold",textvariable=self.stpe5).place(x=1180,y=400,width=200)
        stpe6=Entry(self.newWindow3,font="Algerian 12 bold",textvariable=self.stpe6).place(x=1180,y=460,width=200)
        stpe7=Entry(self.newWindow3,font="Algerian 12 bold",textvariable=self.stpe7).place(x=1180,y=520,width=200)
        stpe8=Entry(self.newWindow3,font="Algerian 12 bold",textvariable=self.stpe8).place(x=1180,y=580,width=200)
        self.from1=StringVar()
        self.to1=StringVar()
        self.day=IntVar()
        self.month=IntVar()
        self.time=StringVar()
        self.noslst=StringVar()
        self.nostst=StringVar()
        self.slpr=StringVar()
        self.stpr=StringVar()
        from2=Entry(self.newWindow3,font="Algerian 14 bold",textvariable=self.from1).place(x=400,y=50,height=30)
        to2=Entry(self.newWindow3,font="Algerian 14 bold",textvariable=self.to1).place(x=400,y=130,height=30)
        date=Entry(self.newWindow3,font="Algerian 14 bold",textvariable=self.day).place(x=400,y=210,height=30)
        month=Entry(self.newWindow3,font="Algerian 14 bold",textvariable=self.month).place(x=400,y=290,height=30)
        time=Entry(self.newWindow3,font="Algerian 14 bold",textvariable=self.time).place(x=400,y=370,height=30)
        noslst1=Entry(self.newWindow3,font="Algerian 14 bold",textvariable=self.noslst).place(x=400,y=450,height=30)
        nostst1=Entry(self.newWindow3,font="Algerian 14 bold",textvariable=self.nostst).place(x=400,y=530,height=30)
        slpr1=Entry(self.newWindow3,font="Algerian 14 bold",textvariable=self.slpr).place(x=400,y=610,height=30)
        stpr1=Entry(self.newWindow3,font="Algerian 14 bold",textvariable=self.stpr).place(x=400,y=690,height=30)
        self.adjWindow=Toplevel(self.master)
        self.adjWindow.title("Available buses")
        self.adjWindow.geometry("1600x800")
        self.photo1=PhotoImage(file="Screenshot (27).png")
        self.img2=Label(self.adjWindow,image=self.photo1)  
        self.img2.pack(fill=BOTH, expand=100)
        journeyadd=Button(self.newWindow3,text="Submit",font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=20,command=self.addjourney).place(x=550,y=800)
    def admin(self):
        admusn = self.adminusername.get()
        admpass = self.adminpass.get()
        if(admusn == "hi" and admpass== "hello"):
            messagebox.showinfo("message","loged in successfully")
            self.newWindow=Toplevel(self.master)
            self.newWindow.title("Admin login")
            self.newWindow.geometry("1600x800")
            self.photo1=PhotoImage(file="Screenshot (10).png")
            self.img1=Label(self.newWindow,image=self.photo1)
            self.img1.pack(fill=BOTH, expand=100)
            self.add1=Button(self.newWindow,text="add journey",font="Algerian 12 bold",bg="cornsilk2",fg="black",height=3,width=25,command=self.add).place(x=640,y=200)
            self.remove=Button(self.newWindow,text="show available buses",font="Algerian 12 bold",bg="cornsilk2",fg="black",height=3,width=25,command=self.avbs).place(x=640,y=500)
        else:
            messagebox.showinfo("message","incorect id or/and password")
    def avbs(self):
        self.newWindow25=Toplevel(self.master)
        self.newWindow25.title("Available buses")
        self.newWindow25.geometry("1600x800")
        self.photo11=PhotoImage(file="Screenshot (164).png")
        self.img17=Label(self.newWindow25,image=self.photo11)
        self.img17.pack(fill=BOTH, expand=100)
        fp=open("1.txt","r")
        lines=fp.readlines()
        w=0
        for line in lines:
            w+=1
            if(w==1):
                label21=Label(self.newWindow25,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=80)
            if(w==5):
                label22=Label(self.newWindow25,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=160)
            if(w==9):
                label23=Label(self.newWindow25,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=240)
            if(w==13):
                label24=Label(self.newWindow25,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=320)
            if(w==17):
                label25=Label(self.newWindow25,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=400)
            if(w==21):
                label26=Label(self.newWindow25,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=480)
            if(w==25):
                label27=Label(self.newWindow25,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=560)
            if(w==29):
                label28=Label(self.newWindow25,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=640)
    def login(self):
        self.frame1=Frame(self.master,height=1000,width=1600)    
        self.photo=PhotoImage(file="Screenshot (3).png")
        self.frame1.pack()
        self.img=Label(self.frame1,image=self.photo)
        self.img.pack(fill=BOTH,expand=1)
        self.admin1=Label(self.frame1,text="Admin login",width=15,height=1,bg="lightcyan2",fg="black",font="Algerian 16 bold").place(x=100,y=20)
        self.usnadmin=Label(self.frame1,text="User name",width=10,height=1,bg="lightcyan2",fg="black",font="Algerian 14 bold").place(x=20,y=100)
        self.passadmin=Label(self.frame1,text="Password",width=10,height=1,bg="lightcyan2",fg="black",font="Algerian 14 bold").place(x=20,y=180)
        self.adminusername=StringVar()
        self.adminpass=StringVar()
        self.e1=Entry(self.frame1,font="Algerian 10 bold",textvariable=self.adminusername).place(x=240,y=100)
        self.e2=Entry(self.frame1,font="Algerian 10 bold",textvariable=self.adminpass).place(x=240,y=180)
        self.sub1=Button(self.frame1,text="Login",font="Algerian 12 bold",bg="cornsilk2",fg="black",height=2,width=10,command=self.admin).place(x=140,y=240)
        self.user=Label(self.frame1,text="User login",width=15,height=1,bg="lightcyan2",fg="black",font="Algerian 16 bold").place(x=100,y=420)
        self.usn=Label(self.frame1,text="User name",width=10,height=1,bg="lightcyan2",fg="black",font="Algerian 14 bold").place(x=20,y=500)
        self.passus=Label(self.frame1,text="Password",width=10,height=1,bg="lightcyan2",fg="black",font="Algerian 14 bold").place(x=20,y=580)
        self.userusername=StringVar()
        self.userpass=StringVar()
        e3=Entry(self.frame1,font="Algerian 10 bold",textvariable=self.userusername).place(x=240,y=500)
        e4=Entry(self.frame1,font="Algerian 10 bold",textvariable=self.userpass).place(x=240,y=580)
        self.sub2=Button(self.frame1,text="Login",font="Algerian 12 bold",bg="cornsilk2",fg="black",height=2,width=10,command=self.user1).place(x=140,y=640)
    def user1(self):
        self.ususn=self.userusername.get()
        self.uspass=self.userpass.get()
        if(self.ususn=="asim" and self.uspass== "abc"):
            messagebox.showinfo("message","Loged in successfully")
            self.newWindow4=Toplevel(self.master)
            self.newWindow4.title("Admin login")
            self.newWindow4.geometry("1600x800")
            self.photo4=PhotoImage(file="Screenshot (107).png")
            self.img7=Label(self.newWindow4,image=self.photo4)
            self.img7.pack(fill=BOTH, expand=100)
            self.busnumb=IntVar()
            selectBus1=Label(self.newWindow4,text="Select Bus",width=45,height=2,bg="cornsilk2",fg="black",font="Algerian 16 bold").place(x=470,y=10)
            busno1=Entry(self.newWindow4,font="Algerian 14 bold",textvariable=self.busnumb).place(x=900,y=700,height=20)
            label112=Label(self.newWindow4,font="Algerian 14 bold",width=30,height=1,bg="cyan4",fg="black",text="Enter Bus Number").place(x=450,y=700,width=250)
            addbus1=Button(self.newWindow4,text="Submit",font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=20,command=self.sleeper).place(x=700,y=750)
            fp=open("1.txt","r")
            lines=fp.readlines()
            w=0
            for line in lines:
                w+=1
                if(w==1):
                    label21=Label(self.newWindow4,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=80)
                if(w==5):
                    label22=Label(self.newWindow4,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=160)
                if(w==9):
                    label23=Label(self.newWindow4,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=240)
                if(w==13):
                    label24=Label(self.newWindow4,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=320)
                if(w==17):
                    label25=Label(self.newWindow4,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=400)
                if(w==21):
                    label26=Label(self.newWindow4,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=480)
                if(w==25):
                    label27=Label(self.newWindow4,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=560)
                if(w==29):
                    label28=Label(self.newWindow4,text=line,font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=120,).place(x=120,y=640)
        else:
            messagebox.showinfo("message","incorect id or/and password")
    def sleeper(self):
        self.newWindow6=Toplevel(self.master)
        self.newWindow6.title("Admin login")
        self.newWindow6.geometry("1600x1000")
        self.photo6=PhotoImage(file="Screenshot (138).png")
        self.img6=Label(self.newWindow6,image=self.photo6)
        self.img6.pack(fill=BOTH, expand=100)
        sl=Label(self.newWindow6,text="Available Sleeper seats ",font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=50,).place(x=50,y=30)
        h1=100
        sl1=self.busnumb.get()
        self.ceckvar1=IntVar()
        self.ceckvar2=IntVar()
        self.ceckvar3=IntVar()
        self.ceckvar4=IntVar()
        self.ceckvar5=IntVar()
        self.ceckvar6=IntVar()
        self.ceckvar7=IntVar()
        self.ceckvar8=IntVar()
        self.ceckvar9=IntVar()
        self.ceckvar10=IntVar()
        self.ceckvar11=IntVar()
        self.ceckvar12=IntVar()
        self.ceckvar13=IntVar()
        self.ceckvar14=IntVar()
        self.ceckvar15=IntVar()
        self.ceckvar16=IntVar()
        self.ceckvar17=IntVar()
        self.ceckvar18=IntVar()
        self.ceckvar19=IntVar()
        self.ceckvar20=IntVar()
        self.ceckvar21=IntVar()
        self.ceckvar22=IntVar()
        self.ceckvar23=IntVar()
        self.ceckvar24=IntVar()
        if(sl1==1):
            fp=open("2.txt","r")
            line=fp.readlines()
        if(sl1==2):
            fp=open("3.txt","r")
            line=fp.readlines()
        if(sl1==3):
            fp=open("4.txt","r")
            line=fp.readlines()
        if(sl1==4):
            fp=open("5.txt","r")
            line=fp.readlines()
        if(sl1==5):
            fp=open("6.txt","r")
            line=fp.readlines()
        if(sl1==6):
            fp=open("7.txt","r")
            line=fp.readlines()
        if(sl1==7):
            fp=open("8.txt","r")
            line=fp.readlines()
        if(sl1==8):
            fp=open("9.txt","r")
            line=fp.readlines()
        with open("1.txt","r") as file:
            cont=file.readlines()
            for ww in cont[(sl1*4)-2].split():
                    if(ww=="01"):
                        flag=0
                        for a in line[0].split():
                            if(a=="01"):
                                flag=1
                        if(flag==0):
                            rb1=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1).place(x=50,y=h1)
                            h1+=30
                    if(ww=="02"):
                        flag=0
                        for a in line[0].split():
                            if(a=="02"):
                                flag=1
                        if(flag==0):
                            rb2=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar2).place(x=50,y=h1)
                            h1+=30
                    if(ww=="03"):
                        flag=0
                        for a in line[0].split():
                            if(a=="03"):
                                flag=1
                        if(flag==0):
                            rb3=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar3).place(x=50,y=h1)
                            h1+=30
                    if(ww=="04"):
                        flag=0
                        for a in line[0].split():
                            if(a=="04"):
                                flag=1
                        if(flag==0):
                            rb4=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar4).place(x=50,y=h1)
                            h1+=30
                    if(ww=="05"):
                        flag=0
                        for a in line[0].split():
                            if(a=="05"):
                                flag=1
                        if(flag==0):
                            rb5=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar5).place(x=50,y=h1)
                            h1+=30
                    if(ww=="06"):
                        flag=0
                        for a in line[0].split():
                            if(a=="06"):
                                flag=1
                        if(flag==0):
                            rb6=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar6).place(x=50,y=h1)
                            h1+=30
                    if(ww=="07"):
                        flag=0
                        for a in line[0].split():
                            if(a=="07"):
                                flag=1
                        if(flag==0):
                            rb7=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar7).place(x=50,y=h1)
                            h1+=30
                    if(ww=="08"):
                        flag=0
                        for a in line[0].split():
                            if(a=="08"):
                                flag=1
                        if(flag==0):
                            rb8=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar8).place(x=50,y=h1)
                            h1+=30
                    if(ww=="09"):
                        flag=0
                        for a in line[0].split():
                            if(a=="09"):
                                flag=1
                        if(flag==0):
                            rb9=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar9).place(x=50,y=h1)
                            h1+=30
                    if(ww=="10"):
                        flag=0
                        for a in line[0].split():
                            if(a=="10"):
                                flag=1
                        if(flag==0):
                            rb10=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar10).place(x=50,y=h1)
                            h1+=30
                    if(ww=="11"):
                        flag=0
                        for a in line[0].split():
                            if(a=="11"):
                                flag=1
                        if(flag==0):
                            rb11=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar11).place(x=50,y=h1)
                            h1+=30
                    if(ww=="12"):
                        flag=0
                        for a in line[0].split():
                            if(a=="12"):
                                flag=1
                        if(flag==0):
                            rb12=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar12).place(x=50,y=h1)
                            h1+=30
                    if(ww=="13"):
                        flag=0
                        for a in line[0].split():
                            if(a=="13"):
                                flag=1
                        if(flag==0):
                            rb13=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar13).place(x=50,y=h1)
                            h1+=30
                    if(ww=="14"):
                        flag=0
                        for a in line[0].split():
                            if(a=="14"):
                                flag=1
                        if(flag==0):
                            rb14=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar14).place(x=50,y=h1)
                            h1+=30
                    if(ww=="15"):
                        flag=0
                        for a in line[0].split():
                            if(a=="15"):
                                flag=1
                        if(flag==0):
                            rb15=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar15).place(x=50,y=h1)
                            h1+=30
                    if(ww=="16"):
                        flag=0
                        for a in line[0].split():
                            if(a=="16"):
                                flag=1
                        if(flag==0):
                            rb16=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar16).place(x=50,y=h1)
                            h1+=30
                    if(ww=="17"):
                        flag=0
                        for a in line[0].split():
                            if(a=="17"):
                                flag=1
                        if(flag==0):
                            rb17=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar17).place(x=50,y=h1)
                            h1+=30
                    if(ww=="18"):
                        flag=0
                        for a in line[0].split():
                            if(a=="18"):
                                flag=1
                        if(flag==0):
                            rb18=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar18).place(x=50,y=h1)
                            h1+=30
                    if(ww=="19"):
                        flag=0
                        for a in line[0].split():
                            if(a=="19"):
                                flag=1
                        if(flag==0):
                            rb19=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar19).place(x=50,y=h1)
                            h1+=30
                    if(ww=="20"):
                        flag=0
                        for a in line[0].split():
                            if(a=="20"):
                                flag=1
                        if(flag==0):
                            rb20=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar20).place(x=50,y=h1)
                            h1+=30
                    if(ww=="21"):
                        flag=0
                        for a in line[0].split():
                            if(a=="21"):
                                flag=1
                        if(flag==0):
                            rb21=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar21).place(x=50,y=h1)
                            h1+=30
                    if(ww=="22"):
                        flag=0
                        for a in line[0].split():
                            if(a=="22"):
                                flag=1
                        if(flag==0):
                            rb22=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar22).place(x=50,y=h1)
                            h1+=30
                    if(ww=="23"):
                        flag=0
                        for a in line[0].split():
                            if(a=="23"):
                                flag=1
                        if(flag==0):
                            rb23=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar23).place(x=50,y=h1)
                            h1+=30
                    if(ww=="24"):
                        flag=0
                        for a in line[0].split():
                            if(a=="24"):
                                flag=1
                        if(flag==0):
                            rb24=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar24).place(x=50,y=h1)
                            h1+=30
        st=Label(self.newWindow6,text="Available Seater seats ",font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=50).place(x=800,y=30)
        h2=100
        self.ceckvar111=IntVar()
        self.ceckvar112=IntVar()
        self.ceckvar113=IntVar()
        self.ceckvar114=IntVar()
        self.ceckvar115=IntVar()
        self.ceckvar116=IntVar()
        self.ceckvar117=IntVar()
        self.ceckvar118=IntVar()
        self.ceckvar119=IntVar()
        self.ceckvar1110=IntVar()
        self.ceckvar1111=IntVar()
        self.ceckvar1112=IntVar()
        self.ceckvar1113=IntVar()
        self.ceckvar1114=IntVar()
        self.ceckvar1115=IntVar()
        self.ceckvar1116=IntVar()
        self.ceckvar1117=IntVar()
        self.ceckvar1118=IntVar()
        self.ceckvar1119=IntVar()
        self.ceckvar1120=IntVar()
        self.ceckvar1121=IntVar()
        self.ceckvar1122=IntVar()
        self.ceckvar1123=IntVar()
        self.ceckvar1124=IntVar()
        with open("1.txt","r") as file:
            cont=file.readlines()
            for ww in cont[(sl1*4)-1].split():
                    if(ww=="01"):
                        flag=0
                        for a in line[1].split():
                            if(a=="01"):
                                flag=1
                        if(flag==0):
                            rb111=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar111).place(x=800,y=h2)
                            h2+=30
                    if(ww=="02"):
                        flag=0
                        for a in line[1].split():
                            if(a=="02"):
                                flag=1
                        if(flag==0):
                            rb112=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar112).place(x=800,y=h2)
                            h2+=30
                    if(ww=="03"):
                        flag=0
                        for a in line[1].split():
                            if(a=="03"):
                                flag=1
                        if(flag==0):
                            rb113=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar113).place(x=800,y=h2)
                            h2+=30
                    if(ww=="04"):
                        flag=0
                        for a in line[1].split():
                            if(a=="04"):
                                flag=1
                        if(flag==0):
                            rb114=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar114).place(x=800,y=h2)
                            h2+=30
                    if(ww=="05"):
                        flag=0
                        for a in line[1].split():
                            if(a=="05"):
                                flag=1
                        if(flag==0):
                            rb115=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar115).place(x=800,y=h2)
                            h2+=30
                    if(ww=="06"):
                        flag=0
                        for a in line[1].split():
                            if(a=="06"):
                                flag=1
                        if(flag==0):
                            rb116=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar116).place(x=800,y=h2)
                            h2+=30
                    if(ww=="07"):
                        flag=0
                        for a in line[1].split():
                            if(a=="07"):
                                flag=1
                        if(flag==0):
                            rb117=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar117).place(x=800,y=h2)
                            h2+=30
                    if(ww=="08"):
                        flag=0
                        for a in line[1].split():
                            if(a=="08"):
                                flag=1
                        if(flag==0):
                            rb118=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar118).place(x=800,y=h2)
                            h2+=30
                    if(ww=="09"):
                        flag=0
                        for a in line[1].split():
                            if(a=="09"):
                                flag=1
                        if(flag==0):
                            rb119=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar119).place(x=800,y=h2)
                            h2+=30
                    if(ww=="10"):
                        flag=0
                        for a in line[1].split():
                            if(a=="10"):
                                flag=1
                        if(flag==0):
                            rb1110=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1110).place(x=800,y=h2)
                            h2+=30
                    if(ww=="11"):
                        flag=0
                        for a in line[1].split():
                            if(a=="11"):
                                flag=1
                        if(flag==0):
                            rb1111=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1111).place(x=800,y=h2)
                            h2+=30
                    if(ww=="12"):
                        flag=0
                        for a in line[1].split():
                            if(a=="12"):
                                flag=1
                        if(flag==0):
                            rb1112=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1112).place(x=800,y=h2)
                            h2+=30
                    if(ww=="13"):
                        flag=0
                        for a in line[1].split():
                            if(a=="13"):
                                flag=1
                        if(flag==0):
                            rb1113=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1113).place(x=800,y=h2)
                            h2+=30
                    if(ww=="14"):
                        flag=0
                        for a in line[1].split():
                            if(a=="14"):
                                flag=1
                        if(flag==0):
                            rb1114=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1114).place(x=800,y=h2)
                            h2+=30
                    if(ww=="15"):
                        flag=0
                        for a in line[1].split():
                            if(a=="15"):
                                flag=1
                        if(flag==0):
                            rb1115=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1115).place(x=800,y=h2)
                            h2+=30
                    if(ww=="16"):
                        flag=0
                        for a in line[1].split():
                            if(a=="16"):
                                flag=1
                        if(flag==0):
                            rb1116=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1116).place(x=800,y=h2)
                            h2+=30
                    if(ww=="17"):
                        flag=0
                        for a in line[1].split():
                            if(a=="17"):
                                flag=1
                        if(flag==0):
                            rb1117=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1117).place(x=800,y=h2)
                            h2+=30
                    if(ww=="18"):
                        flag=0
                        for a in line[1].split():
                            if(a=="18"):
                                flag=1
                        if(flag==0):
                            rb1118=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1118).place(x=800,y=h2)
                            h2+=30
                    if(ww=="19"):
                        flag=0
                        for a in line[1].split():
                            if(a=="19"):
                                flag=1
                        if(flag==0):
                            rb1119=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1119).place(x=800,y=h2)
                            h2+=30
                    if(ww=="20"):
                        flag=0
                        for a in line[1].split():
                            if(a=="20"):
                                flag=1
                        if(flag==0):
                            rb1120=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1120).place(x=800,y=h2)
                            h2+=30
                    if(ww=="21"):
                        flag=0
                        for a in line[1].split():
                            if(a=="21"):
                                flag=1
                        if(flag==0):
                            rb1121=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1121).place(x=800,y=h2)
                            h2+=30
                    if(ww=="22"):
                        flag=0
                        for a in line[1].split():
                            if(a=="22"):
                                flag=1
                        if(flag==0):
                            rb1122=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1122).place(x=800,y=h2)
                            h2+=30
                    if(ww=="23"):
                        flag=0
                        for a in line[1].split():
                            if(a=="23"):
                                flag=1
                        if(flag==0):
                            rb1123=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1123).place(x=800,y=h2)
                            h2+=30
                    if(ww=="24"):
                        flag=0
                        for a in line[1].split():
                            if(a=="24"):
                                flag=1
                        if(flag==0):
                            rb1124=Checkbutton(self.newWindow6,text=ww,height=1,width=50,onvalue=1,offvalue=0,bg="cornsilk2",fg="black",font="Algerian 12 bold",variable=self.ceckvar1124).place(x=800,y=h2)
                            h2+=30
        self.startjrny=StringVar()
        self.destjrny=StringVar()
        book=Button(self.newWindow6,text="Submit",font="Algerian 12 bold",bg="cornflowerblue",fg="black",height=2,width=20,command=self.bill).place(x=630,y=950)
        selectstart=Label(self.newWindow6,text="Enter strat of your journey",width=25,height=1,bg="cornsilk2",fg="black",font="Algerian 16 bold").place(x=300,y=840)
        start=Entry(self.newWindow6,font="Algerian 14 bold",textvariable=self.startjrny).place(x=830,y=840,height=20)
        selectdest=Label(self.newWindow6,text="Enter destination",width=25,height=1,bg="cornsilk2",fg="black",font="Algerian 16 bold").place(x=300,y=900)
        dest=Entry(self.newWindow6,font="Algerian 14 bold",textvariable=self.destjrny).place(x=830,y=900,height=20)
root = Tk()
page(root)
root.mainloop()