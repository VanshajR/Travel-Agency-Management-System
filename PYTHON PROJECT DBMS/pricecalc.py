def state_price(s,t,star,d):    #s= name of state, t= mode of transport, star= no of star hotel, d= no of days
    price=0
    fee=0
    zx=s.upper()
    if zx=="BIHAR":
        a=2000
        price+=a
        if t.upper()=="FLIGHT":
            fare=2000
            price+=fare
        elif t.upper()=="BUS":
            fare=1100
            price+=fare
        elif t.upper()=="TRAIN":
            fare=1300
            price+=fare
        else:
            print("Invalid Option")
        if star=="2":
            hprice= 800
            stay=int(d)*hprice
            fee+=stay
        elif star=="3":
            hprice=1300
            stay=int(d)*hprice
            fee+=stay
        elif star=="4":
            hprice=1800
            stay=int(d)*hprice
            fee+=stay
        else:
            print("Invalid Option")
    elif zx=="CHHATISGARH":
        a=1800
        price+=a
        if t.upper()=="FLIGHT":
            fare=1800
            price+=fare
        elif t.upper()=="BUS":
            fare=1000
            price+=fare
        elif t.upper()=="TRAIN":
            fare=1200
            price+=fare
        else:
            print("Invalid Option")
        if star=="2":
            hprice= 1000
            stay=int(d)*hprice
            fee+=stay
        elif star=="3":
            hprice=1300
            stay=int(d)*hprice
            fee+=stay
        elif star=="4":
            hprice=1500
            stay=int(d)*hprice
            fee+=stay
        else:
            print("Invalid Option")
    elif zx=="GUJARAT":
        a=700
        price+=a
        if t.upper()=="FLIGHT":
            fare=1000
            price+=fare
        elif t.upper()=="BUS":
            fare=600
            price+=fare
        elif t.upper()=="TRAIN":
            fare=900
            price+=fare
        else:
            print("Invalid Option")
        if star=="2":
            hprice= 900
            stay=int(d)*hprice
            fee+=stay
        elif star=="3":
            hprice=1200
            stay=int(d)*hprice
            fee+=stay
        elif star=="4":
            hprice=1350
            stay=int(d)*hprice
            fee+=stay
        else:
            print("Invalid Option")
    elif zx=="MAHARASHTRA":
        a=3000
        price+=a
        if t.upper()=="FLIGHT":
            fare=2000
            price+=fare
        elif t.upper()=="BUS":
            fare=1300
            price+=fare
        elif t.upper()=="TRAIN":
            fare=1600
            price+=fare
        else:
            print("Invalid Option")
        if star=="2":
            hprice= 1000
            stay=int(d)*hprice
            fee+=stay
        elif star=="3":
            hprice=1250
            stay=int(d)*hprice
            fee+=stay
        elif star=="4":
            hprice=1600
            stay=int(d)*hprice
            fee+=stay
        else:
            print("Invalid Option")
    elif zx=="MADHYA PRADESH":
        a=2500
        price+=a
        if t.upper()=="FLIGHT":
            fare=2000
            price+=fare
        elif t.upper()=="BUS":
            fare=1400
            price+=fare
        elif t.upper()=="TRAIN":
            fare=1700
            price+=fare
        else:
            print("Invalid Option")
        if star=="2":
            hprice= 800
            stay=int(d)*hprice
            fee+=stay
        elif star=="3":
            hprice=1100
            stay=int(d)*hprice
            fee+=stay
        elif star=="4":
            hprice=1400
            stay=int(d)*hprice
            fee+=stay
        else:
            print("Invalid Option")
    elif zx=="UTTAR PRADESH":
        a=1700
        price+=a
        if t.upper()=="FLIGHT":
            fare=1600
            price+=fare
        elif t.upper()=="BUS":
            fare=900
            price+=fare
        elif t.upper()=="TRAIN":
            fare=1100
            price+=fare
        else:
            print("Invalid Option")
        if star=="2":
            hprice= 900
            stay=int(d)*hprice
            fee+=stay
        elif star=="3":
            hprice=1150
            stay=int(d)*hprice
            fee+=stay
        elif star=="4":
            hprice=1400
            stay=int(d)*hprice
            fee+=stay
        else:
            print("Invalid Option")
    elif zx=="HARYANA":
        a=1900
        price+=a
        if t.upper()=="FLIGHT":
            fare=2100
            price+=fare
        elif t.upper()=="BUS":
            fare=1100
            price+=fare
        elif t.upper()=="TRAIN":
            fare=1500
            price+=fare
        else:
            print("Invalid Option")
        if star=="2":
            hprice= 600
            stay=int(d)*hprice
            fee+=stay
        elif star=="3":
            hprice=1200
            stay=int(d)*hprice
            fee+=stay
        elif star=="4":
            hprice=1500
            stay=int(d)*hprice
            fee+=stay
        else:
            print("Invalid Option")
    elif zx=="PUNJAB":
        a=2000
        price+=a
        if t.upper()=="FLIGHT":
            fare=2050
            price+=fare
        elif t.upper()=="BUS":
            fare=1150
            price+=fare
        elif t.upper()=="TRAIN":
            fare=1500
            price+=fare
        else:
            print("Invalid Option")
        if star=="2":
            hprice= 1000
            stay=int(d)*hprice
            fee+=stay
        elif star=="3":
            hprice=1300
            stay=int(d)*hprice
            fee+=stay
        elif star=="4":
            hprice=1600
            stay=int(d)*hprice
            fee+=stay
        else:
            print("Invalid Option")
    elif zx=="HIMACHAL PRADESH":
        a=2150
        price+=a
        if t.upper()=="FLIGHT":
            fare=2000
            price+=fare
        elif t.upper()=="BUS":
            fare=1100
            price+=fare
        elif t.upper()=="TRAIN":
            fare=1300
            price+=fare
        else:
            print("Invalid Option")
        if star=="2":
            hprice= 700
            stay=int(d)*hprice
            fee+=stay
        elif star=="3":
            hprice=1400
            stay=int(d)*hprice
            fee+=stay
        elif star=="4":
            hprice=1700
            stay=int(d)*hprice
            fee+=stay
        else:
            print("Invalid Option")
    elif zx=="UTTARAKHAND":
        a=2100
        price+=a
        if t.upper()=="FLIGHT":
            fare=2000
            price+=fare
        elif t.upper()=="BUS":
            fare=1000
            price+=fare
        elif t.upper()=="TRAIN":
            fare=1200
            price+=fare
        else:
            print("Invalid Option")
        if star=="2":
            hprice= 800
            stay=int(d)*hprice
            fee+=stay
        elif star=="3":
            hprice=1300
            stay=int(d)*hprice
            fee+=stay
        elif star=="4":
            hprice=1800
            stay=int(d)*hprice
            fee+=stay
        else:
            print("Invalid Option")
    elif zx=="NEW DELHI":
        a=1700
        price+=a
        if t.upper()=="FLIGHT":
            fare=1800
            price+=fare
        elif t.upper()=="BUS":
            fare=700
            price+=fare
        elif t.upper()=="TRAIN":
            fare=1200
            price+=fare
        else:
            print("Invalid Option")
        if star=="2":
            hprice= 900
            stay=int(d)*hprice
            fee+=stay
        elif star=="3":
            hprice=1400
            stay=int(d)*hprice
            fee+=stay
        elif star=="4":
            hprice=1800
            stay=int(d)*hprice
            fee+=stay
        else:
            print("Invalid Option")
    else:
        print("Sorry, we currently don't offer our services in your state")
    tot_price=fee+price
    print(s)
    print(zx)
    return tot_price


        
