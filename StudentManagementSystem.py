def deletestudent():
    deletee = studenttable.focus()
    content = studenttable.item(deletee)
    pp = content['values'][0]
    strr = 'delete from studentdata where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification','Id {} deleted sucessfully ...'.format(pp))
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    alldata = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in alldata:
        vdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vdata)

def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = dateval.get()
        addedtime = timeval.get()

        strr = 'update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,addeddate=%s,addedtime=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,addeddate,addedtime,id))
        con.commit()
        messagebox.showinfo('Notification', 'Id {} Modified sucessfully...'.format(id),parent=updateroot)

        strr = 'select * from studentdata'
        mycursor.execute(strr)
        alldata = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in alldata:
            vdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vdata)


    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+250+120')
    updateroot.title('Student Management System')
    updateroot.config(bg='blue')
    updateroot.iconbitmap('profileicon.ico')
    updateroot.resizable(False,False)
    ############################################# Updatestudent Lables
    idlabel = Label(updateroot,text='Enter Id : ',font=('times',20,'bold'),bg='gold2',relief=GROOVE,width=12,borderwidth=3)
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot, text='Enter Name : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Enter Mobile : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Enter Email : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Enter Address : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Enter Gender : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Enter D.O.B : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Enter Date : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,
                     borderwidth=3)
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Enter Time : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,
                      borderwidth=3)
    timelabel.place(x=10, y=490)

    #################################################### update student entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=490)
#################################################### add button of add student
    submitbtn = Button(updateroot,text='Submit',font=('roman',15,'bold'),bd=5,width=20,borderwidth=5,activebackground='blue',activeforeground='white',
                       bg='red',command=update)
    submitbtn.place(x=150,y=535)

    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if (len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()

################################################## Search Fileds

def searchstudent():
    def searchadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%y")

        if (id != ''):
            strr = 'select * from studentdata where id=%s'
            mycursor.execute(strr,(id))
            alldata = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in alldata:
                vdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vdata)
        elif (name != ''):
            strr = 'select * from studentdata where name=%s'
            mycursor.execute(strr,(name))
            alldata = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in alldata:
                vdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vdata)
        elif (mobile != ''):
            strr = 'select * from studentdata where mobile=%s'
            mycursor.execute(strr,(mobile))
            alldata = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in alldata:
                vdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vdata)
        elif (email != ''):
            strr = 'select * from studentdata where email=%s'
            mycursor.execute(strr,(email))
            alldata = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in alldata:
                vdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vdata)
        elif (address != ''):
            strr = 'select * from studentdata where address=%s'
            mycursor.execute(strr,(address))
            alldata = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in alldata:
                vdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vdata)
        elif (gender != ''):
            strr = 'select * from studentdata where gender=%s'
            mycursor.execute(strr,(gender))
            alldata = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in alldata:
                vdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vdata)
        elif (dob != ''):
            strr = 'select * from studentdata where dob=%s'
            mycursor.execute(strr,(dob))
            alldata = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in alldata:
                vdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vdata)
        elif (addeddate != ''):
            strr = 'select * from studentdata where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            alldata = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in alldata:
                vdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vdata)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='blue')
    searchroot.iconbitmap('profileicon.ico')
    searchroot.resizable(False,False)
    ############################################# Addstudent Lables
    idlabel = Label(searchroot,text='Enter Id : ',font=('times',20,'bold'),bg='gold2',relief=GROOVE,width=12,borderwidth=3)
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot, text='Enter Name : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text='Enter Mobile : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text='Enter Email : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text='Enter Address : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text='Enter Gender : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text='Enter D.O.B : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text='Enter Date : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,
                     borderwidth=3)
    datelabel.place(x=10, y=430)

    #################################################### addstudent entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)
#################################################### add button of add student
    submitbtn = Button(searchroot,text='Submit',font=('roman',15,'bold'),bd=5,width=20,borderwidth=5,activebackground='blue',activeforeground='white',
                       bg='red',command=searchadd)
    submitbtn.place(x=150,y=485)
    searchroot.mainloop()

############################################### add student
def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%y")
        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notification','Id {} Name {} added sucessfully...and want to clean the form'.format(id,name),parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notification','Id already exist try another id...',parent=addroot)

        strr = 'select * from studentdata'
        mycursor.execute(strr)
        alldata = mycursor.fetchall();
        studenttable.delete(*studenttable.get_children())
        for i in alldata:
            vdata = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vdata)


    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='blue')
    addroot.iconbitmap('profileicon.ico')
    addroot.resizable(False,False)
    ############################################# Addstudent Lables
    idlabel = Label(addroot,text='Enter Id : ',font=('times',20,'bold'),bg='gold2',relief=GROOVE,width=12,borderwidth=3)
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot, text='Enter Name : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter Email : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Enter Address : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text='Enter Gender : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Enter D.O.B : ', font=('times', 20, 'bold'), bg='gold2', relief=GROOVE, width=12,borderwidth=3)
    doblabel.place(x=10, y=370)

    #################################################### addstudent entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)
#################################################### add button of add student
    submitbtn = Button(addroot,text='Submit',font=('roman',15,'bold'),bd=5,width=20,borderwidth=5,activebackground='blue',activeforeground='white',
                       bg='red',command=submitadd)
    submitbtn.place(x=150,y=420)

    addroot.mainloop()

def showstudent():
    strr = 'select * from studentdata'
    mycursor.execute(strr)
    alldata = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in alldata:
        vdata = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vdata)
def exportstudent():
    ff =filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id','Name','Mobile','Email','Adderess','Gender','D.O.B','AddedDate','Addedtime']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notification', 'Student Data Exported At {}'.format(paths))

