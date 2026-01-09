import sys 
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
import Downloader  #arquivo onde está a lógica de download

app = QApplication(sys.argv)#Criando a aplicação

janela = QWidget() #Criando a janela principal
janela.setWindowTitle("Minha Primeira Janela")#Definindo o título da janela
janela.resize(400, 200) #largura, altura

layout = QVBoxLayout() #Criando um layout vertical

texto_aviso = QLabel("aguardando link")

input_link = QLineEdit() #Criando um campo de entrada de texto
input_link.setPlaceholderText("Insira o link aqui") 

botao_enviar = QPushButton("clique aqui ") #Criando um botão
botao_enviar.setStyleSheet("background-color: purple; color: white; font-weight: bold;")

def ao_clicar():
    link = input_link.text() #Obtendo o texto do campo de entrada

   # Avisa na tela que começou
    texto_aviso.setText("Baixando...")
    texto_aviso.repaint() # Força o Qt a atualizar o texto antes de travar
    
    try:
        Downloader.funcao_baixar(link)#Chamando a função de download do outro arquivo
        
        texto_aviso.setText("Download Concluído com Sucesso!")
    
    except Exception as erro:
        texto_aviso.setText(f"❌ Erro: {erro}")

botao_enviar.clicked.connect(ao_clicar) #Conectando o clique do botão à função

# A ordem aqui define a ordem visual na tela (de cima pra baixo)
layout.addWidget(input_link) #Adicionando o campo de entrada ao layout 
layout.addWidget(botao_enviar) #Adicionando o botão ao layout
layout.addWidget(texto_aviso) #Adicionando o rótulo ao layout

janela.setLayout(layout) #Definindo o layout da janela


janela.show() #Exibindo a janela

sys.exit(app.exec()) #Executando a aplicação