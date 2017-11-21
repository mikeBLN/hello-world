# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Dec 21 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


class AppNotebook(wx.Notebook):
    pass


class AppMenuBar(wx.MenuBar):

    def __init__(self):
        wx.MenuBar.__init__(self,style=0)

        self.file_menu = wx.Menu()
        self.file_open = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
        self.file_menu.Append( self.file_open )
        self.file_menu.AppendSeparator()
        self.file_quit = wx.MenuItem( self.file_menu, wx.ID_ANY, u"Quit", wx.EmptyString, wx.ITEM_NORMAL )
        self.file_menu.Append( self.file_quit)
        self.Append( self.file_menu, u"File" )



class AppFrame ( wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size( 542,374 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        #self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.menubar = AppMenuBar()
        self.SetMenuBar(self.menubar)

        app_panel = wx.Panel(self)
        app_notebook = AppNotebook(app_panel)

        nb_sizer = wx.BoxSizer(wx.HORIZONTAL)
        nb_sizer.Add(app_notebook, 1, wx.EXPAND |wx.ALL, 5)
        app_panel.SetSizer(nb_sizer)

        self.Layout()
        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


