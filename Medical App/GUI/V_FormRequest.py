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
## Class MyPanelFormRequest
###########################################################################

class MyPanelFormRequest ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Form Request", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer10.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Phone number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		fgSizer7.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_txtPhoneNumber = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 390,-1 ), 0 )
		fgSizer7.Add( self.m_txtPhoneNumber, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Title", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		fgSizer7.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textTitle = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textTitle, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		fgSizer7.Add( self.m_staticText30, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.m_textDescription = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,150 ), 0 )
		fgSizer7.Add( self.m_textDescription, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer10.Add( fgSizer7, 1, wx.EXPAND, 5 )

		self.m_btnRequest = wx.Button( self, wx.ID_ANY, u"Request", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_btnRequest, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		# Connect Events
		self.m_btnRequest.Bind( wx.EVT_BUTTON, self.m_btnRequestClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def m_btnRequestClick( self, event ):
		form_db = DB_Form()
		info = []
		info.append(self.m_txtPhoneNumber.GetValue())
		info.append(self.m_textTitle.GetValue())
		info.append(self.m_textDescription.GetValue())
		info.append("Pending")
		if self.m_txtPhoneNumber.GetValue() == "" or self.m_textTitle.GetValue() == "" or self.m_textDescription.GetValue() == "":
			dialog = wx.MessageDialog(None, "Please fill out the form", "Notification", wx.OK)
			dialog.ShowModal()
		else:
			check = form_db.CreateRequest(self.username, info)
			if check == -1:
				dialog = wx.MessageDialog(None, "Request fails", "Notification", wx.OK)
				dialog.ShowModal()
			else:
				dialog = wx.MessageDialog(None, "Request suscessfully", "Notification", wx.OK)
				dialog.ShowModal()


