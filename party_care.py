from tkcalendar import Calendar, DateEntry
from tkinter import *
import tkinter  as tk
from tkinter.ttk import Combobox as cb
from tkinter import messagebox
from tkinter import ttk 
import datetime
import pandas as pd
import pyautogui as py


#global variables 
DATE=''
pName=''
capName=''
rName=''
label2=''
labelName=''
entryName=""
labelDate=''
month=''
year=''
search=''
tv=''
top=''
cal=''
namecount=''
datecount=''
nameSearchButton=''
entryNameDate=''
dateSearch=''

def getvalue(key,d): #(KEY,DICTANORY)
    for k,v in d.items():
        if k==key:
            return v

def saveData():
	global DATE,cal
	resortName=c1.get()
	captainName=c2.get()
	waiterName=c3.get()
	dinlunch=c.get()
	#print(DATE)
	#\n1-2-,amar garden,ravi,shaam,DINNER
	print(resortName)
	print(captainName)
	print(waiterName)
	print(dinlunch)
	if DATE=='':
		w=str(datetime.datetime.now()).split(' ')
		DATE=w[0]
	if captainName!='SELECT CAPTAIN FROM LIST' and waiterName!='SELECT WAITER FROM LIST' and resortName!='SELECT RESORT' and dinlunch!='CHOOSE OPTION':
		s='\n'+str(DATE)+','+ resortName+','+captainName.lower()+','+waiterName.lower()+','+dinlunch+'\n'
		print(s)
		f=open('data.csv','a+')
		f.write(s)
		f.close()
		q="ENTRY ADDED \n DATE-"+str(DATE)+'\nNAME-'+waiterName+'\nRESORT_NAME-'+resortName+'\nFor '+dinlunch
		messagebox.showinfo("CONFIRMATION",q)
		#.delete(0,END)
		c1.set('SELECT RESORT')
		c2.set('SELECT CAPTAIN FROM LIST')
		c3.set('SELECT WAITER FROM LIST')
		c.set('CHOOSE OPTION')
		if cal!='':
			cal.place_forget()
			cal=''
	else:
		messagebox.showerror("ERROR!!!", "Sorry! You Have Not Filled All Details!!!.. ")

def searchByName():# to search the person by name
	global tv,entryName,namecount
	tv.delete(*tv.get_children())
	name=entryName.get()
	if entryName.get()!='' or entryName.get() !='SELECT WAITER FROM LIST':
		f=open('data.csv','r')
		w=f.read()
		e=w.split('\n')
		e.pop(0)
		l=[]
		f.close()
		
		s=0
		for i in e:
			if i!='':
				r=i.split(',')
				if r[3]==name:
					s+=1
					l.append(r)
		if s==0:
				print('Name not found')
				messagebox.showwarning("WARNING","NO MATCH FOUND!!!")
		for i in l:
				tv.insert("",'end',values=i )
		if (name!="" or name!='SELECT WAITER FROM LIST' )and s!=0:
			msg='TOTAL NUMBER OF ENTRIES FOR {} - {}'
			messagebox.showinfo("NAME BASED ENTRIES COUNT",msg.format(name,s))
		#namecount=Label(top,text='TOTAL NUMBER OF ENTRIES for  - '+str(s),bg='red',fg='orange')
		#namecount.place(x=600,y=200)


def datesplit(e):
    d=e.split('-')
    return [d[0],d[1]]
    
