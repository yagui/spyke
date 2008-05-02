"""Main spyke window"""

import wx
import wx.html
import cPickle
import os

import spyke
from spyke import core, surf, probes
import plot
import wxglade_gui


class SpykeFrame(wxglade_gui.SpykeFrame):
    """spyke's main frame, inherits gui layout code auto-generated by wxGlade"""

    DEFAULTDIR = '/data/ptc15'

    def __init__(self, *args, **kwargs):
        wxglade_gui.SpykeFrame.__init__(self, *args, **kwargs)
        self.surffname = ""
        self.sortfname = ""
        self.frames = {} # holds spike, chart, and lfp frames
        self.spiketw = 1000 # spike frame temporal window width (us)
        self.charttw = 50000 # chart frame temporal window width (us)

        self.Bind(wx.EVT_CLOSE, self.OnExit)
        self.Bind(wx.EVT_ICONIZE, self.OnIconize)
        self.Bind(wx.EVT_ACTIVATE, self.OnActivate)

        # TODO: load recent file history and add it to menu (see wxGlade code that uses wx.FileHistory)

        #self.OpenSurfFile(self.DEFAULTDIR + '/87 - track 7c spontaneous craziness.srf') # have this here just to make testing faster

    def OnNew(self, event):
        # TODO: what should actually go here? just check if an existing collection exists,
        # check if it's saved (if not, prompt to save), and then del it and init a new one?
        pass

    def OnOpen(self, event):
        dlg = wx.FileDialog(self, message="Open surf or sort file",
                            defaultDir=self.DEFAULTDIR, defaultFile='',
                            wildcard="All files (*.*)|*.*|Surf files (*.srf)|*.srf|Sort files (*.sort)|*.sort",
                            style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            fname = dlg.GetPath()
            self.OpenFile(fname)
        dlg.Destroy()

    def OnSave(self, event):
        if not self.sortfname:
            self.OnSaveAs(event)
        else:
            self.SaveFile(self.sortfname) # save to existing sort fname

    def OnSaveAs(self, event):
        """Save collection to new .sort file"""
        dlg = wx.FileDialog(self, message="Save collection as",
                            defaultDir=self.DEFAULTDIR, defaultFile='',
                            wildcard="Sort files (*.sort)|*.sort|All files (*.*)|*.*",
                            style=wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            fname = dlg.GetPath()
            self.SaveFile(fname)
        dlg.Destroy()

    def OnClose(self, event):
        # TODO: add confirmation dialog if collection not saved
        self.CloseSurfFile()

    def OnExit(self, event):
        # TODO: add confirmation dialog if collection not saved
        self.CloseSurfFile()
        event.Skip()

    def OnAbout(self, event):
        dlg = SpykeAbout(self)
        dlg.ShowModal()
        dlg.Destroy()

    def OnIconize(self, event):
        for frame in self.frames.values():
            if not frame.Hide(): # returns False if it's already hidden
                frame.Show()
        print 'iconizing'
        event.Skip()

    def OnActivate(self, event):
        """When you change tasks to this frame, say by clicking on taskbar button.
        Have this here so that data frames will also be raised"""
        print 'in OnActivate'
        activating = event.GetActive()
        if activating: # going from inactive to active state
            for frame in self.frames.values():
                if not frame.IsActive():
                    print 'raising'
                    frame.Raise()
        event.Skip()

    def OnSliderScroll(self, event):
        self.seek(self.slider.GetValue())
        event.Skip()

    def OpenFile(self, fname):
        """Open either .srf or .sort file"""
        ext = os.path.splitext(fname)[1]
        if ext == '.srf':
            self.OpenSurfFile(fname)
        elif ext == '.sort':
            self.OpenSortFile(fname)
        else:
            wx.MessageBox("%s is not a .srf or .sort file" % fname,
                          caption="Error", style=wx.OK|wx.ICON_EXCLAMATION)
            return

    def OpenSurfFile(self, fname):
        """Open a .srf file, and update display accordingly"""
        self.CloseSurfFile() # in case a .srf file and frames are already open
        self.surff = surf.File(fname)
        # TODO: parsing progress dialog
        self.surff.parse()
        self.Refresh() # parsing takes long, can block repainting events
        self.surffname = fname # bind it now that it's been successfully opened and parsed
        self.SetTitle(self.Title + ' - ' + self.surffname) # update the caption

        self.stream = core.Stream(self.surff.highpassrecords) # highpass recording (spike) stream
        self.t0 = self.stream.rts[0] # first record timestamp, time that recording began
        self.layoutrecord = self.surff.layoutrecords[0] # TODO: check this: presumably the first is the spike probe layout
        probename = self.layoutrecord.electrode_name
        probename = probename.replace('\xb5', 'u') # replace 'micro' symbol with 'u'
        self.probe = eval('probes.' + probename)() # yucky. TODO: switch to a dict with keywords?

        # TODO: open spike, chart and LFP windows, depress their toggle buttons, check their toggle menus
        self.OpenFrame('spike')
        # self has focus, but isn't in foreground after opening data frames
        #self.Raise() # doesn't seem to bring self to foreground
        #wx.GetApp().SetTopWindow(self) # neither does this


        self.slider.SetPageSize(self.spiketw) # set slider page size to spike frame temporal width
        self.seek(self.t0) # plot first time window of data for all open frames

        # showing a hidden widget causes drawing problems and requires minimize+maximize to fix
        #self.file_control_panel.Show()
        #self.notebook.Show()
        #self.Refresh() # doesn't seem to help
        # use enable/disable instead, at least for now
        self.file_control_panel.Enable()
        self.notebook.Enable()

    def CloseSurfFile(self):
        """Destroy data frames, close .srf file"""
        # need to specifically get a list of keys, not an iterator,
        # since self.frames dict changes size during iteration
        for frametype in self.frames.keys():
            self.CloseFrame(frametype) # deletes from dict
        try:
            self.surff.close()
        except AttributeError:
            pass
        self.SetTitle("spyke") # update caption
        self.file_control_panel.Enable(False)
        self.notebook.Enable(False)

    def OpenFrame(self, frametype):
        if frametype == 'spike':
            self.spikeframe = SpikeFrame(parent=self, probe=self.probe)
            self.frames[frametype] = self.spikeframe
        elif frametype == 'chart':
            pass
        elif frametype == 'lfp':
            pass

        #self.chartframe = ChartFrame(self.probe, None)
        #self.lfpframe = LFPFrame(self.lfpprobes, None)
        #self.frames['spike'] = self.spikeframe
        self.spikeframe.Show()
        #self.chartframe.Show()
        #self.lfpframe.Show()

    def CloseFrame(self, frametype):
        """Remove frame from from dict of frames, destroy it"""
        frame = self.frames.pop(frametype)
        frame.Destroy()

    def seek(self, offset, relative=False):
        """Seek to position in surf file. offset is time in us,
        relative determines if offset is absolute or relative. If True,
        offset can be negative to seek backwards from current position"""
        if not relative:
            self.pos = offset
        else:
            self.pos = self.pos + offset

        print self.pos

        # update spike frame
        if 'spike' in self.frames:
            spikewaveform = self.stream[self.pos:self.pos+self.spiketw]
            self.spikeframe.spikepanel.plot(spikewaveform) # plot it


        # TODO: update chart and LFP windows
        # TODO: update slider
        # TODO: update statusbar


    def tell(self):
        """Return current position in surf file"""
        return self.pos

    def OpenSortFile(self, fname):
        """Open a collection from a .sort file"""
        # TODO: do something with data (data is the collection object????)
        try:
            f = file(fname, 'rb')
            data = cPickle.load(f)
            f.close()
            self.sortfname = fname # bind it now that it's been successfully loaded
            self.SetTitle(self.Title + ' - ' + self.sortfname)
        except cPickle.UnpicklingError:
            wx.MessageBox("Couldn't open %s as a sort file" % fname,
                          caption="Error", style=wx.OK|wx.ICON_EXCLAMATION)

    def SaveFile(self, fname):
        """Save collection to a .sort file"""
        if not os.path.splitext(fname)[1]:
            fname = fname + '.sort'
        f = file(fname, 'wb')
        cPickle.dump(self.collection, f)
        f.close()
        self.sortfname = fname # bind it now that it's been successfully saved
        self.SetTitle(self.Title + ' - ' + self.sortfname)


class SpikeFrame(wxglade_gui.SpikeFrame):
    """Frame to hold the custom spike panel widget.
    Copied and modified from auto-generated wxglade_gui.py code.
    Only thing really inherited is __set_properties()"""
    def __init__(self, parent=None, probe=None, *args, **kwds):
        kwds["style"] = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.RESIZE_BORDER|wx.FRAME_TOOL_WINDOW|wx.FRAME_NO_TASKBAR # need SYSTEM_MENU to make close box appear in a TOOL_WINDOW, at least on win32
        wx.Frame.__init__(self, parent, *args, **kwds)
        self.spikepanel = plot.SpikePanel(self, -1, layout=probe.SiteLoc)

        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.__set_properties()
        self.__do_layout()

    def __do_layout(self):
        spikeframe_sizer = wx.BoxSizer(wx.HORIZONTAL)
        spikeframe_sizer.Add(self.spikepanel, 1, wx.EXPAND, 0) # added by mspacek
        self.SetSizer(spikeframe_sizer)
        self.Layout()

    def OnClose(self, event):
        self.Parent.CloseFrame('spike')


class SpykeAbout(wx.Dialog):
    text = '''
        <html>
        <body bgcolor="#D4D0C8">
        <center><table bgcolor="#000000" width="100%" cellspacing="0"
        cellpadding="0" border="0">
        <tr>
            <td align="center"><h1><font color="#00FF00">spyke</font></h1></td>
        </tr>
        </table>
        </center>
        <p><b>spyke</b> is a tool for neuronal spike sorting.
        </p>

        <p>Copyright &copy; 2008 Reza Lotun, Martin Spacek</p>
        </body>
        </html>'''

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, -1, 'About spyke', size=(350, 250))

        html = wx.html.HtmlWindow(self)
        html.SetPage(self.text)
        button = wx.Button(self, wx.ID_OK, "OK")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(html, 1, wx.EXPAND|wx.ALL, 5)
        sizer.Add(button, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizer(sizer)
        self.Layout()


class SpykeApp(wx.App):
    def OnInit(self, splash=False):
        if splash:
            bmp = wx.Image("res/splash.png").ConvertToBitmap()
            wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT, 1000, None, -1)
            wx.Yield()
        spykeframe = SpykeFrame(None)
        spykeframe.Show()
        self.SetTopWindow(spykeframe)
        return True


if __name__ == '__main__':
    app = SpykeApp(False)
    app.MainLoop()
