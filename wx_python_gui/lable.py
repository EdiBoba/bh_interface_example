import wx

app = wx.App()
window = wx.Frame(None, title="Button", size=(300, 200))
panel = wx.Panel(window)
lable = wx.StaticText(panel, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
window.Show(True)
app.MainLoop()