def searchByDateName():
	global month,year,entryNameDate,datecount
	tv.delete(*tv.get_children())
	e={'JANUARY':'01','FEBRUARY':'02','MARCH':'03','APRIL':'04','MAY':'05','JUNE':'06','JULY':'07','AUGUST':'08','SEPTEMBER':"09",'OCTOBER':"10",'NOVEMBER':'11','DECEMBER':'12'}
	MONTH=getvalue(month.get(),e)
	YEAR=year.get()
	#print(MONTH,YEAR)
	f=open('data.csv','r')
	w=f.read()
	e=w.split('\n')
	f.close()
	e.pop(0)
	l=[]
	waitername=entryNameDate.get()
	count=0
	for i in e:
		if i!='':
			r=i.split(',')
			d=r[0]
			d=datesplit(d)
			if YEAR==d[0] and MONTH==d[1] and waitername.lower()==r[3].lower():
				count+=1
				l.append(r)


	if count==0:
		print('data not found')
		messagebox.showerror('Error!!','NO Result Found!!!!')
	else:
		for i in l:
			tv.insert("",'end',values=i )
		if (waitername!="" or waitername!="SELECT WAITER FROM LIST") and (month.get()!="" or month.get()!="SELECT MONTH") and (year!="" or year!="SELECT YEAR") and count!=0:
			msg="WAITER_NAME-{}\nMonth-{}\nNo OF DAYS WORKED -{}".format(waitername,month.get(),count)
			messagebox.showinfo("REPORT",msg)
		#datecount=Label(top,text='TOTAL NUMBER OF ENTRIES   - '+str(count),bg='red',fg='orange')
		#datecount.place(x=900,y=1000)






def searchoption():
	global label2,labelName,entryName,labelDate,month,year,search,tv,top,namecount,nameSearchButton,entryNameDate,dateSearch,datecount

	print(search.get())

	if search.get()=="ALL":
		if nameSearchButton!='':
			nameSearchButton.place_forget()
			nameSearchButton=''

		if dateSearch!='':
			dateSearch.place_forget()
			dateSearch=''

		if labelName!='':
			labelName.place_forget()
			labelName=''

		if entryNameDate!='':
			entryNameDate.place_forget()
			entryNameDate=''


		if entryName!="":
			entryName.place_forget()
			entryName=""

		if year!='':
			year.place_forget()
			year=''

		if month!='':
			month.place_forget()
			month=''

		if labelDate!='':
			labelDate.place_forget()
			labelDate=''


		
		#frm.pack(side=tk.LEFT,fill=tk.X)
		#frm.pack(side=tk.TOP,padx=20)
		"""
	
		if namecount!='':
			namecount.place_forget()
			namecount=''




		if datecount!='':
			datecount.place_forget()
			datecount='' """

		tv.delete(*tv.get_children()) 

		f=open('data.csv','r')
		w=f.read()
		e=w.split('\n\n')
		l=[]
		count=0
		for i in e:
			if i!='' or i !=' ' or i!='\n':
				r=i.split(',')
				l.append(r)
				count+=1
		l.pop(0)#remove the first row
		for i in l:
			if i!='':
				tv.insert("",'end',values=i )
		#label2=Label(top,text='TOTAL NUMBER OF ENTRIES - '+str(count),bg='green',fg='orange')
		#label2.place(x=200,y=200)
		messagebox.showinfo("ENTRIES COUNT",'TOTAL NUMBER OF ENTRIES - '+str(len(l)))
		
		

		search.set("CHOOSE OPTION")
	elif search.get()=='NAME':
		print('NAME')



		if year!='':
			year.place_forget()
			year=''

		if month!='':
			month.place_forget()
			month=''

		if labelDate!='':
			labelDate.place_forget()
			labelDate=''

		if dateSearch!='':
			dateSearch.place_forget()
			dateSearch=''


		tv.delete(*tv.get_children())
	    
		labelName=Label(top,text='Enter The Name of Waiter To Search:',bg='green',fg='orange')
		labelName.place(x=220,y=150)
		f=open('waiter_names.csv','r')
		cf=f.read()
		e=cf.split('\n')
		e.remove('WAITER_NAMES')
		f.close()
		wat=[i for i in e if i!='']
		entryName=cb(top,value=wat,width=25)
		entryName.set('SELECT WAITER FROM LIST')
		entryName.place(x=500,y=150)
		#entryName=Entry(top,width=25)
		#entryName.place(x=500,y=150)
		nameSearchButton=Button(top, text='Search',command=searchByName)
		nameSearchButton.place(x=800,y=150)

		


            



		#place_forget()--to remove any widget
		#b = Button(root, text="Delete me", command=lambda: b.pack_forget())
		#b.pack()
	elif search.get()=='DATE':
		tv.delete(*tv.get_children())
		if nameSearchButton!='':
			nameSearchButton.place_forget()
			nameSearchButton=''

		if entryName!='':
			entryName.place_forget()
			entryName=''

		if labelName!='':
			labelName.place_forget()
			labelName=''

		"""if label2!='':
			label2.place_forget()
			label2=''


		if namecount!='':
			namecount.place_forget()
			namecount=''
		"""

		labelDate=Label(top,text='ENTER NAME & DATE:- ',bg='green',fg='orange')
		labelDate.place(x=220,y=150)
		f=open('waiter_names.csv','r')
		cf=f.read()
		e=cf.split('\n')
		f.close()
		e.remove('WAITER_NAMES')
		wat=[i for i in e if i!='']
		entryNameDate=cb(top,value=wat,width=25)
		entryNameDate.set('SELECT WAITER FROM LIST')
		entryNameDate.place(x=220,y=200)

		e={'JANUARY':'01','FEBRUARY':'02','MARCH':'03','APRIL':'04','MAY':'05','JUNE':'06','JULY':'07','AUGUST':'08','SEPTEMBER':"09",'OCTOBER':"10",'NOVEMBER':'11','DECEMBER':'12'}
		month=cb(top,value=list(e.keys()),width=25)
		month.set('SELECT MONTH')
		month.place(x=500,y=150)
		l=['2020','2021','2022','2023','2024','2025']
		year=cb(top,value=l,width=25)
		year.set('SELECT YEAR')
		year.place(x=500,y=200)
		dateSearch=Button(top, text='Search',command=searchByDateName)
		dateSearch.place(x=800,y=200)

	else:
		tv.delete(*tv.get_children())
		"""
		if label2!='':
			label2.place_forget()
			label2=''
		if labelName!='':
			labelName.place_forget()
			labelName=''
		if entryName!='':
			entryName.place_forget()
			entryName=''
		if year!='':
			year.place_forget()
			year=''
		if month!='':
			month.place_forget()
			month=''
		if labelDate!='':
			labelDate.place_forget()
			labelDate=''
		if namecount!='':
			namecount.place_forget()
			namecount=''
		if nameSearchButton!='':
			nameSearchButton.place_forget()
			nameSearchButton=''

		if entryNameDate!='':
			entryNameDate.place_forget()
			entryNameDate=''

		if dateSearch!='':
			dateSearch.place_forget()
			dateSearch=''
		if datecount!='':
			datecount.place_forget()
			datecount=''"""
	    
		messagebox.showinfo("PROBLEM!!","You have not Choosen any option!!!")



