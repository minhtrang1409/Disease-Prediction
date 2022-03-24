# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv
from Models.M_DB_User import DB_User

###########################################################################
## Class MyPanelProfile
###########################################################################

class MyPanelProfile ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,265 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText17 = wx.StaticText( self, wx.ID_ANY, u"Profile", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText17.Wrap( -1 )

        self.m_staticText17.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

        bSizer.Add( self.m_staticText17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer6.SetFlexibleDirection( wx.BOTH )
        fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText19.Wrap( -1 )

        fgSizer6.Add( self.m_staticText19, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_txtFirstName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer6.Add( self.m_txtFirstName, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText20.Wrap( -1 )

        fgSizer6.Add( self.m_staticText20, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_txtLastName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer6.Add( self.m_txtLastName, 1, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Gender", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        fgSizer6.Add( self.m_staticText21, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_ChoiceGenderChoices = [ u"Male", u"Female", u"Transgender", u"I don't want to provide" ]
        self.m_ChoiceGender = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_ChoiceGenderChoices, 0 )
        self.m_ChoiceGender.SetSelection( 2 )
        fgSizer6.Add( self.m_ChoiceGender, 0, wx.ALL, 5 )

        self.m_staticText22 = wx.StaticText( self, wx.ID_ANY, u"Date of Birth", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText22.Wrap( -1 )

        fgSizer6.Add( self.m_staticText22, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_datePicker1 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DROPDOWN )
        fgSizer6.Add( self.m_datePicker1, 0, wx.ALL|wx.EXPAND, 5 )

        self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Job", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText23.Wrap( -1 )

        fgSizer6.Add( self.m_staticText23, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_txtJob = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer6.Add( self.m_txtJob, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer.Add( fgSizer6, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_btnUpdate = wx.Button( self, wx.ID_ANY, u"Update profile", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer.Add( self.m_btnUpdate, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer )
        self.Layout()

        # Connect Events
        self.m_btnUpdate.Bind( wx.EVT_BUTTON, self.m_btnUpdateOnClick )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def m_btnUpdateOnClick( self, event ):
        user_db = DB_User()
        info = []
        info.append(str(self.m_txtFirstName.GetValue()))
        info.append(self.m_txtLastName.GetValue())
        info.append(self.m_ChoiceGender.GetString(self.m_ChoiceGender.GetCurrentSelection()))
        info.append(str(self.m_datePicker1.GetValue()))
        date = info[3].split(" ")
        info[3] = date[0]
        info.append(self.m_txtJob.GetValue())
        check = user_db.UpdateProfile(self.username, info)
        print(info)
        if check == -1:
            dialog = wx.MessageDialog(None, "Update fails", "Notification", wx.OK)
            dialog.ShowModal()
        else:
            dialog = wx.MessageDialog(None, "Update suscessfully", "Notification", wx.OK)
            dialog.ShowModal()

