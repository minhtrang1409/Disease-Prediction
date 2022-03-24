# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Models.M_JS_Symptom import *
from Models.M_JS_Illness import *
from GUI.V_FormRequest import MyPanelFormRequest
from GUI.V_GlobalChat import MyBrowser
from GUI.V_Account import MyPanelAccount
from GUI.V_Report import MyPanelReport
from GUI.V_ProfileAccount import MyPanelProfile
from GUI.V_RequestHandle import MyPanelRequestAccept
from GUI.V_ModerateAccount import MyPanelAccModerator
from GUI.V_DiseaseInformation import MyPanelDiseases

from Models.M_DB_Form import DB_Form
from Models.M_DB_User import DB_User

###########################################################################
## Class MyFrameWelcome
###########################################################################

class MyFrameWelcome ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Welcome", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.username = ""
        self.role = 0
        self.db_user = DB_User()
        self.lst_item = []
        self.lst_index = []
        self.mode = 0

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        self.m_menubar = wx.MenuBar( 0 )
        self.m_menuApp = wx.Menu()
        self.m_menuItem1 = wx.MenuItem( self.m_menuApp, wx.ID_ANY, u"Diseases Searching", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuApp.AppendItem( self.m_menuItem1 )
        
        self.m_menuItem2 = wx.MenuItem( self.m_menuApp, wx.ID_ANY, u"Global chat", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuApp.AppendItem( self.m_menuItem2 )
        
        self.m_menuItem3 = wx.MenuItem( self.m_menuApp, wx.ID_ANY, u"Make a request", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuApp.AppendItem( self.m_menuItem3 )
        
        self.m_menuApp.AppendSeparator()
        
        self.m_menuItem4 = wx.MenuItem( self.m_menuApp, wx.ID_ANY, u"Exit app", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuApp.AppendItem( self.m_menuItem4 )
        
        self.m_menubar.Append( self.m_menuApp, u"A&pplication" ) 
        
        self.m_menuAcc = wx.Menu()
        self.m_menuItem5 = wx.MenuItem( self.m_menuAcc, wx.ID_ANY, u"Manage Account", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuAcc.AppendItem( self.m_menuItem5 )
        
        self.m_menuItem6 = wx.MenuItem( self.m_menuAcc, wx.ID_ANY, u"Edit Profile", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuAcc.AppendItem( self.m_menuItem6 )
        
        self.m_menubar.Append( self.m_menuAcc, u"A&ccount" ) 
        
        self.m_menuDoctor = wx.Menu()
        self.m_menuItem7 = wx.MenuItem( self.m_menuDoctor, wx.ID_ANY, u"Request Handle", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuDoctor.Append( self.m_menuItem7 )

        self.m_menubar.Append( self.m_menuDoctor, u"&Doctor" )

        self.m_menuModerator = wx.Menu()
        self.m_menuItem8 = wx.MenuItem( self.m_menuModerator, wx.ID_ANY, u"Suspend account", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menuModerator.Append( self.m_menuItem8 )

        self.m_menubar.Append( self.m_menuModerator, u"&Moderator" )

        self.SetMenuBar( self.m_menubar )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
        fgSizer3.SetFlexibleDirection( wx.BOTH )
        fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_searchCtrl = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        self.m_searchCtrl.ShowSearchButton( True )
        self.m_searchCtrl.ShowCancelButton( True )
        fgSizer3.Add( self.m_searchCtrl, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_btnReport = wx.Button( self, wx.ID_ANY, u"Report", wx.DefaultPosition, wx.DefaultSize, 0 )
        fgSizer3.Add( self.m_btnReport, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer1.Add( fgSizer3, 0, wx.EXPAND, 5 )
        
        self.m_checkListSymptom = ParseSymptoms()
        self.m_checkListSymptom = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, self.m_checkListSymptom, 0 )
        bSizer1.Add( self.m_checkListSymptom, 1, wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_MENU, self.menuItem1_selected, id = self.m_menuItem1.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItem2_selected, id = self.m_menuItem2.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItem3_selected, id = self.m_menuItem3.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItem4_selected, id = self.m_menuItem4.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItem5_selected, id = self.m_menuItem5.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItem6_selected, id = self.m_menuItem6.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItem7_selected, id = self.m_menuItem7.GetId() )
        self.Bind( wx.EVT_MENU, self.menuItem8_selected, id = self.m_menuItem8.GetId() )
        self.m_searchCtrl.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.m_OnCancelSearch )
        self.m_searchCtrl.Bind( wx.EVT_TEXT, self.m_OnTextChanged )
        self.m_btnReport.Bind( wx.EVT_BUTTON, self.m_btnReportClick )
        self.m_checkListSymptom.Bind( wx.EVT_CHECKLISTBOX, self.m_OnListBoxToggle )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def menuItem1_selected( self, event ):
        frameDiseaseInfo = wx.Frame(None, title = u"Form Request", pos = wx.DefaultPosition, size = wx.Size( 530,340 ), style= wx.TAB_TRAVERSAL | wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX) 
        panel_DiseaseInfo = MyPanelDiseases(frameDiseaseInfo)
        lstInfo = GetListIllnessInfo()
        index=0
        for i in lstInfo[0]:
            panel_DiseaseInfo.m_listIllness.InsertItem(index, i)
        panel_DiseaseInfo.listIllness = lstInfo[0]
        panel_DiseaseInfo.listSymptom = lstInfo[1]
        print(lstInfo[1])
        frameDiseaseInfo.Show(True)
    
    def menuItem2_selected( self, event ):
        dialog = MyBrowser(None, -1) 
        dialog.browser.MSWSetEmulationLevel(level=11)
        dialog.browser.LoadURL("https://realtime-chat-system.herokuapp.com/?uname=" + self.username) 
        dialog.Show() 
    
    def menuItem3_selected( self, event ):
        frameFormRequest = wx.Frame(None, title = u"Form Request", pos = wx.DefaultPosition, size = wx.Size( 530,300 ), style= wx.TAB_TRAVERSAL | wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX) 
        panel_FormRequest = MyPanelFormRequest(frameFormRequest)
        panel_FormRequest.username = self.username
        frameFormRequest.Show(True)
    
    def menuItem4_selected( self, event ):
        self.Close()
    
    def menuItem5_selected( self, event ):
        frameAccount = wx.Frame(None, title = u"Account manager", pos = wx.DefaultPosition, size = wx.Size( 580,300 ), style= wx.TAB_TRAVERSAL | wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX) 
        panel_Account = MyPanelAccount(frameAccount)
        panel_Account.m_textUsername.SetValue(self.username)
        email = self.db_user.GetEmail(self.username)
        panel_Account.m_textEmail.SetValue(email)
        frameAccount.Show(True)
    
    def menuItem6_selected( self, event ):
        frameProfile = wx.Frame(None, title = u"Profile manager", pos = wx.DefaultPosition, size = wx.Size( 400,300 ), style= wx.TAB_TRAVERSAL | wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX) 
        panel_Profile = MyPanelProfile(frameProfile)
        panel_Profile.username = self.username
        profile = self.db_user.GetProfile(self.username)
        # print(type(profile))
        panel_Profile.m_txtFirstName.SetValue(profile[0])
        panel_Profile.m_txtLastName.SetValue(profile[1])
        panel_Profile.m_ChoiceGender.SetSelection(int(profile[2]))
        day, month, year = profile[3].split('/')
        displayDate = wx.DateTimeFromDMY(int(day), int(month) - 1, int(year))
        panel_Profile.m_datePicker1.SetValue(displayDate)
        panel_Profile.m_txtJob.SetValue(profile[4])
        frameProfile.Show(True)
    
    def menuItem7_selected( self, event ):
        frameHandleRequest = wx.Frame(None, title = u"Request Handler", pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style= wx.TAB_TRAVERSAL | wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX) 
        panel_HandleRequest = MyPanelRequestAccept(frameHandleRequest)
        form_db = DB_Form()
        requests = form_db.GetRequests()
        index=0
        for i in requests:
            panel_HandleRequest.m_listRequest.InsertItem(index, str(i[0]))
            panel_HandleRequest.m_listRequest.SetItem(index, 1, i[1])
            panel_HandleRequest.m_listRequest.SetItem(index, 2, i[2])
            panel_HandleRequest.m_listRequest.SetItem(index, 3, i[3])
            panel_HandleRequest.m_listRequest.SetItem(index, 4, i[4])
        frameHandleRequest.Show(True)

    def menuItem8_selected( self, event ):
        frameModerateAccount = wx.Frame(None, title = u"Moderate Account", pos = wx.DefaultPosition, size = wx.Size( 250,300 ), style= wx.TAB_TRAVERSAL | wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX) 
        panel_ModerateAccount = MyPanelAccModerator(frameModerateAccount)
        panel_ModerateAccount.m_searchUsername.SetDescriptiveText("Type in username")
        user_db = DB_User()
        users = user_db.SearchUsername("")
        index=0
        for i in users:
            panel_ModerateAccount.m_listAccount.InsertItem(index, str(i[0]))
            if int(i[1]) == 0:
                role = "Patient"
            elif int(i[1]) == 1:
                role = "Doctor"
            else:
                role = "Moderator"
            panel_ModerateAccount.m_listAccount.SetItem(index, 1, role)
        frameModerateAccount.Show(True)
    
    def m_OnCancelSearch( self, event ):
        self.m_searchCtrl.SetValue("")
        self.mode = 0
    
    def m_OnTextChanged( self, event ):
        key = self.m_searchCtrl.GetValue()
        self.mode = 1
        if key == "":
            self.mode = 0
        SearchListSymptom = SearchSymptoms(key)
        # print(SearchListSymptom)
        self.m_checkListSymptom.Set(SearchListSymptom)
        self.tmp_lst = []
        for index in SearchListSymptom:
            if not self.lst_item:
                break
            for i in self.lst_item:
                if i == index:
                    self.tmp_lst.append(i)
        self.m_checkListSymptom.SetCheckedStrings(self.tmp_lst)
                    
    
    def m_btnReportClick( self, event ):
        lstIndex = list(self.m_checkListSymptom.GetCheckedStrings())
        lstIllness = ParseIllnesses(lstIndex)
        sort_lstIllness = sorted(lstIllness, key=lambda item: item[2])
        frameReport = wx.Frame(None, title = 'Report', size=(400, 300))
        panel_Report = MyPanelReport(frameReport)

        for i in sort_lstIllness:
            panel_Report.m_listCtrlReport.InsertItem(0, i[0])
            panel_Report.m_listCtrlReport.SetStringItem(0, 1, str(i[2]) + "%")
        frameReport.Show(True)
    
    def m_OnListBoxToggle( self, event ):
        lstItem = self.m_checkListSymptom.GetCheckedStrings()
        if self.mode == 1:
            if len(lstItem) > len(self.tmp_lst):
                self.tmp_lst = lstItem
                minus_lst = [item for item in self.tmp_lst if item not in self.lst_item]
                self.lst_item.extend(minus_lst)
            if len(lstItem) < len(self.tmp_lst):
                tmp_lst2 = lstItem
                minus_lst = [item for item in self.tmp_lst if item not in tmp_lst2]
                minus_item = ''.join(minus_lst)
                self.tmp_lst = lstItem
                self.lst_item.remove(minus_item)
        if self.mode == 0:
            if len(lstItem) < len(self.lst_item):
                self.lst_item = list(lstItem)
            if len(lstItem) > len(self.lst_item):
                for item in lstItem:
                    if not self.lst_item:
                        self.lst_item.append(item)
                        break
                    flag = 1
                    for i in self.lst_item:
                        if i == item:
                            flag = 0
                    if flag == 1:
                        self.lst_item.append(item)
        print(self.lst_item)
