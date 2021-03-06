import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

NITEMS = 1000
#INITIALFETCHSIZE = 5000
#FETCHSIZE = 2000


class TestWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.list = TestListView(self)
        self.setCentralWidget(self.list)
        self.resize(500, 500)


class TestListView(QtGui.QListView):
    def __init__(self, parent):
        QtGui.QListView.__init__(self, parent)
        self.setModel(TestListModel(parent))
        #self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setSelectionMode(QtGui.QListView.ExtendedSelection)
        self.setLayoutMode(QtGui.QListView.Batched) # prevents lockup during huge layout ops
        self.setResizeMode(QtGui.QListView.Adjust) # recalculates layout on resize
        self.setUniformItemSizes(True) # speeds up listview
        self.setFlow(QtGui.QListView.LeftToRight) # default is TopToBottom
        self.setWrapping(True)
        self.setBatchSize(500)
        #self.setViewMode(QtGui.QListView.IconMode)


class TestListModel(QtCore.QAbstractListModel):
    def __init__(self, parent):
        QtCore.QAbstractListModel.__init__(self, parent)
        #self.nfetched = 0 # should be reset to 0 in self.reset(), maybe between begin and end

    '''
    def updateAll(self):
        """Emit dataChanged signal so that view updates itself immediately.
        Hard to believe this doesn't already exist in some form"""
        i0 = self.createIndex(0, 0) # row, col
        i1 = self.createIndex(self.rowCount()-1, 0) # seems this isn't necessary
        #i1 = self.createIndex(100, 0) # seems this isn't necessary
        #self.dataChanged.emit(i0, i0) # seems to refresh all, though should only refresh 1st row
        self.dataChanged.emit(i0, i1) # refresh all
    '''
    def rowCount(self, parent=None):
        return NITEMS
        #return self.nfetched
    '''
    def trueRowCount(self):
        return NITEMS
    '''
    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and index.isValid():
            return index.row()
    '''
    def canFetchMore(self, index):
        if self.nfetched < self.trueRowCount():
            return True
        else:
            return False

    def fetchMore(self, index):
        remaining = self.trueRowCount() - self.nfetched
        if self.nfetched == 0:
            fetchsize = INITIALFETCHSIZE
        else:
            fetchsize = FETCHSIZE
        nitemstofetch = min(fetchsize, remaining)
        self.beginInsertRows(index, self.nfetched, self.nfetched+nitemstofetch)
        self.nfetched += nitemstofetch
        self.endInsertRows()
        print('done fetchmore: fetched: %d, self.nfetched: %d, remaining: %d' % (nitemstofetch, self.nfetched, self.trueRowCount() - self.nfetched))
    '''

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = TestWindow()
    win.show()
    try:
        from IPython import appstart_qt4
        appstart_qt4(app)
    except ImportError:
        sys.exit(app.exec_())

