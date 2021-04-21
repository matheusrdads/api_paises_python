import json
import sys

import requests

URL_ALL = "https://restcountries.eu/rest/v2/all"
URL_NAME = "https://restcountries.eu/rest/v2/name"


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print("Erro ao fazer requidição em: ", url)


def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)  # converte a string recebida da url em objeto python
    except:
        print("Erro ao fazer parsing")


def contagem_de_paises():
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            return len(lista_de_paises)


def lista_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais["name"])

def mostrar_populacao(nome_do_pais):
    resposta = requisicao('{}/{}'.format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('{}: {} habitantes'.format(pais['name'], pais['population']))
    else:
        print("País não encontrado")

def mostrar_moedas(nome_do_pais):
    resposta = requisicao("{}/{}".format(URL_NAME, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print("Moeda do pais", pais['name'])
                moedas = pais['currencies']
                for moeda in moedas:
                    print("{} - {}".format(moeda['name'], moeda['code']))
    else:
        print("Pais não encontrado")


def ler_nome_do_pais():
    try:
        nome_do_pais = sys.argv[2]
        return nome_do_pais                                                 # se der erro retorna None
    except:
        print("É preciso passar o nome do país")


if __name__ == "__main__":
    if len(sys.argv) == 1:                                        #sys.argv transforma os argumentos de entrada em uma lista, começa no indice zero,  indice 1 é nome do arquivo, se tiver 1 pq não foi passado nenhum argumento ainda
        print("## Bem vindo ao sitema de países ##")
        print("Uso python paises.py <ação> <nome do pais>")
        print("Açôes disponíveis: contagem, moeda e população")
    else:
        argumento1 = sys.argv[1]                                  #sys.args[0] == "nome do arquivo que será executado" e sys.argv[1] == "recebe efetivamento o primeiro argumento"

        if argumento1 == "contagem":
            numero_de_paises = contagem_de_paises()
            print("Existe {} paises no mundo todo".format(numero_de_paises))
        elif argumento1 == "moeda":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_moedas(pais)
        elif argumento1 == "populacao":
            pais = ler_nome_do_pais()
            if pais:
                mostrar_populacao(pais)
        else:                                              # exit(0) "0" avisa que saiu do programa sem nenhum erro, se for "1" é po houve algum erro
            print("Argumento inválido")