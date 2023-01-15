# pyuic5 RFNode_GUI_5.ui -o RFNode_GUI_5.py

from PyQt5 import QtCore, QtGui, QtWidgets
from RFNode_GUI_18_Scan import Ui_Dialog
from RFNode_GUI_18_Timer import Ui_T2_Timer
from RFNode_GUI_18 import Ui_MainWindow
import copy
import os
import func
import ctypes

myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class TasksWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(TasksWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('resources/if_logo-removebg-preview.ico'))


class TasksWindowTimer(QtWidgets.QDialog, Ui_T2_Timer):
    def __init__(self):
        super(TasksWindowTimer, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('resources/if_logo-removebg-preview.ico'))


class PrincipalWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(PrincipalWindow, self).__init__()
        self.setupUi(self)
        self.window = TasksWindow()
        self.window.setupUi(self.window)
        self.window_timer = TasksWindowTimer()
        self.window_timer.setupUi(self.window_timer)
        self.setWindowIcon(QtGui.QIcon('resources/if_logo-removebg-preview.ico'))

        # Validação de existencia de identificador
        alfabeto = "[abcdefghijklmnopqrstuvwxyz1234567890_-]{50}"
        self.conf_var_edit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(alfabeto)))

        alfabeto_nome_scan = "[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_-]{50}"
        # Validação caracteres para nome do bloco de execução
        self.scan_nome_edit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(alfabeto_nome_scan)))

        # Validação de existencia de identificador
        alfabeto = "[abcdefghijklmnopqrstuvwxyz]"
        self.stream_id_edit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp(alfabeto)))

        # validação numerica para udp
        self.stream_porta_edit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{50}")))

        # validação numerica para scan e timer intervalo
        self.scan_inter_edit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{50}")))

        # validação do campo de valor variaveis livres
        self.conf_valor_edit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{50}")))

        # validação numerica para scan e timer resolução
        # self.scan_resol_edit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{50}")))

        # troca a cor de fundo da scroll area
        self.prev_area.setStyleSheet("background-color: white")

        # self.scan_lista_lwid.setStyleSheet("QListWidget::item { border: 0px solid black; }")

        # self.prev_area.keyPressEvent(self.atualiza_texto, QtCore.Qt.Key_Enter)

        self.conf_tipo_cbox.currentTextChanged.connect(self.limpa_bloco)
        # evento botao tasks preview
        self.scan_tarefas_bt.clicked.connect(self.selecionaaaasada_bloco)
        # evento botao inserir identificador
        self.conf_inserir_bt.clicked.connect(self.inserir_variaveis)
        # evento botao inserir identificador
        self.conf_apagar_bt.clicked.connect(self.remover_variavel)
        # evento botao inserir identificador
        self.stream_inserir_bt.clicked.connect(self.inserir_stream)
        # evento botao apagar identificador
        self.stream_apagar_bt.clicked.connect(self.apagar_stream)
        # evento botao inserir timer
        self.scan_inserir_bt.clicked.connect(self.inserir_execucao)
        # evento botao apagar bloco de execução
        self.scan_apagar_bt_3.clicked.connect(self.apagar_blocos)
        # evento botao inserir scan
        self.prev_gerar_bt.clicked.connect(self.gerar_arquivo)
        # evento botao preview
        self.prev_preview_bt.clicked.connect(self.render_preview)
        # logica habilita/desabilita radio button
        self.stream_http_radio.toggled.connect(self.habilita_http)
        self.stream_udp_radio.toggled.connect(self.habilita_udp)
        self.stream_arq_radio.toggled.connect(self.habilita_arquivo)
        self.scan_timer_radio.toggled.connect(self.habilita_timer)
        self.scan_scan_radio.toggled.connect(self.habilita_scan)
        self.scan_finicial_radio.toggled.connect(self.habilita_flimites)
        self.scan_central_radio.toggled.connect(self.habilita_fcentral)
        self.conf_tamanho_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_tamanho_check', 'conf_tamanho_sbox'))
        self.conf_estacao_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_estacao_check', 'conf_estacao_edit'))
        self.conf_dir_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_dir_check', 'conf_dir_edit'))
        self.conf_metodo_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_metodo_check', 'conf_metodo_edit'))
        self.conf_logdir_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_logdir_check', 'conf_logdir_edit'))
        self.conf_logdir_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_logdir_check', 'conf_logname_edit'))
        # avançado
        self.conf_versao_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_versao_check', 'conf_versao_sbox'))
        self.conf_antena_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_antena_check', 'conf_antena_sbox'))
        self.conf_logmax_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_logmax_check', 'conf_logmax_sbox'))
        self.conf_logback_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_logback_check', 'conf_logback_sbox'))
        self.conf_loglevel_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_loglevel_check', 'conf_loglevel_cbox'))
        self.conf_logfalldir_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_logfalldir_check', 'conf_logfalldir_edit'))
        self.conf_logfalldir_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_logfalldir_check', 'conf_logfallname_edit'))
        self.conf_udpport_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_udpport_check', 'conf_udpport_sbox'))
        self.conf_httpport_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_httpport_check', 'conf_httpport_sbox'))
        self.conf_latitude_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_latitude_check', 'conf_latitude_sbox'))
        self.conf_longitude_check.stateChanged.connect \
            (lambda: self.habilita_campo('conf_longitude_check', 'conf_longitude_sbox'))

    linha_occ = 0
    linha_peak = 0
    linha_gps = 0
    linha_info = 0
    linha_mean = 0
    linha_audit = 0
    linha_msg = 0

    list_tasks_occ = []
    list_tasks_peak = []
    list_tasks_gps = []
    list_tasks_info = []
    list_tasks_mean = []
    list_tasks_audit = []
    list_tasks_msg = []

    task_occ = ''
    task_peak = ''
    task_gps = ''
    task_info = ''
    task_mean = ''
    task_audit = ''
    task_msg = ''

    def limpa_bloco(self):
        self.conf_valor_edit.setText('')
        if self.conf_tipo_cbox.currentText() == 'numérico':
            self.conf_valor_edit.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]{50}")))
        else:
            self.conf_valor_edit.setValidator(None)

    def seleciona_bloco(self):
        if self.scan_scan_radio.isChecked():
            self.abre_tasks()
        else:
            self.abre_tasks_timer()

    def abre_tasks_timer(self):
        self.window_timer.gps_streamid_cbox.clear()
        self.window_timer.gps_streamid_cbox.addItems(self.list_id)

        self.window_timer.info_streamid_cbox.clear()
        self.window_timer.info_streamid_cbox.addItems(self.list_id)

        self.window_timer.audit_streamid_cbox.clear()
        self.window_timer.audit_streamid_cbox.addItems(self.list_id)

        self.window_timer.msg_streamid_cbox.clear()
        self.window_timer.msg_streamid_cbox.addItems(self.list_id)

        self.window_timer.gps_inserir_bt.clicked.connect(self.inserir_gps)
        self.window_timer.info_inserir_bt.clicked.connect(self.inserir_info)
        self.window_timer.audit_inserir_bt.clicked.connect(self.inserir_audit)
        self.window_timer.msg_inserir_bt.clicked.connect(self.inserir_msg)

        # evento botao finalizar
        self.window_timer.finalizar_bt.clicked.connect(self.finalizar_tarefa)
        self.window_timer.gps_apagar_bt.clicked.connect(lambda: self.excluir_linha('gps'))
        self.window_timer.info_apagar_bt.clicked.connect(lambda: self.excluir_linha('info'))
        self.window_timer.audit_apagar_bt.clicked.connect(lambda: self.excluir_linha('audit'))
        self.window_timer.msg_apagar_bt.clicked.connect(lambda: self.excluir_linha('msg'))

        self.window_timer.gps_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('gps'))
        self.window_timer.info_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('info'))
        self.window_timer.audit_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('audit'))
        self.window_timer.msg_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('msg'))

        self.window_timer.gps_apagar_streamid_bt.clicked.connect(lambda: self.apagar_streamid('gps'))
        self.window_timer.info_apagar_streamid_bt.clicked.connect(lambda: self.apagar_streamid('info'))
        self.window_timer.audit_apagar_streamid_bt.clicked.connect(lambda: self.apagar_streamid('audit'))
        self.window_timer.msg_apagar_streamid_bt.clicked.connect(lambda: self.apagar_streamid('msg'))

        self.window_timer.gps_force_check.stateChanged.connect \
            (lambda: self.habilita_campo('gps_force_check', 'gps_force_sbox'))
        self.window_timer.gps_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('gps_group_check', 'gps_group_sbox'))
        self.window_timer.info_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('info_group_check', 'info_group_sbox'))
        self.window_timer.audit_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('audit_group_check', 'audit_group_sbox'))
        self.window_timer.msg_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('msg_group_check', 'msg_group_sbox'))
        self.window_timer.exec_()

    def abre_tasks(self):
        self.window.occ_streamid_cbox.clear()
        self.window.occ_streamid_cbox.addItems(self.list_id)

        self.window.peak_streamid_cbox.clear()
        self.window.peak_streamid_cbox.addItems(self.list_id)

        self.window.gps_streamid_cbox.clear()
        self.window.gps_streamid_cbox.addItems(self.list_id)

        self.window.info_streamid_cbox.clear()
        self.window.info_streamid_cbox.addItems(self.list_id)

        self.window.mean_streamid_cbox.clear()
        self.window.mean_streamid_cbox.addItems(self.list_id)

        self.window.audit_streamid_cbox.clear()
        self.window.audit_streamid_cbox.addItems(self.list_id)

        self.window.msg_streamid_cbox.clear()
        self.window.msg_streamid_cbox.addItems(self.list_id)

        self.window.occ_inserir_bt.clicked.connect(self.inserir_occ)
        self.window.peak_inserir_bt.clicked.connect(self.inserir_peak)
        self.window.gps_inserir_bt.clicked.connect(self.inserir_gps)
        self.window.info_inserir_bt.clicked.connect(self.inserir_info)
        self.window.mean_inserir_bt.clicked.connect(self.inserir_mean)
        self.window.audit_inserir_bt.clicked.connect(self.inserir_audit)
        self.window.msg_inserir_bt.clicked.connect(self.inserir_msg)

        # evento botao finalizar
        self.window.finalizar_bt.clicked.connect(self.finalizar_tarefa)
        self.window.occ_apagar_bt.clicked.connect(lambda: self.excluir_linha('occ'))
        self.window.peak_apagar_bt.clicked.connect(lambda: self.excluir_linha('peak'))
        self.window.gps_apagar_bt.clicked.connect(lambda: self.excluir_linha('gps'))
        self.window.info_apagar_bt.clicked.connect(lambda: self.excluir_linha('info'))
        self.window.mean_apagar_bt.clicked.connect(lambda: self.excluir_linha('mean'))
        self.window.audit_apagar_bt.clicked.connect(lambda: self.excluir_linha('audit'))
        self.window.msg_apagar_bt.clicked.connect(lambda: self.excluir_linha('msg'))

        # self.window.occ_inserir_streamid_bt.clicked.connect(self.inserir_streamid_occ)
        # self.window.occ_apagar_streamid_bt.clicked.connect(self.apagar_streamid_occ)

        self.window.occ_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('occ'))
        self.window.peak_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('peak'))
        self.window.gps_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('gps'))
        self.window.info_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('info'))
        self.window.mean_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('mean'))
        self.window.audit_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('audit'))
        self.window.msg_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('msg'))

        self.window_timer.gps_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('gps'))
        self.window_timer.info_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('info'))
        self.window_timer.audit_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('audit'))
        self.window_timer.msg_inserir_streamid_bt.clicked.connect(lambda: self.inserir_streamid('msg'))

        self.window.occ_apagar_streamid_bt.clicked.connect(lambda: self.apagar_streamid('occ'))
        self.window.peak_apagar_streamid_bt.clicked.connect(lambda: self.apagar_streamid('peak'))
        self.window.gps_apagar_streamid_bt.clicked.connect(lambda: self.apagar_streamid('gps'))
        self.window.info_apagar_streamid_bt.clicked.connect(lambda: self.apagar_streamid('info'))
        self.window.mean_apagar_streamid_bt.clicked.connect(lambda: self.apagar_streamid('mean'))
        self.window.audit_apagar_streamid_bt.clicked.connect(lambda: self.apagar_streamid('audit'))
        self.window.msg_apagar_streamid_bt.clicked.connect(lambda: self.apagar_streamid('msg'))

        self.window_timer.gps_force_check.stateChanged.connect \
            (lambda: self.habilita_campo('gps_force_check', 'gps_force_sbox'))
        self.window_timer.gps_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('gps_group_check', 'gps_group_sbox'))
        self.window_timer.info_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('info_group_check', 'info_group_sbox'))
        self.window_timer.audit_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('audit_group_check', 'audit_group_sbox'))
        self.window_timer.msg_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('msg_group_check', 'msg_group_sbox'))

        self.window.occ_trigger_check.stateChanged.connect \
            (lambda: self.habilita_campo('occ_trigger_check', 'occ_trigger_sbox'))
        self.window.occ_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('occ_group_check', 'occ_group_sbox'))
        self.window.peak_cont_check.stateChanged.connect \
            (lambda: self.habilita_campo('peak_cont_check', 'peak_cont_sbox'))
        self.window.peak_thresh_check.stateChanged.connect \
            (lambda: self.habilita_campo('peak_thresh_check', 'peak_thresh_sbox'))
        self.window.peak_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('peak_group_check', 'peak_group_sbox'))
        self.window.gps_force_check.stateChanged.connect \
            (lambda: self.habilita_campo('gps_force_check', 'gps_force_sbox'))
        self.window.gps_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('gps_group_check', 'gps_group_sbox'))
        self.window.info_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('info_group_check', 'info_group_sbox'))
        self.window.mean_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('mean_group_check', 'mean_group_sbox'))
        self.window.mean_thresh_check.stateChanged.connect \
            (lambda: self.habilita_campo('mean_thresh_check', 'mean_thresh_sbox'))
        self.window.audit_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('audit_group_check', 'audit_group_sbox'))
        self.window.msg_group_check.stateChanged.connect \
            (lambda: self.habilita_campo('msg_group_check', 'msg_group_sbox'))

        self.window.exec_()

    def inserir_streamid(self, task_tab):
        if task_tab == 'occ':
            if self.window.occ_streamid_cbox.currentText() not in self.window.occ_streamid_edit.text():
                self.window.occ_streamid_edit.setText(
                    self.window.occ_streamid_edit.text() + self.window.occ_streamid_cbox.currentText())
        if task_tab == 'peak':
            if self.window.peak_streamid_cbox.currentText() not in self.window.peak_streamid_edit.text():
                self.window.peak_streamid_edit.setText(
                    self.window.peak_streamid_edit.text() + self.window.peak_streamid_cbox.currentText())
        if task_tab == 'mean':
            if self.window.mean_streamid_cbox.currentText() not in self.window.mean_streamid_edit.text():
                self.window.mean_streamid_edit.setText(
                    self.window.mean_streamid_edit.text() + self.window.mean_streamid_cbox.currentText())
        if task_tab == 'gps':
            if self.scan_scan_radio.isChecked():
                if self.window.gps_streamid_cbox.currentText() not in self.window.gps_streamid_edit.text():
                    self.window.gps_streamid_edit.setText(
                        self.window.gps_streamid_edit.text() + self.window.gps_streamid_cbox.currentText())
            elif self.scan_timer_radio.isChecked():
                if self.window_timer.gps_streamid_cbox.currentText() not in self.window_timer.gps_streamid_edit.text():
                    self.window_timer.gps_streamid_edit.setText(
                        self.window_timer.gps_streamid_edit.text() + self.window_timer.gps_streamid_cbox.currentText())
        if task_tab == 'info':
            if self.scan_scan_radio.isChecked():
                if self.window.info_streamid_cbox.currentText() not in self.window.info_streamid_edit.text():
                    self.window.info_streamid_edit.setText(
                        self.window.info_streamid_edit.text() + self.window.info_streamid_cbox.currentText())
            elif self.scan_timer_radio.isChecked():
                if self.window_timer.info_streamid_cbox.currentText() not in self.window_timer.info_streamid_edit.text():
                    self.window_timer.info_streamid_edit.setText(
                        self.window_timer.info_streamid_edit.text() + self.window_timer.info_streamid_cbox.currentText())
        if task_tab == 'audit':
            if self.scan_scan_radio.isChecked():
                if self.window.audit_streamid_cbox.currentText() not in self.window.audit_streamid_edit.text():
                    self.window.audit_streamid_edit.setText(
                        self.window.audit_streamid_edit.text() + self.window.audit_streamid_cbox.currentText())
            elif self.scan_timer_radio.isChecked():
                if self.window_timer.audit_streamid_cbox.currentText() not in self.window_timer.audit_streamid_edit.text():
                    self.window_timer.audit_streamid_edit.setText(
                        self.window_timer.audit_streamid_edit.text() + self.window_timer.audit_streamid_cbox.currentText())
        if task_tab == 'msg':
            if self.scan_scan_radio.isChecked():
                if self.window.msg_streamid_cbox.currentText() not in self.window.msg_streamid_edit.text():
                    self.window.msg_streamid_edit.setText(
                        self.window.msg_streamid_edit.text() + self.window.msg_streamid_cbox.currentText())
            elif self.scan_timer_radio.isChecked():
                if self.window_timer.msg_streamid_cbox.currentText() not in self.window_timer.msg_streamid_edit.text():
                    self.window_timer.msg_streamid_edit.setText(
                        self.window_timer.msg_streamid_edit.text() + self.window_timer.msg_streamid_cbox.currentText())

    def apagar_streamid(self, task_tab):
        if task_tab == 'occ':
            texto_streamid_edit = self.window.occ_streamid_edit.text()
            texto_streamid_edit = texto_streamid_edit[:-1]
            self.window.occ_streamid_edit.clear()
            self.window.occ_streamid_edit.repaint()
            self.window.occ_streamid_edit.setText(str(texto_streamid_edit))
        if task_tab == 'peak':
            texto_streamid_edit = self.window.peak_streamid_edit.text()
            texto_streamid_edit = texto_streamid_edit[:-1]
            self.window.peak_streamid_edit.clear()
            self.window.peak_streamid_edit.repaint()
            self.window.peak_streamid_edit.setText(str(texto_streamid_edit))
        if task_tab == 'mean':
            texto_streamid_edit = self.window.mean_streamid_edit.text()
            texto_streamid_edit = texto_streamid_edit[:-1]
            self.window.mean_streamid_edit.clear()
            self.window.mean_streamid_edit.repaint()
            self.window.mean_streamid_edit.setText(str(texto_streamid_edit))
        if task_tab == 'gps':
            if self.scan_scan_radio.isChecked():
                texto_streamid_edit = self.window.gps_streamid_edit.text()
                texto_streamid_edit = texto_streamid_edit[:-1]
                self.window.gps_streamid_edit.clear()
                self.window.gps_streamid_edit.repaint()
                self.window.gps_streamid_edit.setText(str(texto_streamid_edit))
            elif self.scan_timer_radio.isChecked():
                texto_streamid_edit = self.window_timer.gps_streamid_edit.text()
                texto_streamid_edit = texto_streamid_edit[:-1]
                self.window_timer.gps_streamid_edit.clear()
                self.window_timer.gps_streamid_edit.repaint()
                self.window_timer.gps_streamid_edit.setText(str(texto_streamid_edit))
        if task_tab == 'info':
            if self.scan_scan_radio.isChecked():
                texto_streamid_edit = self.window.info_streamid_edit.text()
                texto_streamid_edit = texto_streamid_edit[:-1]
                self.window.info_streamid_edit.clear()
                self.window.info_streamid_edit.repaint()
                self.window.info_streamid_edit.setText(str(texto_streamid_edit))
            elif self.scan_timer_radio.isChecked():
                texto_streamid_edit = self.window_timer.info_streamid_edit.text()
                texto_streamid_edit = texto_streamid_edit[:-1]
                self.window_timer.info_streamid_edit.clear()
                self.window_timer.info_streamid_edit.repaint()
                self.window_timer.info_streamid_edit.setText(str(texto_streamid_edit))
        if task_tab == 'audit':
            if self.scan_scan_radio.isChecked():
                texto_streamid_edit = self.window.audit_streamid_edit.text()
                texto_streamid_edit = texto_streamid_edit[:-1]
                self.window.audit_streamid_edit.clear()
                self.window.audit_streamid_edit.repaint()
                self.window.audit_streamid_edit.setText(str(texto_streamid_edit))
            elif self.scan_timer_radio.isChecked():
                texto_streamid_edit = self.window_timer.audit_streamid_edit.text()
                texto_streamid_edit = texto_streamid_edit[:-1]
                self.window_timer.audit_streamid_edit.clear()
                self.window_timer.audit_streamid_edit.repaint()
                self.window_timer.audit_streamid_edit.setText(str(texto_streamid_edit))
        if task_tab == 'msg':
            if self.scan_scan_radio.isChecked():
                texto_streamid_edit = self.window.msg_streamid_edit.text()
                texto_streamid_edit = texto_streamid_edit[:-1]
                self.window.msg_streamid_edit.clear()
                self.window.msg_streamid_edit.repaint()
                self.window.msg_streamid_edit.setText(str(texto_streamid_edit))
            elif self.scan_timer_radio.isChecked():
                texto_streamid_edit = self.window_timer.msg_streamid_edit.text()
                texto_streamid_edit = texto_streamid_edit[:-1]
                self.window_timer.msg_streamid_edit.clear()
                self.window_timer.msg_streamid_edit.repaint()
                self.window_timer.msg_streamid_edit.setText(str(texto_streamid_edit))

    def inserir_occ(self):
        if self.window.occ_streamid_edit.text() != '' and self.window.occ_condition_edit.text() != '' \
                and self.window.occ_desc_edit.text() != '' and self.window.occ_threshold_sbox != '':

            self.window.occ_table.setRowCount(self.linha_occ + 1)
            self.window.occ_table.setItem(self.linha_occ, 0,
                                          QtWidgets.QTableWidgetItem(self.window.occ_threadid_sbox.text()))
            self.window.occ_table.setItem(self.linha_occ, 1,
                                          QtWidgets.QTableWidgetItem(self.window.occ_streamid_edit.text()))
            self.window.occ_table.setItem(self.linha_occ, 2,
                                          QtWidgets.QTableWidgetItem(self.window.occ_condition_edit.text()))
            self.window.occ_table.setItem(self.linha_occ, 3,
                                          QtWidgets.QTableWidgetItem(self.window.occ_desc_edit.text()))
            self.window.occ_table.setItem(self.linha_occ, 4,
                                          QtWidgets.QTableWidgetItem(self.window.occ_threshold_sbox.text()))

            if self.window.occ_trigger_check.isChecked():
                self.window.occ_table.setItem(self.linha_occ, 5,
                                              QtWidgets.QTableWidgetItem(self.window.occ_trigger_sbox.text()))
            else:
                self.window.occ_table.setItem(self.linha_occ, 5, QtWidgets.QTableWidgetItem(''))
            if self.window.occ_group_check.isChecked():
                self.window.occ_table.setItem(self.linha_occ, 6,
                                              QtWidgets.QTableWidgetItem(self.window.occ_group_sbox.text()))
            else:
                self.window.occ_table.setItem(self.linha_occ, 6, QtWidgets.QTableWidgetItem(''))

            self.task_occ += self.window.occ_table.item(self.linha_occ, 0).text() + ', '
            self.task_occ += self.window.occ_table.item(self.linha_occ, 1).text() + ', '
            self.task_occ += self.window.occ_table.item(self.linha_occ, 2).text() + ', '
            self.task_occ += '"' + self.window.occ_table.item(self.linha_occ, 3).text() + '"'
            self.task_occ += ', ' + self.window.occ_table.item(self.linha_occ, 4).text()
            if self.window.occ_trigger_check.isChecked():
                self.task_occ += ', trigger=' + self.window.occ_table.item(self.linha_occ, 5).text()
            if self.window.occ_group_check.isChecked():
                self.task_occ += ', group=' + self.window.occ_table.item(self.linha_occ, 6).text()
            self.list_tasks_occ.append(self.task_occ)

            self.task_occ = ''
            self.window.occ_streamid_edit.setText('')
            self.window.occ_condition_edit.setText('')
            self.window.occ_desc_edit.setText('')
            print(self.list_tasks_occ[self.linha_occ])
            print(self.list_tasks_occ)
            self.linha_occ = self.linha_occ + 1

    def inserir_peak(self):
        if self.window.peak_streamid_edit.text() != '' and \
                self.window.peak_condition_edit.text() != '' and \
                self.window.peak_desc_edit.text() != '':

            self.window.peak_table.setRowCount(self.linha_peak + 1)
            self.window.peak_table.setItem(self.linha_peak, 0,
                                           QtWidgets.QTableWidgetItem(self.window.peak_threadid_sbox.text()))
            self.window.peak_table.setItem(self.linha_peak, 1,
                                           QtWidgets.QTableWidgetItem(self.window.peak_streamid_edit.text()))
            self.window.peak_table.setItem(self.linha_peak, 2,
                                           QtWidgets.QTableWidgetItem(self.window.peak_condition_edit.text()))
            self.window.peak_table.setItem(self.linha_peak, 3,
                                           QtWidgets.QTableWidgetItem(self.window.peak_desc_edit.text()))

            if self.window.peak_cont_check.isChecked():
                self.window.peak_table.setItem(self.linha_peak, 4,
                                               QtWidgets.QTableWidgetItem(self.window.peak_cont_sbox.text()))
            else:
                self.window.peak_table.setItem(self.linha_peak, 4, QtWidgets.QTableWidgetItem(''))

            if self.window.peak_thresh_check.isChecked():
                self.window.peak_table.setItem(self.linha_peak, 5,
                                               QtWidgets.QTableWidgetItem(self.window.peak_thresh_sbox.text()))
            else:
                self.window.peak_table.setItem(self.linha_peak, 5, QtWidgets.QTableWidgetItem(''))

            if self.window.peak_group_check.isChecked():
                self.window.peak_table.setItem(self.linha_peak, 6,
                                               QtWidgets.QTableWidgetItem(self.window.peak_group_sbox.text()))
            else:
                self.window.peak_table.setItem(self.linha_peak, 6, QtWidgets.QTableWidgetItem(''))

            self.task_peak += self.window.peak_table.item(self.linha_peak, 0).text() + ', '
            self.task_peak += self.window.peak_table.item(self.linha_peak, 1).text() + ', '
            self.task_peak += self.window.peak_table.item(self.linha_peak, 2).text() + ', '
            self.task_peak += '"' + self.window.peak_table.item(self.linha_peak, 3).text() + '"'
            if self.window.peak_cont_check.isChecked():
                self.task_peak += ', cont=' + self.window.peak_table.item(self.linha_peak, 4).text()
            if self.window.peak_thresh_check.isChecked():
                self.task_peak += ', thresh=' + self.window.peak_table.item(self.linha_peak, 5).text()
            if self.window.peak_group_check.isChecked():
                self.task_peak += ', group=' + self.window.peak_table.item(self.linha_peak, 6).text()
            self.list_tasks_peak.append(self.task_peak)
            self.task_peak = ''
            self.window.peak_streamid_edit.setText('')
            self.window.peak_condition_edit.setText('')
            self.window.peak_desc_edit.setText('')
            print(self.list_tasks_peak[self.linha_peak])
            print(self.list_tasks_peak)
            self.linha_peak = self.linha_peak + 1

    def inserir_gps(self):
        if self.scan_scan_radio.isChecked():
            if self.window.gps_streamid_edit.text() != '' and \
                    self.window.gps_condition_edit.text() != '' and \
                    self.window.gps_desc_edit.text() != '':

                self.window.gps_table.setRowCount(self.linha_gps + 1)
                self.window.gps_table.setItem(self.linha_gps, 0,
                                              QtWidgets.QTableWidgetItem(self.window.gps_threadid_sbox.text()))
                self.window.gps_table.setItem(self.linha_gps, 1,
                                              QtWidgets.QTableWidgetItem(self.window.gps_streamid_edit.text()))
                self.window.gps_table.setItem(self.linha_gps, 2,
                                              QtWidgets.QTableWidgetItem(self.window.gps_condition_edit.text()))
                self.window.gps_table.setItem(self.linha_gps, 3,
                                              QtWidgets.QTableWidgetItem(self.window.gps_desc_edit.text()))

                if self.window.gps_force_check.isChecked():
                    self.window.gps_table.setItem(self.linha_gps, 4,
                                                  QtWidgets.QTableWidgetItem(self.window.gps_force_sbox.text()))
                else:
                    self.window.gps_table.setItem(self.linha_gps, 4, QtWidgets.QTableWidgetItem(''))

                if self.window.gps_group_check.isChecked():
                    self.window.gps_table.setItem(self.linha_gps, 5,
                                                  QtWidgets.QTableWidgetItem(self.window.gps_group_sbox.text()))
                else:
                    self.window.gps_table.setItem(self.linha_gps, 5, QtWidgets.QTableWidgetItem(''))

                self.task_gps += self.window.gps_table.item(self.linha_gps, 0).text() + ', '
                self.task_gps += self.window.gps_table.item(self.linha_gps, 1).text() + ', '
                self.task_gps += self.window.gps_table.item(self.linha_gps, 2).text() + ', '
                self.task_gps += '"' + self.window.gps_table.item(self.linha_gps, 3).text() + '"'
                if self.window.gps_force_check.isChecked():
                    self.task_gps += ', force=' + self.window.gps_table.item(self.linha_gps, 4).text()
                if self.window.gps_group_check.isChecked():
                    self.task_gps += ', group=' + self.window.gps_table.item(self.linha_gps, 5).text()
                self.list_tasks_gps.append(self.task_gps)
                self.task_gps = ''
                self.window.gps_streamid_edit.setText('')
                self.window.gps_condition_edit.setText('')
                self.window.gps_desc_edit.setText('')
                print(self.list_tasks_gps[self.linha_gps])
                print(self.list_tasks_gps)
                self.linha_gps = self.linha_gps + 1
        elif self.scan_timer_radio.isChecked():
            if self.window_timer.gps_streamid_edit.text() != '' and \
                    self.window_timer.gps_condition_edit.text() != '' and \
                    self.window_timer.gps_desc_edit.text() != '':

                self.window_timer.gps_table.setRowCount(self.linha_gps + 1)
                self.window_timer.gps_table.setItem(self.linha_gps, 0,
                                                    QtWidgets.QTableWidgetItem(
                                                        self.window_timer.gps_threadid_sbox.text()))
                self.window_timer.gps_table.setItem(self.linha_gps, 1,
                                                    QtWidgets.QTableWidgetItem(
                                                        self.window_timer.gps_streamid_edit.text()))
                self.window_timer.gps_table.setItem(self.linha_gps, 2,
                                                    QtWidgets.QTableWidgetItem(
                                                        self.window_timer.gps_condition_edit.text()))
                self.window_timer.gps_table.setItem(self.linha_gps, 3,
                                                    QtWidgets.QTableWidgetItem(
                                                        self.window_timer.gps_desc_edit.text()))

                if self.window_timer.gps_force_check.isChecked():
                    self.window_timer.gps_table.setItem(self.linha_gps, 4,
                                                        QtWidgets.QTableWidgetItem(
                                                            self.window_timer.gps_force_sbox.text()))
                else:
                    self.window_timer.gps_table.setItem(self.linha_gps, 4, QtWidgets.QTableWidgetItem(''))

                if self.window_timer.gps_group_check.isChecked():
                    self.window_timer.gps_table.setItem(self.linha_gps, 5,
                                                        QtWidgets.QTableWidgetItem(
                                                            self.window_timer.gps_group_sbox.text()))
                else:
                    self.window_timer.gps_table.setItem(self.linha_gps, 5, QtWidgets.QTableWidgetItem(''))

                self.task_gps += self.window_timer.gps_table.item(self.linha_gps, 0).text() + ', '
                self.task_gps += self.window_timer.gps_table.item(self.linha_gps, 1).text() + ', '
                self.task_gps += self.window_timer.gps_table.item(self.linha_gps, 2).text() + ', '
                self.task_gps += '"' + self.window_timer.gps_table.item(self.linha_gps, 3).text() + '"'
                if self.window_timer.gps_force_check.isChecked():
                    self.task_gps += ', force=' + self.window_timer.gps_table.item(self.linha_gps, 4).text()
                if self.window_timer.gps_group_check.isChecked():
                    self.task_gps += ', group=' + self.window_timer.gps_table.item(self.linha_gps, 5).text()
                self.list_tasks_gps.append(self.task_gps)
                self.task_gps = ''
                self.window_timer.gps_streamid_edit.setText('')
                self.window_timer.gps_condition_edit.setText('')
                self.window_timer.gps_desc_edit.setText('')
                print(self.list_tasks_gps[self.linha_gps])
                print(self.list_tasks_gps)
                self.linha_gps = self.linha_gps + 1

    def inserir_info(self):
        if self.scan_scan_radio.isChecked():
            if self.window.info_streamid_edit.text() != '' and \
                    self.window.info_condition_edit.text() != '' and \
                    self.window.info_desc_edit.text() != '':

                self.window.info_table.setRowCount(self.linha_info + 1)
                self.window.info_table.setItem(self.linha_info, 0,
                                               QtWidgets.QTableWidgetItem(self.window.info_threadid_sbox.text()))
                self.window.info_table.setItem(self.linha_info, 1,
                                               QtWidgets.QTableWidgetItem(self.window.info_streamid_edit.text()))
                self.window.info_table.setItem(self.linha_info, 2,
                                               QtWidgets.QTableWidgetItem(self.window.info_condition_edit.text()))
                self.window.info_table.setItem(self.linha_info, 3,
                                               QtWidgets.QTableWidgetItem(self.window.info_desc_edit.text()))

                if self.window.info_group_check.isChecked():
                    self.window.info_table.setItem(self.linha_info, 5,
                                                   QtWidgets.QTableWidgetItem(self.window.info_group_sbox.text()))
                else:
                    self.window.info_table.setItem(self.linha_info, 5, QtWidgets.QTableWidgetItem(''))

                self.task_info += self.window.info_table.item(self.linha_info, 0).text() + ', '
                self.task_info += self.window.info_table.item(self.linha_info, 1).text() + ', '
                self.task_info += self.window.info_table.item(self.linha_info, 2).text() + ', '
                self.task_info += '"' + self.window.info_table.item(self.linha_info, 3).text() + '"'
                if self.window.info_group_check.isChecked():
                    self.task_info += ', group=' + self.window.info_table.item(self.linha_info, 5).text()
                self.list_tasks_info.append(self.task_info)
                self.task_info = ''
                self.window.info_streamid_edit.setText('')
                self.window.info_condition_edit.setText('')
                self.window.info_desc_edit.setText('')
                print(self.list_tasks_info[self.linha_info])
                print(self.list_tasks_info)
                self.linha_info = self.linha_info + 1
        elif self.scan_timer_radio.isChecked():
            if self.window_timer.info_streamid_edit.text() != '' and \
                    self.window_timer.info_condition_edit.text() != '' and \
                    self.window_timer.info_desc_edit.text() != '':

                self.window_timer.info_table.setRowCount(self.linha_info + 1)
                self.window_timer.info_table.setItem(self.linha_info, 0,
                                                     QtWidgets.QTableWidgetItem(
                                                         self.window_timer.info_threadid_sbox.text()))
                self.window_timer.info_table.setItem(self.linha_info, 1,
                                                     QtWidgets.QTableWidgetItem(
                                                         self.window_timer.info_streamid_edit.text()))
                self.window_timer.info_table.setItem(self.linha_info, 2,
                                                     QtWidgets.QTableWidgetItem(
                                                         self.window_timer.info_condition_edit.text()))
                self.window_timer.info_table.setItem(self.linha_info, 3,
                                                     QtWidgets.QTableWidgetItem(
                                                         self.window_timer.info_desc_edit.text()))

                if self.window_timer.info_group_check.isChecked():
                    self.window_timer.info_table.setItem(self.linha_info, 5,
                                                         QtWidgets.QTableWidgetItem(
                                                             self.window_timer.info_group_sbox.text()))
                else:
                    self.window_timer.info_table.setItem(self.linha_info, 5, QtWidgets.QTableWidgetItem(''))

                self.task_info += self.window_timer.info_table.item(self.linha_info, 0).text() + ', '
                self.task_info += self.window_timer.info_table.item(self.linha_info, 1).text() + ', '
                self.task_info += self.window_timer.info_table.item(self.linha_info, 2).text() + ', '
                self.task_info += '"' + self.window_timer.info_table.item(self.linha_info, 3).text() + '"'
                if self.window_timer.info_group_check.isChecked():
                    self.task_info += ', group=' + self.window_timer.info_table.item(self.linha_info, 5).text()
                self.list_tasks_info.append(self.task_info)
                self.task_info = ''
                self.window_timer.info_streamid_edit.setText('')
                self.window_timer.info_condition_edit.setText('')
                self.window_timer.info_desc_edit.setText('')
                print(self.list_tasks_info[self.linha_info])
                print(self.list_tasks_info)
                self.linha_info = self.linha_info + 1

    def inserir_mean(self):
        if self.window.mean_streamid_edit.text() != '' and \
                self.window.mean_condition_edit.text() != '' and \
                self.window.mean_desc_edit.text() != '':

            self.window.mean_table.setRowCount(self.linha_mean + 1)
            self.window.mean_table.setItem(self.linha_mean, 0,
                                           QtWidgets.QTableWidgetItem(self.window.mean_threadid_sbox.text()))
            self.window.mean_table.setItem(self.linha_mean, 1,
                                           QtWidgets.QTableWidgetItem(self.window.mean_streamid_edit.text()))
            self.window.mean_table.setItem(self.linha_mean, 2,
                                           QtWidgets.QTableWidgetItem(self.window.mean_condition_edit.text()))
            self.window.mean_table.setItem(self.linha_mean, 3,
                                           QtWidgets.QTableWidgetItem(self.window.mean_desc_edit.text()))

            if self.window.mean_thresh_check.isChecked():
                self.window.mean_table.setItem(self.linha_mean, 4,
                                               QtWidgets.QTableWidgetItem(self.window.mean_thresh_sbox.text()))
            else:
                self.window.mean_table.setItem(self.linha_mean, 4, QtWidgets.QTableWidgetItem(''))

            if self.window.mean_group_check.isChecked():
                self.window.mean_table.setItem(self.linha_mean, 5,
                                               QtWidgets.QTableWidgetItem(self.window.mean_group_sbox.text()))
            else:
                self.window.mean_table.setItem(self.linha_mean, 5, QtWidgets.QTableWidgetItem(''))

            self.task_mean += self.window.mean_table.item(self.linha_mean, 0).text() + ', '
            self.task_mean += self.window.mean_table.item(self.linha_mean, 1).text() + ', '
            self.task_mean += self.window.mean_table.item(self.linha_mean, 2).text() + ', '
            self.task_mean += '"' + self.window.mean_table.item(self.linha_mean, 3).text() + '"'
            if self.window.mean_thresh_check.isChecked():
                self.task_mean += ', thresh=' + self.window.mean_table.item(self.linha_mean, 4).text()
            if self.window.mean_group_check.isChecked():
                self.task_mean += ', group=' + self.window.mean_table.item(self.linha_mean, 5).text()
            self.list_tasks_mean.append(self.task_mean)
            self.task_mean = ''
            self.window.mean_streamid_edit.setText('')
            self.window.mean_condition_edit.setText('')
            self.window.mean_desc_edit.setText('')
            print(self.list_tasks_mean[self.linha_mean])
            print(self.list_tasks_mean)
            self.linha_mean = self.linha_mean + 1

    def inserir_audit(self):
        if self.scan_scan_radio.isChecked():
            if self.window.audit_streamid_edit.text() != '' and \
                    self.window.audit_condition_edit.text() != '' and \
                    self.window.audit_desc_edit.text() != '':

                self.window.audit_table.setRowCount(self.linha_audit + 1)
                self.window.audit_table.setItem(self.linha_audit, 0,
                                                QtWidgets.QTableWidgetItem(self.window.audit_threadid_sbox.text()))
                self.window.audit_table.setItem(self.linha_audit, 1,
                                                QtWidgets.QTableWidgetItem(self.window.audit_streamid_edit.text()))
                self.window.audit_table.setItem(self.linha_audit, 2,
                                                QtWidgets.QTableWidgetItem(self.window.audit_condition_edit.text()))
                self.window.audit_table.setItem(self.linha_audit, 3,
                                                QtWidgets.QTableWidgetItem(self.window.audit_desc_edit.text()))

                if self.window.audit_group_check.isChecked():
                    self.window.audit_table.setItem(self.linha_audit, 4,
                                                    QtWidgets.QTableWidgetItem(self.window.audit_group_sbox.text()))
                else:
                    self.window.audit_table.setItem(self.linha_audit, 4, QtWidgets.QTableWidgetItem(''))

                self.task_audit += self.window.audit_table.item(self.linha_audit, 0).text() + ', '
                self.task_audit += self.window.audit_table.item(self.linha_audit, 1).text() + ', '
                self.task_audit += self.window.audit_table.item(self.linha_audit, 2).text() + ', '
                self.task_audit += '"' + self.window.audit_table.item(self.linha_audit, 3).text() + '"'
                if self.window.audit_group_check.isChecked():
                    self.task_audit += ', group=' + self.window.audit_table.item(self.linha_audit, 4).text()
                self.list_tasks_audit.append(self.task_audit)
                self.task_audit = ''
                self.window.audit_streamid_edit.setText('')
                self.window.audit_condition_edit.setText('')
                self.window.audit_desc_edit.setText('')
                print(self.list_tasks_audit[self.linha_audit])
                print(self.list_tasks_audit)
                self.linha_audit = self.linha_audit + 1
        elif self.scan_timer_radio.isChecked():
            if self.window_timer.audit_streamid_edit.text() != '' and \
                    self.window_timer.audit_condition_edit.text() != '' and \
                    self.window_timer.audit_desc_edit.text() != '':

                self.window_timer.audit_table.setRowCount(self.linha_audit + 1)
                self.window_timer.audit_table.setItem(self.linha_audit, 0,
                                                      QtWidgets.QTableWidgetItem(
                                                          self.window_timer.audit_threadid_sbox.text()))
                self.window_timer.audit_table.setItem(self.linha_audit, 1,
                                                      QtWidgets.QTableWidgetItem(
                                                          self.window_timer.audit_streamid_edit.text()))
                self.window_timer.audit_table.setItem(self.linha_audit, 2,
                                                      QtWidgets.QTableWidgetItem(
                                                          self.window_timer.audit_condition_edit.text()))
                self.window_timer.audit_table.setItem(self.linha_audit, 3,
                                                      QtWidgets.QTableWidgetItem(
                                                          self.window_timer.audit_desc_edit.text()))

                if self.window_timer.audit_group_check.isChecked():
                    self.window_timer.audit_table.setItem(self.linha_audit, 4,
                                                          QtWidgets.QTableWidgetItem(
                                                              self.window_timer.audit_group_sbox.text()))
                else:
                    self.window_timer.audit_table.setItem(self.linha_audit, 4, QtWidgets.QTableWidgetItem(''))

                self.task_audit += self.window_timer.audit_table.item(self.linha_audit, 0).text() + ', '
                self.task_audit += self.window_timer.audit_table.item(self.linha_audit, 1).text() + ', '
                self.task_audit += self.window_timer.audit_table.item(self.linha_audit, 2).text() + ', '
                self.task_audit += '"' + self.window_timer.audit_table.item(self.linha_audit, 3).text() + '"'
                if self.window_timer.audit_group_check.isChecked():
                    self.task_audit += ', group=' + self.window_timer.audit_table.item(self.linha_audit, 4).text()
                self.list_tasks_audit.append(self.task_audit)
                self.task_audit = ''
                self.window_timer.audit_streamid_edit.setText('')
                self.window_timer.audit_condition_edit.setText('')
                self.window_timer.audit_desc_edit.setText('')
                print(self.list_tasks_audit[self.linha_audit])
                print(self.list_tasks_audit)
                self.linha_audit = self.linha_audit + 1

    def inserir_msg(self):
        if self.scan_scan_radio.isChecked():
            if self.window.msg_streamid_edit.text() != '' and \
                    self.window.msg_condition_edit.text() != '' and \
                    self.window.msg_desc_edit.text() != '':

                self.window.msg_table.setRowCount(self.linha_msg + 1)
                self.window.msg_table.setItem(self.linha_msg, 0,
                                              QtWidgets.QTableWidgetItem(self.window.msg_threadid_sbox.text()))
                self.window.msg_table.setItem(self.linha_msg, 1,
                                              QtWidgets.QTableWidgetItem(self.window.msg_streamid_edit.text()))
                self.window.msg_table.setItem(self.linha_msg, 2,
                                              QtWidgets.QTableWidgetItem(self.window.msg_condition_edit.text()))
                self.window.msg_table.setItem(self.linha_msg, 3,
                                              QtWidgets.QTableWidgetItem(self.window.msg_desc_edit.text()))

                if self.window.msg_group_check.isChecked():
                    self.window.msg_table.setItem(self.linha_msg, 4,
                                                  QtWidgets.QTableWidgetItem(self.window.msg_group_sbox.text()))
                else:
                    self.window.msg_table.setItem(self.linha_msg, 4, QtWidgets.QTableWidgetItem(''))

                self.task_msg += self.window.msg_table.item(self.linha_msg, 0).text() + ', '
                self.task_msg += self.window.msg_table.item(self.linha_msg, 1).text() + ', '
                self.task_msg += self.window.msg_table.item(self.linha_msg, 2).text() + ', '
                self.task_msg += '"' + self.window.msg_table.item(self.linha_msg, 3).text() + '"'
                if self.window.msg_group_check.isChecked():
                    self.task_msg += ', group=' + self.window.msg_table.item(self.linha_msg, 4).text()
                self.list_tasks_msg.append(self.task_msg)
                self.task_msg = ''
                self.window.msg_streamid_edit.setText('')
                self.window.msg_condition_edit.setText('')
                self.window.msg_desc_edit.setText('')
                print(self.list_tasks_msg[self.linha_msg])
                print(self.list_tasks_msg)
                self.linha_msg = self.linha_msg + 1
        elif self.scan_timer_radio.isChecked():
            if self.window_timer.msg_streamid_edit.text() != '' and \
                    self.window_timer.msg_condition_edit.text() != '' and \
                    self.window_timer.msg_desc_edit.text() != '':

                self.window_timer.msg_table.setRowCount(self.linha_msg + 1)
                self.window_timer.msg_table.setItem(self.linha_msg, 0,
                                                    QtWidgets.QTableWidgetItem(
                                                        self.window_timer.msg_threadid_sbox.text()))
                self.window_timer.msg_table.setItem(self.linha_msg, 1,
                                                    QtWidgets.QTableWidgetItem(
                                                        self.window_timer.msg_streamid_edit.text()))
                self.window_timer.msg_table.setItem(self.linha_msg, 2,
                                                    QtWidgets.QTableWidgetItem(
                                                        self.window_timer.msg_condition_edit.text()))
                self.window_timer.msg_table.setItem(self.linha_msg, 3,
                                                    QtWidgets.QTableWidgetItem(
                                                        self.window_timer.msg_desc_edit.text()))

                if self.window_timer.msg_group_check.isChecked():
                    self.window_timer.msg_table.setItem(self.linha_msg, 4,
                                                        QtWidgets.QTableWidgetItem(
                                                            self.window_timer.msg_group_sbox.text()))
                else:
                    self.window_timer.msg_table.setItem(self.linha_msg, 4, QtWidgets.QTableWidgetItem(''))

                self.task_msg += self.window_timer.msg_table.item(self.linha_msg, 0).text() + ', '
                self.task_msg += self.window_timer.msg_table.item(self.linha_msg, 1).text() + ', '
                self.task_msg += self.window_timer.msg_table.item(self.linha_msg, 2).text() + ', '
                self.task_msg += '"' + self.window_timer.msg_table.item(self.linha_msg, 3).text() + '"'
                if self.window_timer.msg_group_check.isChecked():
                    self.task_msg += ', group=' + self.window_timer.msg_table.item(self.linha_msg, 4).text()
                self.list_tasks_msg.append(self.task_msg)
                self.task_msg = ''
                self.window_timer.msg_streamid_edit.setText('')
                self.window_timer.msg_condition_edit.setText('')
                self.window_timer.msg_desc_edit.setText('')
                print(self.list_tasks_msg[self.linha_msg])
                print(self.list_tasks_msg)
                self.linha_msg = self.linha_msg + 1

    def excluir_linha(self, task_tab):
        if self.scan_scan_radio.isChecked():
            if self.window.occ_table.currentRow() >= 0 and task_tab == 'occ':
                self.list_tasks_occ.pop(self.window.occ_table.currentRow())
                print(self.window.occ_table.currentRow())
                self.window.occ_table.removeRow(self.window.occ_table.currentRow())
                print(self.list_tasks_occ)
                self.linha_occ = self.linha_occ - 1
            elif self.window.peak_table.currentRow() >= 0 and task_tab == 'peak':
                self.list_tasks_peak.pop(self.window.peak_table.currentRow())
                self.window.peak_table.removeRow(self.window.peak_table.currentRow())
                print(self.list_tasks_peak)
                self.linha_peak = self.linha_peak - 1
            elif self.window.gps_table.currentRow() >= 0 and task_tab == 'gps':
                self.list_tasks_gps.pop(self.window.gps_table.currentRow())
                self.window.gps_table.removeRow(self.window.gps_table.currentRow())
                print(self.list_tasks_gps)
                self.linha_gps = self.linha_gps - 1
            elif self.window.info_table.currentRow() >= 0 and task_tab == 'info':
                self.list_tasks_info.pop(self.window.info_table.currentRow())
                self.window.info_table.removeRow(self.window.info_table.currentRow())
                print(self.list_tasks_info)
                self.linha_info = self.linha_info - 1
            elif self.window.mean_table.currentRow() >= 0 and task_tab == 'mean':
                self.list_tasks_mean.pop(self.window.mean_table.currentRow())
                self.window.mean_table.removeRow(self.window.mean_table.currentRow())
                print(self.list_tasks_mean)
                self.linha_mean = self.linha_mean - 1
            elif self.window.audit_table.currentRow() >= 0 and task_tab == 'audit':
                self.list_tasks_audit.pop(self.window.audit_table.currentRow())
                self.window.audit_table.removeRow(self.window.audit_table.currentRow())
                print(self.list_tasks_audit)
                self.linha_audit = self.linha_audit - 1
            elif self.window.msg_table.currentRow() >= 0 and task_tab == 'msg':
                self.list_tasks_msg.pop(self.window.msg_table.currentRow())
                self.window.msg_table.removeRow(self.window.msg_table.currentRow())
                print(self.list_tasks_msg)
                self.linha_msg = self.linha_msg - 1
        elif self.scan_timer_radio.isChecked():
            if self.window_timer.gps_table.currentRow() >= 0 and task_tab == 'gps':
                self.list_tasks_gps.pop(self.window_timer.gps_table.currentRow())
                self.window_timer.gps_table.removeRow(self.window_timer.gps_table.currentRow())
                print(self.list_tasks_gps)
                self.linha_gps = self.linha_gps - 1
            elif self.window_timer.info_table.currentRow() >= 0 and task_tab == 'info':
                self.list_tasks_info.pop(self.window_timer.info_table.currentRow())
                self.window_timer.info_table.removeRow(self.window_timer.info_table.currentRow())
                print(self.list_tasks_info)
                self.linha_info = self.linha_info - 1
            elif self.window_timer.audit_table.currentRow() >= 0 and task_tab == 'audit':
                self.list_tasks_audit.pop(self.window_timer.audit_table.currentRow())
                self.window_timer.audit_table.removeRow(self.window_timer.audit_table.currentRow())
                print(self.list_tasks_audit)
                self.linha_audit = self.linha_audit - 1
            elif self.window_timer.msg_table.currentRow() >= 0 and task_tab == 'msg':
                self.list_tasks_msg.pop(self.window_timer.msg_table.currentRow())
                self.window_timer.msg_table.removeRow(self.window_timer.msg_table.currentRow())
                print(self.list_tasks_msg)
                self.linha_msg = self.linha_msg - 1

    tarefas_list = []

    def finalizar_tarefa(self):
        if self.scan_scan_radio.isChecked():
            self.window.close()
        elif self.scan_timer_radio.isChecked():
            self.window_timer.close()

    def habilita_http(self, enabled):
        if enabled:
            self.stream_porta_edit.setEnabled(False)
            self.stream_end_edit.setEnabled(False)
            self.stream_nome_edit.setEnabled(False)

    def habilita_udp(self, enabled):
        if enabled:
            self.stream_porta_edit.setEnabled(True)
            self.stream_end_edit.setEnabled(False)
            self.stream_nome_edit.setEnabled(False)

    def habilita_arquivo(self, enabled):
        if enabled:
            self.stream_porta_edit.setEnabled(False)
            self.stream_end_edit.setEnabled(True)
            self.stream_nome_edit.setEnabled(True)

    def habilita_timer(self, enabled):
        if enabled:
            self.groupBox.setEnabled(False)
            self.scan_scan_radio.setChecked(False)

    def habilita_scan(self, enabled):
        if enabled:
            self.groupBox.setEnabled(True)
            self.scan_timer_radio.setChecked(False)
            self.scan_antena_cbox.setEnabled(True)
            self.scan_finicial_radio.setEnabled(True)
            self.scan_central_radio.setEnabled(True)
            self.scan_resol_sbox.setEnabled(True)
            self.scan_ciclo_cbox.setEnabled(True)
            if self.scan_finicial_radio.isChecked():
                self.scan_fmin_sbox.setEnabled(True)
                self.scan_fmax_sbox.setEnabled(True)
                self.scan_fcentral_sbox.setEnabled(False)
                self.scan_span_sbox.setEnabled(False)
            else:
                self.scan_fmin_sbox.setEnabled(False)
                self.scan_fmax_sbox.setEnabled(False)
                self.scan_fcentral_sbox.setEnabled(True)
                self.scan_span_sbox.setEnabled(True)

    def habilita_flimites(self, enabled):
        if enabled:
            self.scan_central_radio.setChecked(False)
            self.scan_fmin_sbox.setEnabled(True)
            self.scan_fmax_sbox.setEnabled(True)
            self.scan_fcentral_sbox.setEnabled(False)
            self.scan_span_sbox.setEnabled(False)

    def habilita_fcentral(self, enabled):
        if enabled:
            self.scan_finicial_radio.setChecked(False)
            self.scan_fmin_sbox.setEnabled(False)
            self.scan_fmax_sbox.setEnabled(False)
            self.scan_fcentral_sbox.setEnabled(True)
            self.scan_span_sbox.setEnabled(True)

    def habilita_campo(self, check, campo):
        try:
            check_box = getattr(self, check)
            campo_box = getattr(self, campo)
            if check_box.isChecked():
                campo_box.setEnabled(True)
            else:
                campo_box.setEnabled(False)
        except:
            if self.scan_scan_radio.isChecked():
                check_box = getattr(self.window, check)
                campo_box = getattr(self.window, campo)
            if self.scan_timer_radio.isChecked():
                check_box = getattr(self.window_timer, check)
                campo_box = getattr(self.window_timer, campo)
            if check_box.isChecked():
                campo_box.setEnabled(True)
            else:
                campo_box.setEnabled(False)

    def visualizar_blocos(self):
        # for x in range(len(self.list_occ_timer)):
        # self.scan_lista_lwid.addItem(str(self.list_nome_timer))
        # for x in range(len(self.list_interv)):
        #     self.scan_lista_lwid.addItem(self.list_nome_timer[x])
        self.scan_lista_lwid.clear()
        self.scan_lista_lwid.repaint()
        for x in range(len(self.list_temp)):
            variavel = "[run timer " + self.list_nome_timer[x] + "]"
            variavel += '\n' + 'timer' + ' = ' + self.list_temp[x] + ' ' + self.list_unit[x]
            if len(self.list_occ_timer[x]):
                lista = self.list_occ_timer[x]
                for i in range(len(lista)):
                    variavel += "\nocc" + str(i) + " = " + lista[i]
            if len(self.list_peak_timer[x]):
                lista_peak = self.list_peak_timer[x]
                for i in range(len(lista_peak)):
                    variavel += "\npeak" + str(i) + " = " + lista_peak[i]
            if len(self.list_gps_timer[x]):
                lista_gps = self.list_gps_timer[x]
                for i in range(len(lista_gps)):
                    variavel += "\ngps" + str(i) + " = " + lista_gps[i]
            if len(self.list_info_timer[x]):
                lista_info = self.list_info_timer[x]
                for i in range(len(lista_info)):
                    variavel += "\ninfo" + str(i) + " = " + lista_info[i]
            if len(self.list_mean_timer[x]):
                lista_mean = self.list_mean_timer[x]
                for i in range(len(lista_mean)):
                    variavel += "\nmean" + str(i) + " = " + lista_mean[i]
            if len(self.list_audit_timer[x]):
                lista_audit = self.list_audit_timer[x]
                for i in range(len(lista_audit)):
                    variavel += "\naudit" + str(i) + " = " + lista_audit[i]
            if len(self.list_msg_timer[x]):
                lista_msg = self.list_msg_timer[x]
                for i in range(len(lista_msg)):
                    variavel += "\nmessage" + str(i) + " = " + lista_msg[i]
            self.scan_lista_lwid.addItem(variavel)
        # variavel = ''
        for x in range(len(self.list_interv)):
            variavel = "[run scan " + self.list_nome_scan[x] + "]"
            variavel += ('\n' + 'scan' + ' = ' +
                         self.list_interv[x] + ' ' + self.list_interv_unit[x] +
                         ',' + self.list_antena[x] +
                         ',' + self.list_freq_min[x] +
                         ',' + self.list_freq_max[x] +
                         ',' + self.list_resol[x] + self.list_resol_unit[x] +
                         ',' + self.list_ciclo[x])

            if len(self.list_occ_scan[x]):
                lista = self.list_occ_scan[x]
                for i in range(len(lista)):
                    variavel += "\nocc" + str(i) + " = " + lista[i]
            if len(self.list_peak_scan[x]):
                lista_peak = self.list_peak_scan[x]
                for i in range(len(lista_peak)):
                    variavel += "\npeak" + str(i) + " = " + lista_peak[i]
            if len(self.list_gps_scan[x]):
                lista_gps = self.list_gps_scan[x]
                for i in range(len(lista_gps)):
                    variavel += "\ngps" + str(i) + " = " + lista_gps[i]
            if len(self.list_info_scan[x]):
                lista_info = self.list_info_scan[x]
                for i in range(len(lista_info)):
                    variavel += "\ninfo" + str(i) + " = " + lista_info[i]
            if len(self.list_mean_scan[x]):
                lista_mean = self.list_mean_scan[x]
                for i in range(len(lista_mean)):
                    variavel += "\nmean" + str(i) + " = " + lista_mean[i]
            if len(self.list_audit_scan[x]):
                lista_audit = self.list_audit_scan[x]
                for i in range(len(lista_audit)):
                    variavel += "\naudit" + str(i) + " = " + lista_audit[i]
            if len(self.list_msg_scan[x]):
                lista_msg = self.list_msg_scan[x]
                for i in range(len(lista_msg)):
                    variavel += "\nmessage" + str(i) + " = " + lista_msg[i]
            self.scan_lista_lwid.addItem(variavel)
        for i in range(self.scan_lista_lwid.count()):
            self.scan_lista_lwid.item(i).setBackground(QtGui.QColor(250, 250, 250))
            if i % 2:
                self.scan_lista_lwid.item(i).setBackground(QtGui.QColor(235, 235, 235))

    def apagar_blocos(self):
        listItems = self.scan_lista_lwid.selectedItems()
        if not listItems: return
        for item in listItems:
            var = str(item.text().split('\n')[0]).split(' ')[2][:-1]
            print(var)
            if str(item.text().split('\n')[0]).split(' ')[1] == 'timer':
                if var in self.list_nome_timer:
                    print('achei')
                    print(str(self.list_nome_timer.index(var)))
                    indice = int(self.list_nome_timer.index(var))
                    self.list_nome_timer.pop(indice)
                    self.list_temp.pop(indice)
                    self.list_unit.pop(indice)
                    self.list_occ_timer.pop(indice)
                    self.list_peak_timer.pop(indice)
                    self.list_gps_timer.pop(indice)
                    self.list_info_timer.pop(indice)
                    self.list_mean_timer.pop(indice)
                    self.list_audit_timer.pop(indice)
                    self.list_msg_timer.pop(indice)
            if str(item.text().split('\n')[0]).split(' ')[1] == 'scan':
                if var in self.list_nome_scan:
                    indice = int(self.list_nome_scan.index(var))
                    self.list_nome_scan.pop(indice)
                    self.list_interv.pop(indice)
                    self.list_interv_unit.pop(indice)
                    self.list_antena.pop(indice)
                    self.list_freq_min.pop(indice)
                    self.list_freq_max.pop(indice)
                    self.list_resol.pop(indice)
                    self.list_resol_unit.pop(indice)
                    self.list_ciclo.pop(indice)
                    self.list_occ_scan.pop(indice)
                    self.list_peak_scan.pop(indice)
                    self.list_gps_scan.pop(indice)
                    self.list_info_scan.pop(indice)
                    self.list_mean_scan.pop(indice)
                    self.list_audit_scan.pop(indice)
                    self.list_msg_scan.pop(indice)
        self.visualizar_blocos()

    def remover_variavel(self):
        listItems = self.conf_lista_lwid.selectedItems()
        if not listItems: return
        for item in listItems:
            self.conf_lista_lwid.takeItem(self.conf_lista_lwid.row(item))

    def inserir_variaveis(self):
        var_reservadas = ["max_file_size",
                          "unit_info",
                          "data_dir",
                          "method",
                          "log_dir",
                          "log_file",
                          "file_version",
                          "antenna#",
                          "log_max_size",
                          "log_backups",
                          "log_level",
                          "log_fallback_dir",
                          "log_fallback",
                          "udp_port",
                          "http_port",
                          "fixed_latitude",
                          "fixed_longitude",
                          ]
        if self.conf_var_edit.text() in str(var_reservadas):
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint |
                               QtCore.Qt.WindowTitleHint
                               )
            msg.setText("Variável reservada.")
            msg.setInformativeText('Insira outro nome para esta variável.')
            msg.setWindowTitle("Erro")
            msg.exec_()
            return

        for index in range(self.conf_lista_lwid.count()):
            # if self.conf_var_edit.text() in str(self.conf_lista_lwid.item(index).text()):
            if self.conf_var_edit.text() in str(self.conf_lista_lwid.item(index).text()).split(" ", 1):
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint |
                                   QtCore.Qt.WindowTitleHint
                                   )
                msg.setText("Variável já existente.")
                msg.setInformativeText('Insira outro nome para esta variável ou exclua a existente.')
                msg.setWindowTitle("Erro")
                msg.exec_()
                return

        if self.conf_var_edit.text() != '' and self.conf_valor_edit.text() != '':
            if self.conf_tipo_cbox.currentText() == 'numérico':
                variavel = self.conf_var_edit.text() + " = " + self.conf_valor_edit.text()
                self.conf_var_edit.setText('')
                self.conf_valor_edit.setText('')
                self.conf_lista_lwid.addItem(variavel)
            else:
                variavel = self.conf_var_edit.text() + " = " + '"' + self.conf_valor_edit.text() + '"'
                self.conf_var_edit.setText('')
                self.conf_valor_edit.setText('')
                self.conf_lista_lwid.addItem(variavel)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint |
                               QtCore.Qt.WindowTitleHint
                               )
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("Campo vazio.")
            msg.setInformativeText('Nome ou valor da variável está vazio.')
            msg.setWindowTitle("Erro")
            msg.exec_()
            return

    list_id = []
    list_tipo = []
    list_param = []

    def apagar_stream(self):
        listItems = self.stream_lista_lwid.selectedItems()
        if not listItems: return
        for item in listItems:
            print(item.text()[:1])
            indice = self.list_id.index(item.text()[:1])
            self.list_id.pop(indice)
            self.list_tipo.pop(indice)
            self.list_param.pop(indice)
            self.stream_lista_lwid.takeItem(self.stream_lista_lwid.row(item))

    def inserir_stream(self):
        if self.stream_id_edit.text() != '':
            if (self.stream_porta_edit.text() != '' and self.stream_udp_radio.isChecked()) \
                    or (self.stream_end_edit.text() != '' or self.stream_nome_edit.text() != ''
                        and self.stream_arq_radio.isChecked()) \
                    or self.stream_http_radio.isChecked():
                if self.stream_id_edit.text() in self.list_id:
                    indice = self.list_id.index(self.stream_id_edit.text())
                    self.list_id[indice] = self.stream_id_edit.text()
                    if self.stream_http_radio.isChecked():
                        self.list_tipo[indice] = 'http'
                        self.list_param[indice] = ''
                    elif self.stream_udp_radio.isChecked():
                        self.list_tipo[indice] = 'udp'
                        self.list_param[indice] = self.stream_porta_edit.text()
                    elif self.stream_arq_radio.isChecked():
                        self.list_tipo[indice] = 'file'
                        self.list_param[indice] = self.stream_end_edit.text() + "/" + self.stream_nome_edit.text()
                    self.stream_lista_lwid.clear()
                    for x in range(len(self.list_id)):
                        print(self.list_id[x], self.list_tipo[x], self.list_param[x])
                        if self.list_tipo[x] == 'file':
                            self.stream_lista_lwid.addItem(
                                self.list_id[x] + ' = ' + self.list_tipo[x] + ',"' + self.list_param[x] + '.bin"')
                        else:
                            self.stream_lista_lwid.addItem(
                                self.list_id[x] + ' = ' + self.list_tipo[x] + ' ' + self.list_param[x])

                else:
                    self.list_id.append(self.stream_id_edit.text())
                    variavel = self.stream_id_edit.text() + " "
                    if self.stream_http_radio.isChecked():
                        self.list_tipo.append('http')
                        self.list_param.append('')
                        variavel += 'http'
                    elif self.stream_udp_radio.isChecked():
                        self.list_tipo.append('udp')
                        self.list_param.append(self.stream_porta_edit.text())
                        variavel += 'udp' + ' ' + self.stream_porta_edit.text()
                    elif self.stream_arq_radio.isChecked():
                        self.list_tipo.append('file')
                        self.list_param.append(self.stream_end_edit.text() + "/" + self.stream_nome_edit.text())
                        variavel += 'file' + ' ' + self.stream_end_edit.text() + "/" + self.stream_nome_edit.text()
                    self.stream_lista_lwid.clear()
                    for x in range(len(self.list_id)):
                        print(self.list_id[x], self.list_tipo[x], self.list_param[x])
                        if self.list_tipo[x] == 'file':
                            self.stream_lista_lwid.addItem(
                                self.list_id[x] + ' = ' + self.list_tipo[x] + ',"' + self.list_param[x] + '.bin"')
                        else:
                            self.stream_lista_lwid.addItem(
                                self.list_id[x] + ' = ' + self.list_tipo[x] + ' ' + self.list_param[x])
                self.stream_id_edit.setText('')
                self.stream_porta_edit.setText('')
                self.stream_end_edit.setText('')

    list_nome_scan = []
    list_nome_timer = []
    list_temp = []
    list_unit = []

    list_interv = []
    list_interv_unit = []
    list_antena = []
    list_freq_min = []
    list_freq_max = []
    list_resol = []
    list_resol_unit = []
    list_ciclo = []

    list_peak_scan = []
    list_occ_scan = []
    list_gps_scan = []
    list_info_scan = []
    list_mean_scan = []
    list_audit_scan = []
    list_msg_scan = []

    list_occ_timer = []
    list_peak_timer = []
    list_gps_timer = []
    list_info_timer = []
    list_mean_timer = []
    list_audit_timer = []
    list_msg_timer = []

    def inserir_execucao(self):
        if self.scan_timer_radio.isChecked():
            if self.scan_inter_edit.text() != '' and self.scan_nome_edit.text() != '':
                if (self.scan_nome_edit.text() in self.list_nome_timer) or \
                        (self.scan_nome_edit.text() in self.list_nome_scan):
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint |
                                       QtCore.Qt.WindowTitleHint
                                       )
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("""Já existe um bloco com esse nome.""")
                    msg.setWindowTitle("Nome repetido!")
                    msg.exec_()
                    return
                self.list_nome_timer.append(self.scan_nome_edit.text())
                self.list_temp.append(self.scan_inter_edit.text())
                self.list_unit.append(func.converte_tempo_2(self.scan_temp_cbox.currentText()))
                for x in range(len(self.list_temp)):
                    print(self.list_temp[x], self.list_unit[x])

                self.scan_inter_edit.setText('')
                self.scan_nome_edit.setText('')

                self.list_occ_timer.append(copy.deepcopy(self.list_tasks_occ))
                self.list_tasks_occ.clear()
                print(self.list_occ_timer)
                self.linha_occ = 0

                self.list_peak_timer.append(copy.deepcopy(self.list_tasks_peak))
                self.list_tasks_peak.clear()
                self.linha_peak = 0

                self.list_gps_timer.append(copy.deepcopy(self.list_tasks_gps))
                self.list_tasks_gps.clear()
                self.linha_gps = 0

                self.list_info_timer.append(copy.deepcopy(self.list_tasks_info))
                self.list_tasks_info.clear()
                self.linha_info = 0

                self.list_mean_timer.append(copy.deepcopy(self.list_tasks_mean))
                self.list_tasks_mean.clear()
                self.linha_mean = 0

                self.list_audit_timer.append(copy.deepcopy(self.list_tasks_audit))
                self.list_tasks_audit.clear()
                self.linha_audit = 0

                self.list_msg_timer.append(copy.deepcopy(self.list_tasks_msg))
                self.list_tasks_msg.clear()
                self.linha_msg = 0

                self.window_timer = TasksWindowTimer()
                self.window_timer.setupUi(self.window_timer)

        elif self.scan_scan_radio.isChecked():
            if self.scan_inter_edit.text() != '' and self.scan_resol_sbox.text() != '' and self.scan_nome_edit.text() != '':
                if (self.scan_nome_edit.text() in self.list_nome_timer) or \
                        (self.scan_nome_edit.text() in self.list_nome_scan):
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowFlags(QtCore.Qt.CustomizeWindowHint |
                                       QtCore.Qt.WindowTitleHint
                                       )
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("""Já existe um bloco com esse nome.""")
                    msg.setWindowTitle("Nome repetido!")
                    msg.exec_()
                    return
                self.list_nome_scan.append(self.scan_nome_edit.text())
                self.list_interv.append(self.scan_inter_edit.text())
                self.list_interv_unit.append(func.converte_tempo_2(self.scan_temp_cbox.currentText()))
                if self.scan_antena_cbox.currentText() == 'Auto':
                    self.list_antena.append('0')
                else:
                    self.list_antena.append(self.scan_antena_cbox.currentText())
                if self.scan_finicial_radio.isChecked():
                    self.list_freq_min.append(self.scan_fmin_sbox.text())
                    self.list_freq_max.append(self.scan_fmax_sbox.text())
                elif self.scan_central_radio.isChecked():
                    self.list_freq_min.append(
                        str(int(self.scan_fcentral_sbox.text()) - int(int(self.scan_span_sbox.text()) / 2)))
                    self.list_freq_max.append(
                        str(int(self.scan_fcentral_sbox.text()) + int(int(self.scan_span_sbox.text()) / 2)))
                self.list_resol.append(self.scan_resol_sbox.text())
                self.list_resol_unit.append("")
                self.list_ciclo.append(self.scan_ciclo_cbox.text())

                for x in range(len(self.list_interv)):
                    print(self.list_interv[x],
                          self.list_interv_unit[x],
                          self.list_antena[x],
                          self.list_freq_min[x],
                          self.list_freq_max[x],
                          self.list_resol[x],
                          self.list_resol_unit[x],
                          self.list_ciclo[x]
                          )

                self.scan_inter_edit.setText('')
                # self.scan_resol_edit.setText('')
                self.scan_nome_edit.setText('')

                self.list_occ_scan.append(copy.deepcopy(self.list_tasks_occ))
                self.list_tasks_occ.clear()
                print(self.list_occ_scan)
                self.linha_occ = 0

                self.list_peak_scan.append(copy.deepcopy(self.list_tasks_peak))
                self.list_tasks_peak.clear()
                self.linha_peak = 0

                self.list_gps_scan.append(copy.deepcopy(self.list_tasks_gps))
                self.list_tasks_gps.clear()
                self.linha_gps = 0

                self.list_info_scan.append(copy.deepcopy(self.list_tasks_info))
                self.list_tasks_info.clear()
                self.linha_info = 0

                self.list_mean_scan.append(copy.deepcopy(self.list_tasks_mean))
                self.list_tasks_mean.clear()
                self.linha_mean = 0

                self.list_audit_scan.append(copy.deepcopy(self.list_tasks_audit))
                self.list_tasks_audit.clear()
                self.linha_audit = 0

                self.list_msg_scan.append(copy.deepcopy(self.list_tasks_msg))
                self.list_tasks_msg.clear()
                self.linha_msg = 0

                self.window = TasksWindow()
                self.window.setupUi(self.window)

        self.visualizar_blocos()

    def gerar_arquivo(self):
        nome, _ = QtWidgets.QFileDialog.getSaveFileName(filter="Logger File (*.cfg)", directory=os.getcwd())
        if nome:
            sobrescreve = open(nome, "w")
            sobrescreve.close()
            # with open("config.txt ", "a") as arquivo:
            with open(nome, "a", newline='\n') as arquivo:
                texto_preview = self.prev_area.toPlainText()
                arquivo.write(str(texto_preview))

    def render_preview(self):
        formLayout = QtWidgets.QFormLayout()
        groupBox = QtWidgets.QGroupBox()
        self.prev_area.clear()
        # versao 2
        listaCodigo = []
        listaCodigo.append("#Script RFeye")

        listaCodigo.append("\n\n[config]\n")

        if self.conf_tamanho_check.isChecked():
            listaCodigo.append("\nmax_file_size = " + str(int(self.conf_tamanho_sbox.text()) * 1000))
        if self.conf_estacao_check.isChecked():
            listaCodigo.append("\nunit_info = " + '"' + str(self.conf_estacao_edit.text()) + '"')
        if self.conf_dir_check.isChecked():
            listaCodigo.append("\ndata_dir = " + '"' + str(self.conf_dir_edit.text()) + '"')

        if not self.conf_dir_check.isChecked():
            listaCodigo.append("\ndata_dir = " + '"' + '/mnt/internal' + '"')

        if self.conf_metodo_check.isChecked():
            listaCodigo.append("\nmethod = " + '"' + str(self.conf_metodo_edit.text()) + '"')
        if self.conf_logdir_check.isChecked():
            listaCodigo.append("\nlog_dir = " + '"' + str(self.conf_logdir_edit.text()) + '"')
            listaCodigo.append \
                ("\nlog_file = " + '"' + "%(log_dir)s/" + str(self.conf_logname_edit.text()) + '.log"')
        if self.conf_versao_check.isChecked():
            listaCodigo.append("\nfile_version = " + str(self.conf_versao_sbox.text()))
        if self.conf_antena_check.isChecked():
            listaCodigo.append("\nantenna# = " + str(self.conf_antena_sbox.text()))
        if self.conf_logmax_check.isChecked():
            listaCodigo.append("\nlog_max_size = " + str(self.conf_logmax_sbox.text()))
        if self.conf_logback_check.isChecked():
            listaCodigo.append("\nlog_backups = " + str(self.conf_logback_sbox.text()))
        if self.conf_loglevel_check.isChecked():
            listaCodigo.append("\nlog_level = " + '"' + str(self.conf_loglevel_cbox.currentText()) + '"')
        if self.conf_logfalldir_check.isChecked():
            listaCodigo.append("\nlog_fallback_dir = " + '"' + str(self.conf_logfalldir_edit.text()) + '/' + '"')
            listaCodigo.append \
                ("\nlog_fallback = " + '"' + "%(log_fallback_dir)s/" + str(self.conf_logfallname_edit.text()) + '.log"')
        if self.conf_udpport_check.isChecked():
            listaCodigo.append("\nudp_port = " + str(self.conf_udpport_sbox.text()))
        if self.conf_httpport_check.isChecked():
            listaCodigo.append("\nhttp_port = " + str(self.conf_httpport_sbox.text()))
        if self.conf_latitude_check.isChecked():
            listaCodigo.append("\nfixed_latitude = " + str(self.conf_latitude_sbox.text()).replace(",", "."))
        if self.conf_longitude_check.isChecked():
            listaCodigo.append("\nfixed_longitude = " + str(self.conf_longitude_sbox.text().replace(",", ".")))

        if self.conf_lista_lwid:
            listaCodigo.append("\n\n#Variáveis de usuário")
            for x in range(self.conf_lista_lwid.count()):
                listaCodigo.append("\n" + str(self.conf_lista_lwid.item(x).text()))

        listaCodigo.append("\n\n[streams]\n")

        for x in range(len(self.list_id)):
            if self.list_tipo[x] == 'http':
                listaCodigo.append("\n" + self.list_id[x] + ' = ' + self.list_tipo[x])
            elif self.list_tipo[x] == 'udp':
                listaCodigo.append("\n" + self.list_id[x] + ' = ' + self.list_tipo[x] + ',' + self.list_param[x])
            elif self.list_tipo[x] == 'file':
                listaCodigo.append("\n" + self.list_id[x] + ' = ' + self.list_tipo[x] + ',' + '"' + self.list_param[x]
                                   + ".bin" + '"')

        for x in range(len(self.list_temp)):
            listaCodigo.append("\n\n[run timer " + self.list_nome_timer[x] + "]\n")
            listaCodigo.append('\n' + 'timer' + ' = ' + self.list_temp[x] + ' ' + self.list_unit[x])

            if len(self.list_occ_timer[x]):
                lista = self.list_occ_timer[x]
                for i in range(len(lista)):
                    listaCodigo.append("\nocc" + str(i) + " = " + lista[i])
            if len(self.list_peak_timer[x]):
                lista_peak = self.list_peak_timer[x]
                for i in range(len(lista_peak)):
                    listaCodigo.append("\npeak" + str(i) + " = " + lista_peak[i])
            if len(self.list_gps_timer[x]):
                lista_gps = self.list_gps_timer[x]
                for i in range(len(lista_gps)):
                    listaCodigo.append("\ngps" + str(i) + " = " + lista_gps[i])
            if len(self.list_info_timer[x]):
                lista_info = self.list_info_timer[x]
                for i in range(len(lista_info)):
                    listaCodigo.append("\ninfo" + str(i) + " = " + lista_info[i])
            if len(self.list_mean_timer[x]):
                lista_mean = self.list_mean_timer[x]
                for i in range(len(lista_mean)):
                    listaCodigo.append("\nmean" + str(i) + " = " + lista_mean[i])
            if len(self.list_audit_timer[x]):
                lista_audit = self.list_audit_timer[x]
                for i in range(len(lista_audit)):
                    listaCodigo.append("\naudit" + str(i) + " = " + lista_audit[i])
            if len(self.list_msg_timer[x]):
                lista_msg = self.list_msg_timer[x]
                for i in range(len(lista_msg)):
                    listaCodigo.append("\nmessage" + str(i) + " = " + lista_msg[i])

        for x in range(len(self.list_interv)):
            listaCodigo.append("\n\n[run scan " + self.list_nome_scan[x] + "]\n")
            listaCodigo.append('\n' + 'scan' + ' = ' +
                               self.list_interv[x] + ' ' + self.list_interv_unit[x] +
                               ',' + self.list_antena[x] +
                               ',' + self.list_freq_min[x] +
                               ',' + self.list_freq_max[x] +
                               # ',' + self.list_resol[x] + self.list_resol_unit[x] +
                               ',' + self.list_resol[x] +
                               ',' + self.list_ciclo[x])

            if len(self.list_occ_scan[x]):
                lista = self.list_occ_scan[x]
                for i in range(len(lista)):
                    listaCodigo.append("\nocc" + str(i) + " = " + lista[i])
            if len(self.list_peak_scan[x]):
                lista_peak = self.list_peak_scan[x]
                for i in range(len(lista_peak)):
                    listaCodigo.append("\npeak" + str(i) + " = " + lista_peak[i])
            if len(self.list_gps_scan[x]):
                lista_gps = self.list_gps_scan[x]
                for i in range(len(lista_gps)):
                    listaCodigo.append("\ngps" + str(i) + " = " + lista_gps[i])
            if len(self.list_info_scan[x]):
                lista_info = self.list_info_scan[x]
                for i in range(len(lista_info)):
                    listaCodigo.append("\ninfo" + str(i) + " = " + lista_info[i])
            if len(self.list_mean_scan[x]):
                lista_mean = self.list_mean_scan[x]
                for i in range(len(lista_mean)):
                    listaCodigo.append("\nmean" + str(i) + " = " + lista_mean[i])
            if len(self.list_audit_scan[x]):
                lista_audit = self.list_audit_scan[x]
                for i in range(len(lista_audit)):
                    listaCodigo.append("\naudit" + str(i) + " = " + lista_audit[i])
            if len(self.list_msg_scan[x]):
                lista_msg = self.list_msg_scan[x]
                for i in range(len(lista_msg)):
                    listaCodigo.append("\nmessage" + str(i) + " = " + lista_msg[i])

        listaCodigo.append("\n")
        for linhas in range(len(listaCodigo)):
            self.prev_area.insertPlainText(listaCodigo[linhas])

        textboxValue = self.prev_area.toPlainText()
        print(textboxValue)
        print(type(textboxValue))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = PrincipalWindow()
    w.show()
    sys.exit(app.exec_())
