from tkinter import *
import mysql.connector
from random import *
import exp2

x="localhost"
y="root"
z="vanshaj"
mydb = mysql.connector.connect(host=x,user=y,passwd=z)

mydb = mysql.connector.connect(host=x,user=y,passwd=z,database="traveltest16")
mycursor = mydb.cursor()
def confirm():          #defining the function for confirm button
    name_=name.get()
    age_=age.get()
    gen_=gen.get()
    state_=state.get()
    days_=days.get()
    st_date_=st_date.get()
    tran_=transport.get()
    hotel_=hotelst.get()
    email_=email.get()
    dest_=dest.get()
    cust_id=randint(1000,2000)
    mycursor.execute("INSERT INTO customer VALUES(%s,%s,%s,%s,%s)",(cust_id,name_,age_,email_,st_date_))
    mycursor.execute("INSERT INTO booking VALUES(%s,%s,%s,%s,%s)",(cust_id,dest_,tran_,days_,hotel_))
    mydb.commit()

def display():          #defining the function to display deatils before confirming
    s=state.get()
    t=transport.get()
    star=hotelst.get()
    d=days.get()
    print("Your details have been confirmed as follows:")
    print("Name:",name.get())
    print("Age:",age.get())
    print("Gender:",gen.get())
    print("State:",s)
    print("Number of days of stay:",d)
    print("Start Date:",st_date.get())
    print("Transport:",t)
    print("Hotel:",star,"star")
    print("Email:",email.get())
    print("Destination:",dest.get())
    print("Total Price:",exp2.state_price(s,t,star,d))




print("**************WELCOME TO THE TRAVEL AGENCY BOOKING SYSTEM!!!**************")
print()
print()
print("We offer tour packages across Rajashtan, for the magnificent cities of JAIPUR, JODHPUR, JAISALMWER, AND AJMER. Travel to these breathtaking places with us!")
print()
print("To book a tour, fill in the details in the Entry Window, and first DISPLAY, to review the details you have entered and see the calculated price on the basis of your choices, and then CONFIRM your details to make a booking with us.")
print()
print("At the present time, we only offer our services to the states of BIHAR, CHHATTISGARH, GUJARAT, HARYANA, HIMACHAL PRADESH, MADHYA PRADESH, MAHARASHTRA, NEW DELHI, PUNJAB, UTTAR PRADESH and UTTARAKHAND")
print()
print()





window=Tk()
window.title("Entry window")
window.configure(background="black")         #creating the gui interface

Label(window,bg="black",fg="white",text="TRAVEL AGENCY",font="Calibri 36 bold").grid(row=0,column=0)


Label(window,bg="black",fg="white",text="Enter your name:",font="Calibri 14").grid(row=2,column=0,sticky=W)   #taking input of Name of customer
name=Entry(window,width=30,bg="white")
name.grid(row=3,column=0,sticky=W)


Label(window,bg="black",fg="white",text="Enter your age:",font="Calibri 14").grid(row=2,column=1,sticky=W)    #taking input of Age of customer
age=Entry(window,width=30,bg="white")
age.grid(row=3,column=1,sticky=W)


Label(window,bg="black",fg="white",text="Enter Gender(Male/Female)",font="Calibri 14").grid(row=4,column=0,sticky=W)    #taking input of Gender
gen=Entry(window,width=30,bg="white")
gen.grid(row=5,column=0,sticky=W)


Label(window,bg="black",fg="white",text="Enter the name of your state:",font="Calibri 14").grid(row=4,column=1,sticky=W)    #taking input of State
state=Entry(window,width=30,bg="white")
state.grid(row=5,column=1,sticky=W)


Label(window,bg="black",fg="white",text="Enter Number of days you'd like to stay:",font="Calibri 14").grid(row=6,column=0,sticky=W)  #taking input of Number of days guest will be staying 
days=Entry(window,width=30,bg="white")
days.grid(row=7,column=0,sticky=W)


Label(window,bg="black",fg="white",text="Enter Start date(YYYY/MM/DD):",font="Calibri 14").grid(row=6,column=1,sticky=W)  #taking input of Date of start of journey
st_date=Entry(window,width=30,bg="white")
st_date.grid(row=7,column=1,sticky=W)


Label(window,bg="black",fg="white",text="Enter your mode of transportation(Filght/Bus/Train):",font="Calibri 14").grid(row=8,column=0,sticky=W) #taking input of Mode of Transport
transport=Entry(window,width=30,bg="white")
transport.grid(row=9,column=0,sticky=W)


Label(window,bg="black",fg="white",text="Enter the number of star hotel you'd like:",font="Calibri 14").grid(row=8,column=1,sticky=W) #taking input of hotel that customer would like
hotelst=Entry(window,width=30,bg="white")
hotelst.grid(row=9,column=1,sticky=W)


Label(window,bg="black",fg="white",text="Enter your e-mail:",font="Calibri 14").grid(row=10,column=0,sticky=W)  #taking input of E-mail
email=Entry(window,width=30,bg="white")
email.grid(row=11,column=0,sticky=W)



Label(window,bg="black",fg="white",text="Enter your Destination:",font="Calibri 14").grid(row=10,column=1,sticky=W)   #taking input of Destination City
dest=Entry(window,width=30,bg="white")
dest.grid(row=11,column=1,sticky=W)


b2=Button(window,text="Display Details",command=display).grid(row=14,column=0,sticky=W) #Button to display details the customer has entered and the claculated price
b1=Button(window,text="Confirm",command=confirm).grid(row=14,column=1,sticky=W)

window.mainloop()
