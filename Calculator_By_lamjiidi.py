#بسم الله  الرحمان الرحيم
#في الاول اعتذر على كل خطأ لغوي أو املائي  سوف اقترفه في الأسطر القادمة ، انا ضعيف قليلا في اللغة العربية
#لقد حاولت تبسيط الامور قدر المستطاع
# خد ما تشاء ، استعمل ما تشاء، فقط لا تنسبه اليك
# تأكد من تثبيت كل مكتبات ادناه من اجل اشتغال كود بدون مشاكل
import sys
import webbrowser # كل هذه مكتبات ضرورية من اجل اشتغال الكود
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
def main():#دالة المين هي اول دالة سوف تنفد عند تشغيل البرنامج
    app = QApplication(sys.argv)
    root= QWidget() #هذا هو ويدجيت الذي سوف نضع فيه كل الأزرار و واجهات
    root.setWindowTitle("Simple Calculator") #اسم برنامج (سوف يظهر عند تشغيل)
    root.setFixedSize(500,820)# هنا حددنا ابعاد النافدة
    history=QLabel(root)#هنا قمنا ب انشاء مكان ل اظهار نص
    history.resize(500,50)#غيرنا حجمه بما يناسبنا
    history.setStyleSheet("background-color:#505050;color:white;font:17pt Center;")#غيرنا ثيم (لون خلفية ولون وشكل الخط)
    history.setText("")#نص الذي سوف يظهر في لوحة (سوف نغيره لاحقا)
    #نفس شيء ينطبق على كل لوحات من نوع "label"
    entery=QLabel(root)
    entery.resize(500,150)
    entery.move(0,50)
    entery.setStyleSheet("background-color:#505050;color:white;font:50pt Center;")
    entery.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
    entery.setText("")
    def Buttons(): # هذه الدالة وظيفتها إنشاء و اظهار الأزرار
        bmenu=QPushButton(root) # هنا قمنا ب انشاء زر ووضعناه في ويدجت رووت
        bmenu.setText("≡") # نص الذي سوف يكون داخل الزر
        bmenu.resize(35,35) # حجم الزر
        bmenu.move(470,0) # مكان الزر (بالنسبة للويدجيت)
        bmenu.setStyleSheet("background-color:#505050;color:white;font:18pt Center;") # غيرنا لون زر ولون خط وحجمه داخل الزر ومكان نص (راجع css لفهم اكثر)
        bmenu.clicked.connect(lambda : menu()) # عند ضغط على زر يتم استدعاء الدالة الموضوعة بين الاقواس
        #نفس الشيء ينطبق على كل الأزرار
        bdiv= QPushButton(root)
        bdiv.setText("÷")
        bdiv.move(375,200)
        bdiv.resize(125,125)
        bdiv.setStyleSheet("background-color:#FF9500;font:  30pt Bold ;color: white;")
        bdiv.clicked.connect(lambda : show("/"))
        bclear= QPushButton(root)
        bclear.setText("C")
        bclear.move(0,200)
        bclear.resize(125,125)
        bclear.setStyleSheet("background-color:white;font:  21pt Bold ;color: black;")
        bclear.clicked.connect(lambda : clear())
        bdel= QPushButton(root)
        bdel.setText("del")
        bdel.move(125,200)
        bdel.resize(125,125)
        bdel.setStyleSheet("background-color:white;font:  21pt Bold ;color: black;")
        bdel.clicked.connect(lambda : dell())
        b100= QPushButton(root)
        b100.setText("%")
        b100.move(250,200)
        b100.resize(125,125)
        b100.setStyleSheet("background-color:white;font:  21pt Bold ;color: black;")
        bmul= QPushButton(root)
        bmul.setText("x")
        bmul.move(375,325)
        bmul.resize(125,125)
        bmul.setStyleSheet("background-color:#FF9500;font:  21pt Bold  ;color: white;")
        bmul.clicked.connect(lambda : show("*"))
        b7=QPushButton(root)
        b7.setText("7")
        b7.move(0,325)
        b7.resize(125,125)
        b7.setStyleSheet("background-color:white;font:  21pt Bold ;color: black;")
        b7.clicked.connect(lambda : show("7"))
        b8= QPushButton(root)
        b8.setText("8")
        b8.move(125,325)
        b8.resize(125,125)
        b8.setStyleSheet("background-color:white;font:  21pt Bold ;color: black;")
        b8.clicked.connect(lambda :show("8"))
        b9= QPushButton(root)
        b9.setText("9")
        b9.move(250,325)
        b9.resize(125,125)
        b9.setStyleSheet("background-color:white;font:  21pt Bold ;color: black;")
        b9.clicked.connect(lambda : show("9"))
        bsub= QPushButton(root)
        bsub.setText("–")
        bsub.move(375,450)
        bsub.resize(125,125)
        bsub.setStyleSheet("background-color:#FF9500;font:  21pt Bold ;color: white;")
        bsub.clicked.connect(lambda : show("-"))
        b4= QPushButton(root)
        b4.setText("4")
        b4.move(0,450)
        b4.resize(125,125)
        b4.setStyleSheet("background-color:white;font:  21pt Bold ;color: black;")
        b4.clicked.connect(lambda : show("4"))
        b5= QPushButton(root)
        b5.setText("5")
        b5.move(125,450)
        b5.resize(125,125)
        b5.setStyleSheet("background-color:white;font:  21pt Bold ;color: black;")
        b5.clicked.connect(lambda : show("5"))
        b6= QPushButton(root)
        b6.setText("6")
        b6.move(250,450)
        b6.resize(125,125)
        b6.setStyleSheet("background-color:white;font:  21pt Bold ;color: black;")
        b6.clicked.connect(lambda : show("6"))
        badd= QPushButton(root)
        badd.setText("+")
        badd.move(375,575)
        badd.resize(125,125)
        badd.setStyleSheet("background-color:#FF9500;font:  21pt Bold ;color: white;")
        badd.clicked.connect(lambda : show("+"))
        b1= QPushButton(root)
        b1.setText("1")
        b1.move(0,575)
        b1.resize(125,125)
        b1.setStyleSheet("background-color:white;font:  21pt Bold ;color: black;")
        b1.clicked.connect(lambda : show("1"))
        b2= QPushButton(root)
        b2.setText("2")
        b2.move(125,575)
        b2.resize(125,125)
        b2.setStyleSheet("background-color:white;font:  21pt Bold ;color: black;")
        b2.clicked.connect(lambda : show("2"))
        b3= QPushButton(root)
        b3.setText("3")
        b3.move(250,575)
        b3.resize(125,125)
        b3.setStyleSheet("background-color:white;font:  21pt Bold ;color: black;")
        b3.clicked.connect(lambda : show("3"))
        beq= QPushButton(root)
        beq.setText("=")
        beq.move(375,700)
        beq.resize(125,125)
        beq.setStyleSheet("background-color:#FF9500;font:  21pt Bold ;color: white;")
        beq.clicked.connect(lambda : slove())
        bzero= QPushButton(root)
        bzero.setText("0")
        bzero.move(0,700)
        bzero.resize(250,125)
        bzero.setStyleSheet("background-color:white;font:  21pt Bold ;color: black;")
        bzero.clicked.connect(lambda : show("0"))
        bpoin= QPushButton(root)
        bpoin.setText(".")
        bpoin.move(250,700)
        bpoin.resize(125,125)
        bpoin.setStyleSheet("background-color:white;font:  21pt Bold ;color: black;")
        bpoin.clicked.connect(lambda : show("."))
    Buttons() #قمنا ب استدعاء دالة buttons من اجل اظهار الازرار التي انشأنها
    root.show()#هذا ضروري من اجل عرض كل شيء انشأناه
    equation=[]  #هذا المتغيير سوف نخزن فيه المعادلة
    def show(value):# يتم استدعاء هذه الدالة في كل مرة يتم فيها ضغط على اي زر (بإستثناء ازرار del , clear, =)
        equation.append(value) #تستقبل الدالة متغيير من طرف زر الذي تم ضغط عيه وتقوم بتخزينه في Equation
        labelRe(equation) # نرسل قيمة equation الى دالة labelRe()  من اجل اظهارها في شاشة (لوحة التي قمنا ب انشائها في الاول)
    def slove(): # هذه الدالة تقوم بالحساب عند ضغط على زر ’تساوي’
        if equation==[]:
            equation.clear()
            labelRe(equation)
        else:
            r=""
            temp=equation
            for ele in temp:
                r+= ele
            try:
                dis=eval(r)
                labelRe(str(dis))#نرسل خارج الى الشاشة
                Cach(str(r),"=") #نرسل خارج من اجل تخزينه في تاريخ واظهاره اعلا الشاشة
                equation.clear()# تنظيف متغيير equation من استعداد لمعادة اخرى
            except SyntaxError:#في حالة حدوث اي اخطاء في حساب معادلة يتم استدعاء اسطر جديدة من اجل تجنب توقف الرنامج
                equation.clear()
                labelRe(equation)
                Cach("SyntaxError!","")
    def clear(): #يتم استدعاء هذه الدالة عند ضغط على زر
        # ِclear "C" ووظيفتها هي تنظيف كل شيء وبدأ جلسة جديدة
        equation.clear()
        labelRe(equation)
        Cach('','')
    def dell(): # يتم استدعاء هذه الدالة عند ضغط على زر del
        #تحذف اخر قيمة ادخلتها الى equation
        if equation==[]:
            clear()
        else:
            del equation[-1]
            labelRe(equation)
    def labelRe(value): # وظيفة هذه الدالة هي اظهار قيمة التي يتم اعطائها في شاشة (لوحة entery)
            t=""
            for ele in value:
                t += ele
            entery.setText(t.replace('*','×').replace('/','÷'))
    def Cach(ch,e): # وظيفة هذه الدالة هي اظهار قيمة التي يتم اعطائها في شاشة تاريخ (لوحة history)
        history.setText("{}{}".format(str(ch.replace('*','×').replace('/','÷')),e))
    def menu():
        about=QDialog()
        about.setWindowTitle("About.")
        about.setFixedSize(300,120)
        about.setStyleSheet("background-color:#505050")
        craetBy=QLabel(about)
        craetBy.setStyleSheet("background-color:#FF9500;font:  8pt Impact Header ;color: black;")
        craetBy.setText("CREATED BY:")
        craetBy.move(0,10)
        myName=QLabel(about)
        myName.setStyleSheet("background-color:#505050;font:  16pt Impact Header ;color: white;")
        myName.setText("OTHMAN LAMJIIDI.")
        myName.move(0,30)
        textbu=QPushButton(about)
        textbu.setText("Follow me!")
        textbu.move(80,75)
        textbu.resize(150,35)
        textbu.setStyleSheet("background-color:#FF9500;font:  10pt Impact Header ;color: white;border-radius: 12px")
        textbu.clicked.connect(lambda : follow())
        about.show()
        about.exec()
    def follow():
        webbrowser.open("http://www.facebook.com/lamjiidii1")
    sys.exit(app.exec_())# هذا سطر من اجل استمرار عمل برنامج
if __name__ == '__main__':main()
#Creadet by OTHMAN LAMJIIDI , fb/lamjiidii1, Telegram/lamjiidii1


