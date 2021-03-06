# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui

import rcc_rc

from core import *

class View(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(714, 675)
        mainForm.setMinimumSize(QtCore.QSize(714, 675))
        mainForm.setMaximumSize(QtCore.QSize(714, 675))
        mainForm.setWindowTitle("Combinatorics - Обчислення комбінацій та перестановок")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/pl_w_r.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainForm.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(mainForm)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabComb = QtGui.QTabWidget(mainForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabComb.sizePolicy().hasHeightForWidth())
        self.tabComb.setSizePolicy(sizePolicy)
        self.tabComb.setMaximumSize(QtCore.QSize(16777215, 180))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.tabComb.setFont(font)
        self.tabComb.setTabPosition(QtGui.QTabWidget.North)
        self.tabComb.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabComb.setIconSize(QtCore.QSize(16, 16))
        self.tabComb.setElideMode(QtCore.Qt.ElideNone)
        self.tabComb.setUsesScrollButtons(False)
        self.tabComb.setDocumentMode(False)
        self.tabComb.setTabsClosable(False)
        self.tabComb.setMovable(False)
        self.tabComb.setObjectName("tabComb")
        self.tab = QtGui.QWidget()
        
        self.tab.coreGenerator = Core.comb      # Each method that generates comb. stored in his Tab page (QWidget)
        self.tab.coreNumber = Core.comb_number  # Each method that calculates number of comb. stored in his Tab page (QWidget)
        
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFrameShadow(QtGui.QFrame.Plain)
        self.label.setText("<html><head/><body><p><span style=\" font-size:10pt;\">В комбінаториці комбінацією n по k називається набір k елементів, виділених із даної множини, що містить n різних елементів. Набори, що відрізняються тільки порядком слідування елементів (не складом), вважаються однаковими, цим комбінації відрізняються від <a href=\"#tab2\">розміщень</a>. </span></p><p><span style=\" font-size:10pt;\">Число комбінацій із n по k рівно біноміальному коефіціенту:</span><br/><img src=\":/formulas/formulas/comb.png\"/></p></body></html>")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/c.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabComb.addTab(self.tab, icon1, "Комбінації")
        self.tab_2 = QtGui.QWidget()

        self.tab_2.coreGenerator = Core.comb_w_repl      # Each method that generates comb. stored in his Tab page (QWidget)
        self.tab_2.coreNumber = Core.comb_w_repl_number  # Each method that calculates number of comb. stored in his Tab page (QWidget)
        
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_5 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFrameShadow(QtGui.QFrame.Plain)
        self.label_5.setText("<html><head/><body><span style=\" font-size:10pt;\">Комбінацією із повторенням називаються набори, в яких кожен елемент може брати участь декілька разів. Число комбінацій із повторенням n по k рівно біноміальному коефіціенту: </span><p><img src=\":/formulas/formulas/comb_w_r.png\"/></p></body></html>")
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_11.addWidget(self.label_5)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/c_w_r.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabComb.addTab(self.tab_2, icon2, "Комбінації з повторенням")
        self.tab_5 = QtGui.QWidget()

        self.tab_5.coreGenerator = Core.place      # Each method that generates comb. stored in his Tab page (QWidget) 
        self.tab_5.coreNumber = Core.place_number  # Each method that calculates number of comb. stored in his Tab page (QWidget)

        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtGui.QLabel(self.tab_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFrameShadow(QtGui.QFrame.Plain)
        self.label_3.setText("<html><head/><body><p><span style=\" font-size:10pt;\">В комбінаториці, розміщенням із n елементів по m, або впорядкованою (n, m) вибіркою із множини M (потужність n, m≤n) називають довільний кортеж </span><img src=\":/formulas/formulas/p1.png\"/><span style=\" font-size:10pt;\"> що складається із m попарно відмінних елементів. Кількість розміщень із n по m позначається як </span><img src=\":/formulas/formulas/p2.png\"/><span style=\" font-size:10pt;\"> або </span><img src=\":/formulas/formulas/p3.png\"/><span style=\" font-size:10pt;\"> і обчислюється за наступною формулою:</span></p><p><img src=\":/formulas/formulas/p4.png\"/></p></body></html>")
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/pl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabComb.addTab(self.tab_5, icon3, "Розміщення")
        self.tab_3 = QtGui.QWidget()

        self.tab_3.coreGenerator = Core.place_w_repl      # Each method that generates comb. stored in his Tab page (QWidget)
        self.tab_3.coreNumber = Core.place_w_repl_number  # Each method that calculates number of comb. stored in his Tab page (QWidget)

        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFrameShadow(QtGui.QFrame.Plain)
        self.label_2.setText("<html><head/><body><p><span style=\" font-size:10pt;\">Розміщенням з повтореннями із n елементів по m або дворядкованою (n, m) вибіркою з поверненнями називається довільний кортеж </span><img src=\":/formulas/formulas/c_w_r2.png\"/><span style=\" font-size:10pt;\"> елементів множини M, для якого |M| = n. Кількість можливих розміщень з повтореннями із n елементів по m дорівнює n піднесене до степеня m: </span></p><p><img src=\":/formulas/formulas/c_w_r.png\"/></p><p><span style=\" font-size:10pt;\">Наприклад, із цифр 1, 2, 3, 4 можна скласти </span><img src=\":/formulas/formulas/c_w_r3.png\"/><span style=\" font-size:10pt;\"> трьохзначних числа.</span></p></body></html>")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.tabComb.addTab(self.tab_3, icon, "Розміщення із повторенням")
        self.tab_4 = QtGui.QWidget()

        self.tab_4.coreGenerator = Core.perm      # Each method that generates comb. stored in his Tab page (QWidget)
        self.tab_4.coreNumber = Core.perm_number  # Each method that calculates number of comb. stored in his Tab page (QWidget)

        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_4 = QtGui.QLabel(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFrameShadow(QtGui.QFrame.Plain)
        self.label_4.setText("<html><head/><body><p><span style=\" font-size:10pt;\">Перестановкою або підстановкою скінченної множини X називається довільна бієктивна функція </span><img src=\":/formulas/formulas/per1.png\"/><span style=\" font-size:10pt;\">. </span></p><p><span style=\" font-size:10pt;\">Всього існує </span><img src=\":/formulas/formulas/per2.png\"/><span style=\" font-size:10pt;\"> (факторіал) різних перестановок, де </span><img src=\":/formulas/formulas/per3.png\"/><span style=\" font-size:10pt;\"> (потужність множини (кількість елементів в ній) ).</span></p></body></html>")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/p.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabComb.addTab(self.tab_4, icon4, "Перестановки")
        self.verticalLayout.addWidget(self.tabComb)
        self.groupInput = QtGui.QGroupBox(mainForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupInput.sizePolicy().hasHeightForWidth())
        self.groupInput.setSizePolicy(sizePolicy)
        self.groupInput.setTitle("Вхідні дані")
        self.groupInput.setObjectName("groupInput")
        self.gridLayout = QtGui.QGridLayout(self.groupInput)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtGui.QLabel(self.groupInput)
        self.label_6.setText("К-сть вибірок:")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 4, 1, 1)
        self.spinK = QtGui.QSpinBox(self.groupInput)
        self.spinK.setMinimumSize(QtCore.QSize(100, 0))
        self.spinK.setMaximumSize(QtCore.QSize(120, 16777215))
        self.spinK.setMinimum(1)
        self.spinK.setMaximum(100000000)
        self.spinK.setObjectName("spinK")
        self.gridLayout.addWidget(self.spinK, 1, 4, 1, 1)
        self.radioN = QtGui.QRadioButton(self.groupInput)
        self.radioN.setMinimumSize(QtCore.QSize(0, 0))
        self.radioN.setText("числ. послідовність:")
        self.radioN.setChecked(True)
        self.radioN.setObjectName("radioN")
        self.gridLayout.addWidget(self.radioN, 1, 1, 1, 1)
        self.radioNCustom = QtGui.QRadioButton(self.groupInput)
        self.radioNCustom.setText("власний список:")
        self.radioNCustom.setObjectName("radioNCustom")
        self.gridLayout.addWidget(self.radioNCustom, 2, 1, 1, 1)
        self.spinN = QtGui.QSpinBox(self.groupInput)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinN.sizePolicy().hasHeightForWidth())
        self.spinN.setSizePolicy(sizePolicy)
        self.spinN.setMaximumSize(QtCore.QSize(200, 16777215))
        self.spinN.setMinimum(1)
        self.spinN.setMaximum(100000000)
        self.spinN.setObjectName("spinN")
        self.gridLayout.addWidget(self.spinN, 1, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupInput)
        self.label_7.setText("Задайте числову послідовність, <br>\nчи введіть в поле свій набір елементів, розділених пробілами):")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)
        self.plainNCustom = QtGui.QPlainTextEdit(self.groupInput)
        self.plainNCustom.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainNCustom.sizePolicy().hasHeightForWidth())
        self.plainNCustom.setSizePolicy(sizePolicy)
        self.plainNCustom.setMaximumSize(QtCore.QSize(1000, 70))
        self.plainNCustom.setObjectName("plainNCustom")
        self.gridLayout.addWidget(self.plainNCustom, 2, 2, 1, 1)
        self.line = QtGui.QFrame(self.groupInput)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 3, 1, 1)
        self.line_2 = QtGui.QFrame(self.groupInput)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 0, 3, 1, 1)
        self.line_3 = QtGui.QFrame(self.groupInput)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 2, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupInput)
        self.groupBox_7 = QtGui.QGroupBox(mainForm)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setTitle("Обчислення")
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableMetadata = QtGui.QTableWidget(self.groupBox_7)
        self.tableMetadata.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableMetadata.setGridStyle(QtCore.Qt.SolidLine)
        self.tableMetadata.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableMetadata.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableMetadata.setObjectName("tableMetadata")
        self.tableMetadata.setColumnCount(1)
        self.tableMetadata.setRowCount(8)
        self.tableMetadata.horizontalHeader().setVisible(False)
        self.tableMetadata.setVerticalHeaderLabels(["Тип обчислення", "Усього варіантів", "Згенеровано", "Прогрес (%)", "Час обчислення", "Часу залишилось", "Файл із результатом", "Розмір файла"])
        self.horizontalLayout.addWidget(self.tableMetadata)

        # save link to each MetaTable's row in dictionary
        self.metaRows = {}        
        self.metaRows["name"]       = QtGui.QTableWidgetItem("")
        self.metaRows["all"]        = QtGui.QTableWidgetItem("1")
        self.metaRows["complete"]   = QtGui.QTableWidgetItem("0")
        self.metaRows["time"]       = QtGui.QTableWidgetItem("")
        self.metaRows["left"]       = QtGui.QTableWidgetItem("")
        self.metaRows["result"]     = QtGui.QTableWidgetItem("")
        self.metaRows["result"].setToolTip("Двічі клацніть на комірці щоб відкрити файл із результатом")

        self.tableMetadata.setItem(0, 0, self.metaRows["name"])
        self.tableMetadata.setItem(1, 0, self.metaRows["all"])
        self.tableMetadata.setItem(2, 0, self.metaRows["complete"])
        self.tableMetadata.setItem(4, 0, self.metaRows["time"])
        self.tableMetadata.setItem(5, 0, self.metaRows["left"])
        self.tableMetadata.setItem(6, 0, self.metaRows["result"])
        
        # add progressBar to Table Cell
        self.progressWidget = QtGui.QWidget(mainForm)               # solution for CellWidget Vertical alignment
        verticalLayout = QtGui.QVBoxLayout(self.progressWidget)
        verticalLayout.setContentsMargins(5, 0, 0, 0)
    
        self.metaRows["progressBar"] = QtGui.QProgressBar()
        self.metaRows["progressBar"].setMinimum(0)
        self.metaRows["progressBar"].setMaximum(100)
        self.metaRows["progressBar"].setMinimumWidth(300)
        self.metaRows["progressBar"].setMaximumWidth(300)
        self.metaRows["progressBar"].setMaximumHeight(15)
        
        verticalLayout.addWidget(self.metaRows["progressBar"])      # put ProgBar into another Widget so it will be vertical aligned within Table Cell

        self.tableMetadata.setCellWidget(3, 0, self.progressWidget)
          
        # add "File Size" cell
        self.filesizeWidget = QtGui.QWidget(mainForm)               
        horizontalLayout = QtGui.QHBoxLayout(self.filesizeWidget)
        horizontalLayout.setContentsMargins(5, 0, 0, 0)
        
        self.metaRows["labelSize"] = QtGui.QLabel("0 байт")
        self.metaRows["btnClear"] = QtGui.QPushButton("Очистити")
        
        horizontalLayout.addWidget(self.metaRows["labelSize"])
        horizontalLayout.addWidget(self.metaRows["btnClear"])
        horizontalLayout.addItem(QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum))
        
        self.tableMetadata.setCellWidget(7, 0, self.filesizeWidget)
        
        
        self.tableMetadata.resizeColumnsToContents()
        
        
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.checkMetadata = QtGui.QCheckBox(self.groupBox_7)
        self.checkMetadata.setToolTip("У файл із результатом буде включена додаткова інформація:<br>\n- к-сть комбінацій<br>\n- скільки множин згенеровано, і скільки залишилось<br>\n- час генерації/скільки залишилось")
        self.checkMetadata.setText("Включати в результат метадані")
        self.checkMetadata.setChecked(True)
        self.checkMetadata.setObjectName("checkMetadata")
        self.verticalLayout_12.addWidget(self.checkMetadata)
        self.checkShowResult = QtGui.QCheckBox(self.groupBox_7)
        self.checkShowResult.setToolTip("Результат можна переглянути, відкривши вручну файл, куди він зберігається")
        self.checkShowResult.setText("Показувати результат на паузі")
        self.checkShowResult.setChecked(True)
        self.checkShowResult.setObjectName("checkShowResult")
        self.verticalLayout_12.addWidget(self.checkShowResult)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.spinColumns = QtGui.QSpinBox(self.groupBox_7)
        self.spinColumns.setMinimum(1)
        self.spinColumns.setMaximum(100)
        self.spinColumns.setObjectName("spinColumns")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinColumns)
        self.label_8 = QtGui.QLabel(self.groupBox_7)
        self.label_8.setText("Кількість колонок:")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.verticalLayout_12.addLayout(self.formLayout)
        self.btnStart = QtGui.QPushButton(self.groupBox_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.btnStart.setFont(font)
        self.btnStart.setText("Старт обчислень")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStart.setIcon(icon5)
        self.btnStart.setObjectName("btnStart")
        self.verticalLayout_12.addWidget(self.btnStart)
        self.btnStop = QtGui.QPushButton(self.groupBox_7)
        self.btnStop.setEnabled(False)
        self.btnStop.setText("Завершити обчислення")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon6)
        self.btnStop.setObjectName("btnStop")
        self.verticalLayout_12.addWidget(self.btnStop)
        self.btnResultPath = QtGui.QPushButton(self.groupBox_7)
        self.btnResultPath.setText("Розміщення результатів")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnResultPath.setIcon(icon7)
        self.btnResultPath.setObjectName("btnResultPath")
        self.verticalLayout_12.addWidget(self.btnResultPath)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_12)
        self.verticalLayout.addWidget(self.groupBox_7)

        self.retranslateUi(mainForm)
        self.tabComb.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        pass
