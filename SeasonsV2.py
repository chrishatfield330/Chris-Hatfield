input_month = input()
input_day = int(input())

months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']

if input_month not in months or (input_day < 1 or input_day > 31):
    print ('invalid')
    
elif input_month == 'March':
    if not(1<=input_day<=31):
        print ("Invalid")
    elif input_day<=19:
        print("winter")
    else:
        print ("Spring")
elif input_month == 'April' :
    if not(1<=input_day<=30):
        print("Invalid")
    else:
        print("spring")
elif input_month == 'May':
    if not(1<=input_day<=31):
        print("Invalid")
    else:
        print("spring")
elif input_month == 'June':
    if not(1<=input_day<=30):
        print("Invalid")
    elif input_day<=20:
        print ("spring")
    else:
        print("summer")
elif input_month == 'July':
    if not(1<=input_day<=31):
        print("Invalid")
    else: 
        print("summer")
elif input_month == 'August':
    if not(1<=input_day<=31):
        print("Invalid")
    else: 
        print("summer")
elif input_month == 'September':
    if not(1<=input_day<=30):
        print("Invalid")
    elif input_day<=21:
        print ("summer")
    else:
        print ("autumn")
elif input_month == "October":
    if not(1<=input_day<=31):
        print("Invalid")
    else:
        print("autumn")
elif input_month == "November":
    if not(1<=input_day<=30):
        print("Invalid")
    else:
        print ("autumn")
elif input_month == "December":
    if not(1<=input_day<=31):
        print("Invalid")
    elif input_day <=20:
        print ("autumn")
    else:
        print ("winter")
elif input_month == 'January':
    if not(1<=input_day<=31):
        print("Invalid")
    else:
        print("winter")
elif input_month == "February":
    if not(1<=input_day<=29):
        print("Invalid")
    else:
        print ("winter")
