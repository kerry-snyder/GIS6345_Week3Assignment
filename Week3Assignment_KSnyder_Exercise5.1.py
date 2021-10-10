#My code to produce the current time using floor division and modulus 
#import the time module and determine seconds since the epoch
import time
GMT = time.time()
print(GMT)

#Use the total seconds to calcuate the current GMT 
rawseconds = GMT %(24*60*60)
rawminutes = (rawseconds // 60)
hours = rawminutes // 60
totalseconds = rawseconds % 60
seconds = totalseconds // 1
minutes = rawminutes % 60

#Adjustment to eastern time
def eastern_time(hours):
    if hours >= 4:
        return hours - 4
    elif hours == 1:
        return 21
    elif hours == 2:
        return 22
    elif hours == 3:
        return 23
    else: 
        return abs(hours - 20)

print ('The current time (ET) is', eastern_time(hours) , 'hours', minutes, 'minutes', seconds, 'seconds')

#Calculation of whole days since the epoch
wholedays = GMT//(24*60*60)

print('We are currently', wholedays, 'days past the epoch')

#The time.ctime()function returns the current time
print("It is currently", time.ctime())
