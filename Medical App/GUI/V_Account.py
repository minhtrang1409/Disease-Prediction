# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from configparser import ConfigParser
from Models.M_DB_User import DB_User

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

###########################################################################
## Class MyPanelAccount
###########################################################################

class MyPanelAccount ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 560,280 ), style = wx.TAB_TRAVERSAL )
        
        bSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Media/user.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer.Add( self.m_bitmap1, 0, wx.ALL, 5 )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticLabel = wx.StaticText( self, wx.ID_ANY, u"Account settings", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticLabel.Wrap( -1 )
        self.m_staticLabel.SetFont( wx.Font( 22, 70, 90, 90, False, wx.EmptyString ) )
        
        bSizer1.Add( self.m_staticLabel, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.BOTH )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        fgSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        self.m_textUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        fgSizer1.Add( self.m_textUsername, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        fgSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        self.m_textEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer1.Add( self.m_textEmail, 0, wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"New Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        fgSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        self.m_textPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        fgSizer1.Add( self.m_textPassword, 0, wx.ALL, 5 )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Confirm Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        fgSizer1.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        self.m_textConfirmPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        fgSizer1.Add( self.m_textConfirmPassword, 0, wx.ALL, 5 )
        
        
        bSizer1.Add( fgSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_btnVerifyEmail = wx.Button( self, wx.ID_ANY, u"Verify email", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_btnVerifyEmail, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_btnChangePassword = wx.Button( self, wx.ID_ANY, u"Change password", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_btnChangePassword, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        bSizer.Add( bSizer1, 1, wx.EXPAND, 5 )
        
        self.SetSizer( bSizer )
        self.Layout()
        
        self.db_user = DB_User()
        
        # Connect Events
        self.m_btnVerifyEmail.Bind( wx.EVT_BUTTON, self.VerifyEmail )
        self.m_btnChangePassword.Bind( wx.EVT_BUTTON, self.ChangePassword )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def VerifyEmail( self, event ):
        db_user = DB_User()
        db_user.VerifyEmail(self.m_textEmail.GetValue())
    
    def ChangePassword( self, event ):
        password = self.m_textPassword.GetValue()
        confirm_password = self.m_textConfirmPassword.GetValue()

        if password != confirm_password:
            dialog = wx.MessageDialog(None, "Password and cofirm password must be the same", "Notification", wx.OK)
            dialog.ShowModal()
        else:
            check = self.db_user.ChangePassword(self.m_textUsername.GetValue() ,password)
            if check == 0:
                dialog = wx.MessageDialog(None, "Error!! Try again later", "Notification", wx.OK)
                dialog.ShowModal()
            else:
                dialog = wx.MessageDialog(None, "Password changed successfully", "Notification", wx.OK)
                dialog.ShowModal()
                self.m_textPassword.SetValue("")
                self.m_textConfirmPassword.SetValue("")