# This file was automatically generated by pywxrc.
# -*- coding: UTF-8 -*-

import wx
import wx.xrc as xrc

__res = None

def get_resources():
    """ This function provides access to the XML resources in this module."""
    global __res
    if __res == None:
        __init_resources()
    return __res




class xrcManageTopicsFrame(wx.Frame):
#!XRCED:begin-block:xrcManageTopicsFrame.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcManageTopicsFrame.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PreFrame()
        self.PreCreate(pre)
        get_resources().LoadOnFrame(pre, parent, "ManageTopicsFrame")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.toolbar = xrc.XRCCTRL(self, "toolbar")
        self.splitter = xrc.XRCCTRL(self, "splitter")
        self.passage_list_pane = xrc.XRCCTRL(self, "passage_list_pane")
        self.passage_list_splitter = xrc.XRCCTRL(self, "passage_list_splitter")
        self.item_details_panel = xrc.XRCCTRL(self, "item_details_panel")



class xrcTopicDetailsPanel(wx.Panel):
#!XRCED:begin-block:xrcTopicDetailsPanel.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcTopicDetailsPanel.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PrePanel()
        self.PreCreate(pre)
        get_resources().LoadOnPanel(pre, parent, "TopicDetailsPanel")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.name_label = xrc.XRCCTRL(self, "name_label")
        self.name_text = xrc.XRCCTRL(self, "name_text")
        self.display_tag_checkbox = xrc.XRCCTRL(self, "display_tag_checkbox")
        self.description_label = xrc.XRCCTRL(self, "description_label")
        self.description_text = xrc.XRCCTRL(self, "description_text")



class xrcPassageDetailsPanel(wx.Panel):
#!XRCED:begin-block:xrcPassageDetailsPanel.PreCreate
    def PreCreate(self, pre):
        """ This function is called during the class's initialization.
        
        Override it for custom setup before the window is created usually to
        set additional window styles using SetWindowStyle() and SetExtraStyle().
        """
        pass
        
#!XRCED:end-block:xrcPassageDetailsPanel.PreCreate

    def __init__(self, parent):
        # Two stage creation (see http://wiki.wxpython.org/index.cgi/TwoStageCreation)
        pre = wx.PrePanel()
        self.PreCreate(pre)
        get_resources().LoadOnPanel(pre, parent, "PassageDetailsPanel")
        self.PostCreate(pre)

        # Define variables for the controls, bind event handlers
        self.passage_text = xrc.XRCCTRL(self, "passage_text")
        self.comment_text = xrc.XRCCTRL(self, "comment_text")
        self.passage_preview = xrc.XRCCTRL(self, "passage_preview")





# ------------------------ Resource data ----------------------

def __init_resources():
    global __res
    __res = xrc.EmptyXmlResource()

    __res.Load('manage_topics.xrc')

# ----------------------- Gettext strings ---------------------

def __gettext_strings():
    # This is a dummy function that lists all the strings that are used in
    # the XRC file in the _("a string") format to be recognized by GNU
    # gettext utilities (specificaly the xgettext utility) and the
    # mki18n.py script.  For more information see:
    # http://wiki.wxpython.org/index.cgi/Internationalization 
    
    def _(str): pass
    
    _("New topic")
    _("New topic")
    _("Add passage")
    _("Add passage")
    _("Cut")
    _("Cut")
    _("Copy")
    _("Copy")
    _("Paste")
    _("Paste")
    _("Delete")
    _("Delete")
    _("Undo previous action")
    _("Undo")
    _("Redoes the last undone action")
    _("Redo")
    _("Manage Topics")
    _("Name:")
    _("Show tags")
    _("Description:")
    _("Passage:")
    _("Comment:")

