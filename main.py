from PyQt5.QtWidgets import QWidget, QApplication
import math

app = QApplication([])

from UI import *
from style import style

window = QWidget()
window.resize(200, 200)
window.setWindowTitle("Калькулятор")
window.show()

window.setLayout(main_line)

app.setStyleSheet(style)

a = 0
b = False
c = False
d = False
e = False

def click0():
    if label.text() == "0":
        label.setText("0")
    else:
        label.setText(label.text() + "0")
def click1():
    if label.text() == "0":
        label.setText("1")
    else:
        label.setText(label.text() + "1")
def click2():
    if label.text() == "0":
        label.setText("2")
    else:
        label.setText(label.text() + "2")
def click3():
    if label.text() == "0":
        label.setText("3")
    else:
        label.setText(label.text() + "3")
def click4():
    if label.text() == "0":
        label.setText("4")
    else:
        label.setText(label.text() + "4")
def click5():
    if label.text() == "0":
        label.setText("5")
    else:
        label.setText(label.text() + "5")
def click6():
    if label.text() == "0":
        label.setText("6")
    else:
        label.setText(label.text() + "6")
def click7():
    if label.text() == "0":
        label.setText("7")
    else:
        label.setText(label.text() + "7")
def click8():
    if label.text() == "0":
        label.setText("8")
    else:
        label.setText(label.text() + "8")
def click9():
    if label.text() == "0":
        label.setText("9")
    else:
        label.setText(label.text() + "9")
def click_inverse():
    label.setText(str(1 / float(label.text())))
def click_sqr():
    try:
        label.setText(str(float(label.text()) ** 2))
    except:
        label.setText("Переповнення")
        btn_prozent.setEnabled(False)
        btn_otmena.setEnabled(False)
        btn_inverse.setEnabled(False)
        btn_sqr.setEnabled(False)
        btn_sqrt.setEnabled(False)
        btn_delenie.setEnabled(False)
        btn7.setEnabled(False)
        btn8.setEnabled(False)
        btn9.setEnabled(False)
        btn_mul.setEnabled(False)
        btn4.setEnabled(False)
        btn5.setEnabled(False)
        btn6.setEnabled(False)
        btn_minus.setEnabled(False)
        btn1.setEnabled(False)
        btn2.setEnabled(False)
        btn3.setEnabled(False)
        btn_plus.setEnabled(False)
        btn_inv.setEnabled(False)
        btn0.setEnabled(False)
        btn_coma.setEnabled(False)
        btn_ravno.setEnabled(False) 
def click_sqrt():
    try:
        label.setText(str(math.sqrt(float(label.text()))))
    except:
        label.setText("Введено неприпустиме значення")
        btn_prozent.setEnabled(False)
        btn_otmena.setEnabled(False)
        btn_inverse.setEnabled(False)
        btn_sqr.setEnabled(False)
        btn_sqrt.setEnabled(False)
        btn_delenie.setEnabled(False)
        btn7.setEnabled(False)
        btn8.setEnabled(False)
        btn9.setEnabled(False)
        btn_mul.setEnabled(False)
        btn4.setEnabled(False)
        btn5.setEnabled(False)
        btn6.setEnabled(False)
        btn_minus.setEnabled(False)
        btn1.setEnabled(False)
        btn2.setEnabled(False)
        btn3.setEnabled(False)
        btn_plus.setEnabled(False)
        btn_inv.setEnabled(False)
        btn0.setEnabled(False)
        btn_coma.setEnabled(False)
        btn_ravno.setEnabled(False)        
def click_inv():
    label.setText(str(-float(label.text())))
def click_coma():
    label.setText(label.text() + ".")
def click_plus():
    global a
    global b
    b = True
    try:
        a = float(label.text())
        label2.setText(label.text() + "+")
        label.setText("")
    except:
        label.setText("Error")
        btn_prozent.setEnabled(False)
        btn_otmena.setEnabled(False)
        btn_inverse.setEnabled(False)
        btn_sqr.setEnabled(False)
        btn_sqrt.setEnabled(False)
        btn_delenie.setEnabled(False)
        btn7.setEnabled(False)
        btn8.setEnabled(False)
        btn9.setEnabled(False)
        btn_mul.setEnabled(False)
        btn4.setEnabled(False)
        btn5.setEnabled(False)
        btn6.setEnabled(False)
        btn_minus.setEnabled(False)
        btn1.setEnabled(False)
        btn2.setEnabled(False)
        btn3.setEnabled(False)
        btn_plus.setEnabled(False)
        btn_inv.setEnabled(False)
        btn0.setEnabled(False)
        btn_coma.setEnabled(False)
        btn_ravno.setEnabled(False)      
def click_minus():
    global a
    global c
    c = True
    try:
        a = float(label.text())
        label2.setText(label.text() + "-")
        label.setText("")
    except:
        label.setText("Error")
        btn_prozent.setEnabled(False)
        btn_otmena.setEnabled(False)
        btn_inverse.setEnabled(False)
        btn_sqr.setEnabled(False)
        btn_sqrt.setEnabled(False)
        btn_delenie.setEnabled(False)
        btn7.setEnabled(False)
        btn8.setEnabled(False)
        btn9.setEnabled(False)
        btn_mul.setEnabled(False)
        btn4.setEnabled(False)
        btn5.setEnabled(False)
        btn6.setEnabled(False)
        btn_minus.setEnabled(False)
        btn1.setEnabled(False)
        btn2.setEnabled(False)
        btn3.setEnabled(False)
        btn_plus.setEnabled(False)
        btn_inv.setEnabled(False)
        btn0.setEnabled(False)
        btn_coma.setEnabled(False)
        btn_ravno.setEnabled(False)      
