from tkinter import Canvas
from PyQt5 import uic, QtWidgets
import pymysql 
from reportlab.pdfgen import canvas

conexao = pymysql.connect(
    host ='localhost',
    user ='root',
    passwd ='root',
    database ='cadastro_fii'
)

def gerar_pdf():
    cursor = conexao.cursor()
    comando = "SELECT * FROM fiis"
    cursor.execute(comando)
    dados_lidos = cursor.fetchall()
    y = 0 
    pdf = canvas.Canvas("cadastro_fii_pdf")
    pdf.setFont("Times-Bold", 14)
    pdf.drawString(200,800,"FIIs Cadastrados")
    pdf.setFont("Times-Bold",12)

    pdf.drawString(10,750,"ID")
    pdf.drawString(110,750, "TICKER")
    pdf.drawString(210,750, "NOME")
    pdf.drawString(310,750, "PREÇO")
    pdf.drawString(410,750, "CATEGORIA")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10,750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110,750 - y, str(dados_lidos[i][1]))
        pdf.drawString(210,750 - y, str(dados_lidos[i][2]))
        pdf.drawString(310,750 - y, str(dados_lidos[i][3]))
        pdf.drawString(410,750 - y, str(dados_lidos[i][4]))

        pdf.save()
        print('PDF GERADO COM SUCESSO')



def excluir_registro():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = conexao.cursor()
    cursor.execute("SELECT id FROM fiis")
    id_lidos = cursor.fetchall()
    valor = id_lidos[linha][0]
    cursor.execute ("DELETE FROM fiis WHERE id =" + str(valor))
    conexao.commit()
    
   
    



def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    categoria = ''

    if formulario.radioButton.isChecked():
        print("Categoria Papel foi selecionada")
        categoria = 'Papel'
    elif formulario.radioButton_2.isChecked():
        print("Categoria Lajes foi selecionada")
        categoria = 'Lajes'
    elif formulario.radioButton_3.isChecked():
        print("Categoria Logistico foi selecionada")
        categoria = 'Logistico'
    elif formulario.radioButton_4.isChecked():
        print("Categoria Shopping foi selecionada")
        categoria = 'Shopping'
    elif formulario.radioButton_5.isChecked():
        print("Categoria FOF foi selecionada")
        categoria = 'FOF'
    else:
        print("Categoria Renda Urbana foi selecionada")
        categoria = 'Renda Urbana'

    print("Ticker:",linha1)
    print("Nome do FII:",linha2)
    print("Preco:",linha3)

    cursor = conexao.cursor()
    comando = """INSERT INTO FIIs(Ticker, Nome, Preco, Categoria) VALUES (%s,%s,%s,%s)"""
    dados = (str(linha1), str(linha2), str(linha3), categoria)
    cursor.execute(comando, dados)
    conexao.commit()

    formulario.lineEdit.setText('')
    formulario.lineEdit_2.setText('')
    formulario.lineEdit_3.setText('')

def chama_segunda_tela():
    segunda_tela.show()

    cursor = conexao.cursor()
    comando = "SELECT * FROM fiis"
    cursor.execute(comando)
    dados_lidos = cursor.fetchall()
   

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            segunda_tela.tableWidget.setItem(i, j, QtWidgets. QTableWidgetItem(str(dados_lidos[i][j])))


app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
segunda_tela = uic.loadUi("listar_dados.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(gerar_pdf)
segunda_tela.pushButton_2.clicked.connect(excluir_registro)

formulario.show()
app.exec()