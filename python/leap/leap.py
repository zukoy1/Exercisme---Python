def is_leap_year(year):
    if year % 4 == 0:
    	value = True
    	if year % 100 == 0:
    		value = False
    		if year % 400 == 0:
    			value = True
    			return value
    		return value
    	else:
    		value = True
    		return value
    else:
    	value = False
    	return value

