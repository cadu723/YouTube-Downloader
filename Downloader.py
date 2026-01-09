import yt_dlp
def funcao_baixar(link_do_video):

    regras_da_analise = {
        'quiet': False,           # ORDEM: "Fique em silêncio (não imprima bagunça no terminal)"
        'extract_flat': False,    # ORDEM: "Apenas extraia os dados (não baixe o vídeo pesado)"
        'format':'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',#limitando a 720p e formatos mp4/m4a pois fica mais leve , embora perca levemente em qualidade 
        'outtmpl': '%(title)s.%(ext)s', # Salva com o nome original do vídeo.
    }
    print("\n  Iniciando a varredura no link...")

    with yt_dlp.YoutubeDL(regras_da_analise) as agente: #criando o agente de download com as regras
            agente.extract_info(link_do_video, download=True)#baixando o video

    return "Sucesso"           
   