def SEARCH():
	a=py.password(text='ENTER THE PASSWORD TO ACCESS THE RECORDS',title='ACCESS',default='',mask='*',root=root)
	#print(a)
	global search,tv,top
	if a=='akash':
		top=Toplevel(root)
		top.config(background='grey')
		top.geometry('1200x800+100+100')
		top.resizable(width=False,height=False)
		top.title('RECORDS')
		label1=Label(top,text='SEARCH By ',bg='green',fg='orange')
		label1.place(x=250,y=100)
		menu=['NAME','DATE','ALL']
		search=StringVar()
		LD=OptionMenu(top,search,*menu)
		search.set("CHOOSE OPTION")
		LD.config(width=15)
		LD.place(x=350,y=100)

		b1=Button(top,text='PRESS TO CHOOSE',bg='green',fg='red',command=searchoption)
		b1.place(x=550,y=100)
		frm=Frame(top)
		frm.pack(side=tk.LEFT,padx=30)
		tv=ttk.Treeview(frm,columns=(1,2,3,4,5),show="headings",height="15")
		tv.pack()
		tv.heading(1,text="DATE",anchor=tk.W)
		tv.heading(2,text="RESORT_NAME")
		tv.heading(3,text="CAPTAIN_NAME")
		tv.heading(4,text="WAITER_NAME")
		tv.heading(5,text="DINNER/LUNCH")
	else:
		messagebox.showwarning("WARNING!!!!", "Password is Incorrect\n Please Try again!!!")



def addwaiter():
	global pName
	w=pd.read_csv('waiter_names.csv')
	print(w['WAITER_NAMES'].tolist())
	old=w['WAITER_NAMES'].tolist()
	new=pName.get()#waiter_name
	if new!='':
		if new not in old:
			f=open('waiter_names.csv','a+')
			f.write('\n'+new)
			f.close()
			messagebox.showinfo("CONFIRMATION",'NAME ADDED TO LIST!!')
			root.destroy()
		else:
			messagebox.showerror("ERROR!!!", "NAME ALREADY IN THE LIST")
	else:
		messagebox.showerror("ERROR!!!", "Sorry! Please Enter the Name...")
		

