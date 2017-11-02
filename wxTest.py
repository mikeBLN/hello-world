#!/usr/bin/python

# menu2.py

import wx


class TheFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(TheFrame, self).__init__(*args, **kw)
        self.InitUI()

    def InitBars(self):

        # menu bar
        menubar = wx.MenuBar()
        file = wx.Menu()
        edit = wx.Menu()
        help = wx.Menu()

        file.Append(101, '&Open', 'Open a CV certificate')
        #file.Append(102, '&Save', 'Save the document')
        file.AppendSeparator()
        quit = wx.MenuItem(file, 105, '&Quit\tCtrl+Q', 'Quit the Application')
        #quit.SetBitmap(wx.Image('stock_exit-16.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        file.Append(quit)

        edit.Append(201, 'expand all', '', wx.ITEM_CHECK)
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

    def InitUI(self):

        self.InitBars()

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.panel1 = wx.Panel(self, -1)
        self.panel2 = wx.Panel(self, -1)

        self.tree = wx.TreeCtrl(self.panel1, 1, wx.DefaultPosition, (-1,-1), wx.TR_HAS_BUTTONS)
        root = self.tree.AddRoot('CV-Certificate')
        body = self.tree.AppendItem(root, 'Certificate Body')
        signature = self.tree.AppendItem(root, 'Signature')
        self.tree.AppendItem(body, 'Certificate Profile Identifier (v1)')
        self.tree.AppendItem(body, 'CAR (DECVCA001)')
        pk = self.tree.AppendItem(body, 'Public Key')
        self.tree.AppendItem( body, 'CHR (DECVCA001)', data=['5F20',9,'DECVCA001'] )
        ch = self.tree.AppendItem(body, 'CHAT')
        self.tree.AppendItem( body, 'Effective Date (2017-09-02)', data=['5F25',6,'2017-09-02'])
        self.tree.AppendItem( body, 'Expiration Date (2018-09-01)', data=['5F24',6,'2018-09-01'])
        self.tree.AppendItem(pk, 'OID')
        self.tree.AppendItem(pk, 'Prime Modulus p')
        self.tree.AppendItem(pk, 'First Coeff a')
        self.tree.AppendItem(pk, 'Second Coeff b')
        self.tree.AppendItem(pk, 'Base Point G')
        self.tree.AppendItem(pk, 'Order r')
        self.tree.AppendItem(pk, 'Public Point Y')
        self.tree.AppendItem(pk, 'Cofactor f')
        self.tree.AppendItem(ch, 'OID')
        self.tree.AppendItem(ch, 'Roles and Rights')
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED , self.OnSelChange , id=1)
        self.display = wx.StaticText(self.panel2, -1, 'test',(10,10), style=wx.ALIGN_CENTRE)
        vbox.Add(self.tree, 1, wx.EXPAND)
        hbox.Add(self.panel1, 1, wx.EXPAND)
        hbox.Add(self.panel2, 1, wx.EXPAND)
        self.panel1.SetSizer(vbox)
        self.SetSizer(hbox)

        self.tree.ExpandAll()

        self.SetTitle('dvviewer 0.1')
        self.SetSize((600, 500))
        self.Centre()
        self.Bind(wx.EVT_MENU, self.OnQuit, id=105)

    def OnSelChange(self, event):
        self.display = wx.StaticText(self.panel2, -1, str(1),(10,10), style=wx.ALIGN_CENTRE)

    def OnOpen(self, event):
        self.statusbar.SetStatusText('Open a file')

    def OnSave(self, event):
        self.statusbar.SetStatusText('Save Command')

    def OnQuit(self, event):
        self.Close()


class MyApp(wx.App):
    def OnInit(self):
        frame = TheFrame(None)
        frame.Show(True)
        return True


app = MyApp(0)
app.MainLoop()
