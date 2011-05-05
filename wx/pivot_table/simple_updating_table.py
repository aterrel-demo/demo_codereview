import wx

class AbstractModel(object):
    def __init__(self):
        self.listeners = []

    def addListener(self, listener_fun):
        self.listeners.append(listener_fun)

    def removeListener(self, listner_fun):
        self.listeners.remove(listner_fun)

    def update(self):
        for fun in self.listeners:
            fun(self)

class SimpleTable(AbstractModel):

    def __init__(self, data_engine):
        AbstractModel.__init__(self)
        self.set(data_engine)

    def set(self, data_engine):
        self.data_engine = data_engine
        self.update()

class SimpleName(AbstractModel):

    def __init__(self, first='', last=''):
        AbstractModel.__init__(self)
        self.set(first, last)

    def set(self, first, last):
        self.first = first
        self.last = last
        self.update()

class SimpleFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Simple Updating Table',
                          size = (340, 200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.textFields = {}
        self.createTextFields(panel)
        self.model = SimpleName()
        self.model.addListener(self.OnUpdate)
        self.createButtonBar(panel)

    def buttonData(self):
        return (("Fredify", self.OnFred),
                ("Wilmafy", self.OnWilma))

    def createButtonBar(self, panel, yPos=0):
        xPos = 0
        for label, handler in self.buttonData():
            pos = (xPos, yPos)
            button = self.buildOneButton(panel, label, handler, pos)
            xPos += button.GetSize().width

    def buildOneButton(self, parent, label, handler, pos=(0,0)):
        button = wx.Button(parent, -1, label, pos)
        self.Bind(wx.EVT_BUTTON, handler, button)
        return button

    def textFieldData(self):
        return (("First Name", (10, 50)),
                ("Last Name", (10, 80)))

    def createTextFields(self, panel):
        for label, pos in self.textFieldData():
            self.createCaptionedText(panel, label, pos)

    def createCaptionedText(self, panel, label, pos):
        static = wx.StaticText(panel, wx.NewId(), label, pos)
        static.SetBackgroundColour("White")
        textPos = (pos[0] + 75, pos[1])
        self.textFields[label] = wx.TextCtrl(panel, wx.NewId(), "",
                                             size=(100, -1), pos=textPos,
                                             style=wx.TE_READONLY)

    def OnUpdate(self, model):
        self.textFields["First Name"].SetValue(model.first)
        self.textFields["Last Name"].SetValue(model.last)

    def OnFred(self, event):
        self.model.set("Fred", "Flintstone")

    def OnWilma(self, event):
        self.model.set("Wilma", "Flintstone")

    def OnCloseWindow(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = SimpleFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()


