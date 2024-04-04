import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de
    similaridade nas assinaturas.'''
    somatoria = 0
    for traco_linguistico in range(len(as_a)):
        somatoria += abs(as_a[traco_linguistico] - as_b[traco_linguistico])
    return somatoria / 6

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases = [frase for sentenca in sentencas for frase in separa_frases(sentenca)]
    palavras = [palavra for frase in frases for palavra in separa_palavras(frase)]

    assinatura = [
        sum(len(palavra) for palavra in palavras) / len(palavras),
        n_palavras_diferentes(palavras) / len(palavras),
        n_palavras_unicas(palavras) / len(palavras),
        sum(len(sentenca) for sentenca in sentencas) / len(sentencas),
        len(frases) / len(sentencas),
        sum(len(frase) for frase in frases) / len(frases)
    ]

    return assinatura

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e deve devolver o número (1 a n)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    graus_de_similaridade = [compara_assinatura(calcula_assinatura(texto), ass_cp) for texto in textos]
    indice_texto_infectado = graus_de_similaridade.index(min(graus_de_similaridade)) + 1
    return indice_texto_infectado

def main():
    assinatura_principal = le_assinatura()
    textos = le_textos()
    infectado = avalia_textos(textos, assinatura_principal)
    print("O autor do texto", infectado, "está infectado com COH-PIAH.")

main()
