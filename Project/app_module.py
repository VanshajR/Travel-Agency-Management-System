import mysql.connector

x="localhost"
y="root"
z="vanshaj"
mydb = mysql.connector.connect(host=x,user=y,passwd=z)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE traveltest16")

mydb = mysql.connector.connect(host=x,user=y,passwd=z,database="traveltest16")
mycursor = mydb.cursor()

# Customer
mycursor.execute("CREATE TABLE customer(cust_id char(5) Primary key,Name char(15),Age integer(2),Email char(20),Start_Date char(50));")
mycursor.execute("CREATE TABLE booking(cust_id char(5) Primary key,Destination char(20),Mode_of_transport char(10),No_Days integer(2),Hotel_Star integer(2));")

# Transport agencies
mycursor.execute("CREATE TABLE agencies(Destination char(20),Mode_of_transport char(5),agen_id char(5) Primary key);")
mycursor.execute("CREATE TABLE agen_names(agen_id char(5) Primary key,Trasport_Agency char(20),Price integer(10));")

# Hotels
mycursor.execute("CREATE TABLE hotels(Destination char(20),Tour_stars integer(2),hotel_id char(5) Primary key);")
mycursor.execute("CREATE TABLE hnames(hotel_id char(5) Primary key,Hotel_name char(20),Rate_per_day integer(10));")


# Inputting Values Agencies table
mycursor.execute("INSERT INTO agencies VALUES('Jaipur','Land','AB01');")
mycursor.execute("INSERT INTO agencies VALUES('Jaipur','Land','BH08');")
mycursor.execute("INSERT INTO agencies VALUES('Jaipur','Air','CG09');")
mycursor.execute("INSERT INTO agencies VALUES('Jaipur','Air','SR03');")

mycursor.execute("INSERT INTO agencies VALUES('Ajmer','Land','AV02');")
mycursor.execute("INSERT INTO agencies VALUES('Ajmer','Land','BK00');")
mycursor.execute("INSERT INTO agencies VALUES('Ajmer','Air','CS04');")
mycursor.execute("INSERT INTO agencies VALUES('Ajmer','Air','SK07');")

mycursor.execute("INSERT INTO agencies VALUES('Jaisalmer','Land','AK06');")
mycursor.execute("INSERT INTO agencies VALUES('Jaisalmer','Land','Bl09');")
mycursor.execute("INSERT INTO agencies VALUES('Jaisalmer','Air','CG02');")
mycursor.execute("INSERT INTO agencies VALUES('Jaisalmer','Air','SM04');")

mycursor.execute("INSERT INTO agencies VALUES('Jodhpur','Land','AK03');")
mycursor.execute("INSERT INTO agencies VALUES('Jodhpur','Land','BS11');")
mycursor.execute("INSERT INTO agencies VALUES('Jodhpur','Air','CQ07');")
mycursor.execute("INSERT INTO agencies VALUES('Jodhpur','Air','SK01');")

mycursor.execute("INSERT INTO agencies VALUES('Udaipur','Land','AV08');")
mycursor.execute("INSERT INTO agencies VALUES('Udaipur','Land','BH09');")
mycursor.execute("INSERT INTO agencies VALUES('Udaipur','Air','CG03');")
mycursor.execute("INSERT INTO agencies VALUES('Udaipur','Air','SM01');")

# Inputting Values Agen_names table
mycursor.execute("INSERT INTO agen_names VALUES('AB01','S K Travels',2000);")
mycursor.execute("INSERT INTO agen_names VALUES('BH08','M K S Transport',1800);")
mycursor.execute("INSERT INTO agen_names VALUES('CG09','Arvind  Travels',2500);")
mycursor.execute("INSERT INTO agen_names VALUES('SR03','Varun Transport',2400);")

mycursor.execute("INSERT INTO agen_names VALUES('AV02','Aman Transport',2100);")
mycursor.execute("INSERT INTO agen_names VALUES('BK00','A K Travels',2000);")
mycursor.execute("INSERT INTO agen_names VALUES('CS04','M K S Transport',2600);")
mycursor.execute("INSERT INTO agen_names VALUES('SK07','Aryan Travels',2500);")

