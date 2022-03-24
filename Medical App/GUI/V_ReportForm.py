# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Models.M_DB_Form import DB_Form

###########################################################################
## Class MyPanelFormReport
###########################################################################

class MyPanelFormReport ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,340 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer15 = wx.BoxSizer( wx.VERTICAL )

        fgSizer12 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer12.SetFlexibleDirection( wx.BOTH )
        fgSizer12.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Phone number", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText32.Wrap( -1 )

        fgSizer12.Add( self.m_staticText32, 0, wx.ALL, 5 )

        self.m_txtPhone = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 390,-1 ), wx.TE_READONLY )
        fgSizer12.Add( self.m_txtPhone, 0, wx.ALL, 5 )

        self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText33.Wrap( -1 )

        fgSizer12.Add( self.m_staticText33, 0, wx.ALL, 5 )

        self.m_txtTitle = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        fgSizer12.Add( self.m_txtTitle, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Decription", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText34.Wrap( -1 )

        fgSizer12.Add( self.m_staticText34, 0, wx.ALL, 5 )

        self.m_txtDescription = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), wx.TE_READONLY )
        fgSizer12.Add( self.m_txtDescription, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Report Reason", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText35.Wrap( -1 )

        fgSizer12.Add( self.m_staticText35, 0, wx.ALL, 5 )

        self.m_txtReason = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,100 ), 0 )
        fgSizer12.Add( self.m_txtReason, 0, wx.ALL|wx.EXPAND, 5 )


        bSizer15.Add( fgSizer12, 1, wx.EXPAND, 5 )

        self.m_btnReport = wx.Button( self, wx.ID_ANY, u"Report Violations", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer15.Add( self.m_btnReport, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer15 )
        self.Layout()

        # Connect Events
        self.m_btnReport.Bind( wx.EVT_BUTTON, self.m_onReportClick )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def m_onReportClick( self, event ):
        form_db = DB_Form()
        if self.m_txtReason.GetValue() == "":
            dialog = wx.MessageDialog(None, "Please give a reason for suspending", "Notification", wx.OK)
            dialog.ShowModal()
        else:
            check = DB_Form.ReportRequest(self.ID, self.m_txtReason.GetValue())
            if check == -1:
                dialog = wx.MessageDialog(None, "Report fails", "Notification", wx.OK)
                dialog.ShowModal()
            else:
                dialog = wx.MessageDialog(None, "Report suscessfully", "Notification", wx.OK)
                dialog.ShowModal()