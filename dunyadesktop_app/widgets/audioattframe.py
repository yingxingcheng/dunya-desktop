from __future__ import absolute_import
import os

from PyQt4 import QtGui, QtCore

from .combobox import ComboBox

QUERY_ICON = ":/compmusic/icons/magnifying-glass.png"
CSS_PATH = os.path.join(os.path.dirname(__file__), '..', 'ui_files', 'css',
                        'audioattframe.css')

class AudioAttFrame(QtGui.QFrame):
    def __init__(self):
        QtGui.QFrame.__init__(self)

        self._set_frame_attributes()

        self.gridLayout_filtering = QtGui.QGridLayout(self)
        self._set_gridlayout_filtering()
        self._retranslate_status_tips()
        self._set_css()

        self.toolButton_query.setDisabled(True)

        # signals
        self.comboBox_melodic.currentIndexChanged.connect(self.set_toolbutton)
        self.comboBox_form.currentIndexChanged.connect(self.set_toolbutton)
        self.comboBox_rhythm.currentIndexChanged.connect(self.set_toolbutton)
        self.comboBox_composer.currentIndexChanged.connect(self.set_toolbutton)
        self.comboBox_performer.currentIndexChanged.connect(
                                                           self.set_toolbutton)
        self.comboBox_instrument.currentIndexChanged.connect(
                                                           self.set_toolbutton)

    def _set_frame_attributes(self):
        size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,
                                        QtGui.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setCursor(
            QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.setFrameShape(QtGui.QFrame.StyledPanel)
        self.setFrameShadow(QtGui.QFrame.Raised)
        self.setLineWidth(1)

    def _set_gridlayout_filtering(self):
        self.gridLayout_filtering.setSizeConstraint(
            QtGui.QLayout.SetNoConstraint)
        self.gridLayout_filtering.setMargin(5)
        self.gridLayout_filtering.setSpacing(5)

        # combo boxes
        # melodic structure
        self.comboBox_melodic = ComboBox(self)
        self.gridLayout_filtering.addWidget(self.comboBox_melodic, 0, 0, 1, 1)

        # form structure
        self.comboBox_form = ComboBox(self)
        self.gridLayout_filtering.addWidget(self.comboBox_form, 0, 2, 1, 1)

        # rhythmic structure
        self.comboBox_rhythm = ComboBox(self)
        self.gridLayout_filtering.addWidget(self.comboBox_rhythm, 0, 4, 1, 1)

        # composer
        self.comboBox_composer = ComboBox(self)
        self.gridLayout_filtering.addWidget(self.comboBox_composer, 1, 0, 1, 1)
        self.comboBox_composer.set_placeholder_text('Composer')

        # performer
        self.comboBox_performer = ComboBox(self)
        self.gridLayout_filtering.addWidget(self.comboBox_performer,
                                            1, 2, 1, 1)
        self.comboBox_performer.set_placeholder_text('Performer')

        # instrument
        self.comboBox_instrument = ComboBox(self)
        self.gridLayout_filtering.addWidget(self.comboBox_instrument,
                                            1, 4, 1, 1)
        self.comboBox_instrument.set_placeholder_text('Instrument')

        spacer_item1 = QtGui.QSpacerItem(7, 20, QtGui.QSizePolicy.Minimum,
                                         QtGui.QSizePolicy.Fixed)

        spacer_item2 = QtGui.QSpacerItem(7, 20, QtGui.QSizePolicy.Minimum,
                                         QtGui.QSizePolicy.Fixed)

        spacer_item3 = QtGui.QSpacerItem(7, 20, QtGui.QSizePolicy.Minimum,
                                         QtGui.QSizePolicy.Fixed)

        self.gridLayout_filtering.addItem(spacer_item1, 1, 1, 1, 1)
        self.gridLayout_filtering.addItem(spacer_item2, 1, 3, 1, 1)
        self.gridLayout_filtering.addItem(spacer_item3, 1, 5, 1, 1)

        # query button and layout
        self.horizontalLayout_query = QtGui.QHBoxLayout()
        self.horizontalLayout_query.setSpacing(0)

        self.toolButton_query = QtGui.QToolButton(self)
        self.toolButton_query.setMinimumSize(QtCore.QSize(50, 50))
        self.toolButton_query.setMaximumSize(QtCore.QSize(60, 60))
        icon_query = QtGui.QIcon()
        icon_query.addPixmap(QtGui.QPixmap(QUERY_ICON),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_query.setIcon(icon_query)
        self.toolButton_query.setIconSize(QtCore.QSize(25, 25))
        self.horizontalLayout_query.addWidget(self.toolButton_query)
        self.gridLayout_filtering.addLayout(self.horizontalLayout_query, 0, 6,
                                            2, 1)

    def _retranslate_status_tips(self):
        self.comboBox_melodic.setStatusTip("Select melodic attribute")
        self.comboBox_form.setStatusTip("Select form attribute")
        self.comboBox_rhythm.setStatusTip("Select rhythm attribute")
        self.comboBox_composer.setStatusTip("Select composer")
        self.comboBox_performer.setStatusTip("Select performer")
        self.comboBox_instrument.setStatusTip("Select instrument")

        self.toolButton_query.setStatusTip("Query your selection")

    def _set_css(self):
        with open(CSS_PATH) as f:
            css = f.read()
        self.setStyleSheet(css)

    def set_toolbutton(self):
        index_melodic = self.comboBox_melodic.currentIndex()
        index_form = self.comboBox_form.currentIndex()
        index_rhythm = self.comboBox_rhythm.currentIndex()
        index_composer = self.comboBox_composer.currentIndex()
        index_performer = self.comboBox_performer.currentIndex()
        index_instrument = self.comboBox_instrument.currentIndex()

        if index_melodic is -1 and index_form is -1 and index_rhythm is -1 \
                and index_composer is -1 and index_performer is -1 and \
                        index_instrument is -1:
            self.toolButton_query.setDisabled(True)
        else:
            self.toolButton_query.setEnabled(True)