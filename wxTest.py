#!/usr/bin/python

# menu2.py

import wx

class MyMenu(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(380, 250))

        # menu bar
        menubar = wx.MenuBar()
        file = wx.Menu()
        edit = wx.Menu()
        help = wx.Menu()
        file.Append(101, '&Open', 'Open a new document')
        file.Append(102, '&Save', 'Save the document')
        file.AppendSeparator()
        quit = wx.MenuItem(file, 105, '&Quit\tCtrl+Q', 'Quit the Application')
        #quit.SetBitmap(wx.Image('stock_exit-16.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        file.Append(quit)
        edit.Append(201, 'check item1', '', wx.ITEM_CHECK)
        edit.Append(202, 'check item2', kind=wx.ITEM_CHECK)
        submenu = wx.Menu()
        submenu.Append(301, 'radio item1', kind=wx.ITEM_RADIO)
        submenu.Append(302, 'radio item2', kind=wx.ITEM_RADIO)
        submenu.Append(303, 'radio item3', kind=wx.ITEM_RADIO)
        edit.Append(203, 'submenu', submenu)
        menubar.Append(file, '&File')
        menubar.Append(edit, '&Edit')
        menubar.Append(help, '&Help')
        self.SetMenuBar(menubar)

        #status bar
        self.statusbar = self.CreateStatusBar()

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        panel1 = wx.Panel(self, -1)
        panel2 = wx.Panel(self, -1)

        self.tree = wx.TreeCtrl(panel1, 1, wx.DefaultPosition, (-1,-1), wx.TR_HIDE_ROOT|wx.TR_HAS_BUTTONS)
        root = self.tree.AddRoot('Programmer')
        os = self.tree.AppendItem(root, 'Operating Systems')
        pl = self.tree.AppendItem(root, 'Programming Languages')
        tk = self.tree.AppendItem(root, 'Toolkits')
        self.tree.AppendItem(os, 'Linux')
        self.tree.AppendItem(os, 'FreeBSD')
        self.tree.AppendItem(os, 'OpenBSD')
        self.tree.AppendItem(os, 'NetBSD')
        self.tree.AppendItem(os, 'Solaris')
        cl = self.tree.AppendItem(pl, 'Compiled languages')
        sl = self.tree.AppendItem(pl, 'Scripting languages')
        self.tree.AppendItem(cl, 'Java')
        self.tree.AppendItem(cl, 'C++')
        self.tree.AppendItem(cl, 'C')
        self.tree.AppendItem(cl, 'Pascal')
        self.tree.AppendItem(sl, 'Python')
        self.tree.AppendItem(sl, 'Ruby')
        self.tree.AppendItem(sl, 'Tcl')
        self.tree.AppendItem(sl, 'PHP')
        self.tree.AppendItem(tk, 'Qt')
        self.tree.AppendItem(tk, 'MFC')
        self.tree.AppendItem(tk, 'wxPython')
        self.tree.AppendItem(tk, 'GTK+')
        self.tree.AppendItem(tk, 'Swing')
        #self.tree.Bind(wx.EVT_TREEBOOK_PAGE_CHANGED , self.On , id=1)
        self.display = wx.StaticText(panel2, -1, '',(10,10), style=wx.ALIGN_CENTRE)
        vbox.Add(self.tree, 1, wx.EXPAND)
        hbox.Add(panel1, 1, wx.EXPAND)
        hbox.Add(panel2, 1, wx.EXPAND)
        panel1.SetSizer(vbox)
        self.SetSizer(hbox)





        self.Centre()
        self.Bind(wx.EVT_MENU, self.OnQuit, id=105)

    def OnOpen(self, event):
        self.statusbar.SetStatusText('Open Command')

    def OnSave(self, event):
        self.statusbar.SetStatusText('Save Command')

    def OnQuit(self, event):
        self.Close()

class MyApp(wx.App):
    def OnInit(self):
        frame = MyMenu(None, -1, 'wxTest.py')
        frame.Show(True)
        return True

app = MyApp(0)
app.MainLoop()
