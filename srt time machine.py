## srt time machine
## Shifts subtitles files - by seconds and miliseconds

import re               ## re is a module for regex
import datetime         ##datetime is for managing time


#this function changes timestamp
def timeshift(line_to_shift):

        #line example
        #00:00:02,785 --> 00:00:04,700

        #convert string to time
        #https://stackoverflow.com/questions/466345/converting-string-into-datetime
        #copy string to --> and use timedetla(seconds = x)
        #copy string from --> and use timedetla(seconds = x)


        #example
        ##b = a + datetime.timedelta(seconds=3)
        ##
        ##import datetime
        ##a = datetime.datetime(100,1,1,11,34,59)
        ##b = a + datetime.timedelta(0,3) # days, seconds, then other fields.
        ##print a.time()
        ##print b.time()

        shifted_line = line_to_shift + 'This was a timestamp\n'
        return  shifted_line


#this is a function to find line with timestamp
def search_and_replace(line_original):

        #TEST: add a marker to show line was changed
        #line_new = stripped_line + '--Modified\n'

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

#read the content line by line and change each line
for line in file_original:
	#change_line(line.rstrip('\n')) #TEST: line.rstrip('\n') - removes end of line
        search_and_replace(line) 

#close the file
file_original.close()

#close new file
file_new.close()
