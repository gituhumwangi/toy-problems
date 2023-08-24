def time_conversion(hrs, mins, period):
    if  hrs <= 9 and mins <=  59 and period == "am"  :
        hr24 =  "0" + str(hrs) + str(mins) + "hrs"
        return hr24
    elif hrs >=10 and mins <=  59 and period == "am"  :
        hr24 =  str(hrs) + str(mins) + "hrs"
        return hr24
    elif hrs <= 12 and mins <= 59 and period == "pm" :
        hrs24 = hrs + 12 
        hr24 =str(hrs24) + str(mins) + "hrs"
        return hr24
    
print(time_conversion(8, 40, "am"))