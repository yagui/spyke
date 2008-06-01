#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.3 on Sat May 31 23:10:44 2008

import wx

# begin wxGlade: extracode
wx.ID_SPIKEWIN = wx.NewId()
wx.ID_CHARTWIN = wx.NewId()
wx.ID_LFPWIN = wx.NewId()
wx.ID_PYSHELL = wx.NewId()
wx.ID_TREF = wx.NewId()
wx.ID_VREF = wx.NewId()
wx.ID_CARET = wx.NewId()
# end wxGlade



class SpykeFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SpykeFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook = wx.Notebook(self, -1, style=0)
        self.validate_pane = wx.Panel(self.notebook, -1)
        self.rip_pane = wx.Panel(self.notebook, -1)
        self.sort_pane = wx.Panel(self.notebook, -1)
        self.detect_pane = wx.Panel(self.notebook, -1)
        self.threshold_sizer_staticbox = wx.StaticBox(self.detect_pane, -1, "Threshold")
        self.range_sizer_staticbox = wx.StaticBox(self.detect_pane, -1, "Range")
        self.lockout_sizer_staticbox = wx.StaticBox(self.detect_pane, -1, "Lockout")
        self.file_control_panel = wx.Panel(self, -1)
        
        # Menu Bar
        self.menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_NEW, "&New\tCtrl-N", "Create new collection", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_OPEN, "&Open\tCtrl-O", "Open .srf or .sort file", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_SAVE, "&Save\tCtrl-S", "Save collection", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_SAVEAS, "Save As", "Save collection as", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_CLOSE, "&Close\tCtrl-W", "Close .srf file", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_EXIT, "E&xit", "Exit", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, "&File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_SPIKEWIN, "Spike window", "Toggle spike window", wx.ITEM_CHECK)
        wxglade_tmp_menu.Append(wx.ID_CHARTWIN, "Chart window", "Toggle chart window", wx.ITEM_CHECK)
        wxglade_tmp_menu.Append(wx.ID_LFPWIN, "LFP window", "Toggle LFP window", wx.ITEM_CHECK)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_PYSHELL, "PyShell window", "Toggle PyShell window", wx.ITEM_CHECK)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_TREF, "Time ref", "Toggle vertical time reference", wx.ITEM_CHECK)
        wxglade_tmp_menu.Append(wx.ID_VREF, "Voltage ref", "Toggle horizontal voltage reference", wx.ITEM_CHECK)
        wxglade_tmp_menu.Append(wx.ID_CARET, "Caret", "Toggle shaded time window", wx.ITEM_CHECK)
        self.menubar.Append(wxglade_tmp_menu, "&View")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ABOUT, "&About...", "Show about window", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, "&Help")
        self.SetMenuBar(self.menubar)
        # Menu Bar end
        
        # Tool Bar
        self.toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL|wx.TB_FLAT)
        self.SetToolBar(self.toolbar)
        self.toolbar.AddLabelTool(wx.ID_NEW, "New", wx.Bitmap("res/new.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Create new collection", "Create new collection")
        self.toolbar.AddLabelTool(wx.ID_OPEN, "Open", wx.Bitmap("res/open.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Open .srf or .sort file", "Open .srf or .sort file")
        self.toolbar.AddLabelTool(wx.ID_CLOSE, "Close", wx.Bitmap("res/close.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Close .srf file", "Close .srf file")
        self.toolbar.AddLabelTool(wx.ID_SAVE, "Save", wx.Bitmap("res/save.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Save collection", "Save collection")
        self.toolbar.AddSeparator()
        self.toolbar.AddLabelTool(wx.ID_SPIKEWIN, "Spike", wx.Bitmap("res/spike.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, "Toggle spike window", "Toggle spike window")
        self.toolbar.AddLabelTool(wx.ID_CHARTWIN, "Chart", wx.Bitmap("res/chart.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, "Toggle chart window", "Toggle chart window")
        self.toolbar.AddLabelTool(wx.ID_LFPWIN, "LFP", wx.Bitmap("res/lfp.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, "Toggle LFP window", "Toggle LFP window")
        self.toolbar.AddSeparator()
        self.toolbar.AddLabelTool(wx.ID_PYSHELL, "PyShell", wx.Bitmap("res/blank.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, "Toggle PyShell window", "Toggle PyShell window")
        # Tool Bar end
        self.file_min_label = wx.StaticText(self.file_control_panel, -1, "file_min_label")
        self.file_spin_ctrl = wx.SpinCtrl(self.file_control_panel, -1, "", min=0, max=100)
        self.file_spin_ctrl_units = wx.StaticText(self.file_control_panel, -1, "us")
        self.file_max_label = wx.StaticText(self.file_control_panel, -1, "file_max_label")
        self.slider = wx.Slider(self.file_control_panel, -1, 0, 0, 10, style=wx.SL_HORIZONTAL|wx.SL_SELRANGE)
        self.play_backward_button = wx.ToggleButton(self.file_control_panel, -1, "<")
        self.play_forward_button = wx.ToggleButton(self.file_control_panel, -1, ">")
        self.pause_button = wx.ToggleButton(self.file_control_panel, -1, "||")
        self.stop_button = wx.Button(self.file_control_panel, -1, ".")
        self.page_left_button = wx.Button(self.file_control_panel, -1, "|<<")
        self.step_left_button = wx.Button(self.file_control_panel, -1, "|<")
        self.step_right_button = wx.Button(self.file_control_panel, -1, ">|")
        self.page_right_button = wx.Button(self.file_control_panel, -1, ">>|")
        self.algorithm_radio_box = wx.RadioBox(self.detect_pane, -1, "Algorithm", choices=["BipolarAmplitude", "MultiPhasic", "DynamicMultiPhasic"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.fixedthresh_radio_btn = wx.RadioButton(self.detect_pane, -1, "Fixed:")
        self.fixedthresh_spin_ctrl = wx.SpinCtrl(self.detect_pane, -1, "", min=0, max=100)
        self.fixedthresh_units_label = wx.StaticText(self.detect_pane, -1, "uV")
        self.dynamicthresh_radio_btn = wx.RadioButton(self.detect_pane, -1, "Dynamic:")
        self.noisemult_spin_ctrl = wx.SpinCtrl(self.detect_pane, -1, "", min=0, max=100)
        self.label_2 = wx.StaticText(self.detect_pane, -1, "*")
        self.noise_method_choice = wx.Choice(self.detect_pane, -1, choices=["median", "stdev"])
        self.range_start_combo_box = wx.ComboBox(self.detect_pane, -1, choices=["start", "now", "end"], style=wx.CB_DROPDOWN)
        self.label_5 = wx.StaticText(self.detect_pane, -1, "to")
        self.range_end_combo_box = wx.ComboBox(self.detect_pane, -1, choices=["end", "now", "start"], style=wx.CB_DROPDOWN)
        self.range_units_label = wx.StaticText(self.detect_pane, -1, "us")
        self.nspikes_label = wx.StaticText(self.detect_pane, -1, "nspikes:")
        self.nspikes_spin_ctrl = wx.SpinCtrl(self.detect_pane, -1, "", min=0, max=100)
        self.blocksize_label = wx.StaticText(self.detect_pane, -1, "blocksize:")
        self.blocksize_combo_box = wx.ComboBox(self.detect_pane, -1, choices=[], style=wx.CB_DROPDOWN)
        self.blocksize_units_label = wx.StaticText(self.detect_pane, -1, "us")
        self.spatial_label = wx.StaticText(self.detect_pane, -1, "Spatial:")
        self.slock_spin_ctrl = wx.SpinCtrl(self.detect_pane, -1, "", min=0, max=100)
        self.spatial_units_label = wx.StaticText(self.detect_pane, -1, "um")
        self.temporal_label = wx.StaticText(self.detect_pane, -1, "Temporal:")
        self.tlock_spin_ctrl = wx.SpinCtrl(self.detect_pane, -1, "", min=0, max=100)
        self.temporal_units_label = wx.StaticText(self.detect_pane, -1, "us")
        self.search_button = wx.Button(self.detect_pane, -1, "Search")
        self.clear_button = wx.Button(self.detect_pane, -1, "Clear")
        self.random_sample_checkbox = wx.CheckBox(self.detect_pane, -1, "random sample")
        self.label_3 = wx.StaticText(self.detect_pane, -1, "total nspikes:")
        self.total_nspikes_label = wx.StaticText(self.detect_pane, -1, "0")
        self.search_history_text_ctrl = wx.TextCtrl(self.detect_pane, -1, "", style=wx.TE_MULTILINE|wx.TE_READONLY)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnNew, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.OnOpen, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.OnSave, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, id=wx.ID_SAVEAS)
        self.Bind(wx.EVT_MENU, self.OnClose, id=wx.ID_CLOSE)
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnSpike, id=wx.ID_SPIKEWIN)
        self.Bind(wx.EVT_MENU, self.OnChart, id=wx.ID_CHARTWIN)
        self.Bind(wx.EVT_MENU, self.OnLFP, id=wx.ID_LFPWIN)
        self.Bind(wx.EVT_MENU, self.OnPyShell, id=wx.ID_PYSHELL)
        self.Bind(wx.EVT_MENU, self.OnTref, id=wx.ID_TREF)
        self.Bind(wx.EVT_MENU, self.OnVref, id=wx.ID_VREF)
        self.Bind(wx.EVT_MENU, self.OnCaret, id=wx.ID_CARET)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)
        self.Bind(wx.EVT_TOOL, self.OnNew, id=wx.ID_NEW)
        self.Bind(wx.EVT_TOOL, self.OnOpen, id=wx.ID_OPEN)
        self.Bind(wx.EVT_TOOL, self.OnClose, id=wx.ID_CLOSE)
        self.Bind(wx.EVT_TOOL, self.OnSave, id=wx.ID_SAVE)
        self.Bind(wx.EVT_TOOL, self.OnSpike, id=wx.ID_SPIKEWIN)
        self.Bind(wx.EVT_TOOL, self.OnChart, id=wx.ID_CHARTWIN)
        self.Bind(wx.EVT_TOOL, self.OnLFP, id=wx.ID_LFPWIN)
        self.Bind(wx.EVT_TOOL, self.OnPyShell, id=wx.ID_PYSHELL)
        self.Bind(wx.EVT_SPINCTRL, self.OnFileSpinCtrl, self.file_spin_ctrl)
        self.Bind(wx.EVT_RADIOBOX, self.OnAlgorithm, self.algorithm_radio_box)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnFixed, self.fixedthresh_radio_btn)
        self.Bind(wx.EVT_RADIOBUTTON, self.OnDynamic, self.dynamicthresh_radio_btn)
        self.Bind(wx.EVT_BUTTON, self.OnSearch, self.search_button)
        self.Bind(wx.EVT_BUTTON, self.OnClear, self.clear_button)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SpykeFrame.__set_properties
        self.SetTitle("spyke")
        self.SetSize((720, 320))
        self.toolbar.Realize()
        self.play_backward_button.SetMinSize((25, 25))
        self.play_backward_button.SetToolTipString("Toggle backward play")
        self.play_forward_button.SetMinSize((25, 25))
        self.play_forward_button.SetToolTipString("Toggle forward play")
        self.pause_button.SetMinSize((25, 25))
        self.pause_button.SetToolTipString("Toggle event detection")
        self.stop_button.SetMinSize((25, 25))
        self.stop_button.SetToolTipString("Stop")
        self.page_left_button.SetMinSize((25, 25))
        self.page_left_button.SetToolTipString("Page left")
        self.step_left_button.SetMinSize((25, 25))
        self.step_left_button.SetToolTipString("Step left")
        self.step_right_button.SetMinSize((25, 25))
        self.step_right_button.SetToolTipString("Step right")
        self.page_right_button.SetMinSize((25, 25))
        self.page_right_button.SetToolTipString("Page right")
        self.algorithm_radio_box.SetSelection(0)
        self.fixedthresh_radio_btn.SetValue(1)
        self.fixedthresh_spin_ctrl.SetMinSize((55, -1))
        self.noisemult_spin_ctrl.SetMinSize((45, -1))
        self.noise_method_choice.SetSelection(0)
        self.range_start_combo_box.SetMinSize((100, -1))
        self.range_start_combo_box.SetSelection(0)
        self.label_5.SetMinSize((15, -1))
        self.range_end_combo_box.SetMinSize((100, -1))
        self.range_end_combo_box.SetSelection(0)
        self.nspikes_spin_ctrl.SetMinSize((100, -1))
        self.blocksize_combo_box.SetMinSize((100, -1))
        self.slock_spin_ctrl.SetMinSize((60, -1))
        self.tlock_spin_ctrl.SetMinSize((60, -1))
        self.detect_pane.SetToolTipString("Event detection")
        self.sort_pane.SetToolTipString("Sort events into templates")
        self.sort_pane.Enable(False)
        self.rip_pane.SetToolTipString("Rip templates against file")
        self.rip_pane.Enable(False)
        self.validate_pane.SetToolTipString("Validate sorted spikes")
        self.validate_pane.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SpykeFrame.__do_layout
        spykeframe_sizer = wx.BoxSizer(wx.VERTICAL)
        validate_sizer = wx.BoxSizer(wx.HORIZONTAL)
        rip_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sort_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7_copy = wx.BoxSizer(wx.HORIZONTAL)
        detect_sizer = wx.BoxSizer(wx.HORIZONTAL)
        lockout_sizer = wx.StaticBoxSizer(self.lockout_sizer_staticbox, wx.HORIZONTAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 3, 0, 0)
        range_sizer = wx.StaticBoxSizer(self.range_sizer_staticbox, wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_11 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        sizer_16_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_17 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_15 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_14 = wx.BoxSizer(wx.HORIZONTAL)
        threshold_sizer = wx.StaticBoxSizer(self.threshold_sizer_staticbox, wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        file_control_sizer = wx.BoxSizer(wx.VERTICAL)
        file_control_buttons_sizer = wx.BoxSizer(wx.HORIZONTAL)
        slider_sizer = wx.BoxSizer(wx.VERTICAL)
        file_spin_ctrl_sizer = wx.GridSizer(1, 3, 0, 0)
        file_spin_ctrl_and_label_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file_spin_ctrl_sizer.Add(self.file_min_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 1)
        file_spin_ctrl_and_label_sizer.Add(self.file_spin_ctrl, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        file_spin_ctrl_and_label_sizer.Add(self.file_spin_ctrl_units, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        file_spin_ctrl_sizer.Add(file_spin_ctrl_and_label_sizer, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        file_spin_ctrl_sizer.Add(self.file_max_label, 0, wx.RIGHT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 1)
        slider_sizer.Add(file_spin_ctrl_sizer, 1, wx.EXPAND, 0)
        file_control_sizer.Add(slider_sizer, 1, wx.EXPAND, 0)
        file_control_sizer.Add(self.slider, 0, wx.EXPAND, 0)
        file_control_buttons_sizer.Add(self.play_backward_button, 0, 0, 0)
        file_control_buttons_sizer.Add(self.play_forward_button, 0, 0, 0)
        file_control_buttons_sizer.Add(self.pause_button, 0, 0, 0)
        file_control_buttons_sizer.Add(self.stop_button, 0, 0, 0)
        file_control_buttons_sizer.Add((15, 25), 0, 0, 0)
        file_control_buttons_sizer.Add(self.page_left_button, 0, 0, 0)
        file_control_buttons_sizer.Add(self.step_left_button, 0, 0, 0)
        file_control_buttons_sizer.Add(self.step_right_button, 0, 0, 0)
        file_control_buttons_sizer.Add(self.page_right_button, 0, 0, 0)
        file_control_sizer.Add(file_control_buttons_sizer, 1, 0, 0)
        self.file_control_panel.SetSizer(file_control_sizer)
        spykeframe_sizer.Add(self.file_control_panel, 0, wx.EXPAND, 1)
        detect_sizer.Add(self.algorithm_radio_box, 0, wx.EXPAND, 0)
        sizer_3.Add(self.fixedthresh_radio_btn, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(self.fixedthresh_spin_ctrl, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(self.fixedthresh_units_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_3.Add(sizer_4, 1, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 1)
        threshold_sizer.Add(sizer_3, 0, 0, 0)
        threshold_sizer.Add((0, 4), 0, 0, 0)
        sizer_5.Add(self.dynamicthresh_radio_btn, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_6_copy.Add(self.noisemult_spin_ctrl, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_6_copy.Add(self.label_2, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_6_copy.Add(self.noise_method_choice, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(sizer_6_copy, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        threshold_sizer.Add(sizer_5, 0, 0, 0)
        detect_sizer.Add(threshold_sizer, 0, wx.EXPAND, 0)
        sizer_14.Add(self.range_start_combo_box, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_14.Add(self.label_5, 1, wx.LEFT|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_14.Add(self.range_end_combo_box, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_14.Add(self.range_units_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        range_sizer.Add(sizer_14, 0, 0, 0)
        sizer_15.Add(self.nspikes_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_12.Add(sizer_15, 1, 0, 0)
        sizer_17.Add(self.nspikes_spin_ctrl, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_12.Add(sizer_17, 1, 0, 0)
        sizer_11.Add(sizer_12, 1, 0, 0)
        sizer_16.Add(self.blocksize_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_13.Add(sizer_16, 1, 0, 0)
        sizer_16_copy.Add(self.blocksize_combo_box, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_16_copy.Add(self.blocksize_units_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_13.Add(sizer_16_copy, 1, 0, 0)
        sizer_11.Add(sizer_13, 1, 0, 0)
        sizer_10.Add(sizer_11, 1, 0, 0)
        range_sizer.Add(sizer_10, 0, 0, 0)
        detect_sizer.Add(range_sizer, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.spatial_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.slock_spin_ctrl, 0, 0, 0)
        grid_sizer_1.Add(self.spatial_units_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.temporal_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.tlock_spin_ctrl, 0, wx.TOP, 4)
        grid_sizer_1.Add(self.temporal_units_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        lockout_sizer.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        detect_sizer.Add(lockout_sizer, 1, wx.EXPAND, 0)
        sizer_6.Add(detect_sizer, 0, wx.EXPAND, 0)
        sizer_7_copy.Add(self.search_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_7_copy.Add(self.clear_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_7_copy.Add(self.random_sample_checkbox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_8.Add(sizer_7_copy, 0, 0, 0)
        sizer_9.Add(self.label_3, 0, wx.ALL, 4)
        sizer_9.Add(self.total_nspikes_label, 0, wx.TOP, 4)
        sizer_8.Add(sizer_9, 0, 0, 0)
        sizer_7.Add(sizer_8, 0, 0, 0)
        sizer_7.Add(self.search_history_text_ctrl, 1, wx.EXPAND, 0)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        self.detect_pane.SetSizer(sizer_6)
        self.sort_pane.SetSizer(sort_sizer)
        self.rip_pane.SetSizer(rip_sizer)
        self.validate_pane.SetSizer(validate_sizer)
        self.notebook.AddPage(self.detect_pane, "Detect")
        self.notebook.AddPage(self.sort_pane, "Sort")
        self.notebook.AddPage(self.rip_pane, "Rip")
        self.notebook.AddPage(self.validate_pane, "Validate")
        spykeframe_sizer.Add(self.notebook, 1, wx.EXPAND, 0)
        self.SetSizer(spykeframe_sizer)
        self.Layout()
        # end wxGlade

    def OnNew(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnNew' not implemented!"
        event.Skip()

    def OnOpen(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnOpen' not implemented!"
        event.Skip()

    def OnSave(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnSave' not implemented!"
        event.Skip()

    def OnSaveAs(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnSaveAs' not implemented!"
        event.Skip()

    def OnClose(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnClose' not implemented!"
        event.Skip()

    def OnExit(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnExit' not implemented!"
        event.Skip()

    def OnSpike(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnSpike' not implemented!"
        event.Skip()

    def OnChart(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnChart' not implemented!"
        event.Skip()

    def OnLFP(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnLFP' not implemented!"
        event.Skip()

    def OnPyShell(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnPyShell' not implemented!"
        event.Skip()

    def OnTref(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnTref' not implemented!"
        event.Skip()

    def OnVref(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnVref' not implemented!"
        event.Skip()

    def OnCaret(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnCaret' not implemented!"
        event.Skip()

    def OnAbout(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnAbout' not implemented!"
        event.Skip()

    def OnFileSpinCtrl(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnFileSpinCtrl' not implemented!"
        event.Skip()

    def OnAlgorithm(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnAlgorithm' not implemented!"
        event.Skip()

    def OnFixed(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnFixed' not implemented!"
        event.Skip()

    def OnDynamic(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnDynamic' not implemented!"
        event.Skip()

    def OnSearch(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnSearch' not implemented!"
        event.Skip()

    def OnClear(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnClear' not implemented!"
        event.Skip()

# end of class SpykeFrame


class DataFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: DataFrame.__init__
        kwds["style"] = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.SYSTEM_MENU|wx.RESIZE_BORDER|wx.FRAME_TOOL_WINDOW|wx.FRAME_NO_TASKBAR|wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: DataFrame.__set_properties
        self.SetTitle("data window")
        self.SetSize((175, 675))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: DataFrame.__do_layout
        dataframe_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(dataframe_sizer)
        self.Layout()
        # end wxGlade

# end of class DataFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    spykeframe = SpykeFrame(None, -1, "")
    app.SetTopWindow(spykeframe)
    spykeframe.Show()
    app.MainLoop()
