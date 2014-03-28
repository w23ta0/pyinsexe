#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx,os,sys
import wx.xrc
import ConfigParser

###########################################################################
## Class MyFrame1
###########################################################################
cf = ConfigParser.ConfigParser()
cf.read("config.ini")
pypath = cf.get("dirconf", "py")
pyinspath = cf.get("dirconf", "pyins")
pyinsdir = cf.get("dirconf", "pyinsdir")



class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        """

        :param parent:
        """
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyInstaller", pos = wx.DefaultPosition, size = wx.Size( 531,283 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        gbSizer6 = wx.GridBagSizer( 0, 0 )
        gbSizer6.SetFlexibleDirection( wx.BOTH )
        gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"PyInstaller", wx.DefaultPosition, wx.Size( -1,-1 ), wx.ALIGN_CENTRE )
        self.m_staticText6.Wrap( -1 )
        self.m_staticText6.SetFont( wx.Font( 16, 70, 90, 90, False, "Snap ITC" ) )
        self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        bSizer2.Add( self.m_staticText6, 0, wx.EXPAND, 5 )

        gbSizer7 = wx.GridBagSizer( 0, 0 )
        gbSizer7.SetFlexibleDirection( wx.BOTH )
        gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"源文件", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_CENTRE )
        self.m_staticText4.Wrap( -1 )
        self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        gbSizer7.Add( self.m_staticText4, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_filePicker2 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.py", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        gbSizer7.Add( self.m_filePicker2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer2.Add( gbSizer7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        gbSizer2 = wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"目的地", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
        self.m_staticText5.Wrap( -1 )
        self.m_staticText5.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        gbSizer2.Add( self.m_staticText5, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_dirPicker2 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        gbSizer2.Add( self.m_dirPicker2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer2.Add( gbSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

        gbSizer21 = wx.GridBagSizer( 0, 0 )
        gbSizer21.SetFlexibleDirection( wx.BOTH )
        gbSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"图标文件", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
        self.m_staticText51.Wrap( -1 )
        self.m_staticText51.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        gbSizer21.Add( self.m_staticText51, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_filePicker21 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.ico", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        gbSizer21.Add( self.m_filePicker21, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer2.Add( gbSizer21, 0, wx.ALL, 5 )


        gbSizer2 = wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        self.m_staticText52 = wx.StaticText( self, wx.ID_ANY, u"UPX目录", wx.DefaultPosition, wx.Size( 50,-1 ), wx.ALIGN_CENTRE|wx.ST_NO_AUTORESIZE )
        self.m_staticText52.Wrap( -1 )
        self.m_staticText52.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )

        gbSizer2.Add( self.m_staticText52, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_dirPicker22 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        gbSizer2.Add( self.m_dirPicker22, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer2.Add( gbSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


        gbSizer6.Add( bSizer2, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.TOP|wx.BOTTOM, 5 )

        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"可选参数" ), wx.VERTICAL )

        self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"-F 就是打包成单独的一个文件", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_checkBox1, 0, wx.ALL, 5 )

        self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, u"-w 就是窗口程序，不会跳出后面的黑框", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_checkBox2, 0, wx.ALL, 5 )

        self.m_checkBox5 = wx.CheckBox( self, wx.ID_ANY, u"-d debug程序", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_checkBox5, 0, wx.ALL, 5 )

        self.m_checkBox6 = wx.CheckBox( self, wx.ID_ANY, u"-c 命令行程序，没有窗口", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_checkBox6, 0, wx.ALL, 5 )


        gbSizer6.Add( sbSizer1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer1.Add( gbSizer6, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        bSizer1.AddSpacer( ( 0, 0), 1, 0, 5 )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        m_sdbSizer5 = wx.StdDialogButtonSizer()
        self.m_sdbSizer5OK = wx.Button( self, wx.ID_OK )
        m_sdbSizer5.AddButton( self.m_sdbSizer5OK )
        self.m_sdbSizer5Cancel = wx.Button( self, wx.ID_CANCEL )
        m_sdbSizer5.AddButton( self.m_sdbSizer5Cancel )
        self.m_sdbSizer5Help = wx.Button( self, wx.ID_HELP )
        m_sdbSizer5.AddButton( self.m_sdbSizer5Help )
        m_sdbSizer5.Realize();

        bSizer4.Add( m_sdbSizer5, 0, 0, 5 )


        bSizer1.Add( bSizer4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_statusBar2 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_filePicker2.Bind( wx.EVT_FILEPICKER_CHANGED, self.m_filePicker2OnFileChanged )
        self.m_dirPicker2.Bind( wx.EVT_DIRPICKER_CHANGED, self.m_dirPicker2OnDirChanged )
        self.m_filePicker21.Bind( wx.EVT_FILEPICKER_CHANGED, self.m_filePicker21OnFileChanged )
        self.m_dirPicker22.Bind( wx.EVT_DIRPICKER_CHANGED, self.m_dirPicker22nDirChanged )
        self.m_checkBox1.Bind( wx.EVT_CHECKBOX, self.m_checkBox1OnCheckBox )
        self.m_checkBox2.Bind( wx.EVT_CHECKBOX, self.m_checkBox2OnCheckBox )
        self.m_checkBox5.Bind( wx.EVT_CHECKBOX, self.m_checkBox5OnCheckBox )
        self.m_checkBox6.Bind( wx.EVT_CHECKBOX, self.m_checkBox6OnCheckBox )
        self.m_sdbSizer5Cancel.Bind( wx.EVT_BUTTON, self.m_sdbSizer5OnCancelButtonClick )
        self.m_sdbSizer5Help.Bind( wx.EVT_BUTTON, self.m_sdbSizer5OnHelpButtonClick )
        self.m_sdbSizer5OK.Bind( wx.EVT_BUTTON, self.m_sdbSizer5OnOKButtonClick )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def m_filePicker2OnFileChanged( self, event ):
        event.Skip()

    def m_dirPicker2OnDirChanged( self, event ):
        event.Skip()

    def m_filePicker21OnFileChanged( self, event ):
        event.Skip()

    def m_dirPicker22nDirChanged( self, event ):
        event.Skip()

    def m_checkBox1OnCheckBox( self, event ):
        event.Skip()

    def m_checkBox2OnCheckBox( self, event ):
        event.Skip()

    def m_checkBox5OnCheckBox( self, event ):
        event.Skip()

    def m_checkBox6OnCheckBox( self, event ):
        event.Skip()

    def m_sdbSizer5OnCancelButtonClick( self, event ):
        self.Close(True)
        event.Skip()
    def m_sdbSizer5OnHelpButtonClick( self, event ):
        """

        :param event:
        """
        b = pyinsdir + "README"
        command = pypath + " " + pyinspath + " -h > " + b
        print b

        if os.path.exists(b):
            for line in open(pyinsdir+"README"):
                print line
        else:
            os.system(command)
            for line in open(pyinsdir+"README"):
                print line
        event.Skip()

    def m_sdbSizer5OnOKButtonClick( self, event ):

        filepath = self.m_filePicker2.GetTextCtrlValue()
        dirpath = self.m_dirPicker2.GetTextCtrlValue()
        iconpath = self.m_filePicker21.GetTextCtrlValue()
        upxpath = self.m_dirPicker22.GetTextCtrlValue()

        if self.m_dirPicker2.GetTextCtrlValue():
            dp = " --distpath=" + dirpath
        else:
            dp = " "

        if self.m_filePicker21.GetTextCtrlValue():
            i = " --icon="  + iconpath
        else:
            i = ""
        if self.m_checkBox1.IsChecked():
            f = " -F "
        else:
            f = ""
        if self.m_checkBox2.IsChecked():
            w = " -w "
        else:
            w = ""
        if self.m_dirPicker22.GetTextCtrlValue():
            x = " --upx-dir="
        else:
            x = ""
        if self.m_checkBox5.IsChecked():
            d = " -d "
        else:
            d = ""
        if self.m_checkBox6.IsChecked():
            c = " -c "
        else:
            c = ""
        command =  pypath + " " + pyinspath + f + w + x + upxpath + d + c + i  + dp + " " + filepath
        os.system(command)
        event.Skip()

class App(wx.App):
    def OnInit(self):
        frame = MyFrame1(None)
        frame.Show()
        return True
if __name__ == '__main__':
    app = App()
    app.MainLoop()
