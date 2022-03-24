# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyPanelDiseases
###########################################################################

class MyPanelDiseases ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer13 = wx.BoxSizer( wx.VERTICAL )

        self.m_searchIllness = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_searchIllness.ShowSearchButton( True )
        self.m_searchIllness.ShowCancelButton( False )
        bSizer13.Add( self.m_searchIllness, 0, wx.ALL|wx.EXPAND, 5 )

        fgSizer10 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer10.SetFlexibleDirection( wx.BOTH )
        fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_listIllness = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,250 ), wx.LC_REPORT )
        self.m_listIllness.InsertColumn(0, 'Name', width = 200)
        fgSizer10.Add( self.m_listIllness, 0, wx.ALL, 5 )

        self.m_txtDescription = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 270,250 ), wx.TE_BESTWRAP|wx.TE_MULTILINE|wx.TE_READONLY )
        fgSizer10.Add( self.m_txtDescription, 0, wx.ALL, 5 )


        bSizer13.Add( fgSizer10, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer13 )
        self.Layout()

        # Connect Events
        self.m_searchIllness.Bind( wx.EVT_TEXT, self.m_OnTextChanged )
        self.m_listIllness.Bind( wx.EVT_LIST_ITEM_SELECTED, self.m_onItemSelected )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def m_OnTextChanged( self, event ):
        SearchItems = []
        key = self.m_searchIllness.GetValue()
        for i in self.listIllness:
            if key in i:
                SearchItems.append(i)
        self.m_listIllness.DeleteAllItems()
        for i in SearchItems:
            self.m_listIllness.InsertItem(0, i)

    def m_onItemSelected( self, event ):
        index = self.m_listIllness.GetFirstSelected()
        data = self.listSymptom[index].split("; ")
        str_data = ""
        for i in data:
            str_data = str_data + i + "\n"
        self.m_txtDescription.SetValue(str_data)