def add_person():
	global pName
	top=Toplevel(root)
	top.config(background='grey')
	top.geometry('600x100+600+200')
	top.resizable(width=False,height=False)
	e=Label(top,text='WAITER_NAME',bg='BLACK',fg='white',font=('',15))
	e.grid(column=3,row=1)
	labelp=Label(top,text='ENTER THE NAME OF WAITER TO ADD',bg='BLACK',fg='white',font=('',15))
	labelp.grid(column=1,row=3)
	pName=Entry(top,width=25)
	pName.grid(column=3,row=3)
	add=Button(top,text='ADD',bg='green',fg='red',command=addwaiter)
	add.grid(column=3,row=5)




def addcaptain():
	global capName
	w=pd.read_csv('captain_names.csv')
	print(w['CAPTAIN_NAMES'].tolist())
	old=w['CAPTAIN_NAMES'].tolist()
	new=capName.get()#captain_name
	if new!='':
		if new not in old:
			f=open('captain_names.csv','a+')
			f.write('\n'+new)
			f.close()
			messagebox.showinfo("CONFIRMATION",'NAME ADDED TO LIST!!')
			root.destroy()
		else:
			messagebox.showerror("ERROR!!!", "NAME ALREADY IN THE LIST")
	else:
		messagebox.showerror("ERROR!!!", "Sorry! Please Enter the Name...")



def add_captain():
	global capName
	top=Toplevel(root)
	top.config(background='grey')
	top.geometry('600x100+600+200')
	top.resizable(width=False,height=False)
	e=Label(top,text='CAPTAIN_NAME',bg='BLACK',fg='white',font=('',15))
	e.grid(column=3,row=1)
	labelp=Label(top,text='ENTER THE NAME OF CAPTAIN-',bg='BLACK',fg='white',font=('',15))
	labelp.grid(column=1,row=3)
	capName=Entry(top,width=25)
	capName.grid(column=3,row=3)
	add=Button(top,text='ADD',bg='green',fg='red',command=addcaptain)
	add.grid(column=3,row=5)


def delete():
	pass

def addresort():
	global rName
	w=pd.read_csv('resort_names.csv')
	print(w['RESORT_NAMES'].tolist())
	old=w['RESORT_NAMES'].tolist()
	new=rName.get()#captain_name
	if new!='':
		if new not in old:
			f=open('resort_names.csv','a+')
			f.write('\n'+new)
			f.close()
			messagebox.showinfo("CONFIRMATION",'RESORT NAME ADDED TO LIST!!')
			root.destroy()
		else:
			messagebox.showerror("ERROR!!!", "RESORT NAME ALREADY IN THE LIST")
	else:
		messagebox.showerror("ERROR!!!", "Sorry! Please Enter the Name...")

def add_resort():
	global rName
	top=Toplevel(root)
	top.config(background='grey')
	top.geometry('600x100+600+200')
	top.resizable(width=False,height=False)
	e=Label(top,text='RESORT_NAME',bg='BLACK',fg='white',font=('',15))
	e.grid(column=3,row=1)
	labelp=Label(top,text='ENTER NEW RESORT NAME-',bg='BLACK',fg='white',font=('',15))
	labelp.grid(column=1,row=3)
	rName=Entry(top,width=25)
	rName.grid(column=3,row=3)
	add=Button(top,text='ADD',bg='green',fg='red',command=addresort)
	add.grid(column=3,row=5)


def date():
    def print_sel():
    	global cal,DATE
    	DATE=calen.selection_get()
    	if DATE!='':
    		cal=Label(root,text=DATE,bg='red',fg='black')
    		cal.place(x=300,y=280)
    		top.destroy()
        

    top = tk.Toplevel(root)
    top.geometry('300x300+650+400')

    import datetime
    today = datetime.date.today()

    #mindate = today
    mindate = datetime.date(year=2018, month=1, day=1)
    #maxdate = today + datetime.timedelta(days=5)
    maxdate = datetime.date(year=2030, month=1, day=1)

    #print(mindate, maxdate)

    calen = Calendar(top, font="Arial 10", selectmode='day', locale='en_US',
                   mindate=mindate, maxdate=maxdate, disabledforeground='red',
                   cursor="hand1", year=2020, month=1, day=1)
    calen.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()