mycursor.execute("INSERT INTO agen_names VALUES('AK06','Varun Transport',1900);")
mycursor.execute("INSERT INTO agen_names VALUES('Bl09','Ajay Transport',1800);")
mycursor.execute("INSERT INTO agen_names VALUES('CG02','S M Travels',2600);")
mycursor.execute("INSERT INTO agen_names VALUES('SM04','A S Transport',2400);")

mycursor.execute("INSERT INTO agen_names VALUES('AK03','Aman Transport',2000);")
mycursor.execute("INSERT INTO agen_names VALUES('BS11','A M Travels',1800);")
mycursor.execute("INSERT INTO agen_names VALUES('CQ07','S M Travels',2600);")
mycursor.execute("INSERT INTO agen_names VALUES('SK01','V R Transport',2500);")

mycursor.execute("INSERT INTO agen_names VALUES('AV08','S M Travels',2000);")
mycursor.execute("INSERT INTO agen_names VALUES('BH09','A M Travels',1800);")
mycursor.execute("INSERT INTO agen_names VALUES('CG05','A C Travels',2600);")
mycursor.execute("INSERT INTO agen_names VALUES('SM01','Arvind  Travels',2500);")

# Inputting Values Hotels table
mycursor.execute("INSERT INTO hotels VALUES('Jaipur',2,'HR01');")
mycursor.execute("INSERT INTO hotels VALUES('Jaipur',3,'HM08');")
mycursor.execute("INSERT INTO hotels VALUES('Jaipur',4,'CR09');")

mycursor.execute("INSERT INTO hotels VALUES('Ajmer',2,'CS02');")
mycursor.execute("INSERT INTO hotels VALUES('Ajmer',3,'AM04');")
mycursor.execute("INSERT INTO hotels VALUES('Ajmer',4,'VR07');")

mycursor.execute("INSERT INTO hotels VALUES('Jaisalmer',2,'AK09');")
mycursor.execute("INSERT INTO hotels VALUES('Jaisalmer',3,'BS04');")
mycursor.execute("INSERT INTO hotels VALUES('Jaisalmer',4,'CG05');")

mycursor.execute("INSERT INTO hotels VALUES('Jodhpur',2,'ZH09');")
mycursor.execute("INSERT INTO hotels VALUES('Jodhpur',3,'HK03');")
mycursor.execute("INSERT INTO hotels VALUES('Jodhpur',4,'CM01');")

mycursor.execute("INSERT INTO hotels VALUES('Udaipur',2,'ZM06');")
mycursor.execute("INSERT INTO hotels VALUES('Udaipur',3,'SH03');")
mycursor.execute("INSERT INTO hotels VALUES('Udaipur',4,'BZ07');")

# Inputting Values Hnames table
mycursor.execute("INSERT INTO hnames VALUES('HR01','A M Hotels',800);")
mycursor.execute("INSERT INTO hnames VALUES('HM08','S R Hotels',900);")
mycursor.execute("INSERT INTO hnames VALUES('CR09','Hotel 65',1000);")

mycursor.execute("INSERT INTO hnames VALUES('CS02','A2Z Hotel',900);")
mycursor.execute("INSERT INTO hnames VALUES('AM04','P J Hotels',1100);")
mycursor.execute("INSERT INTO hnames VALUES('VR07','A C Hotel',1200);")

mycursor.execute("INSERT INTO hnames VALUES('AK09','A2Z Hotel',700);")
mycursor.execute("INSERT INTO hnames VALUES('BS04','Praksh Hotels',900);")
mycursor.execute("INSERT INTO hnames VALUES('CG05','V R Hotels',1100);")

mycursor.execute("INSERT INTO hnames VALUES('ZH09','Hotel Aakash',800);")
mycursor.execute("INSERT INTO hnames VALUES('HK03','Hotel AZ',1000);")
mycursor.execute("INSERT INTO hnames VALUES('CM01','Pacific Hotel',1200);")

mycursor.execute("INSERT INTO hnames VALUES('ZM06','Hotel Sunrise',700);")
mycursor.execute("INSERT INTO hnames VALUES('SH03','Hotel Skyline',900);")
mycursor.execute("INSERT INTO hnames VALUES('BZ07','Hotel Pacific',1000);")


mydb.commit()



















