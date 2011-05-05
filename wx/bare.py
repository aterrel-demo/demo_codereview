"""Simple bare example wx app"""

import wx

class App(wx.App):

    def OnInit(self):
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
