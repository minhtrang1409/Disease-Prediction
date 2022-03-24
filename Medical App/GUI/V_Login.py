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
from Models.M_Version_Check import VersionCheck
from GUI.V_Welcome import MyFrameWelcome
from GUI.V_CreateAccount import MyPanelCreateAccount
from configparser import ConfigParser

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")

###########################################################################
## Class MyPanelLogin
###########################################################################

class MyPanelLogin ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 640,640 ), style = wx.TAB_TRAVERSAL )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Media/login_screen1.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 640,320 ), 0 )
        bSizer1.Add( self.m_bitmap1, 0, wx.ALL, 5 )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( 16, 73, 90, 90, False, wx.EmptyString ) )
        
        bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        bSizer1.Add( ( 10, 10), 0, 0, 5 )
        
        fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer1.SetFlexibleDirection( wx.HORIZONTAL )
        fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        fgSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )
        
        self.m_txtUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), wx.TE_PROCESS_ENTER )
        fgSizer1.Add( self.m_txtUsername, 0, wx.ALL, 5 )
        
        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        fgSizer1.Add( self.m_staticText11, 0, wx.ALL, 5 )
        
        self.m_txtPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
        fgSizer1.Add( self.m_txtPassword, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer1.Add( fgSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        self.m_btnSignIn = wx.Button( self, wx.ID_ANY, u"Sign in", wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
        bSizer1.Add( self.m_btnSignIn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        bSizer1.Add( ( 100, 100), 1, 0, 5 )
        
        self.m_btnCreateAccount = wx.Button( self, wx.ID_ANY, u"Create Account", wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
        bSizer1.Add( self.m_btnCreateAccount, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        # Connect Events
        self.m_btnSignIn.Bind( wx.EVT_BUTTON, self.m_btnSignInClick )
        self.m_txtPassword.Bind( wx.EVT_TEXT_ENTER, self.m_txtPasswordEnter )
        self.m_btnCreateAccount.Bind( wx.EVT_BUTTON, self.m_btnCreateAccountClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def m_btnSignInClick( self, event ):
        username = self.m_txtUsername.GetValue()
        password = self.m_txtPassword.GetValue()

        if username == "" or password == "":
            dialog = wx.MessageDialog(None, "No blank username/password", "Notification", wx.OK)
            dialog.ShowModal()
        else:
            user_db = DB_User()
            check = user_db.CheckLogin(username, password)
            if check == -1:
                dialog = wx.MessageDialog(None, "Wrong username or password", "Notification", wx.OK)
                dialog.ShowModal()
            else:
                role = user_db.GetRole(username)
                status = user_db.GetStatus(username)
                if str(status) == "1":
                    dialog = wx.MessageDialog(None, "You have been suspended! Please contact a moderator to appeal", "Notification", wx.OK)
                    dialog.ShowModal()
                else:
                    #Get the USERINFO section
                    userinfo = config_object["USERINFO"]

                    #Update the password
                    userinfo["username"] = username

                    #Write changes back to file
                    with open('config.ini', 'w') as conf:
                        config_object.write(conf)
                    VersionCheck()
                    self.GetParent().Close()
                    frameWelcome = MyFrameWelcome(None)
                    frameWelcome.username = username
                    frameWelcome.role = role
                    if frameWelcome.role == "0":
                        frameWelcome.m_menuItem7.Enable( False )
                        frameWelcome.m_menuItem8.Enable( False )
                    elif frameWelcome.role == "1": # Doctor
                        frameWelcome.m_menuItem8.Enable( False )
                    elif frameWelcome.role == "2":
                        frameWelcome.m_menuItem7.Enable( False )
                    frameWelcome.Show(True)
    
    def m_txtPasswordEnter( self, event ):
        self.m_btnSignInClick(event)

    def m_btnCreateAccountClick( self, event ):
        frame = wx.Frame(None, title = u"Create Account", pos = wx.DefaultPosition, size = wx.Size( 500,550 ), style= wx.TAB_TRAVERSAL | wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX) 
        _createAccount = MyPanelCreateAccount(frame)
        frame.Show(True)