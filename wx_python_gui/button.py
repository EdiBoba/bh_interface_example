import wx

app = wx.App()
window = wx.Frame(None, title="Button", size=(300, 200))
panel = wx.Panel(window)
button = wx.Button(panel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
window.Show(True)
app.MainLoop()
