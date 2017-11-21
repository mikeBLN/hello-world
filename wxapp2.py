#import images
import wx


########################################################################
class TabPanel(wx.Panel):
    """
    This will be the first notebook tab
    """

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """"""

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        sizer = wx.BoxSizer(wx.VERTICAL)
        txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txtOne, 0, wx.ALL, 5)
        sizer.Add(txtTwo, 0, wx.ALL, 5)

        self.SetSizer(sizer)


########################################################################
class NotebookDemo(wx.Notebook):
    """
    Notebook class
    """

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=
        wx.BK_DEFAULT
                             # wx.BK_TOP
                             # wx.BK_BOTTOM
                             # wx.BK_LEFT
                             # wx.BK_RIGHT
                             )

        # Create the first tab and add it to the notebook
        tabOne = TabPanel(self)
        tabOne.SetBackgroundColour("Gray")
        self.AddPage(tabOne, "TabOne")

        # Show how to put an image on one of the notebook tabs,
        # first make the image list:
        il = wx.ImageList(16, 16)
        #idx1 = il.Add(images.Smiles.GetBitmap())
        self.AssignImageList(il)

        # now put an image on the first tab we just created:
        #self.SetPageImage(0, idx1)

        # Create and add the second tab
        tabTwo = TabPanel(self)
        self.AddPage(tabTwo, "TabTwo")

        # Create and add the third tab
        self.AddPage(TabPanel(self), "TabThree")

        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging)

    def OnPageChanged(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        print('OnPageChanged,  old:%d, new:%d, sel:%d\n' % (old, new, sel))

        event.Skip()

    def OnPageChanging(self, event):
        old = event.GetOldSelection()
        new = event.GetSelection()
        sel = self.GetSelection()
        print('OnPageChanging, old:%d, new:%d, sel:%d\n' % (old, new, sel))
        event.Skip()


class AppMenuBar(wx.MenuBar):
    def __init__(self):
        wx.MenuBar.__init__(self, style=0)

        file_menu = wx.Menu()
        file_open = wx.MenuItem(file_menu, wx.ID_ANY, "Open", wx.EmptyString, wx.ITEM_NORMAL)
        file_quit = wx.MenuItem(file_menu, wx.ID_ANY, '&Quit\tCtrl+Q', 'Quit the Application', wx.ITEM_NORMAL)
        file_menu.Append(file_open)
        file_menu.AppendSeparator()
        file_menu.Append(file_quit)
        self.Append(file_menu, "File")


########################################################################
class DemoFrame(wx.Frame):
    """
    Frame that holds all other widgets
    """

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, wx.ID_ANY, "Notebook Tutorial",size=(600, 400))

        self.statusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)

        appmenubar = AppMenuBar()
        self.SetMenuBar(appmenubar)

        panel = wx.Panel(self)

        notebook = NotebookDemo(panel)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(notebook, 1, wx.ALL | wx.EXPAND, 5)
        panel.SetSizer(sizer)
        self.Layout()

        self.Show()


# ----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App()
    frame = DemoFrame()
    app.MainLoop()