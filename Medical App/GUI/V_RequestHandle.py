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
from GUI.V_ReportForm import MyPanelFormReport

###########################################################################
## Class MyPanelRequestAccept
###########################################################################

class MyPanelRequestAccept ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.ID = ""

        bSizer14 = wx.BoxSizer( wx.VERTICAL )

        self.m_listRequest = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        self.m_listRequest.InsertColumn(0, 'ID', width = 25)
        self.m_listRequest.InsertColumn(1, 'Phone number', width = 100)
        self.m_listRequest.InsertColumn(2, 'Title', wx.LIST_FORMAT_LEFT, 100)
        self.m_listRequest.InsertColumn(3, 'Description', wx.LIST_FORMAT_RIGHT, 250)
        self.m_listRequest.InsertColumn(4, 'Status', wx.LIST_FORMAT_RIGHT, 100)

        bSizer14.Add( self.m_listRequest, 1, wx.ALL|wx.EXPAND, 5 )

        fgSizer11 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer11.SetFlexibleDirection( wx.BOTH )
        fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_btnComplete = wx.Button( self, wx.ID_ANY, u"Complete", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer11.Add( self.m_btnComplete, 0, wx.ALL, 5 )

        self.m_buttonReportViolations = wx.Button( self, wx.ID_ANY, u"Report Violations", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer11.Add( self.m_buttonReportViolations, 0, wx.ALL, 5 )


        bSizer14.Add( fgSizer11, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer14 )
        self.Layout()

        # Connect Events
        self.m_listRequest.Bind( wx.EVT_LIST_ITEM_SELECTED, self.m_onItemSelected )
        self.m_btnComplete.Bind( wx.EVT_BUTTON, self.m_onCompleteClick )
        self.m_buttonReportViolations.Bind( wx.EVT_BUTTON, self.m_onReportClick )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def m_onItemSelected( self, event ):
        self.ID = self.m_listRequest.GetItem(self.m_listRequest.GetFirstSelected(), 0)
        self.ID = self.ID.GetText()
        self.status = self.m_listRequest.GetItem(self.m_listRequest.GetFirstSelected(), 4)
        self.status = self.status.GetText()
            
    def m_onCompleteClick( self, event ):
        if self.ID == "":
            dialog = wx.MessageDialog(None, "Please select a request", "Notification", wx.OK)
            dialog.ShowModal()
        else:
            form_db = DB_Form()
            if self.status == "Completed":
                dialog = wx.MessageDialog(None, "Request already completed", "Notification", wx.OK)
                dialog.ShowModal()
            else:
                check = form_db.CompleteRequest(self.ID)
                if check == -1:
                    dialog = wx.MessageDialog(None, "Update fails", "Notification", wx.OK)
                    dialog.ShowModal()
                else:
                    dialog = wx.MessageDialog(None, "Update suscessfully", "Notification", wx.OK)
                    dialog.ShowModal()
                    requests = form_db.GetRequests()
                    index=0
                    self.m_listRequest.DeleteAllItems()
                    for i in requests:
                        self.m_listRequest.InsertItem(index, str(i[0]))
                        self.m_listRequest.SetItem(index, 1, i[1])
                        self.m_listRequest.SetItem(index, 2, i[2])
                        self.m_listRequest.SetItem(index, 3, i[3])
                        self.m_listRequest.SetItem(index, 4, i[4])

    def m_onReportClick( self, event ):
        if self.ID == "":
            dialog = wx.MessageDialog(None, "Please select a request", "Notification", wx.OK)
            dialog.ShowModal()
        else:
            frameReport = wx.Frame(None, title = u"Report Form", pos = wx.DefaultPosition, size = wx.Size( 580,350 ), style= wx.TAB_TRAVERSAL | wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX) 
            panel_Report = MyPanelFormReport(frameReport)
            phone = self.m_listRequest.GetItem(self.m_listRequest.GetFirstSelected(), 1)
            title = self.m_listRequest.GetItem(self.m_listRequest.GetFirstSelected(), 2)
            description = self.m_listRequest.GetItem(self.m_listRequest.GetFirstSelected(), 3)
            panel_Report.ID = int(self.ID)
            panel_Report.m_txtPhone.SetValue(phone.GetText())
            panel_Report.m_txtTitle.SetValue(title.GetText())
            panel_Report.m_txtDescription.SetValue(description.GetText())
            frameReport.Show(True)
