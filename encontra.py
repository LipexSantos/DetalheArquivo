import os

caminho_procura = input('Caminho: ')  # raiz
termo_procura = input('Termo: ')  # um nome/termo do arquivo que vc quer encontra


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'

    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'

    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'


conta = 0
# gerar os nomes dos arquivos
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                # juntando a raiz e o arquivo
                caminho_completo = os.path.join(raiz, arquivo)
                # aqui ele desempacota e separa em nome do arquivo é a extensão dele.
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                # pego o tamanho em bytes dos arquivos
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho:', tamanho)
                print('Tamanho_Formatado:', formata_tamanho(tamanho))
            except PermissionError as erro:
                print('Sem permissão neste arquivo.')
            except FileNotFoundError as erro:
                print('Arquivo não encontrado.')
            except SyntaxError as erro:
                print('Erro de sintaxe!, reveja seu Caminho.')
            except Exception as erro:
                print('Error Desconhecido:', erro)

print()
print(f'{conta} arquivo(s) encontrado(s).')

