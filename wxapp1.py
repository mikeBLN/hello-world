import wx
import wxgui1

class CvFrame(wxgui1.AppFrame):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        wxgui1.AppFrame.__init__(self, parent)
        self.Bind(wx.EVT_MENU, self.onclose, id=105)

    # neues File öffnen und in neuem Tab anzeigen
    def opencv(self, event):
        pass

    # Tab schließen
    def closecv(self, event):
        pass

    def onclose(self, event):
        self.Close(True)



        # what to when 'Solve' is clicked
    # wx calls this function with and 'event' object
    def solveFunc(self, event):
        try:
            # evaluate the string in 'text' and put the answer back
            ans = eval(self.text.GetValue())
            self.text.SetValue(str(ans))
        except Exception:
            print
            'error'

    # put a blank string in text when 'Clear' is clicked
    def clearFunc(self, event):
        self.text.SetValue(str(''))

        # mandatory in wx, create an app, False stands for not deteriction stdin/stdout
        # refer manual for details


app = wx.App(False)
frame = CvFrame(None)
frame.Show(True)
app.MainLoop()