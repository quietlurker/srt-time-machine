## srt time machine
## Shifts subtitles files - by seconds and miliseconds

import re               ## re is a module for regex
import datetime         ##datetime is for managing time


#this function changes timestamp
def timeshift(line_to_shift):

        #split creates a list that can be referenced by list[index] starting from pos 0
        line_split = line_to_shift.split('-->',)

        #date_split[0] - first position on the list.
        #.replace(' ','') - removes spaces
        time_beg = line_split[0].replace(' ','')
        time_end = line_split[1].replace(' ','')
        time_end = time_end.replace('\n','') #without this datetime freaks out because there's an \r\n at the end of the line and it thinks it's another parameter to parse

        #time format:
        #%H means an hour in 24h format (00 to 23)
        #%I means an hour ub 12h format (01 to 12)
        time_beg_formatted = datetime.datetime.strptime(time_beg, '%H:%M:%S,%f')
        time_end_formatted = datetime.datetime.strptime(time_end, '%H:%M:%S,%f')


        #shift both timestamps
        time_beg_shifted = time_beg_formatted + datetime.timedelta(seconds=seconds_to_shift)
        time_end_shifted = time_end_formatted + datetime.timedelta(seconds=seconds_to_shift)

        #back to string
        time_beg_shifted_string = datetime.datetime.strftime(time_beg_shifted, '%H:%M:%S,%f')
        time_end_shifted_string = datetime.datetime.strftime(time_end_shifted, '%H:%M:%S,%f')
        
        #format back the entire line
        shifted_line = time_beg_shifted_string[:-3]+ ' --> '+ time_end_shifted_string[:-3] +'\n'
        
        return  str(shifted_line)


#this is a function to find line with timestamp
def search_and_replace(line_original):

        line_to_write = line_original

        #search for lines matching mask using re (regex)
        timestamp_check = re.match('^\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d$', line_to_write)

        if timestamp_check:
                line_to_write = timeshift(line_to_write)

        file_new.write(line_to_write)


## read a file
## ask for file name:
file_original_name = input('ENTER FILE TO SHIFT: ')

# open a file to read
file_original = open(file_original_name, 'r')

#create new file (w: open for write, create if doesn't exist)
file_new_name = 'shifted_' + file_original_name
file_new = open(file_new_name, 'w')

seconds_to_shift = float(input('ENTER FILE TO SHIFT (seconds.microseconds format): '))

#read the content line by line and change each line
for line in file_original:
	#change_line(line.rstrip('\n')) #TEST: line.rstrip('\n') - removes end of line
        search_and_replace(line) 

#close the file
file_original.close()

#close new file
file_new.close()
