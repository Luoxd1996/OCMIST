# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1046, 938)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1046, 938))
        MainWindow.setMaximumSize(QtCore.QSize(1046, 938))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(16, 16, 16, 16)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalWidget = QtWidgets.QWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_7.setContentsMargins(0, 6, 0, 6)
        self.verticalLayout_7.setSpacing(9)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem)
        self.button_open = QtWidgets.QPushButton(self.widget)
        self.button_open.setMinimumSize(QtCore.QSize(0, 30))
        self.button_open.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_open.setObjectName("button_open")
        self.verticalLayout_7.addWidget(self.button_open)
        self.button_save = QtWidgets.QPushButton(self.widget)
        self.button_save.setMinimumSize(QtCore.QSize(0, 30))
        self.button_save.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_save.setObjectName("button_save")
        self.verticalLayout_7.addWidget(self.button_save)
        self.button_undo = QtWidgets.QPushButton(self.widget)
        self.button_undo.setMinimumSize(QtCore.QSize(0, 30))
        self.button_undo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_undo.setObjectName("button_undo")
        self.verticalLayout_7.addWidget(self.button_undo)
        self.button_confirm = QtWidgets.QPushButton(self.widget)
        self.button_confirm.setMinimumSize(QtCore.QSize(0, 30))
        self.button_confirm.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_confirm.setObjectName("button_confirm")
        self.verticalLayout_7.addWidget(self.button_confirm)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem1)
        self.container_score = QtWidgets.QWidget(self.widget)
        self.container_score.setObjectName("container_score")
        self._2 = QtWidgets.QVBoxLayout(self.container_score)
        self._2.setContentsMargins(0, 0, 0, 0)
        self._2.setSpacing(6)
        self._2.setObjectName("_2")
        self.label_dice = QtWidgets.QLabel(self.container_score)
        self.label_dice.setText("")
        self.label_dice.setObjectName("label_dice")
        self._2.addWidget(self.label_dice)
        self.bar_dice = QtWidgets.QHBoxLayout()
        self.bar_dice.setContentsMargins(0, 0, -1, -1)
        self.bar_dice.setSpacing(1)
        self.bar_dice.setObjectName("bar_dice")
        self.label_dice1 = QtWidgets.QLabel(self.container_score)
        self.label_dice1.setStyleSheet("background-color: #3f51b5;")
        self.label_dice1.setText("")
        self.label_dice1.setObjectName("label_dice1")
        self.bar_dice.addWidget(self.label_dice1)
        self.label_dice2 = QtWidgets.QLabel(self.container_score)
        self.label_dice2.setStyleSheet("background-color: #9c27b0 ;")
        self.label_dice2.setText("")
        self.label_dice2.setObjectName("label_dice2")
        self.bar_dice.addWidget(self.label_dice2)
        self.label_dice3 = QtWidgets.QLabel(self.container_score)
        self.label_dice3.setStyleSheet("background-color: #9c27b0 ;")
        self.label_dice3.setText("")
        self.label_dice3.setObjectName("label_dice3")
        self.bar_dice.addWidget(self.label_dice3)
        self.label_dice4 = QtWidgets.QLabel(self.container_score)
        self.label_dice4.setStyleSheet("background-color: #f44336;")
        self.label_dice4.setText("")
        self.label_dice4.setObjectName("label_dice4")
        self.bar_dice.addWidget(self.label_dice4)
        self._2.addLayout(self.bar_dice)
        self.label_jaccard = QtWidgets.QLabel(self.container_score)
        self.label_jaccard.setText("")
        self.label_jaccard.setObjectName("label_jaccard")
        self._2.addWidget(self.label_jaccard)
        self.bar_jaccard = QtWidgets.QHBoxLayout()
        self.bar_jaccard.setContentsMargins(-1, 0, 0, -1)
        self.bar_jaccard.setSpacing(1)
        self.bar_jaccard.setObjectName("bar_jaccard")
        self.label_jaccard1 = QtWidgets.QLabel(self.container_score)
        self.label_jaccard1.setStyleSheet("background-color: #3f51b5;")
        self.label_jaccard1.setText("")
        self.label_jaccard1.setObjectName("label_jaccard1")
        self.bar_jaccard.addWidget(self.label_jaccard1)
        self.label_jaccard2 = QtWidgets.QLabel(self.container_score)
        self.label_jaccard2.setStyleSheet("background-color: #9c27b0 ;")
        self.label_jaccard2.setText("")
        self.label_jaccard2.setObjectName("label_jaccard2")
        self.bar_jaccard.addWidget(self.label_jaccard2)
        self.label_jaccard4 = QtWidgets.QLabel(self.container_score)
        self.label_jaccard4.setStyleSheet("background-color: #f44336;")
        self.label_jaccard4.setText("")
        self.label_jaccard4.setObjectName("label_jaccard4")
        self.bar_jaccard.addWidget(self.label_jaccard4)
        self._2.addLayout(self.bar_jaccard)
        self.label_precision = QtWidgets.QLabel(self.container_score)
        self.label_precision.setText("")
        self.label_precision.setObjectName("label_precision")
        self._2.addWidget(self.label_precision)
        self.bar_precision = QtWidgets.QHBoxLayout()
        self.bar_precision.setContentsMargins(-1, 0, 0, -1)
        self.bar_precision.setSpacing(1)
        self.bar_precision.setObjectName("bar_precision")
        self.label_precision1 = QtWidgets.QLabel(self.container_score)
        self.label_precision1.setStyleSheet("background-color: #3f51b5;")
        self.label_precision1.setText("")
        self.label_precision1.setObjectName("label_precision1")
        self.bar_precision.addWidget(self.label_precision1)
        self.label_precision2 = QtWidgets.QLabel(self.container_score)
        self.label_precision2.setStyleSheet("background-color: #9c27b0 ;")
        self.label_precision2.setText("")
        self.label_precision2.setObjectName("label_precision2")
        self.bar_precision.addWidget(self.label_precision2)
        self._2.addLayout(self.bar_precision)
        self.label_recall = QtWidgets.QLabel(self.container_score)
        self.label_recall.setText("")
        self.label_recall.setObjectName("label_recall")
        self._2.addWidget(self.label_recall)
        self.bar_recall = QtWidgets.QHBoxLayout()
        self.bar_recall.setContentsMargins(-1, 0, 0, -1)
        self.bar_recall.setSpacing(1)
        self.bar_recall.setObjectName("bar_recall")
        self.label_recall2 = QtWidgets.QLabel(self.container_score)
        self.label_recall2.setStyleSheet("background-color: #9c27b0 ;")
        self.label_recall2.setText("")
        self.label_recall2.setObjectName("label_recall2")
        self.bar_recall.addWidget(self.label_recall2)
        self.label_recall4 = QtWidgets.QLabel(self.container_score)
        self.label_recall4.setStyleSheet("background-color: #f44336;")
        self.label_recall4.setText("")
        self.label_recall4.setObjectName("label_recall4")
        self.bar_recall.addWidget(self.label_recall4)
        self._2.addLayout(self.bar_recall)
        self.verticalLayout_7.addWidget(self.container_score)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.label_xy = QtWidgets.QLabel(self.widget)
        self.label_xy.setText("")
        self.label_xy.setObjectName("label_xy")
        self.verticalLayout_7.addWidget(self.label_xy)
        self.label_mark = QtWidgets.QLabel(self.widget)
        self.label_mark.setText("")
        self.label_mark.setObjectName("label_mark")
        self.verticalLayout_7.addWidget(self.label_mark)
        self.label_resize = QtWidgets.QLabel(self.widget)
        self.label_resize.setText("")
        self.label_resize.setObjectName("label_resize")
        self.verticalLayout_7.addWidget(self.label_resize)
        self.label_slice = QtWidgets.QLabel(self.widget)
        self.label_slice.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_slice.setText("")
        self.label_slice.setObjectName("label_slice")
        self.verticalLayout_7.addWidget(self.label_slice)
        self.container_sag = QtWidgets.QWidget(self.widget)
        self.container_sag.setMinimumSize(QtCore.QSize(160, 160))
        self.container_sag.setMaximumSize(QtCore.QSize(160, 160))
        self.container_sag.setStyleSheet("")
        self.container_sag.setObjectName("container_sag")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.container_sag)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_sag = QtWidgets.QLabel(self.container_sag)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_sag.sizePolicy().hasHeightForWidth())
        self.label_sag.setSizePolicy(sizePolicy)
        self.label_sag.setMinimumSize(QtCore.QSize(160, 160))
        self.label_sag.setMaximumSize(QtCore.QSize(160, 160))
        self.label_sag.setStyleSheet("background-color: #a0a0a0;")
        self.label_sag.setText("")
        self.label_sag.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sag.setObjectName("label_sag")
        self.horizontalLayout_2.addWidget(self.label_sag)
        self.verticalLayout_7.addWidget(self.container_sag)
        self.container_cor = QtWidgets.QWidget(self.widget)
        self.container_cor.setMinimumSize(QtCore.QSize(160, 160))
        self.container_cor.setMaximumSize(QtCore.QSize(160, 160))
        self.container_cor.setStyleSheet("")
        self.container_cor.setObjectName("container_cor")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.container_cor)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_cor = QtWidgets.QLabel(self.container_cor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cor.sizePolicy().hasHeightForWidth())
        self.label_cor.setSizePolicy(sizePolicy)
        self.label_cor.setMinimumSize(QtCore.QSize(160, 160))
        self.label_cor.setMaximumSize(QtCore.QSize(160, 160))
        self.label_cor.setStyleSheet("background-color: #a0a0a0;")
        self.label_cor.setText("")
        self.label_cor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cor.setObjectName("label_cor")
        self.horizontalLayout_3.addWidget(self.label_cor)
        self.verticalLayout_7.addWidget(self.container_cor)
        self.horizontalLayout.addWidget(self.widget)
        self.gridWidget = QtWidgets.QWidget(self.horizontalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setSpacing(16)
        self.gridLayout.setObjectName("gridLayout")
        self.container_flair = QtWidgets.QWidget(self.gridWidget)
        self.container_flair.setStyleSheet("")
        self.container_flair.setObjectName("container_flair")
        self.layout_flair = QtWidgets.QVBoxLayout(self.container_flair)
        self.layout_flair.setContentsMargins(0, 0, 0, 0)
        self.layout_flair.setSpacing(0)
        self.layout_flair.setObjectName("layout_flair")
        self.label_2 = QtWidgets.QLabel(self.container_flair)
        self.label_2.setObjectName("label_2")
        self.layout_flair.addWidget(self.label_2)
        self.viewer_flair = Viewer(self.container_flair)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.viewer_flair.sizePolicy().hasHeightForWidth())
        self.viewer_flair.setSizePolicy(sizePolicy)
        self.viewer_flair.setMinimumSize(QtCore.QSize(384, 384))
        self.viewer_flair.setMouseTracking(True)
        self.viewer_flair.setStyleSheet("background-color: #a0a0a0;")
        self.viewer_flair.setText("")
        self.viewer_flair.setScaledContents(False)
        self.viewer_flair.setAlignment(QtCore.Qt.AlignCenter)
        self.viewer_flair.setObjectName("viewer_flair")
        self.layout_flair.addWidget(self.viewer_flair)
        self.gridLayout.addWidget(self.container_flair, 1, 2, 1, 1)
        self.container_t2 = QtWidgets.QWidget(self.gridWidget)
        self.container_t2.setStyleSheet("")
        self.container_t2.setObjectName("container_t2")
        self.layout_t2 = QtWidgets.QVBoxLayout(self.container_t2)
        self.layout_t2.setContentsMargins(0, 0, 0, 0)
        self.layout_t2.setSpacing(0)
        self.layout_t2.setObjectName("layout_t2")
        self.label = QtWidgets.QLabel(self.container_t2)
        self.label.setObjectName("label")
        self.layout_t2.addWidget(self.label)
        self.viewer_t2 = Viewer(self.container_t2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.viewer_t2.sizePolicy().hasHeightForWidth())
        self.viewer_t2.setSizePolicy(sizePolicy)
        self.viewer_t2.setMinimumSize(QtCore.QSize(384, 384))
        self.viewer_t2.setMouseTracking(True)
        self.viewer_t2.setStyleSheet("background-color: #a0a0a0;")
        self.viewer_t2.setText("")
        self.viewer_t2.setScaledContents(False)
        self.viewer_t2.setAlignment(QtCore.Qt.AlignCenter)
        self.viewer_t2.setObjectName("viewer_t2")
        self.layout_t2.addWidget(self.viewer_t2)
        self.gridLayout.addWidget(self.container_t2, 1, 1, 1, 1)
        self.container_t1 = QtWidgets.QWidget(self.gridWidget)
        self.container_t1.setStyleSheet("")
        self.container_t1.setObjectName("container_t1")
        self.layout_t1 = QtWidgets.QVBoxLayout(self.container_t1)
        self.layout_t1.setContentsMargins(0, 0, 0, 0)
        self.layout_t1.setSpacing(0)
        self.layout_t1.setObjectName("layout_t1")
        self.label_3 = QtWidgets.QLabel(self.container_t1)
        self.label_3.setObjectName("label_3")
        self.layout_t1.addWidget(self.label_3)
        self.viewer_t1 = Viewer(self.container_t1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.viewer_t1.sizePolicy().hasHeightForWidth())
        self.viewer_t1.setSizePolicy(sizePolicy)
        self.viewer_t1.setMinimumSize(QtCore.QSize(384, 384))
        self.viewer_t1.setMouseTracking(True)
        self.viewer_t1.setStyleSheet("background-color: #a0a0a0;")
        self.viewer_t1.setText("")
        self.viewer_t1.setScaledContents(False)
        self.viewer_t1.setAlignment(QtCore.Qt.AlignCenter)
        self.viewer_t1.setObjectName("viewer_t1")
        self.layout_t1.addWidget(self.viewer_t1)
        self.gridLayout.addWidget(self.container_t1, 0, 1, 1, 1)
        self.container_t1ce = QtWidgets.QWidget(self.gridWidget)
        self.container_t1ce.setStyleSheet("")
        self.container_t1ce.setObjectName("container_t1ce")
        self.layout_t1ce = QtWidgets.QVBoxLayout(self.container_t1ce)
        self.layout_t1ce.setContentsMargins(0, 0, 0, 0)
        self.layout_t1ce.setSpacing(0)
        self.layout_t1ce.setObjectName("layout_t1ce")
        self.label_4 = QtWidgets.QLabel(self.container_t1ce)
        self.label_4.setObjectName("label_4")
        self.layout_t1ce.addWidget(self.label_4)
        self.viewer_t1ce = Viewer(self.container_t1ce)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.viewer_t1ce.sizePolicy().hasHeightForWidth())
        self.viewer_t1ce.setSizePolicy(sizePolicy)
        self.viewer_t1ce.setMinimumSize(QtCore.QSize(384, 384))
        self.viewer_t1ce.setMouseTracking(True)
        self.viewer_t1ce.setStyleSheet("background-color: #a0a0a0;")
        self.viewer_t1ce.setText("")
        self.viewer_t1ce.setScaledContents(False)
        self.viewer_t1ce.setAlignment(QtCore.Qt.AlignCenter)
        self.viewer_t1ce.setObjectName("viewer_t1ce")
        self.layout_t1ce.addWidget(self.viewer_t1ce)
        self.gridLayout.addWidget(self.container_t1ce, 0, 2, 1, 1)
        self.horizontalLayout.addWidget(self.gridWidget)
        self.widget1 = QtWidgets.QWidget(self.horizontalWidget)
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget2 = QtWidgets.QWidget(self.widget1)
        self.widget2.setObjectName("widget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_2.setContentsMargins(0, 6, 0, 6)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.slider = QtWidgets.QSlider(self.widget2)
        self.slider.setFocusPolicy(QtCore.Qt.NoFocus)
        self.slider.setMinimum(1)
        self.slider.setMaximum(128)
        self.slider.setProperty("value", 64)
        self.slider.setOrientation(QtCore.Qt.Vertical)
        self.slider.setInvertedAppearance(False)
        self.slider.setInvertedControls(False)
        self.slider.setObjectName("slider")
        self.verticalLayout_2.addWidget(self.slider)
        self.horizontalLayout_4.addWidget(self.widget2)
        self.horizontalLayout.addWidget(self.widget1)
        self.verticalLayout.addWidget(self.horizontalWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1046, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuTool = QtWidgets.QMenu(self.menuBar)
        self.menuTool.setObjectName("menuTool")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_pred = QtWidgets.QAction(MainWindow)
        self.action_pred.setObjectName("action_pred")
        self.action_extend = QtWidgets.QAction(MainWindow)
        self.action_extend.setObjectName("action_extend")
        self.action_shrink = QtWidgets.QAction(MainWindow)
        self.action_shrink.setObjectName("action_shrink")
        self.action_gt = QtWidgets.QAction(MainWindow)
        self.action_gt.setObjectName("action_gt")
        self.action_undo = QtWidgets.QAction(MainWindow)
        self.action_undo.setObjectName("action_undo")
        self.action_apply = QtWidgets.QAction(MainWindow)
        self.action_apply.setObjectName("action_apply")
        self.action_calculate_box = QtWidgets.QAction(MainWindow)
        self.action_calculate_box.setObjectName("action_calculate_box")
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_save)
        self.menuView.addAction(self.action_pred)
        self.menuView.addAction(self.action_gt)
        self.menuTool.addAction(self.action_extend)
        self.menuTool.addAction(self.action_shrink)
        self.menuTool.addSeparator()
        self.menuTool.addAction(self.action_undo)
        self.menuTool.addAction(self.action_apply)
        self.menuTool.addAction(self.action_calculate_box)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuTool.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OCMIST: One-click medical image segmentation tool!"))
        self.button_open.setText(_translate("MainWindow", "Open"))
        self.button_save.setText(_translate("MainWindow", "Save"))
        self.button_undo.setText(_translate("MainWindow", "Undo"))
        self.button_confirm.setText(_translate("MainWindow", "Apply"))
        self.label_2.setText(_translate("MainWindow", "FLAIR (T2 fluid attenuated inversion recovery)"))
        self.label.setText(_translate("MainWindow", "T2 (T2-weighted)"))
        self.label_3.setText(_translate("MainWindow", "T1 (native)"))
        self.label_4.setText(_translate("MainWindow", "T1Gd (post-contrast T1-weighted)"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuTool.setTitle(_translate("MainWindow", "Tool"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.action_open.setText(_translate("MainWindow", "Open project"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_save.setText(_translate("MainWindow", "Save"))
        self.action_save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_pred.setText(_translate("MainWindow", "Show prediction"))
        self.action_pred.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_extend.setText(_translate("MainWindow", "Extend"))
        self.action_shrink.setText(_translate("MainWindow", "Shrink"))
        self.action_gt.setText(_translate("MainWindow", "Show ground truth"))
        self.action_gt.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.action_undo.setText(_translate("MainWindow", "Undo"))
        self.action_undo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.action_apply.setText(_translate("MainWindow", "Apply"))
        self.action_apply.setShortcut(_translate("MainWindow", "Return"))
        self.action_calculate_box.setText(_translate("MainWindow", "Calculate box"))
        self.action_calculate_box.setShortcut(_translate("MainWindow", "Ctrl+C"))


from main import Viewer
