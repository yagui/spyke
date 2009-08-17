#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade HG on Mon Aug 17 10:39:34 2009

import wx

# begin wxGlade: extracode
from spyke.core import SpykeListCtrl, SpykeVirtualListCtrl, SpykeTreeCtrl
wx.ID_SAVEPARSE = wx.NewId()
wx.ID_SAVERESAMPLE = wx.NewId()
wx.ID_SAVEWAVES = wx.NewId()
wx.ID_SPIKEWIN = wx.NewId()
wx.ID_CHARTWIN = wx.NewId()
wx.ID_LFPWIN = wx.NewId()
wx.ID_SORTWIN = wx.NewId()
wx.ID_PYSHELL = wx.NewId()
wx.ID_WAVEFORMS = wx.NewId()
wx.ID_RASTERS = wx.NewId()
wx.ID_TREF = wx.NewId()
wx.ID_VREF = wx.NewId()
wx.ID_CARET = wx.NewId()
wx.ID_SAMPLING = wx.NewId()
wx.ID_25 = wx.NewId()
wx.ID_50 = wx.NewId()
wx.ID_100 = wx.NewId()
wx.ID_SHCORRECT = wx.NewId()
wx.ID_SORT_TREE = wx.NewId()
wx.ID_MATCH_TEMPLATE = wx.NewId()
from plot import SpikeSortPanel
#from plot import ChartSortPanel # unimplemented
# end wxGlade



class SpykeFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SpykeFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.notebook = wx.Notebook(self, -1, style=0)
        self.extract_pane = wx.Panel(self.notebook, -1)
        self.detect_pane = wx.Panel(self.notebook, -1)
        self.threshold_sizer_staticbox = wx.StaticBox(self.detect_pane, -1, "Threshold")
        self.range_sizer_staticbox = wx.StaticBox(self.detect_pane, -1, "Range")
        self.lockout_sizer_staticbox = wx.StaticBox(self.detect_pane, -1, "Lockout")
        self.file_pos_control_panel = wx.Panel(self, -1)
        
        # Menu Bar
        self.menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_NEW, "&New\tCtrl-N", "Create new sort session", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_OPEN, "&Open\tCtrl-O", "Open .srf or .sort file", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_SAVEPARSE, "Save .parse", "Save parse file with current channel selection", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_SAVERESAMPLE, "Save .resample", "Save all highpass data to contiguous .resample file with current sampling settings, for faster future access", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_SAVE, "&Save .sort\tCtrl-S", "Save sort session", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_SAVEAS, "Save .sort As", "Save sort session as", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_SAVEWAVES, "Save waves in .sort", "Save spike waveforms when saving to .sort file", wx.ITEM_CHECK)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_CLOSE, "&Close\tCtrl-W", "Close .srf file", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(wx.ID_EXIT, "E&xit", "Exit", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, "&File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_SPIKEWIN, "Spike window", "Toggle spike window", wx.ITEM_CHECK)
        wxglade_tmp_menu.Append(wx.ID_CHARTWIN, "Chart window", "Toggle chart window", wx.ITEM_CHECK)
        wxglade_tmp_menu.Append(wx.ID_LFPWIN, "LFP window", "Toggle LFP window", wx.ITEM_CHECK)
        wxglade_tmp_menu.Append(wx.ID_SORTWIN, "Sort window", "Toggle sort window", wx.ITEM_CHECK)
        wxglade_tmp_menu.Append(wx.ID_PYSHELL, "PyShell window", "Toggle PyShell window", wx.ITEM_CHECK)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.ID_WAVEFORMS, "Waveforms", "Toggle waveforms", wx.ITEM_CHECK)
        wxglade_tmp_menu.Append(wx.ID_RASTERS, "Rasters", "Toggle spike rasters", wx.ITEM_CHECK)
        wxglade_tmp_menu.Append(wx.ID_TREF, "Time ref", "Toggle vertical time reference", wx.ITEM_CHECK)
        wxglade_tmp_menu.Append(wx.ID_VREF, "Voltage ref", "Toggle horizontal voltage reference", wx.ITEM_CHECK)
        wxglade_tmp_menu.Append(wx.ID_CARET, "Caret", "Toggle shaded time window", wx.ITEM_CHECK)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu_sub = wx.Menu()
        wxglade_tmp_menu_sub.Append(wx.ID_25, "25 kHz", "", wx.ITEM_RADIO)
        wxglade_tmp_menu_sub.Append(wx.ID_50, "50 kHz", "", wx.ITEM_RADIO)
        wxglade_tmp_menu_sub.Append(wx.ID_100, "100 kHz", "", wx.ITEM_RADIO)
        wxglade_tmp_menu_sub.AppendSeparator()
        wxglade_tmp_menu_sub.Append(wx.ID_SHCORRECT, "Sample && hold correct", "Enable per-channel sample & hold delay correction", wx.ITEM_CHECK)
        wxglade_tmp_menu.AppendMenu(wx.ID_SAMPLING, "Sampling", wxglade_tmp_menu_sub, "")
        self.menubar.Append(wxglade_tmp_menu, "&View")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ABOUT, "&About...", "Show about window", wx.ITEM_NORMAL)
        self.menubar.Append(wxglade_tmp_menu, "&Help")
        self.SetMenuBar(self.menubar)
        # Menu Bar end
        
        # Tool Bar
        self.toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL|wx.TB_FLAT)
        self.SetToolBar(self.toolbar)
        self.toolbar.AddLabelTool(wx.ID_NEW, "New", wx.Bitmap("res/new.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Create new sort session", "Create new sort session")
        self.toolbar.AddLabelTool(wx.ID_OPEN, "Open", wx.Bitmap("res/open.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Open .srf or .sort file", "Open .srf or .sort file")
        self.toolbar.AddLabelTool(wx.ID_CLOSE, "Close", wx.Bitmap("res/close.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Close .srf file", "Close .srf file")
        self.toolbar.AddLabelTool(wx.ID_SAVE, "Save", wx.Bitmap("res/save.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "Save sort session", "Save sort session")
        self.toolbar.AddSeparator()
        self.toolbar.AddLabelTool(wx.ID_SPIKEWIN, "Spike", wx.Bitmap("res/spike.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, "Toggle spike window", "Toggle spike window")
        self.toolbar.AddLabelTool(wx.ID_CHARTWIN, "Chart", wx.Bitmap("res/chart.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, "Toggle chart window", "Toggle chart window")
        self.toolbar.AddLabelTool(wx.ID_LFPWIN, "LFP", wx.Bitmap("res/lfp.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, "Toggle LFP window", "Toggle LFP window")
        self.toolbar.AddSeparator()
        self.toolbar.AddLabelTool(wx.ID_SORTWIN, "Sort", wx.Bitmap("res/sort.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, "Toggle sort window", "Toggle sort window")
        self.toolbar.AddSeparator()
        self.toolbar.AddLabelTool(wx.ID_PYSHELL, "PyShell", wx.Bitmap("res/pyshell.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_CHECK, "Toggle PyShell window", "Toggle PyShell window")
        # Tool Bar end
        self.file_min_label = wx.StaticText(self.file_pos_control_panel, -1, "file_min_label")
        self.file_pos_combo_box = wx.ComboBox(self.file_pos_control_panel, -1, choices=["start", "end"], style=wx.CB_DROPDOWN)
        self.file_pos_combo_box_units_label = wx.StaticText(self.file_pos_control_panel, -1, "us")
        self.file_max_label = wx.StaticText(self.file_pos_control_panel, -1, "file_max_label")
        self.slider = wx.Slider(self.file_pos_control_panel, -1, 0, 0, 10, style=wx.SL_HORIZONTAL|wx.SL_SELRANGE)
        self.globalfixedthresh_radio_btn = wx.RadioButton(self.detect_pane, -1, "GlobalFixed:")
        self.fixedthresh_spin_ctrl = wx.SpinCtrl(self.detect_pane, -1, "", min=0, max=100)
        self.fixedthresh_units_label = wx.StaticText(self.detect_pane, -1, "uV")
        self.chanfixedthresh_radio_btn = wx.RadioButton(self.detect_pane, -1, "ChanFixed;")
        self.dynamicthresh_radio_btn = wx.RadioButton(self.detect_pane, -1, "Dynamic:")
        self.noisemult_text_ctrl = wx.TextCtrl(self.detect_pane, -1, "", style=wx.TE_CENTRE)
        self.label_2 = wx.StaticText(self.detect_pane, -1, "*")
        self.noise_method_choice = wx.Choice(self.detect_pane, -1, choices=["median", "stdev"])
        self.Vpp_label = wx.StaticText(self.detect_pane, -1, "Vpp >= ")
        self.ppthreshmult_text_ctrl = wx.TextCtrl(self.detect_pane, -1, "", style=wx.TE_CENTRE)
        self.Vp_label = wx.StaticText(self.detect_pane, -1, "* thresh; ")
        self.dt_label = wx.StaticText(self.detect_pane, -1, "phase dt <= ")
        self.dt_spin_ctrl = wx.SpinCtrl(self.detect_pane, -1, "", min=0, max=100)
        self.dt_units_label = wx.StaticText(self.detect_pane, -1, "us")
        self.range_start_combo_box = wx.ComboBox(self.detect_pane, -1, choices=["start", "now", "end"], style=wx.CB_DROPDOWN)
        self.label_5 = wx.StaticText(self.detect_pane, -1, "to")
        self.range_end_combo_box = wx.ComboBox(self.detect_pane, -1, choices=["end", "now", "start"], style=wx.CB_DROPDOWN)
        self.range_units_label = wx.StaticText(self.detect_pane, -1, "us")
        self.nspikes_label = wx.StaticText(self.detect_pane, -1, "nspikes:")
        self.blocksize_label = wx.StaticText(self.detect_pane, -1, "blocksize:")
        self.nspikes_spin_ctrl = wx.SpinCtrl(self.detect_pane, -1, "", min=0, max=100)
        self.blocksize_combo_box = wx.ComboBox(self.detect_pane, -1, choices=[], style=wx.CB_DROPDOWN)
        self.blocksize_units_label = wx.StaticText(self.detect_pane, -1, "us")
        self.spatial_label = wx.StaticText(self.detect_pane, -1, "Spatial:")
        self.slock_spin_ctrl = wx.SpinCtrl(self.detect_pane, -1, "", min=0, max=100)
        self.spatial_units_label = wx.StaticText(self.detect_pane, -1, "um")
        self.detect_button = wx.Button(self.detect_pane, -1, "Detect")
        self.random_sample_checkbox = wx.CheckBox(self.detect_pane, -1, "random sample")
        self.label_3 = wx.StaticText(self.detect_pane, -1, "total nspikes:")
        self.total_nspikes_label = wx.StaticText(self.detect_pane, -1, "0")
        self.detection_list = SpykeListCtrl(self.detect_pane, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.extract_radio_box = wx.RadioBox(self.extract_pane, -1, "X-Y localization", choices=["Spatial mean", "Gaussian fit"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.extract_button = wx.Button(self.extract_pane, -1, "Extract")
        self.sort_pane = wx.Panel(self.notebook, -1)
        self.validate_pane = wx.Panel(self.notebook, -1)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.OnNew, id=wx.ID_NEW)
        self.Bind(wx.EVT_MENU, self.OnOpen, id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU, self.OnSaveParse, id=wx.ID_SAVEPARSE)
        self.Bind(wx.EVT_MENU, self.OnSaveResample, id=wx.ID_SAVERESAMPLE)
        self.Bind(wx.EVT_MENU, self.OnSave, id=wx.ID_SAVE)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, id=wx.ID_SAVEAS)
        self.Bind(wx.EVT_MENU, self.OnClose, id=wx.ID_CLOSE)
        self.Bind(wx.EVT_MENU, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnSpike, id=wx.ID_SPIKEWIN)
        self.Bind(wx.EVT_MENU, self.OnChart, id=wx.ID_CHARTWIN)
        self.Bind(wx.EVT_MENU, self.OnLFP, id=wx.ID_LFPWIN)
        self.Bind(wx.EVT_MENU, self.OnSort, id=wx.ID_SORTWIN)
        self.Bind(wx.EVT_MENU, self.OnPyShell, id=wx.ID_PYSHELL)
        self.Bind(wx.EVT_MENU, self.OnWaveforms, id=wx.ID_WAVEFORMS)
        self.Bind(wx.EVT_MENU, self.OnRasters, id=wx.ID_RASTERS)
        self.Bind(wx.EVT_MENU, self.OnTref, id=wx.ID_TREF)
        self.Bind(wx.EVT_MENU, self.OnVref, id=wx.ID_VREF)
        self.Bind(wx.EVT_MENU, self.OnCaret, id=wx.ID_CARET)
        self.Bind(wx.EVT_MENU, self.OnSampling, id=wx.ID_25)
        self.Bind(wx.EVT_MENU, self.OnSampling, id=wx.ID_50)
        self.Bind(wx.EVT_MENU, self.OnSampling, id=wx.ID_100)
        self.Bind(wx.EVT_MENU, self.OnSHCorrect, id=wx.ID_SHCORRECT)
        self.Bind(wx.EVT_MENU, self.OnAbout, id=wx.ID_ABOUT)
        self.Bind(wx.EVT_TOOL, self.OnNew, id=wx.ID_NEW)
        self.Bind(wx.EVT_TOOL, self.OnOpen, id=wx.ID_OPEN)
        self.Bind(wx.EVT_TOOL, self.OnClose, id=wx.ID_CLOSE)
        self.Bind(wx.EVT_TOOL, self.OnSave, id=wx.ID_SAVE)
        self.Bind(wx.EVT_TOOL, self.OnSpike, id=wx.ID_SPIKEWIN)
        self.Bind(wx.EVT_TOOL, self.OnChart, id=wx.ID_CHARTWIN)
        self.Bind(wx.EVT_TOOL, self.OnLFP, id=wx.ID_LFPWIN)
        self.Bind(wx.EVT_TOOL, self.OnSort, id=wx.ID_SORTWIN)
        self.Bind(wx.EVT_TOOL, self.OnPyShell, id=wx.ID_PYSHELL)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnFilePosComboBox, self.file_pos_combo_box)
        self.Bind(wx.EVT_COMBOBOX, self.OnFilePosComboBox, self.file_pos_combo_box)
        self.Bind(wx.EVT_BUTTON, self.OnDetect, self.detect_button)
        self.Bind(wx.EVT_BUTTON, self.OnExtract, self.extract_button)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SpykeFrame.__set_properties
        self.SetTitle("spyke")
        self.SetSize((690, 320))
        self.toolbar.Realize()
        self.file_pos_combo_box.SetMinSize((100, -1))
        self.file_pos_combo_box.SetWindowStyle(wx.TE_PROCESS_ENTER)
        self.file_pos_combo_box.SetSelection(-1)
        self.globalfixedthresh_radio_btn.SetValue(1)
        self.fixedthresh_spin_ctrl.SetMinSize((55, -1))
        self.noisemult_text_ctrl.SetMinSize((35, -1))
        self.noise_method_choice.SetSelection(0)
        self.ppthreshmult_text_ctrl.SetMinSize((35, -1))
        self.dt_spin_ctrl.SetMinSize((50, -1))
        self.range_start_combo_box.SetMinSize((90, -1))
        self.range_start_combo_box.SetSelection(0)
        self.label_5.SetMinSize((-1, -1))
        self.range_end_combo_box.SetMinSize((90, -1))
        self.range_end_combo_box.SetSelection(0)
        self.nspikes_spin_ctrl.SetMinSize((90, -1))
        self.blocksize_combo_box.SetMinSize((90, -1))
        self.slock_spin_ctrl.SetMinSize((60, -1))
        self.detect_button.SetToolTipString("Creates a new detection run")
        self.detection_list.SetToolTipString("List of detection runs")
        self.detect_pane.SetToolTipString("Event detection")
        self.extract_radio_box.SetSelection(0)
        self.extract_pane.SetToolTipString("Sort events into templates")
        self.extract_pane.Enable(False)
        self.sort_pane.SetToolTipString("Validate sorted spikes")
        self.sort_pane.Enable(False)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SpykeFrame.__do_layout
        spykeframe_sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        detect_sizer = wx.BoxSizer(wx.HORIZONTAL)
        lockout_sizer = wx.StaticBoxSizer(self.lockout_sizer_staticbox, wx.HORIZONTAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 3, 0, 0)
        range_sizer = wx.StaticBoxSizer(self.range_sizer_staticbox, wx.HORIZONTAL)
        range_flexgrid_sizer = wx.FlexGridSizer(3, 4, 0, 0)
        threshold_sizer = wx.StaticBoxSizer(self.threshold_sizer_staticbox, wx.VERTICAL)
        sizer_10_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        file_pos_control_panel_sizer = wx.BoxSizer(wx.VERTICAL)
        slider_sizer = wx.BoxSizer(wx.VERTICAL)
        file_pos_sizer = wx.GridSizer(1, 3, 0, 0)
        file_pos_combo_box_sizer = wx.BoxSizer(wx.HORIZONTAL)
        file_pos_sizer.Add(self.file_min_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 1)
        file_pos_combo_box_sizer.Add(self.file_pos_combo_box, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        file_pos_combo_box_sizer.Add(self.file_pos_combo_box_units_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        file_pos_sizer.Add(file_pos_combo_box_sizer, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        file_pos_sizer.Add(self.file_max_label, 0, wx.RIGHT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 1)
        slider_sizer.Add(file_pos_sizer, 1, wx.EXPAND, 0)
        file_pos_control_panel_sizer.Add(slider_sizer, 1, wx.EXPAND, 0)
        file_pos_control_panel_sizer.Add(self.slider, 0, wx.EXPAND, 0)
        self.file_pos_control_panel.SetSizer(file_pos_control_panel_sizer)
        spykeframe_sizer.Add(self.file_pos_control_panel, 0, wx.EXPAND, 1)
        sizer_3.Add(self.globalfixedthresh_radio_btn, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(self.fixedthresh_spin_ctrl, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(self.fixedthresh_units_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_3.Add(sizer_4, 1, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 1)
        threshold_sizer.Add(sizer_3, 0, 0, 0)
        threshold_sizer.Add((0, 4), 0, 0, 0)
        sizer_5.Add(self.chanfixedthresh_radio_btn, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(self.dynamicthresh_radio_btn, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 2)
        sizer_6_copy.Add(self.noisemult_text_ctrl, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_6_copy.Add(self.label_2, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_6_copy.Add(self.noise_method_choice, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_5.Add(sizer_6_copy, 1, wx.ALIGN_CENTER_VERTICAL, 0)
        threshold_sizer.Add(sizer_5, 0, 0, 0)
        sizer_10_copy.Add(self.Vpp_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_10_copy.Add(self.ppthreshmult_text_ctrl, 0, 0, 0)
        sizer_10_copy.Add(self.Vp_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_10_copy.Add(self.dt_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_10_copy.Add(self.dt_spin_ctrl, 0, 0, 0)
        sizer_10_copy.Add(self.dt_units_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        threshold_sizer.Add(sizer_10_copy, 1, wx.EXPAND, 0)
        detect_sizer.Add(threshold_sizer, 0, wx.EXPAND, 0)
        range_flexgrid_sizer.Add(self.range_start_combo_box, 0, 0, 0)
        range_flexgrid_sizer.Add(self.label_5, 1, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        range_flexgrid_sizer.Add(self.range_end_combo_box, 0, 0, 0)
        range_flexgrid_sizer.Add(self.range_units_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        range_flexgrid_sizer.Add(self.nspikes_label, 0, wx.TOP|wx.ALIGN_CENTER_VERTICAL, 4)
        range_flexgrid_sizer.Add((1, 1), 0, 0, 0)
        range_flexgrid_sizer.Add(self.blocksize_label, 0, wx.TOP|wx.ALIGN_CENTER_VERTICAL, 4)
        range_flexgrid_sizer.Add((1, 1), 0, 0, 0)
        range_flexgrid_sizer.Add(self.nspikes_spin_ctrl, 0, wx.TOP, 4)
        range_flexgrid_sizer.Add((1, 1), 0, 0, 0)
        range_flexgrid_sizer.Add(self.blocksize_combo_box, 0, wx.TOP, 4)
        range_flexgrid_sizer.Add(self.blocksize_units_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        range_sizer.Add(range_flexgrid_sizer, 0, 0, 0)
        detect_sizer.Add(range_sizer, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.spatial_label, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.slock_spin_ctrl, 0, 0, 0)
        grid_sizer_1.Add(self.spatial_units_label, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5)
        lockout_sizer.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        detect_sizer.Add(lockout_sizer, 0, wx.EXPAND, 0)
        sizer_6.Add(detect_sizer, 0, wx.EXPAND, 0)
        sizer_8.Add(self.detect_button, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_8.Add(self.random_sample_checkbox, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 4)
        sizer_1.Add(self.label_3, 0, wx.ALL, 4)
        sizer_1.Add(self.total_nspikes_label, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        sizer_8.Add(sizer_1, 1, wx.EXPAND, 0)
        sizer_7.Add(sizer_8, 0, 0, 0)
        sizer_7.Add(self.detection_list, 1, wx.EXPAND, 0)
        sizer_6.Add(sizer_7, 1, wx.EXPAND, 0)
        self.detect_pane.SetSizer(sizer_6)
        sizer_9.Add(self.extract_radio_box, 0, 0, 0)
        sizer_2.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_10.Add(self.extract_button, 0, 0, 0)
        sizer_2.Add(sizer_10, 1, wx.EXPAND, 0)
        self.extract_pane.SetSizer(sizer_2)
        self.notebook.AddPage(self.detect_pane, "Detect")
        self.notebook.AddPage(self.extract_pane, "Extract")
        self.notebook.AddPage(self.sort_pane, "Sort")
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

    def OnSaveParse(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnSaveParse' not implemented!"
        event.Skip()

    def OnSaveResample(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnSaveResample' not implemented!"
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

    def OnSort(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnSort' not implemented!"
        event.Skip()

    def OnPyShell(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnPyShell' not implemented!"
        event.Skip()

    def OnWaveforms(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnWaveforms' not implemented!"
        event.Skip()

    def OnRasters(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnRasters' not implemented!"
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

    def OnSampling(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnSampling' not implemented!"
        event.Skip()

    def OnSHCorrect(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnSHCorrect' not implemented!"
        event.Skip()

    def OnAbout(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnAbout' not implemented!"
        event.Skip()

    def OnFilePosComboBox(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnFilePosComboBox' not implemented!"
        event.Skip()

    def OnDetect(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnDetect' not implemented!"
        event.Skip()

    def OnExtract(self, event): # wxGlade: SpykeFrame.<event_handler>
        print "Event handler `OnExtract' not implemented!"
        event.Skip()

# end of class SpykeFrame


class DataFrame(wx.MiniFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: DataFrame.__init__
        kwds["style"] = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.SYSTEM_MENU|wx.RESIZE_BORDER|wx.FRAME_TOOL_WINDOW|wx.FRAME_NO_TASKBAR|wx.CLIP_CHILDREN
        wx.MiniFrame.__init__(self, *args, **kwds)

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


class SortFrame(wx.MiniFrame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SortFrame.__init__
        kwds["style"] = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.SYSTEM_MENU|wx.RESIZE_BORDER|wx.FRAME_TOOL_WINDOW|wx.FRAME_NO_TASKBAR|wx.CLIP_CHILDREN
        wx.MiniFrame.__init__(self, *args, **kwds)
        self.splitter = wx.SplitterWindow(self, -1, style=wx.SP_3DSASH)
        self.plot_pane = wx.Panel(self.splitter, -1)
        self.sort_splitter = wx.SplitterWindow(self.splitter, -1, style=wx.SP_3DSASH)
        
        # Tool Bar
        self.toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL|wx.TB_FLAT|wx.TB_TEXT|wx.TB_NOICONS|wx.TB_HORZ_LAYOUT|wx.TB_HORZ_TEXT)
        self.SetToolBar(self.toolbar)
        self.toolbar.AddLabelTool(wx.ID_SORT_TREE, "Sort tree", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, "Renumber and spatially sort templates in tree", "")
        self.toolbar.AddLabelTool(wx.ID_MATCH_TEMPLATE, "Match template", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, "Match all events in event list against currently selected template, populate err column", "")
        # Tool Bar end
        self.tree = SpykeTreeCtrl(self.sort_splitter, -1, style=wx.TR_HAS_BUTTONS|wx.TR_LINES_AT_ROOT|wx.TR_MULTIPLE|wx.TR_HIDE_ROOT|wx.TR_MULTIPLE|wx.TR_DEFAULT_STYLE|wx.NO_BORDER|wx.WANTS_CHARS)
        self.list = SpykeVirtualListCtrl(self.sort_splitter, -1, style=wx.LC_REPORT|wx.LC_VIRTUAL|wx.NO_BORDER|wx.WANTS_CHARS)
        self.spikesortpanel = SpikeSortPanel(self.plot_pane, -1)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TOOL, self.OnSortTree, id=wx.ID_SORT_TREE)
        self.Bind(wx.EVT_TOOL, self.OnMatchTemplate, id=wx.ID_MATCH_TEMPLATE)
        self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnListDeselect, self.list)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnListSelect, self.list)
        self.Bind(wx.EVT_LIST_COL_CLICK, self.OnListColClick, self.list)
        self.Bind(wx.EVT_SPLITTER_SASH_POS_CHANGED, self.OnSplitterSashChanged, self.splitter)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SortFrame.__set_properties
        self.SetTitle("sort window")
        self.toolbar.Realize()
        self.spikesortpanel.SetMinSize((160, 670))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SortFrame.__do_layout
        sortframe_sizer = wx.BoxSizer(wx.VERTICAL)
        plot_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sort_splitter.SplitVertically(self.tree, self.list, 117)
        plot_sizer.Add(self.spikesortpanel, 1, wx.EXPAND, 0)
        self.plot_pane.SetSizer(plot_sizer)
        self.splitter.SplitVertically(self.sort_splitter, self.plot_pane, 300)
        sortframe_sizer.Add(self.splitter, 2, wx.EXPAND, 0)
        self.SetSizer(sortframe_sizer)
        sortframe_sizer.Fit(self)
        self.Layout()
        # end wxGlade

    def OnSortTree(self, event): # wxGlade: SortFrame.<event_handler>
        print "Event handler `OnSortTree' not implemented!"
        event.Skip()

    def OnMatchTemplate(self, event): # wxGlade: SortFrame.<event_handler>
        print "Event handler `OnMatchTemplate' not implemented!"
        event.Skip()

    def OnListDeselect(self, event): # wxGlade: SortFrame.<event_handler>
        print "Event handler `OnListDeselect' not implemented!"
        event.Skip()

    def OnListSelect(self, event): # wxGlade: SortFrame.<event_handler>
        print "Event handler `OnListSelect' not implemented!"
        event.Skip()

    def OnListColClick(self, event): # wxGlade: SortFrame.<event_handler>
        print "Event handler `OnListColClick' not implemented!"
        event.Skip()

    def OnSplitterSashChanged(self, event): # wxGlade: SortFrame.<event_handler>
        print "Event handler `OnSplitterSashChanged' not implemented!"
        event.Skip()

# end of class SortFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    spykeframe = SpykeFrame(None, -1, "")
    app.SetTopWindow(spykeframe)
    spykeframe.Show()
    app.MainLoop()
