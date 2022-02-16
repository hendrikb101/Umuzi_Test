def time_converter(num):
    hour = num // 60
    if hour == 0 or 1 :
        hour_string = "hour"
    else:
        hour_string = "hours"
    
    minutes = num - (hour * 60)
    if minutes == 0 or 1:
        minute_string = "minute"
    else:
        minute_string = "minutes"
        
    print(f"{hour} {hour_string}, {minutes} {minute_string}")

time_converter(0)
