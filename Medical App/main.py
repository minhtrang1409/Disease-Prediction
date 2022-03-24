import wx
from GUI.V_Login import *

# def OnExit(event):
#     frame.Close()

# Bring data to app
app = wx.App()
frame = wx.Frame(None, title = u"Medical App", pos = wx.DefaultPosition, size = wx.Size( 640,580 ), style= wx.TAB_TRAVERSAL | wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
frame.SetIcon(wx.Icon("Media/icon.ico"))
_login = MyPanelLogin(frame)

# frame.Bind(wx.EVT_BUTTON, OnExit, _login.m_btnSignIn)

frame.Show(True)
app.MainLoop()