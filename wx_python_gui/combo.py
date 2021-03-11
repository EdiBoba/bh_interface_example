import wx

app = wx.App()
window = wx.Frame(None, title="Button", size=(300, 200))
panel = wx.Panel(window)
m_comboBoxChoices = ['one', 'two', 'three']
button = wx.ComboBox(panel, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBoxChoices, 0)
window.Show(True)
app.MainLoop()
