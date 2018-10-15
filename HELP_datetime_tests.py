import datetime

#why datetime.datetime?
#there's a datetime module, and inside datetime module is a datetime class
#so - module.class
#we can import class only with from module import class
#and then use the class directly without module datetime.strptime
#but then we don't have access to other stuff from the module (like timedelta)
#we could import another class (from datetime import timedelta)
#and use timedelta (seconds=3) directly
#but instead we will import the whole module and use classes from teh module for better understanding

date_in = '00:00:05,163 --> 00:00:07,311'

seconds_to_shift = float(input('seconds to shift: '))
print (seconds_to_shift )

#find time
#split creates a list that can be referenced by list[index] starting from pos 0
date_split = date_in.split('-->',)
print(date_split)
#date_split[0] - first position on the list.
#.replace(' ','') - removes spaces
time_beg = (date_split[0]).replace(' ','')
time_end = (date_split[1]).replace(' ','')
print(time_beg)
print(time_end)

#time format:
#%H means an hour in 24h format (00 to 23)
#%I means an hour ub 12h format (01 to 12)
time_beg_formatted = datetime.datetime.strptime(time_beg, '%H:%M:%S,%f')
time_end_formatted = datetime.datetime.strptime(time_end, '%H:%M:%S,%f')


print(time_beg_formatted)
print(time_end_formatted)

time_beg_shifted = time_beg_formatted + datetime.timedelta(seconds=seconds_to_shift)
time_end_shifted = time_end_formatted + datetime.timedelta(seconds=seconds_to_shift)
print(time_beg_shifted)
print(time_end_shifted)

#back to string

time_beg_shifted_string = datetime.datetime.strftime(time_beg_shifted, '%H:%M:%S,%f')
time_end_shifted_string = datetime.datetime.strftime(time_end_shifted, '%H:%M:%S,%f')
#[:-3] - this removes 3 last characters from the string
print(time_beg_shifted_string[:-3])
print(time_end_shifted_string[:-3])

