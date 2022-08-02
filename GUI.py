from gen_GUI import Ui_Dialog
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QMessageBox, QApplication, QTableWidgetItem
from numpy import array, random
from matplotlib.pyplot import subplots, ion, ioff, show

from Genetic import Genetic
from Func import func
from Input_func import input_func

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.tableWidget.setColumnWidth(0, 30)
        self.ui.tableWidget.setColumnWidth(1, 195)

        self.ui.tableWidget.clicked.connect(self.table_value)
        self.ui.pushButton_run_algoritm.clicked.connect(self.run_algoritm)
        self.ui.pushButton_run.clicked.connect(self.run_vyb)
        self.ui.pushButton_run.clicked.connect(self.run_vyb)
        self.ui.pushButton_exit.clicked.connect(QApplication.instance().quit)
        self.ui.pushButton_FAQ_func.clicked.connect(self.info_vvod_func)
        self.ui.pushButton_FAQ_toch.clicked.connect(self.info_vvod_pohib)

        self.input_data_table()

    def input_data_table(self):
        spisok_func = ["pow(x, 2) + pow(y, 2)", "pow(x - 1, 2) + pow(y - 1, 2)", "20 + pow(x, 2) + pow(y, 2) - 10 * cos(2 * pi * x) - 10 * cos(2 * pi * y)"]

        self.ui.tableWidget.setRowCount(len(spisok_func))

        for i in range(len(spisok_func)):
            for j in range(len(spisok_func)):
                if j == 0:
                    item = QTableWidgetItem(str(i + 1))
                else:
                    item = QTableWidgetItem(str(spisok_func[i]))

                item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)
                self.ui.tableWidget.setItem(i, j, item)
     
    def run_algoritm(self):
        self.ui.pushButton_run.setEnabled(False)
        self.ui.radioButton.setEnabled(False)
        self.ui.radioButton_2.setEnabled(False)
        self.ui.Edit_start_popul.setReadOnly(True)
        self.ui.Edit_end_popul.setReadOnly(True)

        self.ui.label_popul.setText("")
        self.ui.label_mut.setText("")
        self.ui.label_x.setText("")
        self.ui.label_y.setText("")
        self.ui.label_f.setText("")

        f = self.ui.Edit_func.toPlainText()
        a_x = self.ui.Edit_dot_A_x.toPlainText()
        a_y = self.ui.Edit_dot_A_y.toPlainText()
        c_x = self.ui.Edit_dot_C_x.toPlainText()
        c_y = self.ui.Edit_dot_C_y.toPlainText()
        e_power = self.ui.Edit_power.text()
        cnt_mut_dot = self.ui.Edit_cnt_mut_dot.toPlainText()

        if f == "" and a_x == "" and a_y == "" and c_x == "" and c_y == "" and e_power == "" and cnt_mut_dot == "":
            self.Msg("Error", "Поля меж точок, формули та похібки повинні бути не порожніми")

        else:
            prov_func, f = input_func(f)

            if prov_func == False:
                self.Msg("Error", f)
            else:

                try:
                    a = [float(a_x), float(a_y)]
                    c = [float(c_x), float(c_y)]
                    prov_dot = True
                except:
                    self.Msg("Error", "Введено не число! Межі точок повинна бути число!")
                    prov_dot = False

                try:
                    e_power = int(e_power)
                    pohib = pow(10, e_power)
                    prov_pohib = True
                except:
                    self.Msg("Error", "Введено не число! Похибка повинна бути число!")
                    prov_pohib = False
                    self.ui.Edit_power.setText("")


                try:
                    cnt_mut_dot = int(cnt_mut_dot)

                    if cnt_mut_dot <= 0:
                        self.Msg("Error", "Кількість точок для мутації повинна бути більше '0'!")
                        self.ui.Edit_cnt_mut_dot.setText("")
                        prov_mut_dot = False
                    else:
                        prov_mut_dot = True

                except:
                    self.Msg("Error", "Введено не число! Кількість точок для мутації повинна бути цілим число!")
                    self.ui.Edit_cnt_mut_dot.setText("")


                if prov_func and prov_dot and prov_pohib and prov_mut_dot:
                    self.ui.pushButton_run_algoritm.setEnabled(False)
                    
                    fig, ax = subplots()

                    while True:
                        Rand_chisl_for_P_Q = array([round(random.random(), 2), round(random.random(), 2), round(random.random(), 2), round(random.random(), 2)])

                        chet = 0
                        for i in Rand_chisl_for_P_Q:
                            if i == 0 or i == 1:
                                continue
                            else:
                                chet += 1

                        if chet == 4:
                            break
                    
                    self.gen = Genetic(a, c, Rand_chisl_for_P_Q, func, f)

                    ion()

                    info, self.cnt_genetic, cnt_mutation = self.gen.start_genetic(ax, pohib, cnt_mut_dot)

                    ioff()
                    self.Msg("Info", info)
                    show()

                    self.Msg("Info", f"Кількість популяцій: {str(self.cnt_genetic)}.\nКількість мутацій: {str(cnt_mutation)}.\n\nx: {str(self.gen.storoni_pryamoygol_and_minDot_for_one_popul.get(self.cnt_genetic)[-1][0])} | y: {str(self.gen.storoni_pryamoygol_and_minDot_for_one_popul.get(self.cnt_genetic)[-1][1])}\n\nf: {f}.")

                    self.ui.label_popul.setText(f"Кількість популяцій: {str(self.cnt_genetic)}")
                    self.ui.label_mut.setText(f"Кількість мутацій: {str(cnt_mutation)}")
                    self.ui.label_x.setText(f"x:\n{str(self.gen.storoni_pryamoygol_and_minDot_for_one_popul.get(self.cnt_genetic)[-1][0])}")
                    self.ui.label_y.setText(f"y:\n{str(self.gen.storoni_pryamoygol_and_minDot_for_one_popul.get(self.cnt_genetic)[-1][1])}")
                    self.ui.label_f.setText(f"f:\n{f}")

                    self.ui.pushButton_run_algoritm.setEnabled(True)
                    self.ui.pushButton_run.setEnabled(True)
                    self.ui.radioButton.setEnabled(True)
                    self.ui.radioButton_2.setEnabled(True)
                    self.ui.Edit_start_popul.setReadOnly(False)
                    self.ui.Edit_end_popul.setReadOnly(False)

    def run_vyb(self):
        number_of_popul_one = self.ui.Edit_start_popul.toPlainText()
        number_of_popul_two = self.ui.Edit_end_popul.toPlainText()

        if number_of_popul_one == "" and number_of_popul_two == "":
            self.Msg("Error", "Поля початкової та кінцевої популяції не повинні бути порожніми!")
        
        try:
            number_of_popul_one = int(number_of_popul_one)
            number_of_popul_two = int(number_of_popul_two)
        except:
            self.Msg("Error", "Введено не число! Точки повинні бути цілим число!")

        if 0 >= number_of_popul_one <= self.cnt_genetic and 0 >= number_of_popul_two <= self.cnt_genetic:
            self.Msg("Error", f"Число для популяції має бути більшим '0' та менше популяції '{str(self.cnt_genetic)}'!")
                

        if number_of_popul_one > number_of_popul_two:
            self.Msg("Error", "Кінцеве число популяції має бути більше початкового!")
            prover_dot = False
        else:
            prover_dot = True

        if prover_dot:

            if self.ui.radioButton.isChecked():
                fig, ax = subplots()
                ion()

                self.gen.vybor_population(ax, number_of_popul_one, number_of_popul_two)

                ioff()
                show()

                self.Msg("Info", "Закрийте вікно малюнку.")

            if self.ui.radioButton_2.isChecked():
                self.gen.vybor_population_min_dot(number_of_popul_one, number_of_popul_two)
                self.Msg("Info", "Закрийте вікно малюнку.")

    def table_value(self):
        for i in self.ui.tableWidget.selectedItems():
            if i.column() == 1:
                self.ui.Edit_func.setText(i.text())

    def info_vvod_func(self):
        self.Msg("Info", "Для заповнення поля натисніть на формулу таблиці або введіть її вручну.")

    def info_vvod_pohib(self):
        self.Msg("Info", "Для введеня похібки вам потрібно: ввести негативну ступінь числа '10'.")

    def Msg(self, reson, message):
        msg = QMessageBox()
        if reson == "Error": 
            msg.setWindowTitle(reson)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()

        if reson == "Info":
            msg.setWindowTitle(reson)
            msg.setText(message)
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()