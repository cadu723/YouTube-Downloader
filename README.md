# 🎥 VIDownloader

![Status](https://img.shields.io/badge/Status-Concluído-green) ![Python](https://img.shields.io/badge/Python-3.x-blue) ![GUI](https://img.shields.io/badge/Interface-PySide6-purple)

**VIDownloader** é uma aplicação desktop robusta para baixar vídeos e áudios do YouTube. O projeto evoluiu de um script de estudo simples para um software com interface gráfica (GUI), multithreading e sistema de arquivos nativo.

## 🚀 Funcionalidades

- [x] **Interface Gráfica :** Desenvolvida com PySide6 (Qt).
- [x] **Multithreading:** O download roda em segundo plano sem travar a janela.
- [x] **Seletor de Arquivos:** Escolha nativa de onde salvar o vídeo.
- [x] **Portátil:** Versão executável para Linux que não requer instalação de Python.

---

## 📥 Como Baixar e Usar (Para Usuários)

Você não precisa instalar Python! Basta baixar a versão compilada.

1. Vá até a aba **[Releases](https://github.com/cadu723/YouTube-Downloader/releases)** aqui do lado direito.
2. Baixe o arquivo `VIDownloader(linux)`.
3. No seu computador, dê permissão de execução e rode:

```bash
# No terminal, na pasta do arquivo:
chmod +x "VIDownloader(linux)"
./"VIDownloader(linux)"
```

## 💻 Como Rodar o Código Fonte (Para Desenvolvedores)
Se você é desenvolvedor e quer clonar ou modificar o projeto, siga os passos abaixo.

🛠️ Pré-requisitos
Python 3.x

FFmpeg (Essencial para fusão de áudio/vídeo)

📦 Instalação das Dependências
Clone o repositório:

```
git clone [https://github.com/cadu723/YouTube-Downloader.git](https://github.com/cadu723/YouTube-Downloader.git)
cd YouTube-Downloader
```
Crie um ambiente virtual (recomendado):

```
python3 -m venv .venv
source .venv/bin/activate
```
Instale as bibliotecas:
```

pip install yt-dlp PySide6
```
▶️ Executando
```
python interface.py
```
## 🏗️ Estrutura do Projeto
interface.py: O Frontend (Janela, Threads, Lógica de UI).

Downloader.py: O Backend (Lógica do yt-dlp e tratamento de arquivos).
