
day = int(input("Input birthday: "))
month = int(input("Input month of birth:"))
name = input("Input name of the month:")

if (month == 3 and day >= 21 and name=='March') or (month == 4 and day <= 19 and name == 'April'):
    sign = "Aries (Ram)"
elif (month == 4 and day >= 20 and name== 'April') or (month == 5 and day <= 20 and name== 'May'):
    sign = "Taurus (Bull)"
elif (month == 5 and day >= 21 and name== 'May') or (month == 6 and day <= 21 and name =='June'):
    sign = "Gemini (Twins)"
elif (month == 6 and day >= 22 and name =='June' ) or (month == 7 and day <= 22 and name =='July'):
    sign = "Cancer (Crab)"
elif (month == 7 and day >= 23 and name =='July') or (month == 8 and day <= 22 and name =='August'):
    sign = "Leo (Lion)"
elif (month == 8 and day >= 23 and name =='August') or (month == 9 and day <= 22 and name =='September'):
    sign = "Virgo (Virgin)"
elif (month == 9 and day >= 23 and name =='September') or (month == 10 and day <= 23 and name =='October'):
    sign = "Libra (Balance)"
elif (month == 10 and day >= 24 and name =='October') or (month == 11 and day <= 21 and name =='November'):
    sign = "Scorpius (Scorpion)"
elif (month == 11 and day >= 22 and name =='November') or (month == 12 and day <= 21 and name =='December'):
    sign = "Sagittarius (Archer)"
elif (month == 12 and day >= 22 and name =='December') or (month == 1 and day <= 19 and name =='January'):
    sign = "Capricornus (Goat)"
elif (month == 1 and day >= 20 and name =='January') or (month == 2 and day <= 18)and name =='February':
    sign = "Aquarius (Water Bearer)"
elif (month == 2 and day >= 19 and name =='February') or (month == 3 and day <= 20 and name =='March'):
    sign = "Pisces (Fish)"
else:
    sign = ("Invalid date or month or name entered.")

print("Your Astrological sign is:", sign)
