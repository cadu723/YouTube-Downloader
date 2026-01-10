import sys 
from PySide6.QtCore import QThread, Signal 
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit,QFileDialog
import Downloader  #arquivo onde está a lógica de download

class trabalhoThread(QThread):
    sinal_finalizado = Signal(str )  # Sinal para indicar que o trabalho foi concluído
    sinal_erro = Signal(str)  # Sinal para indicar que ocorreu um erro

    def __init__(self, link, pasta):#self e tipo um ponteiro para o objeto atual e o init é o construtor da classe 
        super().__init__()#super chama o construtor da classe pai (QThread)
        self.link = link #armazenando o link passado para a thread
        self.pasta = pasta 

    def run(self):
        try:
            resultado = Downloader.funcao_baixar(self.link , self.pasta)  # Chama a função de download
            self.sinal_finalizado.emit("Download Concluído com Sucesso! 🚀")
        except Exception as e:
            self.sinal_erro.emit(str(e))     


app = QApplication(sys.argv)#Criando a aplicação

janela = QWidget() #Criando a janela principal
janela.setWindowTitle("Vidownloader")#Definindo o título da janela
janela.resize(400, 200) #largura, altura

layout = QVBoxLayout() #Criando um layout vertical

texto_aviso = QLabel("aguardando link")

input_link = QLineEdit() #Criando um campo de entrada de texto
input_link.setPlaceholderText("Insira o link aqui") 

botao_enviar = QPushButton("clique aqui ") #Criando um botão

path_label = QLabel("Salvar em: Pasta do Projeto")
caminho_escolhido = ""

botao_pasta = QPushButton("📂 Escolher Pasta")

def escolher_pasta():
    global caminho_escolhido
    pasta = QFileDialog.getExistingDirectory(janela, "Selecione a pasta para salvar o vídeo")

    if  pasta:
        caminho_escolhido = pasta
        path_label.setText(f"Salvar em: {pasta}")
        print(f"Pasta escolhida: {pasta}")

botao_pasta.clicked.connect(escolher_pasta)        

botao_enviar.setStyleSheet("background-color: purple; color: white; font-weight: bold;")

worker = None


def atualizar_sucesso(mensagem):
    texto_aviso.setText(f"✅ {mensagem}")
    # Reabilita o botão para baixar outro
    botao_enviar.setEnabled(True)
    botao_enviar.setText("Baixar Outro")

def atualizar_erro(erro):
    texto_aviso.setText(f"❌ Falha: {erro}")
    botao_enviar.setEnabled(True)

def ao_clicar():
    link = input_link.text() #Obtendo o texto do campo de entrada

   # Avisa na tela que começou
    texto_aviso.setText("Baixando...")
    texto_aviso.repaint() # Força o Qt a atualizar o texto antes de travar
    
    global worker
    worker = trabalhoThread(link, caminho_escolhido)  # Criando a thread de trabalho
    worker.sinal_finalizado.connect(atualizar_sucesso)  # Conectando o sinal de finalização à função
    worker.sinal_erro.connect(atualizar_erro)   # Conectando o sinal de erro à função
    worker.start()  # Iniciando a thread de trabalho 

botao_enviar.clicked.connect(ao_clicar) #Conectando o clique do botão à função

# A ordem aqui define a ordem visual na tela (de cima pra baixo)
layout.addWidget(input_link) #Adicionando o campo de entrada ao layout 
layout.addWidget(botao_pasta) #Adicionando o botão de escolher pasta ao layout
layout.addWidget(path_label)  #Adicionando o rótulo do caminho ao layout
layout.addWidget(botao_enviar) #Adicionando o botão ao layout
layout.addWidget(texto_aviso) #Adicionando o rótulo ao layout

janela.setLayout(layout) #Definindo o layout da janela


janela.show() #Exibindo a janela

sys.exit(app.exec()) #Executando a aplicação