def click_mul():
    global a
    global d
    d = True
    try:
        a = float(label.text())
        label2.setText(label.text() + "*")
        label.setText("")
    except:
        label.setText("Error")
        btn_prozent.setEnabled(False)
        btn_otmena.setEnabled(False)
        btn_inverse.setEnabled(False)
        btn_sqr.setEnabled(False)
        btn_sqrt.setEnabled(False)
        btn_delenie.setEnabled(False)
        btn7.setEnabled(False)
        btn8.setEnabled(False)
        btn9.setEnabled(False)
        btn_mul.setEnabled(False)
        btn4.setEnabled(False)
        btn5.setEnabled(False)
        btn6.setEnabled(False)
        btn_minus.setEnabled(False)
        btn1.setEnabled(False)
        btn2.setEnabled(False)
        btn3.setEnabled(False)
        btn_plus.setEnabled(False)
        btn_inv.setEnabled(False)
        btn0.setEnabled(False)
        btn_coma.setEnabled(False)
        btn_ravno.setEnabled(False)      
def click_delenie():
    global a
    global e
    e = True
    try:
        a = float(label.text())
        label2.setText(label.text() + "/")
        label.setText("")
    except:
        label.setText("Error")
        btn_prozent.setEnabled(False)
        btn_otmena.setEnabled(False)
        btn_inverse.setEnabled(False)
        btn_sqr.setEnabled(False)
        btn_sqrt.setEnabled(False)
        btn_delenie.setEnabled(False)
        btn7.setEnabled(False)
        btn8.setEnabled(False)
        btn9.setEnabled(False)
        btn_mul.setEnabled(False)
        btn4.setEnabled(False)
        btn5.setEnabled(False)
        btn6.setEnabled(False)
        btn_minus.setEnabled(False)
        btn1.setEnabled(False)
        btn2.setEnabled(False)
        btn3.setEnabled(False)
        btn_plus.setEnabled(False)
        btn_inv.setEnabled(False)
        btn0.setEnabled(False)
        btn_coma.setEnabled(False)
        btn_ravno.setEnabled(False)      
def click_ravno():
    global a
    global b
    global c
    global d
    global e
    if b == True:
        label.setText(str(float(label.text()) + a))
        b = False
        label2.setText("")
    if c == True:
        label.setText(str(a - float(label.text())))
        c = False
        label2.setText("")
    if d == True:
        label.setText(str(float(label.text()) * a))
        d = False
        label2.setText("")
    if e == True:
        try:
            label.setText(str(a / float(label.text())))
        except:
            label.setText("Ділити на нуль не можна")
            btn_prozent.setEnabled(False)
            btn_otmena.setEnabled(False)
            btn_inverse.setEnabled(False)
            btn_sqr.setEnabled(False)
            btn_sqrt.setEnabled(False)
            btn_delenie.setEnabled(False)
            btn7.setEnabled(False)
            btn8.setEnabled(False)
            btn9.setEnabled(False)
            btn_mul.setEnabled(False)
            btn4.setEnabled(False)
            btn5.setEnabled(False)
            btn6.setEnabled(False)
            btn_minus.setEnabled(False)
            btn1.setEnabled(False)
            btn2.setEnabled(False)
            btn3.setEnabled(False)
            btn_plus.setEnabled(False)
            btn_inv.setEnabled(False)
            btn0.setEnabled(False)
            btn_coma.setEnabled(False)
            btn_ravno.setEnabled(False)      
        e = False
        label2.setText("")
def click_C():
    label.setText("0")
    label2.setText("")
    btn_prozent.setEnabled(True)    
    btn_otmena.setEnabled(True)
    btn_inverse.setEnabled(True)
    btn_sqr.setEnabled(True)
    btn_sqrt.setEnabled(True)
    btn_delenie.setEnabled(True)
    btn7.setEnabled(True)
    btn8.setEnabled(True)
    btn9.setEnabled(True)
    btn_mul.setEnabled(True)
    btn4.setEnabled(True)
    btn5.setEnabled(True)
    btn6.setEnabled(True)
    btn_minus.setEnabled(True)
    btn1.setEnabled(True)
    btn2.setEnabled(True)
    btn3.setEnabled(True)
    btn_plus.setEnabled(True)
    btn_inv.setEnabled(True)
    btn0.setEnabled(True)
    btn_coma.setEnabled(True)
    btn_ravno.setEnabled(True)
def click_prozent():
    label.setText(str(float(label.text()) / 100))
def click_otmena():
    label.setText(label.text()[:-1])

btn0.clicked.connect(click0)
btn1.clicked.connect(click1)
btn2.clicked.connect(click2)
btn3.clicked.connect(click3)
btn4.clicked.connect(click4)
btn5.clicked.connect(click5)
btn6.clicked.connect(click6)
btn7.clicked.connect(click7)
btn8.clicked.connect(click8)
btn9.clicked.connect(click9)
btn_inverse.clicked.connect(click_inverse)
btn_sqr.clicked.connect(click_sqr)
btn_sqrt.clicked.connect(click_sqrt)
btn_inv.clicked.connect(click_inv)
btn_coma.clicked.connect(click_coma)
btn_plus.clicked.connect(click_plus)
btn_minus.clicked.connect(click_minus)
btn_mul.clicked.connect(click_mul)
btn_delenie.clicked.connect(click_delenie)
btn_ravno.clicked.connect(click_ravno)
btn_C.clicked.connect(click_C)
btn_CE.clicked.connect(click_C)
btn_prozent.clicked.connect(click_prozent)
btn_otmena.clicked.connect(click_otmena)
    
app.exec()