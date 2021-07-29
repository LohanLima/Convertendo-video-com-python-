# sys, fnmatch,
# https://ffmeg.zeranoe.com/builds/
# https://ffmpeg.org/download.html se caso use windows aqui você faz o download, procura no bin o .exe e copia ele um
#python package
# documentação https://ffmpeg.org/documentation.html para mais detalhe e comandos.
#como preset e crf(qualidade do video)

#convertendo videos com codigo python (script)

"""
ffmpeg -i "ENTRADA" -i "LLEGENDA" -c:v libx264 -crf 23 -preset
ultrafast -c:a aac -b:a 320k
-c:s srt -map v:0 -map a -map 1:0 "SAIDA" (legenda)
-ss 00:00:00 -to 00:00:10 usado nesse código para só converter 10 seg
para o video inteiro não precisa passar o tempo de conversão.
"""

import os
import fnmatch
import sys

# para windowns precisa acessar e fazer o download do ffmpeg no link acima, para ter a pasta bin e copiar o ffmpeg.exe
#para jogar dentro uma pasta ffmpeg

if sys.platform == 'linux':
    comando_ffmpeg = 'ffmpeg'
else:
    comando_ffmpeg = r'ffmepeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10' # vazio video completo

caminho_origem = '' # copia o caminho, para windows colocar r'caminho'
caminho_destino = '' #caminho de saida

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mkv'): # usar os arquivos de video de preferência como .mp4
            continue

        caminho_completo = os.path.join(raiz, arquivo)


        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)

        caminho_legenda = nome_arquivo +'.srt'

        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i"{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''

        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

        # para salvar na mesma pasta -
        # nome_novo_arquivo= nome_arquivo + '_NOVO' + extensao_arquivo
        # arquivo_saida = os.path.join(raiz, nome_novo_arquivo)
        # -.

        arquivo_saida= f'{caminho_destino}/{nome_arquivo}_NOVO{extensao_arquivo}' #extensao_arquivo pode ser novo.mp4

        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} ' \
                  f'{codec_video} {crf}{preset}{codec_audio}{bitrate_audio}' \
                  f'{debug} {map_legenda} "{arquivo_saida}"'

        os.system(comando)



