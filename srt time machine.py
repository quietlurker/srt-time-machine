## srt time machine
## Shifts subtitles files - by seconds and miliseconds


def change_line(stripped_line):
        #TEST: add a marker to show line was changed
        line_new = stripped_line + "--Modified\n"

        #write writes string to a file
        file_new.write(line_new)


## read a file
## ask for file name:
file_original_name = input('ENTER FILE TO SHIFT: ')

# open a file to read
file_original = open(file_original_name, "r")

#create new file (w: open for write, +: create if doesn't exist)
file_new_name = "Modif_" + file_original_name
file_new = open(file_new_name, "w")

#read the content line by line and change each line
for line in file_original:
	change_line(line.rstrip('\n')) #TEST: line.rstrip('\n') - removes end of line

#close the file
file_original.close()

#close new file
file_new.close()


