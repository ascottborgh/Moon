month= int(input("What numerical month are you in? "))
day= int(input("What numerical day are you in? "))
ends_in_31 = [1,3,5,7,8,10,12]
ends_in_30 = [4,6,9,11]
february = 2

def moon_31(day):
    if day <= 3:
        print ("There is a New Moon that day")
    elif day > 3 and day < 7:
        print ("Waning Crescent")
    elif day >= 7 and day <= 11:
        print("Third Qtr")
    elif day > 11 and day <=15:
        print("Full Moon, Beware The Werewolves Are Out!!!")
    elif day > 15 and day <= 18:
        print("Waxing Gibbons")
    elif day > 18 and day <= 22:
        print("First Quarter")
    elif day > 22 and day <= 25:
        print("Waxing Crescent")
    else :
        print("New Moon")

def moon_30(day):
    if day <= 2:
        print("New Moon")
    elif day > 2 and day < 6:
        print("Waning Crescent ")
    elif day >= 6 and day <=10:
        print("Third Qtr")
    elif day > 10 and day <= 14:
        print("Full Moon, Beware The Werewolves Are Out!!!")
    elif day > 14 and day <= 17:
        print("Waxing Gibbons")
    elif day > 17 and day <= 21:
        print("First Quarter")
    elif day > 21 and day <= 24:
        print("Waxing Crescent")

def moon_feb(day):
    if  day > 3 and day < 7:
        print("Waning Crescent")
    elif day >= 7 and day <=9:
        print("Third Qtr")
    elif day > 9 and day <= 13:
        print("Full Moon, Beware The Werewolves Are Out!!!")
    elif day > 13 and day <= 16:
        print("Waxing Gibbons")
    elif day > 16 and day <= 20:
        print("First Quarter")
    elif day > 20 and day <= 23:
        print("Waxing Crescent")
        
if day == ends_in_31:
    moon_31(day)
elif day == ends_in_30:
    moon_30(day)
else:
    moon_feb(day)
    