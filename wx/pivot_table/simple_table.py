import wx
import wx.grid

from pivot_data_engine.numpy_engine import NumpyPivotDataEngine
from pivot_data_engine.utils import generate_data

class SimpleTable(wx.grid.PyGridTableBase):

    def __init__(self, data_engine):
        wx.grid.PyGridTableBase.__init__(self)
        self.data_engine = data_engine

    def GetNumberRows(self):
        return len(self.data_engine.getFullTable())

    def GetNumberCols(self):
        return len(self.data_engine.schema.cols)

    def GetColLabelValue(self, col):
        return self.data_engine.schema.cols.keys()[col]

    # def GetRowLabelValue(self, row):
    #     pass

    def IsEmptyCell(self, row, col):
        return False

    def GetValue(self, row, col):
        col_name = self.GetColLabelValue(col)
        return self.data_engine.getFullTable(columns=[col_name])[row][0]

    def SetValue(self, row, col, value):
        pass

class SimpleGrid(wx.grid.Grid):
    def __init__(self, parent, data_engine):
        wx.grid.Grid.__init__(self, parent, -1)
        self.SetTable(SimpleTable(data_engine))

class TestFrame(wx.Frame):
    def __init__(self, parent, data_engine):
        wx.Frame.__init__(self, parent, -1, "Sample Grid",
                          size = (275, 275))
        grid = SimpleGrid(self, data_engine)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    data_engine = NumpyPivotDataEngine(generate_data(100))
    frame = TestFrame(None, data_engine)
    frame.Show(True)
    app.MainLoop()

