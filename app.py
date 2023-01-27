# instanciar 

from ui_main import Ui_Mainwindow
from PySide6 import QtWidgets



class MainWindow(QtWidgets.QMainWindow, Ui_Mainwindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # conectar os sinais dos botões com os slots
        self.bt0.clicked.connect(self.on_btn_0_clicked)
        self.bt1.clicked.connect(self.on_btn_1_clicked)
        self.bt2.clicked.connect(self.on_btn_2_clicked)
        self.bt3.clicked.connect(self.on_btn_3_clicked)
        self.bt4.clicked.connect(self.on_btn_4_clicked)
        self.bt5.clicked.connect(self.on_btn_5_clicked)
        self.bt6.clicked.connect(self.on_btn_6_clicked)
        self.bt7.clicked.connect(self.on_btn_7_clicked)
        self.bt8.clicked.connect(self.on_btn_8_clicked)
        self.bt9.clicked.connect(self.on_btn_9_clicked)
        self.btsoma.clicked.connect(self.on_btn_soma_clicked)
        self.btsub.clicked.connect(self.on_btn_sub_clicked)
        self.btmult.clicked.connect(self.on_btn_mult_clicked)
        self.btdiv.clicked.connect(self.on_btn_div_clicked)
        self.btigual.clicked.connect(self.on_btn_igual_clicked)
        self.btdelete.clicked.connect(self.on_btn_limpar_clicked)
        self.btponto.clicked.connect(self.on_btn_ponto_clicked)
        self.btce.clicked.connect(self.on_btn_ce_ckicked)



    # quando clicar no botão, aparecer no visor o texto
    textovisor = ""
    
    def on_btn_1_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+"1")

    def on_btn_2_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+"2")

    def on_btn_3_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+"3")

    def on_btn_4_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+"4")

    def on_btn_5_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+"5")

    def on_btn_6_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+"6")

    def on_btn_7_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+"7")

    def on_btn_8_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+"8")

    def on_btn_9_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+"9")

    def on_btn_0_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+"0")

    def on_btn_soma_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+"+")

    def on_btn_sub_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+"-")

    def on_btn_mult_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+"*")

    def on_btn_div_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+"/")

    def on_btn_ponto_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor+".")

    def on_btn_ce_ckicked (self):
        self.visor.setText("")

    def on_btn_limpar_clicked(self):
        textovisor = self.visor.text()
        self.visor.setText(textovisor[:-1])

    def on_btn_igual_clicked(self):
        textovisor = self.visor.text()

        try:
            resultado =  eval(textovisor)
            self.visor.setText(str(resultado))
        except:
            self.visor.setText("Erro")











app = QtWidgets.QApplication([])

window = MainWindow()
window.show()

app.exec_()

# Path: ui_main.py
