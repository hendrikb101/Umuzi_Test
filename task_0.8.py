num = int(input('Enter any number: '))
def time_converter_hour(num):
    hour = num // 60
    return hour
hour = time_converter_hour(num)
if hour == 1 :
    hour_string = "Hour"
else:
    hour_string = "Hours"
    
def time_converter_min(num):
    minutes = num - (hour * 60)
    return minutes
minutes = time_converter_min(num)
if minutes == 1:
        minute_string = "Minute"
else:
        minute_string = "Minutes"
        
print("The number " + str(num),"is equal to " + str(hour) + " " + str(hour_string) + " and " + str(minutes) + " " + str(minute_string))
