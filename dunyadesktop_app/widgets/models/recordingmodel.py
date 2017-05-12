import os
import json

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem

DUNYA_ICON = os.path.join(os.path.dirname(__file__), '..', '..', 'ui_files',
                          'icons', 'dunya.svg')
DOCS_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'cultures',
                         'documents')


class RecordingModel(QStandardItemModel):
    """Recording model is for the results of queries."""
    rec_fetched = pyqtSignal(str)

    def __init__(self, parent=None):
        QStandardItemModel.__init__(self, parent)
        self.set_columns()

    def set_columns(self):
        self.setHorizontalHeaderLabels(['', 'Title', 'Composer', 'Artists'])

    def clear_items(self):
        self.clear()
        self.set_columns()

    def add_recording(self, work):
        for rec in work['recordings']:
            check_item = QStandardItem()
            check_item.setCheckable(True)
            title = QStandardItem(rec['title'])

            composers = ''
            for composer in work['composers']:
                composers += composer['name'] + ","
            composers_item = QStandardItem(composers)

            artists = ''
            rec['artists'] = [dict(tupleized) for tupleized in
                              set(tuple(element.items())
                                  for element in rec['artists'])]

            for artist in rec['artists']:
                artists += artist['name'] + ", "

            artists = artists[:-2]
            artist_item = QStandardItem(artists)

            mbid = rec['mbid']
            self.rec_fetched.emit(mbid)

            if os.path.isdir(os.path.join(DOCS_PATH, str(rec['mbid']))):
                check_item.setCheckState(Qt.Checked)
                check_item.setEnabled(False)

                # brush = QtGui.QBrush(QtGui.QColor(210, 220, 210))
                # check_item.setBackground(brush)
                # check_item.setEnabled(False)
                # title.setBackground(brush)
                # title.setEnabled(False)
                # artist_item.setBackground(brush)
                # artist_item.setEnabled(False)

            self.insertRow(self.rowCount())
            self.setItem(self.rowCount() - 1, 0, check_item)
            self.setItem(self.rowCount() - 1, 1, title)
            self.setItem(self.rowCount() - 1, 2, composers_item)
            self.setItem(self.rowCount() - 1, 3, artist_item)

    def set_checked(self, rows):
        for row in rows:
            check_item = QStandardItem()
            check_item.setCheckState(Qt.Checked)
            check_item.setEnabled(False)
            check_item.setToolTip('Already added to main collection...')
            self.setItem(row, 0, check_item)


class CollectionTableModel(QStandardItemModel):
    def __init__(self):
        QStandardItemModel.__init__(self)
        self.set_columns()
        self.items = {}

    def set_columns(self):
        self.setHorizontalHeaderLabels(['', 'Title', 'Artists', 'Makam', 'Usul',
                                        'Form'])

    def clear_items(self):
        self.clear()
        self.set_columns()
        self.items = {}

    def add_recording(self, recording):
        for index, mbid in enumerate(recording):
            self._get_metadata(mbid[0], index)

    def _get_metadata(self, mbid, index):
        path = os.path.join(DOCS_PATH, mbid, 'audioanalysis--metadata.json')
        self.metadata = json.load(open(path))

        mbid = self.metadata['mbid']
        title = self.metadata['title']
        artists = self._parse_artists()
        makam = self._parse_mattribute('makam')
        usul = self._parse_mattribute('usul')
        form = self._parse_mattribute('form')

        self.insertRow(self.rowCount())
        self.setItem(self.rowCount() - 1, 0, self._make_item(str(self.rowCount())))
        self.setItem(self.rowCount() - 1, 1, self._make_item(title))
        self.setItem(self.rowCount() - 1, 2, self._make_item(artists))
        self.setItem(self.rowCount() - 1, 3, self._make_item(makam))
        self.setItem(self.rowCount() - 1, 4, self._make_item(usul))
        self.setItem(self.rowCount() - 1, 5, self._make_item(form))
        self.items[index] = mbid

    def _make_item(self, text):
        return QStandardItem(text)

    def _parse_artists(self):
        values = self.metadata['artists']
        v = []
        return_s = ''
        for k in values:
            v.append(k['name'])
        for a in v:
            return_s += a + ', '
        return return_s[:-2]

    def _parse_mattribute(self, key):
        for value in self.metadata[key]:
            try:
                mattribute = value['mb_attribute']
                return mattribute
            except KeyError:
                pass
