# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RFNode_GUI_18_Timer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_T2_Timer(object):
    def setupUi(self, T2_Timer):
        T2_Timer.setObjectName("T2_Timer")
        T2_Timer.resize(646, 553)
        self.tabWidget = QtWidgets.QTabWidget(T2_Timer)
        self.tabWidget.setGeometry(QtCore.QRect(16, 20, 611, 471))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gps_desc_edit = QtWidgets.QLineEdit(self.tab_9)
        self.gps_desc_edit.setGeometry(QtCore.QRect(120, 130, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gps_desc_edit.setFont(font)
        self.gps_desc_edit.setObjectName("gps_desc_edit")
        self.gps_group_label = QtWidgets.QLabel(self.tab_9)
        self.gps_group_label.setGeometry(QtCore.QRect(38, 210, 47, 31))
        self.gps_group_label.setObjectName("gps_group_label")
        self.gps_group_check = QtWidgets.QCheckBox(self.tab_9)
        self.gps_group_check.setGeometry(QtCore.QRect(100, 210, 20, 31))
        self.gps_group_check.setText("")
        self.gps_group_check.setObjectName("gps_group_check")
        self.gps_threadid_label = QtWidgets.QLabel(self.tab_9)
        self.gps_threadid_label.setGeometry(QtCore.QRect(16, 10, 91, 31))
        self.gps_threadid_label.setObjectName("gps_threadid_label")
        self.gps_force_label = QtWidgets.QLabel(self.tab_9)
        self.gps_force_label.setGeometry(QtCore.QRect(15, 170, 91, 31))
        self.gps_force_label.setObjectName("gps_force_label")
        self.gps_force_check = QtWidgets.QCheckBox(self.tab_9)
        self.gps_force_check.setGeometry(QtCore.QRect(100, 170, 20, 31))
        self.gps_force_check.setText("")
        self.gps_force_check.setObjectName("gps_force_check")
        self.gps_inserir_bt = QtWidgets.QPushButton(self.tab_9)
        self.gps_inserir_bt.setGeometry(QtCore.QRect(390, 250, 91, 31))
        self.gps_inserir_bt.setObjectName("gps_inserir_bt")
        self.gps_desc_label = QtWidgets.QLabel(self.tab_9)
        self.gps_desc_label.setGeometry(QtCore.QRect(25, 130, 71, 31))
        self.gps_desc_label.setObjectName("gps_desc_label")
        self.gps_streamid_label = QtWidgets.QLabel(self.tab_9)
        self.gps_streamid_label.setGeometry(QtCore.QRect(30, 50, 61, 31))
        self.gps_streamid_label.setObjectName("gps_streamid_label")
        self.gps_condition_label = QtWidgets.QLabel(self.tab_9)
        self.gps_condition_label.setGeometry(QtCore.QRect(25, 90, 71, 31))
        self.gps_condition_label.setObjectName("gps_condition_label")
        self.gps_condition_edit = QtWidgets.QLineEdit(self.tab_9)
        self.gps_condition_edit.setGeometry(QtCore.QRect(120, 90, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gps_condition_edit.setFont(font)
        self.gps_condition_edit.setObjectName("gps_condition_edit")
        self.gps_threadid_sbox = QtWidgets.QSpinBox(self.tab_9)
        self.gps_threadid_sbox.setGeometry(QtCore.QRect(120, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gps_threadid_sbox.setFont(font)
        self.gps_threadid_sbox.setMinimum(2)
        self.gps_threadid_sbox.setMaximum(6000)
        self.gps_threadid_sbox.setSingleStep(1)
        self.gps_threadid_sbox.setProperty("value", 2)
        self.gps_threadid_sbox.setObjectName("gps_threadid_sbox")
        self.gps_group_sbox = QtWidgets.QSpinBox(self.tab_9)
        self.gps_group_sbox.setEnabled(False)
        self.gps_group_sbox.setGeometry(QtCore.QRect(120, 210, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gps_group_sbox.setFont(font)
        self.gps_group_sbox.setMinimum(0)
        self.gps_group_sbox.setMaximum(6000)
        self.gps_group_sbox.setSingleStep(1)
        self.gps_group_sbox.setProperty("value", 1)
        self.gps_group_sbox.setObjectName("gps_group_sbox")
        self.gps_force_sbox = QtWidgets.QSpinBox(self.tab_9)
        self.gps_force_sbox.setEnabled(False)
        self.gps_force_sbox.setGeometry(QtCore.QRect(120, 170, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gps_force_sbox.setFont(font)
        self.gps_force_sbox.setMinimum(0)
        self.gps_force_sbox.setMaximum(6000)
        self.gps_force_sbox.setSingleStep(1)
        self.gps_force_sbox.setProperty("value", 1)
        self.gps_force_sbox.setObjectName("gps_force_sbox")
        self.gps_table = QtWidgets.QTableWidget(self.tab_9)
        self.gps_table.setGeometry(QtCore.QRect(10, 290, 581, 150))
        self.gps_table.setObjectName("gps_table")
        self.gps_table.setColumnCount(6)
        self.gps_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gps_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gps_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gps_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gps_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.gps_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.gps_table.setHorizontalHeaderItem(5, item)
        self.gps_apagar_bt = QtWidgets.QPushButton(self.tab_9)
        self.gps_apagar_bt.setGeometry(QtCore.QRect(500, 250, 91, 31))
        self.gps_apagar_bt.setObjectName("gps_apagar_bt")
        self.gps_streamid_cbox = QtWidgets.QComboBox(self.tab_9)
        self.gps_streamid_cbox.setGeometry(QtCore.QRect(290, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gps_streamid_cbox.setFont(font)
        self.gps_streamid_cbox.setObjectName("gps_streamid_cbox")
        self.gps_apagar_streamid_bt = QtWidgets.QPushButton(self.tab_9)
        self.gps_apagar_streamid_bt.setGeometry(QtCore.QRect(450, 50, 61, 31))
        self.gps_apagar_streamid_bt.setObjectName("gps_apagar_streamid_bt")
        self.gps_inserir_streamid_bt = QtWidgets.QPushButton(self.tab_9)
        self.gps_inserir_streamid_bt.setGeometry(QtCore.QRect(380, 50, 61, 31))
        self.gps_inserir_streamid_bt.setObjectName("gps_inserir_streamid_bt")
        self.gps_streamid_edit = QtWidgets.QLineEdit(self.tab_9)
        self.gps_streamid_edit.setEnabled(True)
        self.gps_streamid_edit.setGeometry(QtCore.QRect(120, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gps_streamid_edit.setFont(font)
        self.gps_streamid_edit.setReadOnly(True)
        self.gps_streamid_edit.setObjectName("gps_streamid_edit")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.info_threadid_label = QtWidgets.QLabel(self.tab_10)
        self.info_threadid_label.setGeometry(QtCore.QRect(21, 10, 81, 31))
        self.info_threadid_label.setObjectName("info_threadid_label")
        self.info_group_label = QtWidgets.QLabel(self.tab_10)
        self.info_group_label.setGeometry(QtCore.QRect(37, 170, 47, 31))
        self.info_group_label.setObjectName("info_group_label")
        self.info_streamid_label = QtWidgets.QLabel(self.tab_10)
        self.info_streamid_label.setGeometry(QtCore.QRect(30, 50, 61, 31))
        self.info_streamid_label.setObjectName("info_streamid_label")
        self.info_condition_label = QtWidgets.QLabel(self.tab_10)
        self.info_condition_label.setGeometry(QtCore.QRect(30, 90, 61, 31))
        self.info_condition_label.setObjectName("info_condition_label")
        self.info_inserir_bt = QtWidgets.QPushButton(self.tab_10)
        self.info_inserir_bt.setGeometry(QtCore.QRect(390, 250, 91, 31))
        self.info_inserir_bt.setObjectName("info_inserir_bt")
        self.info_desc_edit = QtWidgets.QLineEdit(self.tab_10)
        self.info_desc_edit.setGeometry(QtCore.QRect(120, 130, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_desc_edit.setFont(font)
        self.info_desc_edit.setObjectName("info_desc_edit")
        self.info_condition_edit = QtWidgets.QLineEdit(self.tab_10)
        self.info_condition_edit.setGeometry(QtCore.QRect(120, 90, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_condition_edit.setFont(font)
        self.info_condition_edit.setObjectName("info_condition_edit")
        self.info_desc_label = QtWidgets.QLabel(self.tab_10)
        self.info_desc_label.setGeometry(QtCore.QRect(25, 130, 71, 31))
        self.info_desc_label.setObjectName("info_desc_label")
        self.info_group_check = QtWidgets.QCheckBox(self.tab_10)
        self.info_group_check.setGeometry(QtCore.QRect(100, 170, 20, 31))
        self.info_group_check.setText("")
        self.info_group_check.setObjectName("info_group_check")
        self.info_threadid_sbox = QtWidgets.QSpinBox(self.tab_10)
        self.info_threadid_sbox.setGeometry(QtCore.QRect(120, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_threadid_sbox.setFont(font)
        self.info_threadid_sbox.setMinimum(2)
        self.info_threadid_sbox.setMaximum(6000)
        self.info_threadid_sbox.setSingleStep(1)
        self.info_threadid_sbox.setProperty("value", 2)
        self.info_threadid_sbox.setObjectName("info_threadid_sbox")
        self.info_group_sbox = QtWidgets.QSpinBox(self.tab_10)
        self.info_group_sbox.setEnabled(False)
        self.info_group_sbox.setGeometry(QtCore.QRect(120, 170, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_group_sbox.setFont(font)
        self.info_group_sbox.setMinimum(0)
        self.info_group_sbox.setMaximum(6000)
        self.info_group_sbox.setSingleStep(1)
        self.info_group_sbox.setProperty("value", 1)
        self.info_group_sbox.setObjectName("info_group_sbox")
        self.info_table = QtWidgets.QTableWidget(self.tab_10)
        self.info_table.setGeometry(QtCore.QRect(10, 290, 581, 150))
        self.info_table.setObjectName("info_table")
        self.info_table.setColumnCount(5)
        self.info_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setHorizontalHeaderItem(4, item)
        self.info_apagar_bt = QtWidgets.QPushButton(self.tab_10)
        self.info_apagar_bt.setGeometry(QtCore.QRect(500, 250, 91, 31))
        self.info_apagar_bt.setObjectName("info_apagar_bt")
        self.info_streamid_cbox = QtWidgets.QComboBox(self.tab_10)
        self.info_streamid_cbox.setGeometry(QtCore.QRect(290, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_streamid_cbox.setFont(font)
        self.info_streamid_cbox.setObjectName("info_streamid_cbox")
        self.info_apagar_streamid_bt = QtWidgets.QPushButton(self.tab_10)
        self.info_apagar_streamid_bt.setGeometry(QtCore.QRect(450, 50, 61, 31))
        self.info_apagar_streamid_bt.setObjectName("info_apagar_streamid_bt")
        self.info_inserir_streamid_bt = QtWidgets.QPushButton(self.tab_10)
        self.info_inserir_streamid_bt.setGeometry(QtCore.QRect(380, 50, 61, 31))
        self.info_inserir_streamid_bt.setObjectName("info_inserir_streamid_bt")
        self.info_streamid_edit = QtWidgets.QLineEdit(self.tab_10)
        self.info_streamid_edit.setEnabled(True)
        self.info_streamid_edit.setGeometry(QtCore.QRect(120, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.info_streamid_edit.setFont(font)
        self.info_streamid_edit.setReadOnly(True)
        self.info_streamid_edit.setObjectName("info_streamid_edit")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.audit_apagar_streamid_bt = QtWidgets.QPushButton(self.tab_4)
        self.audit_apagar_streamid_bt.setGeometry(QtCore.QRect(450, 50, 61, 31))
        self.audit_apagar_streamid_bt.setObjectName("audit_apagar_streamid_bt")
        self.audit_group_label = QtWidgets.QLabel(self.tab_4)
        self.audit_group_label.setGeometry(QtCore.QRect(37, 170, 47, 31))
        self.audit_group_label.setObjectName("audit_group_label")
        self.audit_inserir_streamid_bt = QtWidgets.QPushButton(self.tab_4)
        self.audit_inserir_streamid_bt.setGeometry(QtCore.QRect(380, 50, 61, 31))
        self.audit_inserir_streamid_bt.setObjectName("audit_inserir_streamid_bt")
        self.audit_threadid_sbox = QtWidgets.QSpinBox(self.tab_4)
        self.audit_threadid_sbox.setGeometry(QtCore.QRect(120, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.audit_threadid_sbox.setFont(font)
        self.audit_threadid_sbox.setMinimum(2)
        self.audit_threadid_sbox.setMaximum(6000)
        self.audit_threadid_sbox.setSingleStep(1)
        self.audit_threadid_sbox.setProperty("value", 2)
        self.audit_threadid_sbox.setObjectName("audit_threadid_sbox")
        self.audit_condition_edit = QtWidgets.QLineEdit(self.tab_4)
        self.audit_condition_edit.setGeometry(QtCore.QRect(120, 90, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.audit_condition_edit.setFont(font)
        self.audit_condition_edit.setObjectName("audit_condition_edit")
        self.audit_apagar_bt = QtWidgets.QPushButton(self.tab_4)
        self.audit_apagar_bt.setGeometry(QtCore.QRect(500, 250, 91, 31))
        self.audit_apagar_bt.setObjectName("audit_apagar_bt")
        self.audit_table = QtWidgets.QTableWidget(self.tab_4)
        self.audit_table.setGeometry(QtCore.QRect(10, 290, 581, 150))
        self.audit_table.setObjectName("audit_table")
        self.audit_table.setColumnCount(5)
        self.audit_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.audit_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.audit_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.audit_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.audit_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.audit_table.setHorizontalHeaderItem(4, item)
        self.audit_streamid_label = QtWidgets.QLabel(self.tab_4)
        self.audit_streamid_label.setGeometry(QtCore.QRect(30, 50, 61, 31))
        self.audit_streamid_label.setObjectName("audit_streamid_label")
        self.audit_streamid_edit = QtWidgets.QLineEdit(self.tab_4)
        self.audit_streamid_edit.setEnabled(True)
        self.audit_streamid_edit.setGeometry(QtCore.QRect(120, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.audit_streamid_edit.setFont(font)
        self.audit_streamid_edit.setReadOnly(True)
        self.audit_streamid_edit.setObjectName("audit_streamid_edit")
        self.audit_desc_edit = QtWidgets.QLineEdit(self.tab_4)
        self.audit_desc_edit.setGeometry(QtCore.QRect(120, 130, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.audit_desc_edit.setFont(font)
        self.audit_desc_edit.setObjectName("audit_desc_edit")
        self.audit_inserir_bt = QtWidgets.QPushButton(self.tab_4)
        self.audit_inserir_bt.setGeometry(QtCore.QRect(390, 250, 91, 31))
        self.audit_inserir_bt.setObjectName("audit_inserir_bt")
        self.audit_streamid_cbox = QtWidgets.QComboBox(self.tab_4)
        self.audit_streamid_cbox.setGeometry(QtCore.QRect(290, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.audit_streamid_cbox.setFont(font)
        self.audit_streamid_cbox.setObjectName("audit_streamid_cbox")
        self.audit_group_check = QtWidgets.QCheckBox(self.tab_4)
        self.audit_group_check.setGeometry(QtCore.QRect(100, 170, 20, 31))
        self.audit_group_check.setText("")
        self.audit_group_check.setObjectName("audit_group_check")
        self.audit_condition_label = QtWidgets.QLabel(self.tab_4)
        self.audit_condition_label.setGeometry(QtCore.QRect(30, 90, 61, 31))
        self.audit_condition_label.setObjectName("audit_condition_label")
        self.audit_group_sbox = QtWidgets.QSpinBox(self.tab_4)
        self.audit_group_sbox.setEnabled(False)
        self.audit_group_sbox.setGeometry(QtCore.QRect(120, 170, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.audit_group_sbox.setFont(font)
        self.audit_group_sbox.setMinimum(0)
        self.audit_group_sbox.setMaximum(6000)
        self.audit_group_sbox.setSingleStep(1)
        self.audit_group_sbox.setProperty("value", 1)
        self.audit_group_sbox.setObjectName("audit_group_sbox")
        self.audit_threadid_label = QtWidgets.QLabel(self.tab_4)
        self.audit_threadid_label.setGeometry(QtCore.QRect(21, 10, 81, 31))
        self.audit_threadid_label.setObjectName("audit_threadid_label")
        self.audit_desc_label = QtWidgets.QLabel(self.tab_4)
        self.audit_desc_label.setGeometry(QtCore.QRect(25, 130, 71, 31))
        self.audit_desc_label.setObjectName("audit_desc_label")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.finalizar_bt_2 = QtWidgets.QPushButton(self.tab)
        self.finalizar_bt_2.setGeometry(QtCore.QRect(289, 500, 91, 31))
        self.finalizar_bt_2.setObjectName("finalizar_bt_2")
        self.msg_streamid_cbox = QtWidgets.QComboBox(self.tab)
        self.msg_streamid_cbox.setGeometry(QtCore.QRect(290, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.msg_streamid_cbox.setFont(font)
        self.msg_streamid_cbox.setObjectName("msg_streamid_cbox")
        self.msg_group_check = QtWidgets.QCheckBox(self.tab)
        self.msg_group_check.setGeometry(QtCore.QRect(100, 170, 20, 31))
        self.msg_group_check.setText("")
        self.msg_group_check.setObjectName("msg_group_check")
        self.msg_group_sbox = QtWidgets.QSpinBox(self.tab)
        self.msg_group_sbox.setEnabled(False)
        self.msg_group_sbox.setGeometry(QtCore.QRect(120, 170, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.msg_group_sbox.setFont(font)
        self.msg_group_sbox.setMinimum(0)
        self.msg_group_sbox.setMaximum(6000)
        self.msg_group_sbox.setSingleStep(1)
        self.msg_group_sbox.setProperty("value", 1)
        self.msg_group_sbox.setObjectName("msg_group_sbox")
        self.msg_condition_label = QtWidgets.QLabel(self.tab)
        self.msg_condition_label.setGeometry(QtCore.QRect(30, 90, 61, 31))
        self.msg_condition_label.setObjectName("msg_condition_label")
        self.msg_table = QtWidgets.QTableWidget(self.tab)
        self.msg_table.setGeometry(QtCore.QRect(10, 290, 581, 150))
        self.msg_table.setObjectName("msg_table")
        self.msg_table.setColumnCount(5)
        self.msg_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.msg_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.msg_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.msg_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.msg_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.msg_table.setHorizontalHeaderItem(4, item)
        self.msg_desc_label = QtWidgets.QLabel(self.tab)
        self.msg_desc_label.setGeometry(QtCore.QRect(25, 130, 71, 31))
        self.msg_desc_label.setObjectName("msg_desc_label")
        self.msg_group_label = QtWidgets.QLabel(self.tab)
        self.msg_group_label.setGeometry(QtCore.QRect(37, 170, 47, 31))
        self.msg_group_label.setObjectName("msg_group_label")
        self.msg_inserir_bt = QtWidgets.QPushButton(self.tab)
        self.msg_inserir_bt.setGeometry(QtCore.QRect(390, 250, 91, 31))
        self.msg_inserir_bt.setObjectName("msg_inserir_bt")
        self.msg_desc_edit = QtWidgets.QLineEdit(self.tab)
        self.msg_desc_edit.setGeometry(QtCore.QRect(120, 130, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.msg_desc_edit.setFont(font)
        self.msg_desc_edit.setObjectName("msg_desc_edit")
        self.msg_threadid_sbox = QtWidgets.QSpinBox(self.tab)
        self.msg_threadid_sbox.setGeometry(QtCore.QRect(120, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.msg_threadid_sbox.setFont(font)
        self.msg_threadid_sbox.setMinimum(2)
        self.msg_threadid_sbox.setMaximum(6000)
        self.msg_threadid_sbox.setSingleStep(1)
        self.msg_threadid_sbox.setProperty("value", 2)
        self.msg_threadid_sbox.setObjectName("msg_threadid_sbox")
        self.msg_apagar_bt = QtWidgets.QPushButton(self.tab)
        self.msg_apagar_bt.setGeometry(QtCore.QRect(500, 250, 91, 31))
        self.msg_apagar_bt.setObjectName("msg_apagar_bt")
        self.msg_condition_edit = QtWidgets.QLineEdit(self.tab)
        self.msg_condition_edit.setGeometry(QtCore.QRect(120, 90, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.msg_condition_edit.setFont(font)
        self.msg_condition_edit.setObjectName("msg_condition_edit")
        self.msg_streamid_label = QtWidgets.QLabel(self.tab)
        self.msg_streamid_label.setGeometry(QtCore.QRect(30, 50, 61, 31))
        self.msg_streamid_label.setObjectName("msg_streamid_label")
        self.msg_apagar_streamid_bt = QtWidgets.QPushButton(self.tab)
        self.msg_apagar_streamid_bt.setGeometry(QtCore.QRect(450, 50, 61, 31))
        self.msg_apagar_streamid_bt.setObjectName("msg_apagar_streamid_bt")
        self.msg_inserir_streamid_bt = QtWidgets.QPushButton(self.tab)
        self.msg_inserir_streamid_bt.setGeometry(QtCore.QRect(380, 50, 61, 31))
        self.msg_inserir_streamid_bt.setObjectName("msg_inserir_streamid_bt")
        self.msg_streamid_edit = QtWidgets.QLineEdit(self.tab)
        self.msg_streamid_edit.setEnabled(True)
        self.msg_streamid_edit.setGeometry(QtCore.QRect(120, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.msg_streamid_edit.setFont(font)
        self.msg_streamid_edit.setReadOnly(True)
        self.msg_streamid_edit.setObjectName("msg_streamid_edit")
        self.msg_threadid_label = QtWidgets.QLabel(self.tab)
        self.msg_threadid_label.setGeometry(QtCore.QRect(21, 10, 81, 31))
        self.msg_threadid_label.setObjectName("msg_threadid_label")
        self.tabWidget.addTab(self.tab, "")
        self.finalizar_bt = QtWidgets.QPushButton(T2_Timer)
        self.finalizar_bt.setGeometry(QtCore.QRect(280, 500, 91, 31))
        self.finalizar_bt.setObjectName("finalizar_bt")

        self.retranslateUi(T2_Timer)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(T2_Timer)

    def retranslateUi(self, T2_Timer):
        _translate = QtCore.QCoreApplication.translate
        T2_Timer.setWindowTitle(_translate("T2_Timer", "Dialog"))
        self.gps_group_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Grupo<br/></span>(group)</p></body></html>"))
        self.gps_threadid_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Identificador</span><br/>(threadid)</p></body></html>"))
        self.gps_force_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Forçar<br/></span>(force)</p></body></html>"))
        self.gps_inserir_bt.setText(_translate("T2_Timer", "inserir"))
        self.gps_desc_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Descrição<br/></span>(desc)</p></body></html>"))
        self.gps_streamid_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Saída</span><br/>(streamid)</p></body></html>"))
        self.gps_condition_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Condição<br/></span>(condition)</p></body></html>"))
        item = self.gps_table.horizontalHeaderItem(0)
        item.setText(_translate("T2_Timer", "Threadid"))
        item = self.gps_table.horizontalHeaderItem(1)
        item.setText(_translate("T2_Timer", "Streamid"))
        item = self.gps_table.horizontalHeaderItem(2)
        item.setText(_translate("T2_Timer", "Condition"))
        item = self.gps_table.horizontalHeaderItem(3)
        item.setText(_translate("T2_Timer", "Desc"))
        item = self.gps_table.horizontalHeaderItem(4)
        item.setText(_translate("T2_Timer", "Force"))
        item = self.gps_table.horizontalHeaderItem(5)
        item.setText(_translate("T2_Timer", "Group"))
        self.gps_apagar_bt.setText(_translate("T2_Timer", "apagar"))
        self.gps_apagar_streamid_bt.setText(_translate("T2_Timer", "apagar"))
        self.gps_inserir_streamid_bt.setText(_translate("T2_Timer", "inserir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("T2_Timer", "Localização (gps)"))
        self.info_threadid_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Identificador</span><br/>(threadid)</p></body></html>"))
        self.info_group_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Grupo<br/></span>(group)</p></body></html>"))
        self.info_streamid_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Saída</span><br/>(streamid)</p></body></html>"))
        self.info_condition_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Condição<br/></span>(condition)</p></body></html>"))
        self.info_inserir_bt.setText(_translate("T2_Timer", "inserir"))
        self.info_desc_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Descrição<br/></span>(desc)</p></body></html>"))
        item = self.info_table.horizontalHeaderItem(0)
        item.setText(_translate("T2_Timer", "Threadid"))
        item = self.info_table.horizontalHeaderItem(1)
        item.setText(_translate("T2_Timer", "Streamid"))
        item = self.info_table.horizontalHeaderItem(2)
        item.setText(_translate("T2_Timer", "Condition"))
        item = self.info_table.horizontalHeaderItem(3)
        item.setText(_translate("T2_Timer", "Desc"))
        item = self.info_table.horizontalHeaderItem(4)
        item.setText(_translate("T2_Timer", "Group"))
        self.info_apagar_bt.setText(_translate("T2_Timer", "apagar"))
        self.info_apagar_streamid_bt.setText(_translate("T2_Timer", "apagar"))
        self.info_inserir_streamid_bt.setText(_translate("T2_Timer", "inserir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("T2_Timer", "Informação (info)"))
        self.audit_apagar_streamid_bt.setText(_translate("T2_Timer", "apagar"))
        self.audit_group_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Grupo<br/></span>(group)</p></body></html>"))
        self.audit_inserir_streamid_bt.setText(_translate("T2_Timer", "inserir"))
        self.audit_apagar_bt.setText(_translate("T2_Timer", "apagar"))
        item = self.audit_table.horizontalHeaderItem(0)
        item.setText(_translate("T2_Timer", "Threadid"))
        item = self.audit_table.horizontalHeaderItem(1)
        item.setText(_translate("T2_Timer", "Streamid"))
        item = self.audit_table.horizontalHeaderItem(2)
        item.setText(_translate("T2_Timer", "Condition"))
        item = self.audit_table.horizontalHeaderItem(3)
        item.setText(_translate("T2_Timer", "Desc"))
        item = self.audit_table.horizontalHeaderItem(4)
        item.setText(_translate("T2_Timer", "Group"))
        self.audit_streamid_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Saída</span><br/>(streamid)</p></body></html>"))
        self.audit_inserir_bt.setText(_translate("T2_Timer", "inserir"))
        self.audit_condition_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Condição<br/></span>(condition)</p></body></html>"))
        self.audit_threadid_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Identificador</span><br/>(threadid)</p></body></html>"))
        self.audit_desc_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Descrição<br/></span>(desc)</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("T2_Timer", "Auditoria (audit)"))
        self.finalizar_bt_2.setText(_translate("T2_Timer", "finalizar"))
        self.msg_condition_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Condição<br/></span>(condition)</p></body></html>"))
        item = self.msg_table.horizontalHeaderItem(0)
        item.setText(_translate("T2_Timer", "Threadid"))
        item = self.msg_table.horizontalHeaderItem(1)
        item.setText(_translate("T2_Timer", "Streamid"))
        item = self.msg_table.horizontalHeaderItem(2)
        item.setText(_translate("T2_Timer", "Condition"))
        item = self.msg_table.horizontalHeaderItem(3)
        item.setText(_translate("T2_Timer", "Desc"))
        item = self.msg_table.horizontalHeaderItem(4)
        item.setText(_translate("T2_Timer", "Group"))
        self.msg_desc_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Descrição<br/></span>(desc)</p></body></html>"))
        self.msg_group_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Grupo<br/></span>(group)</p></body></html>"))
        self.msg_inserir_bt.setText(_translate("T2_Timer", "inserir"))
        self.msg_apagar_bt.setText(_translate("T2_Timer", "apagar"))
        self.msg_streamid_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Saída</span><br/>(streamid)</p></body></html>"))
        self.msg_apagar_streamid_bt.setText(_translate("T2_Timer", "apagar"))
        self.msg_inserir_streamid_bt.setText(_translate("T2_Timer", "inserir"))
        self.msg_threadid_label.setText(_translate("T2_Timer", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Identificador</span><br/>(threadid)</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("T2_Timer", "Mensagem (message)"))
        self.finalizar_bt.setText(_translate("T2_Timer", "finalizar"))
