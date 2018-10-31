# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
import re               ## re is a module for regex
import datetime         ##datetime is for managing time


seconds_to_shift = 0.0
original_file = ''

###########################################################################
## Class MainFrame
###########################################################################


class MainFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"strTimeMachine 1.0", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        fgSizer2 = wx.FlexGridSizer( 1, 0, 0, 0 )
        fgSizer2.SetFlexibleDirection( wx.BOTH )
        fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.Static_SelectFile = wx.StaticText( self, wx.ID_ANY, u"Wybierz plik z napisami do przesunięcia", wx.Point( -1,-1 ), wx.Size( 290,-1 ), 0 )
        self.Static_SelectFile.Wrap( -1 )
        
        self.Static_SelectFile.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        
        fgSizer2.Add( self.Static_SelectFile, 0, wx.ALL, 5 )
        
        self.SelectFile = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.srt", wx.DefaultPosition, wx.Size( 170,-1 ), wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_SMALL )
        fgSizer2.Add( self.SelectFile, 0, wx.ALL, 5 )
        
        
        bSizer2.Add( fgSizer2, 0, 0, 5 )
        
        self.Static_FileSelected = wx.StaticText( self, wx.ID_ANY, u"Oczekiwanie...", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL |wx.ST_NO_AUTORESIZE)
        self.Static_FileSelected.Wrap( -1 )
        
        bSizer2.Add( self.Static_FileSelected, 0, wx.ALL|wx.EXPAND, 5 )
        
        fgSizer3 = wx.FlexGridSizer( 1, 9, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.Static_EnterSeconds = wx.StaticText( self, wx.ID_ANY, u"O ile sekund przesunąć napisy?", wx.DefaultPosition, wx.Size( 290,-1 ), wx.ALIGN_RIGHT )
        self.Static_EnterSeconds.Wrap( -1 )
        
        self.Static_EnterSeconds.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
        
        fgSizer3.Add( self.Static_EnterSeconds, 1, wx.ALL, 5 )
        
        self.InputSeconds = wx.TextCtrl( self, wx.ID_ANY, u"0.0", wx.DefaultPosition, wx.Size( 170,-1 ), wx.TE_CENTRE )
        fgSizer3.Add( self.InputSeconds, 0, wx.ALL, 5 )
        
        bSizer2.Add( fgSizer3, 0, 0, 5 )
        
        bSizer5 = wx.BoxSizer( wx.VERTICAL )
        
        self.Static_Explanation11 = wx.StaticText( self, wx.ID_ANY, u"Jeśli chcesz przesunąć napisy o 3 sekundy do przodu wpisz: 3", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        self.Static_Explanation11.Wrap( -1 )
        
        bSizer5.Add( self.Static_Explanation11, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.Static_Explanation1 = wx.StaticText( self, wx.ID_ANY, u"Jeśli chcesz przesunąć napisy o 2.5 sekundy do tyłu wpisz: -2.5", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
        self.Static_Explanation1.Wrap( -1 )
        
        bSizer5.Add( self.Static_Explanation1, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.MagicButton = wx.Button( self, wx.ID_ANY, u"Czas na Wibbly Wobbly Timey Wimey stuff!", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
        bSizer5.Add( self.MagicButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )
        
        bSizer6 = wx.BoxSizer( wx.VERTICAL )
        
        self.Static_FileChanged_Status = wx.StaticText( self, wx.ID_ANY, u"Oczekiwanie...", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL |wx.ST_NO_AUTORESIZE )
        self.Static_FileChanged_Status.Wrap( -1 )
        
        bSizer6.Add( self.Static_FileChanged_Status, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.Static_FileChanged_Name = wx.StaticText( self, wx.ID_ANY, u"Oczekiwanie...", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL |wx.ST_NO_AUTORESIZE )
        self.Static_FileChanged_Name.Wrap( -1 )
        
        bSizer6.Add( self.Static_FileChanged_Name, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer2 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.SelectFile.Bind( wx.EVT_FILEPICKER_CHANGED, self.FileChangeEvent )
        self.MagicButton.Bind( wx.EVT_BUTTON, self.MagicButtonEvent )
    
    def __del__( self ):
        pass
    
    def FileChangeEvent( self, event ):
        global original_file
        
        original_file = self.SelectFile.GetPath()        
        self.Static_FileSelected.SetLabel('Wybrany plik to ' + original_file)
        
    # Virtual event handlers, overide them in your derived class
    def MagicButtonEvent( self, event ):
        global seconds_to_shift
        global original_file
        
        #clean the display
        self.Static_FileChanged_Status.SetLabel('Working...!')
        self.Static_FileChanged_Name.SetLabel('')
        
        filename = os.path.split(original_file)[1]
        
        self.Static_FileSelected.SetLabel('Wybrany plik to ' + original_file)
        
        filename_new = 'zmieniony_' +filename

        #this adds _changed to filename and creates the full path with changed name
        full_newfile = os.path.join(os.path.split(original_file)[0],filename_new)

        # open a file to read
        file_original = open(original_file, 'r')

        #create new file (w: open for write, create if doesn't exist)
        file_new = open(full_newfile, 'w')

        seconds_to_shift = float(self.InputSeconds.GetLineText(0))

        #read the content line by line and change each line
        for line in file_original:
            #search_and_replace(line)
            file_new.write(search_and_replace(line))

        #close the file
        file_original.close()

        #close new file
        file_new.close()
        
        self.Static_FileChanged_Status.SetLabel('SUKCES!')
        self.Static_FileChanged_Name.SetLabel('Twój nowy plik nazywa się ' + filename_new)
        

###########################################################################
## this function changes timestamp
###########################################################################

def timeshift(line_to_shift):
    
        global seconds_to_shift
        
        #split creates a list that can be referenced by list[index] starting from pos 0
        line_split = line_to_shift.split('-->',)

        #date_split[0] - first position on the list.
        #.replace(' ','') - removes spaces
        time_beg = line_split[0]
        time_end = line_split[1]
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
        test = ''

        #format back the entire line
        shifted_line = time_beg_shifted_string[:-3]+ ' --> '+ time_end_shifted_string[:-3] +'\n'

        return  shifted_line

###########################################################################
## this is a function to find line with timestamp
###########################################################################

def search_and_replace(line_original):

        line_to_write = line_original
        
        #remove spaces before check, and the remove tab
        line_to_write_no_spaces = line_original.replace(' ', '').replace('\t', '')
        
        #search for lines matching mask using re (regex)
        timestamp_check = re.match('^\d\d:\d\d:\d\d,\d\d\d-->\d\d:\d\d:\d\d,\d\d\d$', line_to_write_no_spaces)

        if timestamp_check:
                line_to_write = timeshift(line_to_write_no_spaces)

        return line_to_write
        ##file_new.write(line_to_write)
        

###########################################################################
## WX display
###########################################################################     
myApp = wx.App()
frame = MainFrame(None)
frame.Show()
myApp.MainLoop()