def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do You Want To Exit..?')
    if(res==True):
        root.destroy()


######################################## Connection of Database

def connectdb():
    def connecteddb():
        global con,mycursor;

        host = hostval.get()
        user = userval.get()
        password = passwordval.get()

        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()

        except:
            messagebox.showerror('Notifications','Data is incorrect please ry again')
            return

        try:
            strr = 'create database studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)

            strr = 'create table studentdata(id int NOT NULL,name varchar(20),mobile varchar(15),email varchar(30),address varchar(100),gender varchar(6),dob varchar(20),addeddate varchar(40),addedtime varchar(40),PRIMARY KEY (id))'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Database Created & now you are connected to the database.....',parent=dbroot)
        except:
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)

            messagebox.showinfo('Notification','Now you are connected to the database.....',parent=dbroot)
        dbroot.destroy()

    dbroot= Toplevel()
    dbroot.grab_set()
    dbroot.iconbitmap('profileicon.ico')
    dbroot.geometry('470x250+680+230')
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')

    ####################################################### Connect Db Labels

    idlable = Label(dbroot,text='Enter Host: ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    idlable.place(x=10,y=10)

    namelabel = Label(dbroot, text='Enter Username: ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=13, anchor='w')
    namelabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text='Enter Password: ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,width=13, anchor='w')
    passwordlabel.place(x=10, y=130)

    hostentry = Entry(dbroot,font=('roman',15),bd=5)
    hostentry.place(x=250,y=10)

    hostentry = Entry(dbroot, font=('roman', 15), bd=5)
    hostentry.place(x=250, y=70)

    hostentry = Entry(dbroot, font=('roman', 15), bd=5)
    hostentry.place(x=250, y=130)

    ####################################################### Connect Db Submit Button

    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()


    hosontry = Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hosontry.place(x=250,y=10)

    userval = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userval.place(x=250, y=70)

    passwordlabel = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordlabel.place(x=250, y=130)

    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackgroun='blue',
                          activeforeground='white',command=connecteddb)
    submitbutton.place(x=140,y=190)

    dbroot.mainloop()

###################################################################
def clockt():
    time_strint = time.strftime("%H:%M:%S")
    datetime_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+datetime_string+"\nTime : "+time_strint)
    clock.after(20,clockt)
##################################################################
import random
colors = ['red','green','blue','yellow','yellow','red2']
ss=random
def IntroLabelColor():
    fg = random.choice(colors)
    SliderLable.config(fg=fg)
    SliderLable.after(40,IntroLabelColor)
##########################################
def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        SliderLable.config(text=text)
    else:
        text = text+ss[count]
        SliderLable.config(text=text)
        count += 1
    SliderLable.after(200,IntroLabelTick)
#################################################
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time

root=Tk()
root.title('Student Management System')
root.config(bg='gold2')
root.geometry('1174x700+100+20')
root.iconbitmap('profileicon.ico')
root.resizable(False,False)
###################################################### Frames

DataEntryFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

############################################################# Data Entry Frame

welclabel = Label(DataEntryFrame,text='-------------Welcome-------------',width=25,font=('arial',22,'italic bold'),bg='gold2')
welclabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='1. Add Student',font=('chiller',20,'bold'),width=25,bd=6,bg='skyblue3',activebackground='blue',relief=GROOVE,
                activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

#######################################################################

searchbtn = Button(DataEntryFrame,text='2. Search Student',font=('chiller',20,'bold'),width=25,bd=6,bg='skyblue3',activebackground='blue',relief=GROOVE,
                activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete Student',font=('chiller',20,'bold'),width=25,bd=6,bg='skyblue3',activebackground='blue',relief=GROOVE,
                activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Student',font=('chiller',20,'bold'),width=25,bd=6,bg='skyblue3',activebackground='blue',relief=GROOVE,
                activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showbtn = Button(DataEntryFrame,text='5. Show All',font=('chiller',20,'bold'),width=25,bd=6,bg='skyblue3',activebackground='blue',relief=GROOVE,
                activeforeground='white',command=showstudent)
showbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Export Data',font=('chiller',20,'bold'),width=25,bd=6,bg='skyblue3',activebackground='blue',relief=GROOVE,
                activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7. Exit',font=('chiller',20,'bold'),width=25,bd=6,bg='skyblue3',activebackground='blue',relief=GROOVE,
                activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)

############################################################ Show data frame
ShowDataFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)

##################################################### Show DataFrame
style = ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),foreground='black',background='cyan')

scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
scroll_y.pack(side=RIGHT,fill=Y)

studenttable = Treeview(ShowDataFrame,columns=('ID','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time'),
                        yscrollcommand = scroll_y,xscrollcommand=scroll_x)

scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

studenttable.heading('ID',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile',text='Mobile')
studenttable.heading('Email',text='Address')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')

studenttable['show'] = 'headings'

studenttable.column('ID',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)

studenttable.pack(fill=BOTH,expand=1)

####################################################### Slider
ss = "Welcome To Student Management System"
count = 0
text = ''

SliderLable = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=5,width=35,bg='cyan')
SliderLable.place(x=260,y=0)
IntroLabelTick()
IntroLabelColor()
######################################################## Clock

clock = Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='lawn green')
clock.place(x=0,y=0)
clockt()
########################################################## ConnectDatabaseButton
connectbutton = Button(root,text='Connect TO Database',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bg='green2',
                       activebackgroun='blue',activeforeground='white',command=connectdb)
connectbutton.place(x=930,y=0)

root.mainloop()
