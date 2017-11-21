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
        vboxTree = wx.BoxSizer(wx.VERTICAL)
        vboxDetails = wx.BoxSizer(wx.VERTICAL)
        self.tlbox = wx.BoxSizer(wx.HORIZONTAL)
        self.valbox = wx.BoxSizer(wx.HORIZONTAL)
        self.panel1 = wx.Panel(self, -1)
        #self.panel2 = wx.Panel(self, -1)

        self.tree = wx.TreeCtrl(self.panel1, 1, wx.DefaultPosition, (-1,-1), wx.TR_HAS_BUTTONS)
        cvRoot = self.tree.AddRoot('CV-Certificate', data=['7F21',20123,'certificate body'])
        cvBody = self.tree.AppendItem(cvRoot, 'Certificate Body', data=['7F21',20123,'certificate body'])
        cvSignature = self.tree.AppendItem(cvRoot, 'Signature')
        self.tree.AppendItem(cvBody, 'Certificate Profile Identifier (v1)')
        self.tree.AppendItem(cvBody, 'CAR (DECVCA001)')
        cvPublicKey = self.tree.AppendItem(cvBody, 'Public Key')
        self.tree.AppendItem( cvBody, 'CHR (DECVCA001)', data=['5F20',9,'DECVCA001'] )
        cvChat = self.tree.AppendItem(cvBody, 'CHAT')
        self.tree.AppendItem( cvBody, 'Effective Date (2017-09-02)', data=['5F25',6,'2017-09-02'])
        self.tree.AppendItem( cvBody, 'Expiration Date (2018-09-01)', data=['5F24',6,'2018-09-01'])
        self.tree.AppendItem(cvPublicKey, 'OID')
        self.tree.AppendItem(cvPublicKey, 'Prime Modulus p')
        self.tree.AppendItem(cvPublicKey, 'First Coeff a')
        self.tree.AppendItem(cvPublicKey, 'Second Coeff b')
        self.tree.AppendItem(cvPublicKey, 'Base Point G')
        self.tree.AppendItem(cvPublicKey, 'Order r')
        self.tree.AppendItem(cvPublicKey, 'Public Point Y')
        self.tree.AppendItem(cvPublicKey, 'Cofactor f')
        self.tree.AppendItem(cvChat, 'OID')
        self.tree.AppendItem(cvChat, 'Roles and Rights')
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED , self.OnSelChange , id=1)
        self.stlabel1 = wx.StaticText(self.tlbox, -1, '',(10,10), style=wx.ALIGN_LEFT)
        self.stvalue1 = wx.StaticText(self.tlbox, -1, '', (30, 10), style=wx.ALIGN_LEFT)

        vboxTree.Add(self.tree, 1, wx.EXPAND)
        vboxDetails.Add(self.tlbox, 1, wx.EXPAND)
        vboxDetails.Add(self.valbox, 1, wx.EXPAND)
        hbox.Add(self.panel1, 1, wx.EXPAND)
        hbox.Add(vboxDetails, 1, wx.EXPAND)
        self.panel1.SetSizer(vboxTree)
        self.SetSizer(hbox)

        self.tree.ExpandAll()

        self.SetTitle('dvviewer 0.1')
        self.SetSize((600, 500))
        self.Centre()
        self.Bind(wx.EVT_MENU, self.OnQuit, id=105)

    def OnSelChange(self, event):
        eItem = event.GetItem()
        eItemData = self.tree.GetItemData(eItem)
        self.stvalue1.SetLabel(str(eItemData))

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
