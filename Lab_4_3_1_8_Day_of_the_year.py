<<<<<<< HEAD
import math
import datetime

def is_year_leap(year):

	leapYear = False
	
	if(year % 400 == 0) and (year % 100 == 0):
	    leapYear = True 
	       
	elif(year % 4 == 0) and (year % 100 != 0):
	    leapYear = True
	    
	
	return leapYear

def days_in_month(year, month):
    
    monthsNumberDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    isLeapYear = is_year_leap(year)
    if (not(isLeapYear)):
        return monthsNumberDays[month-1]
        
    elif month != 2:
        return monthsNumberDays[month-1]
    
    else:
        return 29

def day_of_year(year, month, day):
    
    if (isinstance(year, int)) and (isinstance(month, int)) and (isinstance(day, int)):
    
        #needed by formula, january and feb are treated as they were in the previous year given
        if(month == 1): month = 11; year-=1
        if(month == 2): month = 12; year-=1
        if(month != 1) and (month != 2): month -=2 
        
        date = datetime.datetime(year,month,day)#date object
        c = int (date.strftime("%C"))#Century
        y = int(date.strftime("%y") )#year without century
        
        weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        m = ["January","February","March","April","May","June","July","August","September","Octuber","November","December"]
        
        w = ((day + math.floor( (2.6 * month) - 0.2) - (2 * c) + y + math.floor(c / 4) + math.floor(c / 4)) % 7)
        print(str(w))
        return weekday[w]
        
    else:
	    print("No son enteros, Ingrese fecha correcta")
	
print(day_of_year(2022, 4, 28))
=======
import math
import datetime

def is_year_leap(year):

	leapYear = False
	
	if(year % 400 == 0) and (year % 100 == 0):
	    leapYear = True 
	       
	elif(year % 4 == 0) and (year % 100 != 0):
	    leapYear = True
	    
	
	return leapYear

def days_in_month(year, month):
    
    monthsNumberDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    isLeapYear = is_year_leap(year)
    if (not(isLeapYear)):
        return monthsNumberDays[month-1]
        
    elif month != 2:
        return monthsNumberDays[month-1]
    
    else:
        return 29

def day_of_year(year, month, day):
    
    if (isinstance(year, int)) and (isinstance(month, int)) and (isinstance(day, int)):
    
        #needed by formula, january and feb are treated as they were in the previous year given
        if(month == 1): month = 11; year-=1
        if(month == 2): month = 12; year-=1
        if(month != 1) and (month != 2): month -=2 
        
        date = datetime.datetime(year,month,day)#date object
        c = int (date.strftime("%C"))#Century
        y = int(date.strftime("%y") )#year without century
        
        weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        m = ["January","February","March","April","May","June","July","August","September","Octuber","November","December"]
        
        w = ((day + math.floor( (2.6 * month) - 0.2) - (2 * c) + y + math.floor(c / 4) + math.floor(c / 4)) % 7)
        print(str(w))
        return weekday[w]
        
    else:
	    print("No son enteros, Ingrese fecha correcta")
	
print(day_of_year(2022, 4, 28))
>>>>>>> dfd5fcc97c4e4339a5e4684ceb9fc1247b7c2ddc
