# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Models.M_DB_User import DB_User
from GUI.V_SuspendAccount import MyPanelAccSuspend

###########################################################################
## Class MyPanelAccModerator
###########################################################################

class MyPanelAccModerator ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        self.user_db = DB_User()

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        self.m_searchUsername = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_searchUsername.ShowSearchButton( True )
        self.m_searchUsername.ShowCancelButton( False )
        bSizer10.Add( self.m_searchUsername, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_listAccount = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        self.m_listAccount.InsertColumn(0, 'Username', width = 125)
        self.m_listAccount.InsertColumn(1, 'Role', width = 75)
        bSizer10.Add( self.m_listAccount, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer10 )
        self.Layout()

        # Connect Events
        self.m_searchUsername.Bind( wx.EVT_TEXT, self.m_onTextChanged )
        self.m_listAccount.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.m_onItemActivated )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def m_onTextChanged( self, event ):
        key = self.m_searchUsername.GetValue()
        lst_username = self.user_db.SearchUsername(key)
        self.m_listAccount.DeleteAllItems()
        for i in lst_username:
            self.m_listAccount.InsertItem(0, str(i[0]))
            if int(i[1]) == 0:
                role = "Patient"
            elif int(i[1]) == 1:
                role = "Doctor"
            else:
                role = "Moderator"
            self.m_listAccount.SetItem(0, 1, role)

    def m_onItemActivated( self, event ):
        frameSuspend = wx.Frame(None, title = u"Suspend Account", pos = wx.DefaultPosition, size = wx.Size( 580,350 ), style= wx.TAB_TRAVERSAL | wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX) 
        panel_Suspend = MyPanelAccSuspend(frameSuspend)
        username = self.m_listAccount.GetItem(self.m_listAccount.GetFirstSelected(), 0)
        profile_user = self.user_db.GetProfile(username.GetText())
        panel_Suspend.m_txtUsername.SetValue(username.GetText())
        panel_Suspend.m_txtFirstName.SetValue(profile_user[0])
        panel_Suspend.m_txtLastName.SetValue(profile_user[1])
        print(profile_user)
        frameSuspend.Show(True)

