import mysql.connector
from tkinter import *
x="localhost"
y="root"
z="vr123"
mydb = mysql.connector.connect(host=x,user=y,passwd=z)

mydb = mysql.connector.connect(host=x,user=y,passwd=z,database="travel")
mycursor = mydb.cursor()

def showall():
    cmd="SELECT * FROM customer"
    mycursor.execute(cmd)
    S=mycursor.fetchall()
    print("="*161)
    F="%14s%14s%14s%14s%14s"
    print(F%("Customer ID","Name","Age","Email","Start Date"))
    for i in S:
        for j in i:
            print("%14s" % j, end=' ')
        print()
    print("="*161)


def hoteldet():
    print("Destinations: 'Jaipur', 'Jaisalmer', 'Udaipur','Ajmer'")
    destin=input("Enter your Destination")
    mycursor.execute("SELECT B.Hotel_name, A.hotel_id, A.Tour_stars from hotels A, hnames B where A.hotel_id=B.hotel_id and Destination= '%s'"%(destin))
    S=mycursor.fetchall()
    print("="*161)
    F="%14s%14s%14s"
    print(F%("Hotel Name","Hotel ID","Stars"))
    for i in S:
        for j in i:
            print("%14s" % j, end=' ')
        print()
    print("="*161)

def transdet():
    print("If you are going by Flight, enter 'Air', and if by bus or train, enter 'Land'")
    transit=input("Enter your Mode")
    destin=input("Enter your destination:")
    mycursor.execute("SELECT B.Trasport_Agency, A.agen_id from agencies A, agen_names B where A.agen_id=B.agen_id and Destination = '%s' and A.Mode_of_Transport='%s'"%(destin,transit))
    S=mycursor.fetchall()
    print("="*161)
    F="%14s%14s"
    print(F%("Agency Name","Agency ID",))
    for i in S:
        for j in i:
            print("%14s" % j, end=' ')
        print()
    print("="*161)