root=Tk()

root.title("THE PARTY CARE")
root.config(bg='grey')
#root.geometry('1920x1080')
root.geometry('900x750+600+150')
root.resizable(width=False,height=True)

label=Label(root,text='THE PARTY CARE',bg='black',fg='red',font=('',40))
label.pack()

label1=Label(root,text='OWNED By',bg='azure2',fg='black',font=('Arial',15))
label1.pack()

label2=Label(root,text='AMAR DHILLON',bg='BLACK',fg='white',font=('',20))
label2.pack()
#Button(root, text='REFRESH', command=date).place(x=250,y=250)

label3=Label(root,text='RESORT NAME',bg='black',fg='red')
label3.place(x=65,y=210)
#l=pd.read_csv('resort_names.csv')
#l=l['RESORT_NAMES'].tolist()
#print(s['RESORT_NAMES'].tolist())
f=open('resort_names.csv','r')
cf=f.read()
e=cf.split('\n')
e.remove('RESORT_NAMES')
f.close()
e=[i for i in e if i!='']
c1=cb(root,value=e,width=25)
c1.set('SELECT RESORT')
c1.place(x=250,y=210)

#Date of function
label4=Label(root,text='DATE FOR FUNCTION',bg='black',fg='red')
label4.place(x=65,y=250)
Button(root, text='SET DATE FOR THE FUNCTION', command=date).place(x=250,y=250)

#captain name
label5=Label(root,text='CAPTAIN NAME',bg='black',fg='red')
label5.place(x=65,y=310)
#cap=pd.read_csv('captain_names.csv')
#cap=cap['CAPTAIN_NAMES'].tolist()
#cap.append('NONE')
f=open('captain_names.csv','r')
cf=f.read()
e=cf.split('\n')
e.remove('CAPTAIN_NAMES')
e=[i for i in e if i!='']
c2=cb(root,value=e,width=25)
c2.set('SELECT CAPTAIN FROM LIST')
c2.place(x=250,y=310)
f.close()




#waiter name
label6=Label(root,text='WAITER NAME',bg='black',fg='red')
label6.place(x=65,y=360)
#wat=pd.read_csv('waiter_names.csv')
#wat=wat['WAITER_NAMES'].tolist()
#wat.append('Other')
f=open('waiter_names.csv','r')
cf=f.read()
e=cf.split('\n')
f.close()
e.remove('WAITER_NAMES')
wat=[i for i in e if i!='']
c3=cb(root,value=wat,width=25)
c3.set('SELECT WAITER FROM LIST')
c3.place(x=250,y=360)


#lunch/dinner
label7=Label(root,text='LUNCH/DINNER',bg='black',fg='red')
label7.place(x=65,y=400)
menu=['LUNCH','DINNER','OTHER']
c=StringVar()
LD=OptionMenu(root,c,*menu)
c.set("CHOOSE OPTION")
LD.config(width=15)
LD.place(x=250,y=400)

#buttons
b=Button(root,text='SAVE_DETAIL',width=30,bg='black',fg='red',command=saveData)
b.place(x=250,y=460)


b1=Button(root,text='SEARCH RECORDS',width=30,bg='black',fg='red',command=SEARCH)
b1.place(x=250,y=500)


br=Button(root,text='ADD_NEW_RESORT',width=30,bg='black',fg='red',command=add_resort)
br.place(x=250,y=550)

b2=Button(root,text='ADD_PERSON',width=20,bg='black',fg='red',command=add_person)
b2.place(x=400,y=600)

b3=Button(root,text='ADD_CAPTAIN',width=20,bg='black',fg='red',command=add_captain)
b3.place(x=200,y=600)


b5=Button(root,text='DELETE_ENTRY',width=30,bg='black',fg='red',command=delete)
b5.place(x=250,y=650)

b4=Button(root,text='EXIT',width=30,bg='black',fg='red',command=root.destroy)
b4.place(x=250,y=700)

root.mainloop()
