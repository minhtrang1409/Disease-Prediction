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

###########################################################################
## Class MyPanelAccSuspend
###########################################################################

class MyPanelAccSuspend ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.user_db = DB_User()

		fgSizer8 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"First Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		fgSizer8.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.m_txtFirstName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 380,-1 ), wx.TE_READONLY )
		fgSizer8.Add( self.m_txtFirstName, 0, wx.ALL, 5 )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Last Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		fgSizer8.Add( self.m_staticText26, 0, wx.ALL, 5 )

		self.m_txtLastName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer8.Add( self.m_txtLastName, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		fgSizer8.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.m_txtUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer8.Add( self.m_txtUsername, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Suspend Reason", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		fgSizer8.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_txtReason = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,150 ), wx.TE_MULTILINE )
		fgSizer8.Add( self.m_txtReason, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer11.Add( fgSizer8, 1, wx.EXPAND, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_btnSuspend = wx.Button( self, wx.ID_ANY, u"Suspend", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_btnSuspend, 0, wx.ALL, 5 )

		self.m_btnUnsuspend = wx.Button( self, wx.ID_ANY, u"Unsuspend", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_btnUnsuspend, 0, wx.ALL, 5 )


		bSizer11.Add( fgSizer9, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		# Connect Events
		self.m_btnSuspend.Bind( wx.EVT_BUTTON, self.m_btnSuspendClick )
		self.m_btnUnsuspend.Bind( wx.EVT_BUTTON, self.m_btnUnsuspendClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_btnSuspendClick( self, event ):
		if self.m_txtReason.GetValue() == "":
			dialog = wx.MessageDialog(None, "Please give a reason for banning", "Notification", wx.OK)
			dialog.ShowModal()
		else:
			check = self.user_db.UpdateStatus(self.m_txtUsername.GetValue(), 1, self.m_txtReason.GetValue())
			if check == -1:
				dialog = wx.MessageDialog(None, "Suspend fails", "Notification", wx.OK)
				dialog.ShowModal()
			else:
				dialog = wx.MessageDialog(None, "Suspend successfully", "Notification", wx.OK)
				dialog.ShowModal()

	def m_btnUnsuspendClick( self, event ):
		check = self.user_db.UpdateStatus(self.m_txtUsername.GetValue(), 0, "")
		if check == -1:
			dialog = wx.MessageDialog(None, "Unsuspend fails", "Notification", wx.OK)
			dialog.ShowModal()
		else:
			dialog = wx.MessageDialog(None, "Unsuspend successfully", "Notification", wx.OK)
			dialog.ShowModal()


