# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug  8 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

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
		
		self.Static_FileSelected = wx.StaticText( self, wx.ID_ANY, u"Oczekiwanie...", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.ST_NO_AUTORESIZE )
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
		
		self.Static_FileChanged_Status = wx.StaticText( self, wx.ID_ANY, u"Oczekiwanie...", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.ST_NO_AUTORESIZE )
		self.Static_FileChanged_Status.Wrap( -1 )
		
		bSizer6.Add( self.Static_FileChanged_Status, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.Static_FileChanged_Name = wx.StaticText( self, wx.ID_ANY, u"Oczekiwanie...", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL|wx.ST_NO_AUTORESIZE )
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
	
	
	# Virtual event handlers, overide them in your derived class
	def FileChangeEvent( self, event ):
		event.Skip()
	
	def MagicButtonEvent( self, event ):
		event.Skip()
	

