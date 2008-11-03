import wx
import wx.html
from util.unicode import to_str, to_unicode
from backend.bibleinterface import biblemgr
from xrc.fontchoice_xrc import *
import guiconfig
import config
from gui import htmlbase
from module_tree import LanguageModuleTree
from displayframe import DisplayFrameXRC
from util import osutils
from gui import fonts
from gui.fonts import font_settings

DefaultFont = object()

	
class FontChoiceDialog(xrcFontChoiceDialog):
	def __init__(self, parent):
		super(FontChoiceDialog, self).__init__(parent)
		self.font_face.Bind(wx.EVT_CHOICE, self.on_font_changed)
		self.font_size.Bind(wx.EVT_SPINCTRL, self.on_font_changed)
		self.gui_use_default_font.Bind(wx.EVT_CHECKBOX, 
			lambda evt: self.on_use_default_font(evt.Checked()))
		
		self.tree = FontTree(self.filterable_tree_holder)
		self.tree.on_module_choice += self.on_module_choice
		self.tree.on_category_choice += self.on_category_choice
		self.filterable_tree_holder.Sizer.Add(self.tree, 1, wx.GROW)
		self.filterable_tree_holder.Layout()
		names = wx.FontEnumerator().GetFacenames()
		names.sort()
		self.font_face.Clear()
		self.font_face.AppendItems(names)
		self.preview.handle_links = False

		#if size is None:
		#	size = max(wx.NORMAL_FONT.PointSize, 10)
		#
		#if font is None:
		#	font = wx.Font(size, wx.SWISS, wx.NORMAL, wx.NORMAL, False);
		#
		#	font = font.FaceName
		
		self.on_default_choice()
	
	def on_use_default_font(self, checked):
		if checked:
			font, size, use_in_gui = fonts.get_default_font(self.tree_item)
			self.set_font_params(font, size)
			if self.tree_item == DefaultFont:
				font_settings["default_fonts"] = None
			else:
				if self.item_to_set in self.item_section:
					del self.item_section[self.item_to_set]
				
		
	def set_font_params(self, font, size):
		if not self.font_face.SetStringSelection(font):
			self.font_face.SetSelection(0)

		self.font_size.SetValue(size)
		self.update_preview()
		

	def on_font_changed(self, event):
		font, size = self.font_face.StringSelection, self.font_size.Value
		gui = self.gui_use_in_ui.Value
		self.gui_use_default_font.SetValue(False)
		self.item_section[self.item_to_set] = font, size, gui
		self.update_preview()

	def on_item_choice(self, data, parent_data, font_details_getter):
		default, (font, size, use_in_gui) = font_details_getter(data)
		self.set_font_params(font, size)
		self.tree_item = data
		
		self.on_use_default_font(default)
		
		self.gui_use_default_font.SetValue(default)
		self.gui_use_default_font.ContainingSizer.Show(0, True)#data!=DefaultFont)
		self.Layout()
		self.filterable_tree_holder.Parent.Layout()
		
		# refresh to ensure that the static text doesn't get painted anywhere
		# else
		self.Refresh()
	
	def on_module_choice(self, data, parent_data):
		self.mod = data
		self.preview.mod = data
		self.item_section = font_settings["module_fonts"]
		self.item_to_set = data.Name()
		
		self.on_item_choice(data, parent_data, fonts.get_module_font_params)

	def on_category_choice(self, data, parent_data):
		if data == DefaultFont:
			return self.on_default_choice(data, parent_data)
		
		# set the preview's mod to None, as we don't want any font based on
		# the module we happen to be preview with
		self.preview.mod = data
		
		self.mod = None
		books = [biblemgr.bible, biblemgr.commentary, 
			biblemgr.dictionary, biblemgr.genbook]
		
		# if there is a book which uses this language open, 
		# use this for the preview
		for book in books:
			if book.mod.Lang() == data:
				self.mod = book.mod
				break
		
		# otherwise just take the first one of the language		
		else:
			self.mod = self.tree.data[data][0]
		
		self.item_section = font_settings["language_fonts"]
		self.item_to_set = data
		
		self.on_item_choice(data, parent_data, fonts.get_language_font_params)
	
	def on_default_choice(self, data=DefaultFont, parent_data=None):
		self.item_section = font_settings
		self.item_to_set = "default_fonts"
		self.preview.mod = None
		self.mod = biblemgr.bible.mod
		
		
		self.on_item_choice(data, parent_data, 
			lambda data:fonts.default_fonts())
		
		
	

	def update_preview(self):
		#self.preview.font 
		# self.preview.SetStandardFonts(self.font_size.Value, 
		#	self.font_face.StringSelection, "")
		if self.mod is None:
			self.preview.SetPage(config.MODULE_MISSING_STRING)
			return

		try:
			books = [biblemgr.bible, biblemgr.commentary, 
				biblemgr.dictionary, biblemgr.genbook]
			frames = guiconfig.mainfrm.frames

			for book, frame in zip(books, frames):
				if self.mod.Name() not in book.GetModuleList():
					continue

				# if we are already set to that book, use it
				### should we get a better key here?
				if self.mod == frame.mod or True:
					if isinstance(frame.reference, basestring):
						ref = frame.reference
					else:
						ref = frame.reference.text
						
				self.mod.KeyText(to_str(ref, self.mod))
				
				text = self.mod.RenderText()
				# if there is no text here, look back and forth for text
				if not text:
					old = self.mod.getSkipConsecutiveLinks()
					self.mod.setSkipConsecutiveLinks(True)
					
					for direction in 1, -1:
						self.mod.increment(direction)
						text = self.mod.RenderText()
						if text:
							break
					
					self.mod.setSkipConsecutiveLinks(old)

				ref = self.mod.getKeyText()
				self.preview.SetPage("%s (%s)<br>%s" % (
					to_unicode(ref, self.mod), self.mod.Name(), text
				))
				
		finally:
			pass
			#preview % tuple(guiconfig.get_window_colours()))
	
	def ShowModal(self):
		old_fonts = (
			font_settings["default_fonts"], 
			font_settings["language_fonts"].copy(),
			font_settings["module_fonts"].copy(),
		)

		ansa = super(FontChoiceDialog, self).ShowModal()

		if ansa != wx.ID_OK:
			(font_settings["default_fonts"], 
			 font_settings["language_fonts"],			
			 font_settings["module_fonts"]) = old_fonts
		
		return ansa

class FontTree(LanguageModuleTree):
	def add_first_level_groups(self):
		self.model.add_child("Default Font", data=DefaultFont)
		super(FontTree, self).add_first_level_groups()
		self.data[DefaultFont] = []

if __name__ == '__main__':
	a=wx.App(0)
	FontChoiceDialog(None).ShowModal()

