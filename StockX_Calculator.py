import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5 import QtCore
from PyQt5 import QtGui
import qdarkgraystyle
##from PyQt5.QtWidgets import QLabel



##mainWindow class inherits PyQt5 Qwidget
class mainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        ##Set window structure
        self.setWindowTitle("StockX Calculator")
        self.setGeometry(875,400,500,600)       ##Set window size
        self.setLayout(qtw.QVBoxLayout())       ##Sets the mainWindow layout
        self.setWindowIcon(QtGui.QIcon("stockX.png")) ##Sets windows icon on bar
        self.show()                             ##Display all the windows created in the mainWindow class
        
        
        ##Call calc function
        self.btns()


    def btns(self):
        box = qtw.QWidget()
        box.setLayout(qtw.QGridLayout())
        ##Labels

        self.lbl_itemCost = qtw.QLabel("Item Cost:")
        self.lbl_soldPrice = qtw.QLabel("Sold Price:")
        self.lbl_profit = qtw.QLabel("Profit: ")

        self.lbl_fees = qtw.QLabel("StockX Fees: ")

        ##Fields

        #ItemCost 
        self.itemCost_field = qtw.QLineEdit()
        self.itemCost_field.setFixedWidth(120)
        validator = QRegExpValidator(QRegExp("^(([0-9]+\.[0-9]*[1-9][0-9]*)|([0-9 ]*[1-9][0-9]*\.[0-9]+)|([0-9]*[1-9][0-9]*))$"))                   ##Input Validator (Positive number including decimal)
        self.itemCost_field.setValidator(validator)

        #soldPrice
        self.soldPrice_field = qtw.QLineEdit()
        self.soldPrice_field.setFixedWidth(120)
        self.soldPrice_field.setValidator(validator)

        #Profit
        self.profit_field = qtw.QLineEdit()
        self.profit_field.setFixedWidth(120)
        self.profit_field.setReadOnly(True)
        
        ##Checkbox 
        group = qtw.QButtonGroup(self)
        self.sellerLevel_1 = qtw.QCheckBox("Seller Level 1", self)
        self.sellerLevel_2 = qtw.QCheckBox("Seller Level 2", self)
        self.sellerLevel_3 = qtw.QCheckBox("Seller Level 3", self)
        self.sellerLevel_4 = qtw.QCheckBox("Seller Level 4", self)
        
        group.addButton(self.sellerLevel_1)
        group.addButton(self.sellerLevel_2)
        group.addButton(self.sellerLevel_3)
        group.addButton(self.sellerLevel_4)

        ##Button
        self.calculate_btn = qtw.QPushButton("Calculate")
        self.calculate_btn.setStyleSheet("border: 1px solid;"
                                         "border-color: green;")
        self.calculate_btn.clicked.connect(self.calculate_profits)

        
        ##Add widgets to box
        box.layout().addWidget(self.lbl_itemCost,0,0,1,1)
        box.layout().addWidget(self.itemCost_field,0,1,1,1)

        box.layout().addWidget(self.lbl_soldPrice,1,0,1,1)
        box.layout().addWidget(self.soldPrice_field,1,1,1,1)

        box.layout().addWidget(self.sellerLevel_1,2,0,1,1)
        box.layout().addWidget(self.sellerLevel_2,3,0,1,1)
        box.layout().addWidget(self.sellerLevel_3,4,0,1,1)
        box.layout().addWidget(self.sellerLevel_4,5,0,1,1)

        box.layout().addWidget(self.calculate_btn,6,0,1,1)
        box.layout().addWidget(self.lbl_fees,6,1,1,1)



        box.layout().addWidget(self.lbl_profit,8,0,1,1)
        box.layout().addWidget(self.profit_field,8,1,1,3)


        ##Add items to UI
        ##inset gridbox layout to UI
        self.layout().addWidget(box)

    def calculate_profits(self):
        if self.sellerLevel_1.isChecked():
            self.lbl_fees.setText("StockX Fees: 12.5%")
            itemCost = float(self.itemCost_field.text())
            #print(itemCost)
            soldPrice = float(self.soldPrice_field.text())
            #print(soldPrice)
            itemFee = float((soldPrice / 100) * 12.5)
            #print(itemFee)
            payout = soldPrice - itemFee
            #print(payout)
            profit = payout - itemCost
            #print(profit)

            self.profit_field.setText(str(profit))
        elif self.sellerLevel_2.isChecked():
            self.lbl_fees.setText("StockX Fees: 12%")
            itemCost = float(self.itemCost_field.text())
            #print(itemCost)
            soldPrice = float(self.soldPrice_field.text())
            #print(soldPrice)
            itemFee = float((soldPrice / 100) * 12)
            #print(itemFee)
            payout = soldPrice - itemFee
            #print(payout)
            profit = payout - itemCost
            #print(profit)

            self.profit_field.setText(str(profit))
        elif self.sellerLevel_3.isChecked():
            self.lbl_fees.setText("StockX Fees: 11.5%")
            itemCost = float(self.itemCost_field.text())
            #print(itemCost)
            soldPrice = float(self.soldPrice_field.text())
            #print(soldPrice)
            itemFee = float((soldPrice / 100) * 11.5)
            #print(itemFee)
            payout = soldPrice - itemFee
            #print(payout)
            profit = payout - itemCost
            #print(profit)

            self.profit_field.setText(str(profit))
        elif self.sellerLevel_4.isChecked():
            self.lbl_fees.setText("StockX Fees: 11%")
            itemCost = float(self.itemCost_field.text())
            #print(itemCost)
            soldPrice = float(self.soldPrice_field.text())
            #print(soldPrice)
            itemFee = float((soldPrice / 100) * 11)
            #print(itemFee)
            payout = soldPrice - itemFee
            #print(payout)
            profit = payout - itemCost
            #print(profit)

            self.profit_field.setText(str(profit))


            


        



            


##Creates pyqt5 app
app = qtw.QApplication([])
app.setStyleSheet(qdarkgraystyle.load_stylesheet())
##mainWindow object
mw = mainWindow()

##Python runs appilcation
app.exec_()