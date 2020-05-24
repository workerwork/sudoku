#!/usr/bin/python3

import sys
from PyQt5 import QtWidgets, QtCore
from sudokuUI import Ui_MainWindow
from solution import solution
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

s = []
for i in range(9):
    s.append([0] * 9)



class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow, solution):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        regex_lineEdit = QRegExp("[1-9]{1}")
        validator_lineEdit = QRegExpValidator(regex_lineEdit, self)
        self.lineEdit.setValidator(validator_lineEdit)
        self.lineEdit_2.setValidator(validator_lineEdit)
        self.lineEdit_3.setValidator(validator_lineEdit)
        self.lineEdit_4.setValidator(validator_lineEdit)
        self.lineEdit_5.setValidator(validator_lineEdit)
        self.lineEdit_6.setValidator(validator_lineEdit)
        self.lineEdit_7.setValidator(validator_lineEdit)
        self.lineEdit_8.setValidator(validator_lineEdit)
        self.lineEdit_9.setValidator(validator_lineEdit)
        self.lineEdit_10.setValidator(validator_lineEdit)
        self.lineEdit_11.setValidator(validator_lineEdit)
        self.lineEdit_12.setValidator(validator_lineEdit)
        self.lineEdit_13.setValidator(validator_lineEdit)
        self.lineEdit_14.setValidator(validator_lineEdit)
        self.lineEdit_15.setValidator(validator_lineEdit)
        self.lineEdit_16.setValidator(validator_lineEdit)
        self.lineEdit_17.setValidator(validator_lineEdit)
        self.lineEdit_18.setValidator(validator_lineEdit)
        self.lineEdit_19.setValidator(validator_lineEdit)
        self.lineEdit_20.setValidator(validator_lineEdit)
        self.lineEdit_21.setValidator(validator_lineEdit)
        self.lineEdit_22.setValidator(validator_lineEdit)
        self.lineEdit_23.setValidator(validator_lineEdit)
        self.lineEdit_24.setValidator(validator_lineEdit)
        self.lineEdit_25.setValidator(validator_lineEdit)
        self.lineEdit_26.setValidator(validator_lineEdit)
        self.lineEdit_27.setValidator(validator_lineEdit)
        self.lineEdit_28.setValidator(validator_lineEdit)
        self.lineEdit_29.setValidator(validator_lineEdit)
        self.lineEdit_30.setValidator(validator_lineEdit)
        self.lineEdit_31.setValidator(validator_lineEdit)
        self.lineEdit_32.setValidator(validator_lineEdit)
        self.lineEdit_33.setValidator(validator_lineEdit)
        self.lineEdit_34.setValidator(validator_lineEdit)
        self.lineEdit_35.setValidator(validator_lineEdit)
        self.lineEdit_36.setValidator(validator_lineEdit)
        self.lineEdit_37.setValidator(validator_lineEdit)
        self.lineEdit_38.setValidator(validator_lineEdit)
        self.lineEdit_39.setValidator(validator_lineEdit)
        self.lineEdit_40.setValidator(validator_lineEdit)
        self.lineEdit_41.setValidator(validator_lineEdit)
        self.lineEdit_42.setValidator(validator_lineEdit)
        self.lineEdit_43.setValidator(validator_lineEdit)
        self.lineEdit_44.setValidator(validator_lineEdit)
        self.lineEdit_45.setValidator(validator_lineEdit)
        self.lineEdit_46.setValidator(validator_lineEdit)
        self.lineEdit_47.setValidator(validator_lineEdit)
        self.lineEdit_48.setValidator(validator_lineEdit)
        self.lineEdit_49.setValidator(validator_lineEdit)
        self.lineEdit_50.setValidator(validator_lineEdit)
        self.lineEdit_51.setValidator(validator_lineEdit)
        self.lineEdit_52.setValidator(validator_lineEdit)
        self.lineEdit_53.setValidator(validator_lineEdit)
        self.lineEdit_54.setValidator(validator_lineEdit)
        self.lineEdit_55.setValidator(validator_lineEdit)
        self.lineEdit_56.setValidator(validator_lineEdit)
        self.lineEdit_57.setValidator(validator_lineEdit)
        self.lineEdit_58.setValidator(validator_lineEdit)
        self.lineEdit_59.setValidator(validator_lineEdit)
        self.lineEdit_60.setValidator(validator_lineEdit)
        self.lineEdit_61.setValidator(validator_lineEdit)
        self.lineEdit_62.setValidator(validator_lineEdit)
        self.lineEdit_63.setValidator(validator_lineEdit)
        self.lineEdit_64.setValidator(validator_lineEdit)
        self.lineEdit_65.setValidator(validator_lineEdit)
        self.lineEdit_66.setValidator(validator_lineEdit)
        self.lineEdit_67.setValidator(validator_lineEdit)
        self.lineEdit_68.setValidator(validator_lineEdit)
        self.lineEdit_69.setValidator(validator_lineEdit)
        self.lineEdit_70.setValidator(validator_lineEdit)
        self.lineEdit_71.setValidator(validator_lineEdit)
        self.lineEdit_72.setValidator(validator_lineEdit)
        self.lineEdit_73.setValidator(validator_lineEdit)
        self.lineEdit_74.setValidator(validator_lineEdit)
        self.lineEdit_75.setValidator(validator_lineEdit)
        self.lineEdit_76.setValidator(validator_lineEdit)
        self.lineEdit_77.setValidator(validator_lineEdit)
        self.lineEdit_78.setValidator(validator_lineEdit)
        self.lineEdit_79.setValidator(validator_lineEdit)
        self.lineEdit_80.setValidator(validator_lineEdit)
        self.lineEdit_81.setValidator(validator_lineEdit)

        #self.lineEdit.setStyleSheet('color:red')
        #self.lineEdit.setStyleSheet('background-color:green')
        #self.lineEdit.setStyleSheet('background-color:lightgrey')

        self.lineEdit.textChanged.connect(self.textChanged_lineEdit)
        self.lineEdit_2.textChanged.connect(self.textChanged_lineEdit_2)
        self.lineEdit_3.textChanged.connect(self.textChanged_lineEdit_3)
        self.lineEdit_4.textChanged.connect(self.textChanged_lineEdit_4)
        self.lineEdit_5.textChanged.connect(self.textChanged_lineEdit_5)
        self.lineEdit_6.textChanged.connect(self.textChanged_lineEdit_6)
        self.lineEdit_7.textChanged.connect(self.textChanged_lineEdit_7)
        self.lineEdit_8.textChanged.connect(self.textChanged_lineEdit_8)
        self.lineEdit_9.textChanged.connect(self.textChanged_lineEdit_9)
        self.lineEdit_10.textChanged.connect(self.textChanged_lineEdit_10)
        self.lineEdit_11.textChanged.connect(self.textChanged_lineEdit_11)
        self.lineEdit_12.textChanged.connect(self.textChanged_lineEdit_12)
        self.lineEdit_13.textChanged.connect(self.textChanged_lineEdit_13)
        self.lineEdit_14.textChanged.connect(self.textChanged_lineEdit_14)
        self.lineEdit_15.textChanged.connect(self.textChanged_lineEdit_15)
        self.lineEdit_16.textChanged.connect(self.textChanged_lineEdit_16)
        self.lineEdit_17.textChanged.connect(self.textChanged_lineEdit_17)
        self.lineEdit_18.textChanged.connect(self.textChanged_lineEdit_18)
        self.lineEdit_19.textChanged.connect(self.textChanged_lineEdit_19)
        self.lineEdit_20.textChanged.connect(self.textChanged_lineEdit_20)
        self.lineEdit_21.textChanged.connect(self.textChanged_lineEdit_21)
        self.lineEdit_22.textChanged.connect(self.textChanged_lineEdit_22)
        self.lineEdit_23.textChanged.connect(self.textChanged_lineEdit_23)
        self.lineEdit_24.textChanged.connect(self.textChanged_lineEdit_24)
        self.lineEdit_25.textChanged.connect(self.textChanged_lineEdit_25)
        self.lineEdit_26.textChanged.connect(self.textChanged_lineEdit_26)
        self.lineEdit_27.textChanged.connect(self.textChanged_lineEdit_27)
        self.lineEdit_28.textChanged.connect(self.textChanged_lineEdit_28)
        self.lineEdit_29.textChanged.connect(self.textChanged_lineEdit_29)
        self.lineEdit_30.textChanged.connect(self.textChanged_lineEdit_30)
        self.lineEdit_31.textChanged.connect(self.textChanged_lineEdit_31)
        self.lineEdit_32.textChanged.connect(self.textChanged_lineEdit_32)
        self.lineEdit_33.textChanged.connect(self.textChanged_lineEdit_33)
        self.lineEdit_34.textChanged.connect(self.textChanged_lineEdit_34)
        self.lineEdit_35.textChanged.connect(self.textChanged_lineEdit_35)
        self.lineEdit_36.textChanged.connect(self.textChanged_lineEdit_36)
        self.lineEdit_37.textChanged.connect(self.textChanged_lineEdit_37)
        self.lineEdit_38.textChanged.connect(self.textChanged_lineEdit_38)
        self.lineEdit_39.textChanged.connect(self.textChanged_lineEdit_39)
        self.lineEdit_40.textChanged.connect(self.textChanged_lineEdit_40)
        self.lineEdit_41.textChanged.connect(self.textChanged_lineEdit_41)
        self.lineEdit_42.textChanged.connect(self.textChanged_lineEdit_42)
        self.lineEdit_43.textChanged.connect(self.textChanged_lineEdit_43)
        self.lineEdit_44.textChanged.connect(self.textChanged_lineEdit_44)
        self.lineEdit_45.textChanged.connect(self.textChanged_lineEdit_45)
        self.lineEdit_46.textChanged.connect(self.textChanged_lineEdit_46)
        self.lineEdit_47.textChanged.connect(self.textChanged_lineEdit_47)
        self.lineEdit_48.textChanged.connect(self.textChanged_lineEdit_48)
        self.lineEdit_49.textChanged.connect(self.textChanged_lineEdit_49)
        self.lineEdit_50.textChanged.connect(self.textChanged_lineEdit_50)
        self.lineEdit_51.textChanged.connect(self.textChanged_lineEdit_51)
        self.lineEdit_52.textChanged.connect(self.textChanged_lineEdit_52)
        self.lineEdit_53.textChanged.connect(self.textChanged_lineEdit_53)
        self.lineEdit_54.textChanged.connect(self.textChanged_lineEdit_54)
        self.lineEdit_55.textChanged.connect(self.textChanged_lineEdit_55)
        self.lineEdit_56.textChanged.connect(self.textChanged_lineEdit_56)
        self.lineEdit_57.textChanged.connect(self.textChanged_lineEdit_57)
        self.lineEdit_58.textChanged.connect(self.textChanged_lineEdit_58)
        self.lineEdit_59.textChanged.connect(self.textChanged_lineEdit_59)
        self.lineEdit_60.textChanged.connect(self.textChanged_lineEdit_60)
        self.lineEdit_61.textChanged.connect(self.textChanged_lineEdit_61)
        self.lineEdit_62.textChanged.connect(self.textChanged_lineEdit_62)
        self.lineEdit_63.textChanged.connect(self.textChanged_lineEdit_63)
        self.lineEdit_64.textChanged.connect(self.textChanged_lineEdit_64)
        self.lineEdit_65.textChanged.connect(self.textChanged_lineEdit_65)
        self.lineEdit_66.textChanged.connect(self.textChanged_lineEdit_66)
        self.lineEdit_67.textChanged.connect(self.textChanged_lineEdit_67)
        self.lineEdit_68.textChanged.connect(self.textChanged_lineEdit_68)
        self.lineEdit_69.textChanged.connect(self.textChanged_lineEdit_69)
        self.lineEdit_70.textChanged.connect(self.textChanged_lineEdit_70)
        self.lineEdit_71.textChanged.connect(self.textChanged_lineEdit_71)
        self.lineEdit_72.textChanged.connect(self.textChanged_lineEdit_72)
        self.lineEdit_73.textChanged.connect(self.textChanged_lineEdit_73)
        self.lineEdit_74.textChanged.connect(self.textChanged_lineEdit_74)
        self.lineEdit_75.textChanged.connect(self.textChanged_lineEdit_75)
        self.lineEdit_76.textChanged.connect(self.textChanged_lineEdit_76)
        self.lineEdit_77.textChanged.connect(self.textChanged_lineEdit_77)
        self.lineEdit_78.textChanged.connect(self.textChanged_lineEdit_78)
        self.lineEdit_79.textChanged.connect(self.textChanged_lineEdit_79)
        self.lineEdit_80.textChanged.connect(self.textChanged_lineEdit_80)
        self.lineEdit_81.textChanged.connect(self.textChanged_lineEdit_81)
        self.pushButton.clicked.connect(self.s_solution)
        self.pushButton_2.clicked.connect(self.clear)

    def textChanged_lineEdit(self):
        if self.lineEdit.text() == '':
            s[0][0] = 0
            self.lineEdit.setStyleSheet('background-color:white')
        else:
            s[0][0] = int(self.lineEdit.text())
            self.lineEdit.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_2(self):
        if self.lineEdit_2.text() == '':
            s[0][1] = 0
            self.lineEdit_2.setStyleSheet('background-color:white')
        else:
            s[0][1] = int(self.lineEdit_2.text())
            self.lineEdit_2.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_3(self):
        if self.lineEdit_3.text() == '':
            s[0][2] = 0
            self.lineEdit_3.setStyleSheet('background-color:white')
        else:
            s[0][2] = int(self.lineEdit_3.text())
            self.lineEdit_3.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_4(self):
        if self.lineEdit_4.text() == '':
            s[0][3] = 0
            self.lineEdit_4.setStyleSheet('background-color:white')
        else:
            s[0][3] = int(self.lineEdit_4.text())
            self.lineEdit_4.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_5(self):
        if self.lineEdit_5.text() == '':
            s[0][4] = 0
            self.lineEdit_5.setStyleSheet('background-color:white')
        else:
            s[0][4] = int(self.lineEdit_5.text())
            self.lineEdit_5.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_6(self):
        if self.lineEdit_6.text() == '':
            s[0][5] = 0
            self.lineEdit_6.setStyleSheet('background-color:white')
        else:
            s[0][5] = int(self.lineEdit_6.text())
            self.lineEdit_6.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_7(self):
        if self.lineEdit_7.text() == '':
            s[0][6] = 0
            self.lineEdit_7.setStyleSheet('background-color:white')
        else:
            s[0][6] = int(self.lineEdit_7.text())
            self.lineEdit_7.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_8(self):
        if self.lineEdit_8.text() == '':
            s[0][7] = 0
            self.lineEdit_8.setStyleSheet('background-color:white')
        else:
            s[0][7] = int(self.lineEdit_8.text())
            self.lineEdit_8.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_9(self):
        if self.lineEdit_9.text() == '':
            s[0][8] = 0
            self.lineEdit_9.setStyleSheet('background-color:white')
        else:
            s[0][8] = int(self.lineEdit_9.text())
            self.lineEdit_9.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_10(self):
        if self.lineEdit_10.text() == '':
            s[1][0] = 0
            self.lineEdit_10.setStyleSheet('background-color:white')
        else:
            s[1][0] = int(self.lineEdit_10.text())
            self.lineEdit_10.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_11(self):
        if self.lineEdit_11.text() == '':
            s[1][1] = 0
            self.lineEdit_11.setStyleSheet('background-color:white')
        else:
            s[1][1] = int(self.lineEdit_11.text())
            self.lineEdit_11.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_12(self):
        if self.lineEdit_12.text() == '':
            s[1][2] = 0
            self.lineEdit_12.setStyleSheet('background-color:white')
        else:
            s[1][2] = int(self.lineEdit_12.text())
            self.lineEdit_12.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_13(self):
        if self.lineEdit_13.text() == '':
            s[1][3] = 0
            self.lineEdit_13.setStyleSheet('background-color:white')
        else:
            s[1][3] = int(self.lineEdit_13.text())
            self.lineEdit_13.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_14(self):
        if self.lineEdit_14.text() == '':
            s[1][4] = 0
            self.lineEdit_14.setStyleSheet('background-color:white')
        else:
            s[1][4] = int(self.lineEdit_14.text())
            self.lineEdit_14.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_15(self):
        if self.lineEdit_15.text() == '':
            s[1][5] = 0
            self.lineEdit_15.setStyleSheet('background-color:white')
        else:
            s[1][5] = int(self.lineEdit_15.text())
            self.lineEdit_15.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_16(self):
        if self.lineEdit_16.text() == '':
            s[1][6] = 0
            self.lineEdit_16.setStyleSheet('background-color:white')
        else:
            s[1][6] = int(self.lineEdit_16.text())
            self.lineEdit_16.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_17(self):
        if self.lineEdit_17.text() == '':
            s[1][7] = 0
            self.lineEdit_17.setStyleSheet('background-color:white')
        else:
            s[1][7] = int(self.lineEdit_17.text())
            self.lineEdit_17.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_18(self):
        if self.lineEdit_18.text() == '':
            s[1][8] = 0
            self.lineEdit_18.setStyleSheet('background-color:white')
        else:
            s[1][8] = int(self.lineEdit_18.text())
            self.lineEdit_18.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_19(self):
        if self.lineEdit_19.text() == '':
            s[2][0] = 0
            self.lineEdit_19.setStyleSheet('background-color:white')
        else:
            s[2][0] = int(self.lineEdit_19.text())
            self.lineEdit_19.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_20(self):
        if self.lineEdit_20.text() == '':
            s[2][1] = 0
            self.lineEdit_20.setStyleSheet('background-color:white')
        else:
            s[2][1] = int(self.lineEdit_20.text())
            self.lineEdit_20.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_21(self):
        if self.lineEdit_21.text() == '':
            s[2][2] = 0
            self.lineEdit_21.setStyleSheet('background-color:white')
        else:
            s[2][2] = int(self.lineEdit_21.text())
            self.lineEdit_21.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_22(self):
        if self.lineEdit_22.text() == '':
            s[2][3] = 0
            self.lineEdit_22.setStyleSheet('background-color:white')
        else:
            s[2][3] = int(self.lineEdit_22.text())
            self.lineEdit_22.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_23(self):
        if self.lineEdit_23.text() == '':
            s[2][4] = 0
            self.lineEdit_23.setStyleSheet('background-color:white')
        else:
            s[2][4] = int(self.lineEdit_23.text())
            self.lineEdit_23.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_24(self):
        if self.lineEdit_24.text() == '':
            s[2][5] = 0
            self.lineEdit_24.setStyleSheet('background-color:white')
        else:
            s[2][5] = int(self.lineEdit_24.text())
            self.lineEdit_24.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_25(self):
        if self.lineEdit_25.text() == '':
            s[2][6] = 0
            self.lineEdit_25.setStyleSheet('background-color:white')
        else:
            s[2][6] = int(self.lineEdit_25.text())
            self.lineEdit_25.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_26(self):
        if self.lineEdit_26.text() == '':
            s[2][7] = 0
            self.lineEdit_26.setStyleSheet('background-color:white')
        else:
            s[2][7] = int(self.lineEdit_26.text())
            self.lineEdit_26.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_27(self):
        if self.lineEdit_27.text() == '':
            s[2][8] = 0
            self.lineEdit_27.setStyleSheet('background-color:white')
        else:
            s[2][8] = int(self.lineEdit_27.text())
            self.lineEdit_27.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_28(self):
        if self.lineEdit_28.text() == '':
            s[3][0] = 0
            self.lineEdit_28.setStyleSheet('background-color:white')
        else:
            s[3][0] = int(self.lineEdit_28.text())
            self.lineEdit_28.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_29(self):
        if self.lineEdit_29.text() == '':
            s[3][1] = 0
            self.lineEdit_29.setStyleSheet('background-color:white')
        else:
            s[3][1] = int(self.lineEdit_29.text())
            self.lineEdit_29.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_30(self):
        if self.lineEdit_30.text() == '':
            s[3][2] = 0
            self.lineEdit_30.setStyleSheet('background-color:white')
        else:
            s[3][2] = int(self.lineEdit_30.text())
            self.lineEdit_30.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_31(self):
        if self.lineEdit_31.text() == '':
            s[3][3] = 0
            self.lineEdit_31.setStyleSheet('background-color:white')
        else:
            s[3][3] = int(self.lineEdit_31.text())
            self.lineEdit_31.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_32(self):
        if self.lineEdit_32.text() == '':
            s[3][4] = 0
            self.lineEdit_32.setStyleSheet('background-color:white')
        else:
            s[3][4] = int(self.lineEdit_32.text())
            self.lineEdit_32.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_33(self):
        if self.lineEdit_33.text() == '':
            s[3][5] = 0
            self.lineEdit_33.setStyleSheet('background-color:white')
        else:
            s[3][5] = int(self.lineEdit_33.text())
            self.lineEdit_33.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_34(self):
        if self.lineEdit_34.text() == '':
            s[3][6] = 0
            self.lineEdit_34.setStyleSheet('background-color:white')
        else:
            s[3][6] = int(self.lineEdit_34.text())
            self.lineEdit_34.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_35(self):
        if self.lineEdit_35.text() == '':
            s[3][7] = 0
            self.lineEdit_35.setStyleSheet('background-color:white')
        else:
            s[3][7] = int(self.lineEdit_35.text())
            self.lineEdit_35.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_36(self):
        if self.lineEdit_36.text() == '':
            s[3][8] = 0
            self.lineEdit_36.setStyleSheet('background-color:white')
        else:
            s[3][8] = int(self.lineEdit_36.text())
            self.lineEdit_36.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_37(self):
        if self.lineEdit_37.text() == '':
            s[4][0] = 0
            self.lineEdit_37.setStyleSheet('background-color:white')
        else:
            s[4][0] = int(self.lineEdit_37.text())
            self.lineEdit_37.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_38(self):
        if self.lineEdit_38.text() == '':
            s[4][1] = 0
            self.lineEdit_38.setStyleSheet('background-color:white')
        else:
            s[4][1] = int(self.lineEdit_38.text())
            self.lineEdit_38.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_39(self):
        if self.lineEdit_39.text() == '':
            s[4][2] = 0
            self.lineEdit_39.setStyleSheet('background-color:white')
        else:
            s[4][2] = int(self.lineEdit_39.text())
            self.lineEdit_39.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_40(self):
        if self.lineEdit_40.text() == '':
            s[4][3] = 0
            self.lineEdit_40.setStyleSheet('background-color:white')
        else:
            s[4][3] = int(self.lineEdit_40.text())
            self.lineEdit_40.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_41(self):
        if self.lineEdit_41.text() == '':
            s[4][4] = 0
            self.lineEdit_41.setStyleSheet('background-color:white')
        else:
            s[4][4] = int(self.lineEdit_41.text())
            self.lineEdit_41.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_42(self):
        if self.lineEdit_42.text() == '':
            s[4][5] = 0
            self.lineEdit_42.setStyleSheet('background-color:white')
        else:
            s[4][5] = int(self.lineEdit_42.text())
            self.lineEdit_42.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_43(self):
        if self.lineEdit_43.text() == '':
            s[4][6] = 0
            self.lineEdit_43.setStyleSheet('background-color:white')
        else:
            s[4][6] = int(self.lineEdit_43.text())
            self.lineEdit_43.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_44(self):
        if self.lineEdit_44.text() == '':
            s[4][7] = 0
            self.lineEdit_44.setStyleSheet('background-color:white')
        else:
            s[4][7] = int(self.lineEdit_44.text())
            self.lineEdit_44.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_45(self):
        if self.lineEdit_45.text() == '':
            s[4][8] = 0
            self.lineEdit_45.setStyleSheet('background-color:white')
        else:
            s[4][8] = int(self.lineEdit_45.text())
            self.lineEdit_45.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_46(self):
        if self.lineEdit_46.text() == '':
            s[5][0] = 0
            self.lineEdit_46.setStyleSheet('background-color:white')
        else:
            s[5][0] = int(self.lineEdit_46.text())
            self.lineEdit_46.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_47(self):
        if self.lineEdit_47.text() == '':
            s[5][1] = 0
            self.lineEdit_47.setStyleSheet('background-color:white')
        else:
            s[5][1] = int(self.lineEdit_47.text())
            self.lineEdit_47.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_48(self):
        if self.lineEdit_48.text() == '':
            s[5][2] = 0
            self.lineEdit_48.setStyleSheet('background-color:white')
        else:
            s[5][2] = int(self.lineEdit_48.text())
            self.lineEdit_48.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_49(self):
        if self.lineEdit_49.text() == '':
            s[5][3] = 0
            self.lineEdit_49.setStyleSheet('background-color:white')
        else:
            s[5][3] = int(self.lineEdit_49.text())
            self.lineEdit_49.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_50(self):
        if self.lineEdit_50.text() == '':
            s[5][4] = 0
            self.lineEdit_50.setStyleSheet('background-color:white')
        else:
            s[5][4] = int(self.lineEdit_50.text())
            self.lineEdit_50.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_51(self):
        if self.lineEdit_51.text() == '':
            s[5][5] = 0
            self.lineEdit_51.setStyleSheet('background-color:white')
        else:
            s[5][5] = int(self.lineEdit_51.text())
            self.lineEdit_51.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_52(self):
        if self.lineEdit_52.text() == '':
            s[5][6] = 0
            self.lineEdit_52.setStyleSheet('background-color:white')
        else:
            s[5][6] = int(self.lineEdit_52.text())
            self.lineEdit_52.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_53(self):
        if self.lineEdit_53.text() == '':
            s[5][7] = 0
            self.lineEdit_53.setStyleSheet('background-color:white')
        else:
            s[5][7] = int(self.lineEdit_53.text())
            self.lineEdit_53.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_54(self):
        if self.lineEdit_54.text() == '':
            s[5][8] = 0
            self.lineEdit_54.setStyleSheet('background-color:white')
        else:
            s[5][8] = int(self.lineEdit_54.text())
            self.lineEdit_54.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_55(self):
        if self.lineEdit_55.text() == '':
            s[6][0] = 0
            self.lineEdit_55.setStyleSheet('background-color:white')
        else:
            s[6][0] = int(self.lineEdit_55.text())
            self.lineEdit_55.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_56(self):
        if self.lineEdit_56.text() == '':
            s[6][1] = 0
            self.lineEdit_56.setStyleSheet('background-color:white')
        else:
            s[6][1] = int(self.lineEdit_56.text())
            self.lineEdit_56.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_57(self):
        if self.lineEdit_57.text() == '':
            s[6][2] = 0
            self.lineEdit_57.setStyleSheet('background-color:white')
        else:
            s[6][2] = int(self.lineEdit_57.text())
            self.lineEdit_57.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_58(self):
        if self.lineEdit_58.text() == '':
            s[6][3] = 0
            self.lineEdit_58.setStyleSheet('background-color:white')
        else:
            s[6][3] = int(self.lineEdit_58.text())
            self.lineEdit_58.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_59(self):
        if self.lineEdit_59.text() == '':
            s[6][4] = 0
            self.lineEdit_59.setStyleSheet('background-color:white')
        else:
            s[6][4] = int(self.lineEdit_59.text())
            self.lineEdit_59.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_60(self):
        if self.lineEdit_60.text() == '':
            s[6][5] = 0
            self.lineEdit_60.setStyleSheet('background-color:white')
        else:
            s[6][5] = int(self.lineEdit_60.text())
            self.lineEdit_60.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_61(self):
        if self.lineEdit_61.text() == '':
            s[6][6] = 0
            self.lineEdit_61.setStyleSheet('background-color:white')
        else:
            s[6][6] = int(self.lineEdit_61.text())
            self.lineEdit_61.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_62(self):
        if self.lineEdit_62.text() == '':
            s[6][7] = 0
            self.lineEdit_62.setStyleSheet('background-color:white')
        else:
            s[6][7] = int(self.lineEdit_62.text())
            self.lineEdit_62.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_63(self):
        if self.lineEdit_63.text() == '':
            s[6][8] = 0
            self.lineEdit_63.setStyleSheet('background-color:white')
        else:
            s[6][8] = int(self.lineEdit_63.text())
            self.lineEdit_63.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_64(self):
        if self.lineEdit_64.text() == '':
            s[7][0] = 0
            self.lineEdit_64.setStyleSheet('background-color:white')
        else:
            s[7][0] = int(self.lineEdit_64.text())
            self.lineEdit_64.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_65(self):
        if self.lineEdit_65.text() == '':
            s[7][1] = 0
            self.lineEdit_65.setStyleSheet('background-color:white')
        else:
            s[7][1] = int(self.lineEdit_65.text())
            self.lineEdit_65.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_66(self):
        if self.lineEdit_66.text() == '':
            s[7][2] = 0
            self.lineEdit_66.setStyleSheet('background-color:white')
        else:
            s[7][2] = int(self.lineEdit_66.text())
            self.lineEdit_66.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_67(self):
        if self.lineEdit_67.text() == '':
            s[7][3] = 0
            self.lineEdit_67.setStyleSheet('background-color:white')
        else:
            s[7][3] = int(self.lineEdit_67.text())
            self.lineEdit_67.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_68(self):
        if self.lineEdit_68.text() == '':
            s[7][4] = 0
            self.lineEdit_68.setStyleSheet('background-color:white')
        else:
            s[7][4] = int(self.lineEdit_68.text())
            self.lineEdit_68.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_69(self):
        if self.lineEdit_69.text() == '':
            s[7][5] = 0
            self.lineEdit_69.setStyleSheet('background-color:white')
        else:
            s[7][5] = int(self.lineEdit_69.text())
            self.lineEdit_69.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_70(self):
        if self.lineEdit_70.text() == '':
            s[7][6] = 0
            self.lineEdit_70.setStyleSheet('background-color:white')
        else:
            s[7][6] = int(self.lineEdit_70.text())
            self.lineEdit_70.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_71(self):
        if self.lineEdit_71.text() == '':
            s[7][7] = 0
            self.lineEdit_71.setStyleSheet('background-color:white')
        else:
            s[7][7] = int(self.lineEdit_71.text())
            self.lineEdit_71.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_72(self):
        if self.lineEdit_72.text() == '':
            s[7][8] = 0
            self.lineEdit_72.setStyleSheet('background-color:white')
        else:
            s[7][8] = int(self.lineEdit_72.text())
            self.lineEdit_72.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_73(self):
        if self.lineEdit_73.text() == '':
            s[8][0] = 0
            self.lineEdit_73.setStyleSheet('background-color:white')
        else:
            s[8][0] = int(self.lineEdit_73.text())
            self.lineEdit_73.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_74(self):
        if self.lineEdit_74.text() == '':
            s[8][1] = 0
            self.lineEdit_74.setStyleSheet('background-color:white')
        else:
            s[8][1] = int(self.lineEdit_74.text())
            self.lineEdit_74.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_75(self):
        if self.lineEdit_75.text() == '':
            s[8][2] = 0
            self.lineEdit_75.setStyleSheet('background-color:white')
        else:
            s[8][2] = int(self.lineEdit_75.text())
            self.lineEdit_75.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_76(self):
        if self.lineEdit_76.text() == '':
            s[8][3] = 0
            self.lineEdit_76.setStyleSheet('background-color:white')
        else:
            s[8][3] = int(self.lineEdit_76.text())
            self.lineEdit_76.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_77(self):
        if self.lineEdit_77.text() == '':
            s[8][4] = 0
            self.lineEdit_77.setStyleSheet('background-color:white')
        else:
            s[8][4] = int(self.lineEdit_77.text())
            self.lineEdit_77.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_78(self):
        if self.lineEdit_78.text() == '':
            s[8][5] = 0
            self.lineEdit_78.setStyleSheet('background-color:white')
        else:
            s[8][5] = int(self.lineEdit_78.text())
            self.lineEdit_78.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_79(self):
        if self.lineEdit_79.text() == '':
            s[8][6] = 0
            self.lineEdit_79.setStyleSheet('background-color:white')
        else:
            s[8][6] = int(self.lineEdit_79.text())
            self.lineEdit_79.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_80(self):
        if self.lineEdit_80.text() == '':
            s[8][7] = 0
            self.lineEdit_80.setStyleSheet('background-color:white')
        else:
            s[8][7] = int(self.lineEdit_80.text())
            self.lineEdit_80.setStyleSheet('background-color:lightgrey')
    def textChanged_lineEdit_81(self):
        if self.lineEdit_81.text() == '':
            s[8][8] = 0
            self.lineEdit_81.setStyleSheet('background-color:white')
        else:
            s[8][8] = int(self.lineEdit_81.text())
            self.lineEdit_81.setStyleSheet('background-color:lightgrey')

    def clear(self):
        self.lineEdit.setText('')
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_2.setText('')
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_3.setText('')
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_4.setText('')
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_5.setText('')
        self.lineEdit_5.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_6.setText('')
        self.lineEdit_6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_7.setText('')
        self.lineEdit_7.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_8.setText('')
        self.lineEdit_8.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_9.setText('')
        self.lineEdit_9.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_10.setText('')
        self.lineEdit_10.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_11.setText('')
        self.lineEdit_11.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_12.setText('')
        self.lineEdit_12.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_13.setText('')
        self.lineEdit_13.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_14.setText('')
        self.lineEdit_14.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_15.setText('')
        self.lineEdit_15.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_16.setText('')
        self.lineEdit_16.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_17.setText('')
        self.lineEdit_17.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_18.setText('')
        self.lineEdit_18.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_19.setText('')
        self.lineEdit_19.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_20.setText('')
        self.lineEdit_20.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_21.setText('')
        self.lineEdit_21.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_22.setText('')
        self.lineEdit_22.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_23.setText('')
        self.lineEdit_23.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_24.setText('')
        self.lineEdit_24.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_25.setText('')
        self.lineEdit_25.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_26.setText('')
        self.lineEdit_26.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_27.setText('')
        self.lineEdit_27.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_28.setText('')
        self.lineEdit_28.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_29.setText('')
        self.lineEdit_29.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_30.setText('')
        self.lineEdit_30.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_31.setText('')
        self.lineEdit_31.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_32.setText('')
        self.lineEdit_32.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_33.setText('')
        self.lineEdit_33.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_34.setText('')
        self.lineEdit_34.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_35.setText('')
        self.lineEdit_35.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_36.setText('')
        self.lineEdit_36.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_37.setText('')
        self.lineEdit_37.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_38.setText('')
        self.lineEdit_38.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_39.setText('')
        self.lineEdit_39.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_40.setText('')
        self.lineEdit_40.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_41.setText('')
        self.lineEdit_41.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_42.setText('')
        self.lineEdit_42.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_43.setText('')
        self.lineEdit_43.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_44.setText('')
        self.lineEdit_44.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_45.setText('')
        self.lineEdit_45.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_46.setText('')
        self.lineEdit_46.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_47.setText('')
        self.lineEdit_47.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_48.setText('')
        self.lineEdit_48.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_49.setText('')
        self.lineEdit_49.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_50.setText('')
        self.lineEdit_50.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_51.setText('')
        self.lineEdit_51.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_52.setText('')
        self.lineEdit_52.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_53.setText('')
        self.lineEdit_53.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_54.setText('')
        self.lineEdit_54.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_55.setText('')
        self.lineEdit_55.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_56.setText('')
        self.lineEdit_56.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_57.setText('')
        self.lineEdit_57.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_58.setText('')
        self.lineEdit_58.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_59.setText('')
        self.lineEdit_59.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_60.setText('')
        self.lineEdit_60.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_61.setText('')
        self.lineEdit_61.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_62.setText('')
        self.lineEdit_62.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_63.setText('')
        self.lineEdit_63.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_64.setText('')
        self.lineEdit_64.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_65.setText('')
        self.lineEdit_65.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_66.setText('')
        self.lineEdit_66.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_67.setText('')
        self.lineEdit_67.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_68.setText('')
        self.lineEdit_68.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_69.setText('')
        self.lineEdit_69.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_70.setText('')
        self.lineEdit_70.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_71.setText('')
        self.lineEdit_71.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_72.setText('')
        self.lineEdit_72.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_73.setText('')
        self.lineEdit_73.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_74.setText('')
        self.lineEdit_74.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_75.setText('')
        self.lineEdit_75.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_76.setText('')
        self.lineEdit_76.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_77.setText('')
        self.lineEdit_77.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_78.setText('')
        self.lineEdit_78.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_79.setText('')
        self.lineEdit_79.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_80.setText('')
        self.lineEdit_80.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_81.setText('')
        self.lineEdit_81.setFocusPolicy(QtCore.Qt.StrongFocus)

    def input_result(self):
        if self.lineEdit.text() == '':
            self.lineEdit.setText(str(s[0][0]))
            self.lineEdit.setStyleSheet('background-color:white')
        self.lineEdit.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_2.text() == '':
            self.lineEdit_2.setText(str(s[0][1]))
            self.lineEdit_2.setStyleSheet('background-color:white')
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_3.text() == '':
            self.lineEdit_3.setText(str(s[0][2]))
            self.lineEdit_3.setStyleSheet('background-color:white')
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_4.text() == '':
            self.lineEdit_4.setText(str(s[0][3]))
            self.lineEdit_4.setStyleSheet('background-color:white')
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_5.text() == '':
            self.lineEdit_5.setText(str(s[0][4]))
            self.lineEdit_5.setStyleSheet('background-color:white')
        self.lineEdit_5.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_6.text() == '':
            self.lineEdit_6.setText(str(s[0][5]))
            self.lineEdit_6.setStyleSheet('background-color:white')
        self.lineEdit_6.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_7.text() == '':
            self.lineEdit_7.setText(str(s[0][6]))
            self.lineEdit_7.setStyleSheet('background-color:white')
        self.lineEdit_7.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_8.text() == '':
            self.lineEdit_8.setText(str(s[0][7]))
            self.lineEdit_8.setStyleSheet('background-color:white')
        self.lineEdit_8.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_9.text() == '':
            self.lineEdit_9.setText(str(s[0][8]))
            self.lineEdit_9.setStyleSheet('background-color:white')
        self.lineEdit_9.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_10.text() == '':
            self.lineEdit_10.setText(str(s[1][0]))
            self.lineEdit_10.setStyleSheet('background-color:white')
        self.lineEdit_10.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_11.text() == '':
            self.lineEdit_11.setText(str(s[1][1]))
            self.lineEdit_11.setStyleSheet('background-color:white')
        self.lineEdit_11.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_12.text() == '':
            self.lineEdit_12.setText(str(s[1][2]))
            self.lineEdit_12.setStyleSheet('background-color:white')
        self.lineEdit_12.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_13.text() == '':
            self.lineEdit_13.setText(str(s[1][3]))
            self.lineEdit_13.setStyleSheet('background-color:white')
        self.lineEdit_13.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_14.text() == '':
            self.lineEdit_14.setText(str(s[1][4]))
            self.lineEdit_14.setStyleSheet('background-color:white')
        self.lineEdit_14.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_15.text() == '':
            self.lineEdit_15.setText(str(s[1][5]))
            self.lineEdit_15.setStyleSheet('background-color:white')
        self.lineEdit_15.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_16.text() == '':
            self.lineEdit_16.setText(str(s[1][6]))
            self.lineEdit_16.setStyleSheet('background-color:white')
        self.lineEdit_16.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_17.text() == '':
            self.lineEdit_17.setText(str(s[1][7]))
            self.lineEdit_17.setStyleSheet('background-color:white')
        self.lineEdit_17.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_18.text() == '':
            self.lineEdit_18.setText(str(s[1][8]))
            self.lineEdit_18.setStyleSheet('background-color:white')
        self.lineEdit_18.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_19.text() == '':
            self.lineEdit_19.setText(str(s[2][0]))
            self.lineEdit_19.setStyleSheet('background-color:white')
        self.lineEdit_19.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_20.text() == '':
            self.lineEdit_20.setText(str(s[2][1]))
            self.lineEdit_20.setStyleSheet('background-color:white')
        self.lineEdit_20.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_21.text() == '':
            self.lineEdit_21.setText(str(s[2][2]))
            self.lineEdit_21.setStyleSheet('background-color:white')
        self.lineEdit_21.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_22.text() == '':
            self.lineEdit_22.setText(str(s[2][3]))
            self.lineEdit_22.setStyleSheet('background-color:white')
        self.lineEdit_22.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_23.text() == '':
            self.lineEdit_23.setText(str(s[2][4]))
            self.lineEdit_23.setStyleSheet('background-color:white')
        self.lineEdit_23.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_24.text() == '':
            self.lineEdit_24.setText(str(s[2][5]))
            self.lineEdit_24.setStyleSheet('background-color:white')
        self.lineEdit_24.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_25.text() == '':
            self.lineEdit_25.setText(str(s[2][6]))
            self.lineEdit_25.setStyleSheet('background-color:white')
        self.lineEdit_25.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_26.text() == '':
            self.lineEdit_26.setText(str(s[2][7]))
            self.lineEdit_26.setStyleSheet('background-color:white')
        self.lineEdit_26.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_27.text() == '':
            self.lineEdit_27.setText(str(s[2][8]))
            self.lineEdit_27.setStyleSheet('background-color:white')
        self.lineEdit_27.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_28.text() == '':
            self.lineEdit_28.setText(str(s[3][0]))
            self.lineEdit_28.setStyleSheet('background-color:white')
        self.lineEdit_28.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_29.text() == '':
            self.lineEdit_29.setText(str(s[3][1]))
            self.lineEdit_29.setStyleSheet('background-color:white')
        self.lineEdit_29.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_30.text() == '':
            self.lineEdit_30.setText(str(s[3][2]))
            self.lineEdit_30.setStyleSheet('background-color:white')
        self.lineEdit_30.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_31.text() == '':
            self.lineEdit_31.setText(str(s[3][3]))
            self.lineEdit_31.setStyleSheet('background-color:white')
        self.lineEdit_31.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_32.text() == '':
            self.lineEdit_32.setText(str(s[3][4]))
            self.lineEdit_32.setStyleSheet('background-color:white')
        self.lineEdit_32.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_33.text() == '':
            self.lineEdit_33.setText(str(s[3][5]))
            self.lineEdit_33.setStyleSheet('background-color:white')
        self.lineEdit_33.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_34.text() == '':
            self.lineEdit_34.setText(str(s[3][6]))
            self.lineEdit_34.setStyleSheet('background-color:white')
        self.lineEdit_34.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_35.text() == '':
            self.lineEdit_35.setText(str(s[3][7]))
            self.lineEdit_35.setStyleSheet('background-color:white')
        self.lineEdit_35.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_36.text() == '':
            self.lineEdit_36.setText(str(s[3][8]))
            self.lineEdit_36.setStyleSheet('background-color:white')
        self.lineEdit_36.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_37.text() == '':
            self.lineEdit_37.setText(str(s[4][0]))
            self.lineEdit_37.setStyleSheet('background-color:white')
        self.lineEdit_37.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_38.text() == '':
            self.lineEdit_38.setText(str(s[4][1]))
            self.lineEdit_38.setStyleSheet('background-color:white')
        self.lineEdit_38.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_39.text() == '':
            self.lineEdit_39.setText(str(s[4][2]))
            self.lineEdit_39.setStyleSheet('background-color:white')
        self.lineEdit_39.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_40.text() == '':
            self.lineEdit_40.setText(str(s[4][3]))
            self.lineEdit_40.setStyleSheet('background-color:white')
        self.lineEdit_40.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_41.text() == '':
            self.lineEdit_41.setText(str(s[4][4]))
            self.lineEdit_41.setStyleSheet('background-color:white')
        self.lineEdit_41.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_42.text() == '':
            self.lineEdit_42.setText(str(s[4][5]))
            self.lineEdit_42.setStyleSheet('background-color:white')
        self.lineEdit_42.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_43.text() == '':
            self.lineEdit_43.setText(str(s[4][6]))
            self.lineEdit_43.setStyleSheet('background-color:white')
        self.lineEdit_43.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_44.text() == '':
            self.lineEdit_44.setText(str(s[4][7]))
            self.lineEdit_44.setStyleSheet('background-color:white')
        self.lineEdit_44.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_45.text() == '':
            self.lineEdit_45.setText(str(s[4][8]))
            self.lineEdit_45.setStyleSheet('background-color:white')
        self.lineEdit_45.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_46.text() == '':
            self.lineEdit_46.setText(str(s[5][0]))
            self.lineEdit_46.setStyleSheet('background-color:white')
        self.lineEdit_46.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_47.text() == '':
            self.lineEdit_47.setText(str(s[5][1]))
            self.lineEdit_47.setStyleSheet('background-color:white')
        self.lineEdit_47.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_48.text() == '':
            self.lineEdit_48.setText(str(s[5][2]))
            self.lineEdit_48.setStyleSheet('background-color:white')
        self.lineEdit_48.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_49.text() == '':
            self.lineEdit_49.setText(str(s[5][3]))
            self.lineEdit_49.setStyleSheet('background-color:white')
        self.lineEdit_49.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_50.text() == '':
            self.lineEdit_50.setText(str(s[5][4]))
            self.lineEdit_50.setStyleSheet('background-color:white')
        self.lineEdit_50.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_51.text() == '':
            self.lineEdit_51.setText(str(s[5][5]))
            self.lineEdit_51.setStyleSheet('background-color:white')
        self.lineEdit_51.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_52.text() == '':
            self.lineEdit_52.setText(str(s[5][6]))
            self.lineEdit_52.setStyleSheet('background-color:white')
        self.lineEdit_52.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_53.text() == '':
            self.lineEdit_53.setText(str(s[5][7]))
            self.lineEdit_53.setStyleSheet('background-color:white')
        self.lineEdit_53.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_54.text() == '':
            self.lineEdit_54.setText(str(s[5][8]))
            self.lineEdit_54.setStyleSheet('background-color:white')
        self.lineEdit_54.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_55.text() == '':
            self.lineEdit_55.setText(str(s[6][0]))
            self.lineEdit_55.setStyleSheet('background-color:white')
        self.lineEdit_55.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_56.text() == '':
            self.lineEdit_56.setText(str(s[6][1]))
            self.lineEdit_56.setStyleSheet('background-color:white')
        self.lineEdit_56.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_57.text() == '':
            self.lineEdit_57.setText(str(s[6][2]))
            self.lineEdit_57.setStyleSheet('background-color:white')
        self.lineEdit_57.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_58.text() == '':
            self.lineEdit_58.setText(str(s[6][3]))
            self.lineEdit_58.setStyleSheet('background-color:white')
        self.lineEdit_58.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_59.text() == '':
            self.lineEdit_59.setText(str(s[6][4]))
            self.lineEdit_59.setStyleSheet('background-color:white')
        self.lineEdit_59.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_60.text() == '':
            self.lineEdit_60.setText(str(s[6][5]))
            self.lineEdit_60.setStyleSheet('background-color:white')
        self.lineEdit_60.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_61.text() == '':
            self.lineEdit_61.setText(str(s[6][6]))
            self.lineEdit_61.setStyleSheet('background-color:white')
        self.lineEdit_61.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_62.text() == '':
            self.lineEdit_62.setText(str(s[6][7]))
            self.lineEdit_62.setStyleSheet('background-color:white')
        self.lineEdit_62.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_63.text() == '':
            self.lineEdit_63.setText(str(s[6][8]))
            self.lineEdit_63.setStyleSheet('background-color:white')
        self.lineEdit_63.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_64.text() == '':
            self.lineEdit_64.setText(str(s[7][0]))
            self.lineEdit_64.setStyleSheet('background-color:white')
        self.lineEdit_64.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_65.text() == '':
            self.lineEdit_65.setText(str(s[7][1]))
            self.lineEdit_65.setStyleSheet('background-color:white')
        self.lineEdit_65.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_66.text() == '':
            self.lineEdit_66.setText(str(s[7][2]))
            self.lineEdit_66.setStyleSheet('background-color:white')
        self.lineEdit_66.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_67.text() == '':
            self.lineEdit_67.setText(str(s[7][3]))
            self.lineEdit_67.setStyleSheet('background-color:white')
        self.lineEdit_67.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_68.text() == '':
            self.lineEdit_68.setText(str(s[7][4]))
            self.lineEdit_68.setStyleSheet('background-color:white')
        self.lineEdit_68.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_69.text() == '':
            self.lineEdit_69.setText(str(s[7][5]))
            self.lineEdit_69.setStyleSheet('background-color:white')
        self.lineEdit_69.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_70.text() == '':
            self.lineEdit_70.setText(str(s[7][6]))
            self.lineEdit_70.setStyleSheet('background-color:white')
        self.lineEdit_70.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_71.text() == '':
            self.lineEdit_71.setText(str(s[7][7]))
            self.lineEdit_71.setStyleSheet('background-color:white')
        self.lineEdit_71.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_72.text() == '':
            self.lineEdit_72.setText(str(s[7][8]))
            self.lineEdit_72.setStyleSheet('background-color:white')
        self.lineEdit_72.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_73.text() == '':
            self.lineEdit_73.setText(str(s[8][0]))
            self.lineEdit_73.setStyleSheet('background-color:white')
        self.lineEdit_73.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_74.text() == '':
            self.lineEdit_74.setText(str(s[8][1]))
            self.lineEdit_74.setStyleSheet('background-color:white')
        self.lineEdit_74.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_75.text() == '':
            self.lineEdit_75.setText(str(s[8][2]))
            self.lineEdit_75.setStyleSheet('background-color:white')
        self.lineEdit_75.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_76.text() == '':
            self.lineEdit_76.setText(str(s[8][3]))
            self.lineEdit_76.setStyleSheet('background-color:white')
        self.lineEdit_76.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_77.text() == '':
            self.lineEdit_77.setText(str(s[8][4]))
            self.lineEdit_77.setStyleSheet('background-color:white')
        self.lineEdit_77.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_78.text() == '':
            self.lineEdit_78.setText(str(s[8][5]))
            self.lineEdit_78.setStyleSheet('background-color:white')
        self.lineEdit_78.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_79.text() == '':
            self.lineEdit_79.setText(str(s[8][6]))
            self.lineEdit_79.setStyleSheet('background-color:white')
        self.lineEdit_79.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_80.text() == '':
            self.lineEdit_80.setText(str(s[8][7]))
            self.lineEdit_80.setStyleSheet('background-color:white')
        self.lineEdit_80.setFocusPolicy(QtCore.Qt.NoFocus) 
        if self.lineEdit_81.text() == '':
            self.lineEdit_81.setText(str(s[8][8]))
            self.lineEdit_81.setStyleSheet('background-color:white')
        self.lineEdit_81.setFocusPolicy(QtCore.Qt.NoFocus) 

    def s_solution(self):
        for i in range(8):
            print(s[i])
        print()
        solution(s).start()
        self.input_result()

"""
s = solution([[8,0,0,0,0,0,0,0,0],
[0,0,3,6,0,0,0,0,0],
[0,7,0,0,9,0,2,0,0],
[0,5,0,0,0,7,0,0,0],
[0,0,0,8,4,5,7,0,0],
[0,0,0,1,0,0,0,3,0],
[0,0,1,0,0,0,0,6,8],
[0,0,8,5,0,0,0,1,0],
[0,9,0,0,0,0,4,0,0]])

"""

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
