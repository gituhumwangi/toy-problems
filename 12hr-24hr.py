def time_conversion (hrs, mins, period) :
    if hrs <= 12 and mins <=  59 and period == "am"  :
        hr24 = str(hrs) + str(mins) + "hrs"
        return hr24
    elif hrs <= 12 and mins <= 59 and period == "pm" :
        hrs24 = hrs + 12 
        hr24 =str(hrs24) + str(mins) + "hrs"
        return hr24
    

        
