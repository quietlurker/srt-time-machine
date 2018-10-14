## srt time machine
## Shifts subtitles files - by seconds and miliseconds

## read a file
## ask for file name:
file_original_name = input('ENTER FILE TO SHIFT: ')

# open a file to read
#file_original = open("TEST01.srt", "r")
file_original = open(file_original_name, "r")

#read the content
file_content = file_original.read()

#close the file
file_original.close()

#create new file (w: open for write, +: create if doesn't exist)
file_new_name = "Modif_" + file_original_name
file_new = open(file_new_name, "w+")

#copy content of original file to new file
file_new.write(file_content)

#close new file
file_new.close()





