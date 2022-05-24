import requests
import os 

'''Aqui eu usei o módulo OS pois me ajuda a construtir os caminhos relativos,
no caso para salvar cada iteração do arquivo eu criei uma pasta e usei o os pra salvar um por um nela'''

def baixa_arquivo(url, endereco): #(url: endereço de onde o arquivo está, diretório local aonde será salvo)
    #Realiza requisição ao servidor
    resposta = requests.get(url) #Contem o conteudo da URL e algumas informações extras
    if resposta.status_code == requests.codes.OK: #usei esse método pra garantir que o get conseguiu pegar o arquivo certinho, caso contrario vai pro else com o erro
        with open(endereco, 'wb') as novo_arquivo: 
            novo_arquivo.write(resposta.content) #escrevendo em binario o arquivo que pegamos pelo get no diretório que passamos como parametro
        print(f'Download finalizado, salvo em {endereco}')
    else:
        resposta.raise_for_status() #Método para mostrar HTTP erro da prórpia bilbioteca request


if __name__ == "__main__":
    BASE_URL = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'
    OUTPUT_DIR = 'output'

    for i in range(1, 26):
        nome_arquivo = ('nota_de_aula{}.pdf'.format(i))
        baixa_arquivo(BASE_URL.format(i), nome_arquivo)

