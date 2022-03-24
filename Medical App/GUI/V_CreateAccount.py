# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Models.M_DB_User import DB_User

###########################################################################
## Class MyPanelCreateAccount
###########################################################################

class MyPanelCreateAccount ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,500 ), style = wx.TAB_TRAVERSAL )
        
        bSizer = wx.BoxSizer( wx.VERTICAL )
        
        self.m_bitmap = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Media/account_screen.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer.Add( self.m_bitmap, 0, wx.ALL, 5 )
        
        self.m_staticText = wx.StaticText( self, wx.ID_ANY, u"Create Account", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText.Wrap( -1 )
        self.m_staticText.SetFont( wx.Font( 16, 70, 90, 90, False, wx.EmptyString ) )
        
        bSizer.Add( self.m_staticText, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        fgSizer = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer.SetFlexibleDirection( wx.BOTH )
        fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Email Account", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        fgSizer.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        self.m_textEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer.Add( self.m_textEmail, 0, wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        fgSizer.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        self.m_textUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        fgSizer.Add( self.m_textUsername, 0, wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        fgSizer.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        self.m_textPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PASSWORD )
        fgSizer.Add( self.m_textPassword, 0, wx.ALL, 5 )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Confirm Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        fgSizer.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.m_textConfirmPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), wx.TE_PASSWORD | wx.TE_PROCESS_ENTER )
        fgSizer.Add( self.m_textConfirmPassword, 0, wx.ALL, 5 )
        
        
        bSizer.Add( fgSizer, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_btnCreate = wx.Button( self, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer.Add( self.m_btnCreate, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        self.SetSizer( bSizer )
        self.Layout()
        
        # Connect Events
        self.m_textConfirmPassword.Bind( wx.EVT_TEXT_ENTER, self.m_formEnter )
        self.m_btnCreate.Bind( wx.EVT_BUTTON, self.m_btnCreateClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def m_btnCreateClick( self, event ):
        email = self.m_textEmail.GetValue()
        username = self.m_textUsername.GetValue()
        password = self.m_textPassword.GetValue()
        confirm_password = self.m_textConfirmPassword.GetValue()

        if password != confirm_password:
            dialog = wx.MessageDialog(None, "Password and cofirm password must be the same", "Notification", wx.OK)
            dialog.ShowModal()
        else:
            user_db = DB_User()
            check = user_db.CreateAccount(username, password, email)
            if check == 0:
                dialog = wx.MessageDialog(None, "Email already exists", "Notification", wx.OK)
                dialog.ShowModal()
            elif check == 1:
                dialog = wx.MessageDialog(None, "Username already exists", "Notification", wx.OK)
                dialog.ShowModal()
            else:
                dialog = wx.MessageDialog(None, "Create account successfully", "Notification", wx.OK)
                dialog.ShowModal()
                self.GetParent().Close()

    def m_formEnter( self, event ):
        event.Skip()
    