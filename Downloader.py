import yt_dlp

link = input("Enter the video link: ")

regras_da_analise = {
    'quiet': False,           # ORDEM: "Fique em silêncio (não imprima bagunça no terminal)"
    'extract_flat': False,    # ORDEM: "Apenas extraia os dados (não baixe o vídeo pesado)"
    'format':'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',#limitando a 720p e formatos mp4/m4a pois fica mais leve , embora perca levemente em qualidade 
    'outtmpl': '%(title)s.%(ext)s', # Salva com o nome original do vídeo.
}
print("\n  Iniciando a varredura no link...")

with yt_dlp.YoutubeDL(regras_da_analise) as agente_investigador:#with e tipo um "abre e fecha automático" malloc da linguagem C     
    try:
        # O agente vai lá no site e busca a ficha técnica
        ficha_tecnica = agente_investigador.extract_info(link, download=True)
        
        # 4. Exibindo o Relatório
        print("-" * 30)
        print(f" Título do Vídeo: {ficha_tecnica['title']}")
        print(f" Dono do Canal:   {ficha_tecnica['uploader']}")
        print(f" Visualizações:   {ficha_tecnica['view_count']}")
        print(f" Duração (seg):   {ficha_tecnica['duration']}")
        print("-" * 30)
        
    except Exception as erro_encontrado:
        print("A investigação falhou. Motivo:", erro_encontrado)
