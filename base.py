"""
Pretendemos justificar uma cadeia de caracteres, que nao seja vazia, utilizando um
numero inteiro positivo correspondente ah largura de coluna configuravel retornando um tuplo de cadeias com
tamanho igual ah largura pretendida, sendo necessario, inserir mais espacos entre as palavras, ou no caso
da ultima cadeia, acrescentar os espacos no fim.
"""


def limpa_texto(t):
    '''
    Esta funcao recebe uma cadeia de carateres e devolve a cadeia de carateres limpa (sem caracteres brancos).
    ------------------------------------
    {cad. carateres} -> {cad. carateres}
    '''
    return  " ".join(t.split())


def corta_texto(string, int):
    '''
    Esta funcao recebe uma cadeia de caracteres e um numero inteiro a que correspondem, respetivamente, a um
    texto limpo (podendo recorrer a funcao anterior) e a largura da coluna. Ao separar o texto em 2, esta
    nao corta nenhuma palavra, ou seja, as palavras ficam todas completas e este tera no maximo um comprimento
    igual a largura fornecida. A segunda cadeira corresponde ao resto.
    ----------------------------------------------------------------
    {cad. carateres x inteiro} -> {cad. carateres x cad. caracteres}
    '''
    tuplo = string.split() 
    length = 0 
    res = ["", ""]
    extra = False 

    for e in tuplo:
        lenE = len(e)
        if (length + lenE) <= int and not extra: 
            length += lenE +1 
            res[0] += f"{e} "
        else:
            extra = True 
            res[1] += f"{e} " 
    resultado = res[0], res[1]

    return tuple(resultado)


def insere_espacos(string, int):
    '''
    Esta funcao recebe uma cadeia de carateres e um inteiro positivo correspondentes a um texto limpo e uma
    largura de coluna respetivamente, e no caso da cadeia de entrada conter duas ou mais palavras devolve uma
    cadeia de carateres de comprimento igual a largura da coluna formada pela cadeia original com espacos
    entre palavras. Caso contrario, devolve a cadeia de comprimento igual a largura da coluna formada pela
    cadeia original seguida de espacos.
    ----------------------------------------------
    {cad. carateres x inteiro} -> {cad. carateres}
    '''
    res = ""
    split = string.split() 
    palavras = len(split) 
    espacos = int - len(string.replace(" ","")) 
    spaces = [0] * (palavras-1) 

    if palavras == 1: 
        res = split[0] + " "*espacos 
        return res
    
    while espacos > 0: 
        for i in range(len(spaces)):
            if espacos > 0:
                espacos -= 1 
                spaces[i] += 1 

    i = 0

    for p in split:
        if (i+1) == len(split): 
            res += p
        else:
            res += p+" "*spaces[i] 
        i+=1
    return res
    

def justifica_texto(string, inteiro):
    '''
    Esta funcao recebe uma cadeia de caracteres e um numero positivo correspondentes a um texto e uma
    largura de coluna. Este ira devolver um tuplo com textos justificados, ou seja, com comprimento
    IGUAL a largura da coluna inserindo espacos entre palavras ou no fim da frase (caso esta seja a
    ultima do tuplo).
    -------------------------------------
    {cad. carateres x inteiro} -> {tuplo}
    '''
    if not isinstance(string, str) or not isinstance(inteiro, int) or inteiro <= 0 or len(string) == 0: 
        raise ValueError("justifica_texto: argumentos invalidos")
    for e in string.split():
        if len(e) > inteiro:
            raise ValueError("justifica_texto: argumentos invalidos")

    string = limpa_texto(string)
    res = ()
    cortado = corta_texto(string, inteiro)
    while cortado[1] != "":
        res += (insere_espacos(cortado[0], inteiro),)
        cortado = corta_texto(cortado[1],inteiro) 
    res += (cortado[0] + " "*(inteiro - len(cortado[0])), ) 
    return res