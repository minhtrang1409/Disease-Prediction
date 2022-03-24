import wx 
import wx.html2 

class MyBrowser(wx.Dialog): 
    def __init__(self, *args, **kwds): 
        wx.Dialog.__init__(self, *args, **kwds) 
        sizer = wx.BoxSizer(wx.VERTICAL) 
        self.browser = wx.html2.WebView.New(self) 
        # wx.html2.WebViewBackendWebKit()
        sizer.Add(self.browser, 1, wx.EXPAND, 10) 
        self.SetSizer(sizer) 
        self.SetSize((520, 520)) 

        self.browser.Bind( wx.html2.EVT_WEBVIEW_ERROR, self.Error )

    def Error (self, event):
        print("error")

# if __name__ == '__main__': 
#     app = wx.App() 
#     dialog = MyBrowser(None, -1) 
#     dialog.browser.MSWSetEmulationLevel(level=11)
#     dialog.browser.LoadURL("https://realtime-chat-system.herokuapp.com/?uname=") 
#     dialog.Show() 
#     app.MainLoop()   