# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyPanelReport
###########################################################################

class MyPanelReport ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
        
        bSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_listCtrlReport = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer.Add( self.m_listCtrlReport, 1, wx.ALL|wx.EXPAND, 5 )
        
        self.m_listCtrlReport.InsertColumn(0, 'Illness', width = 250)
        self.m_listCtrlReport.InsertColumn(1, 'Possibilities', wx.LIST_FORMAT_RIGHT, 100)

        self.SetSizer( bSizer )
        self.Layout()
    
    def __del__( self ):
        pass
    

