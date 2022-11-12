from base import *


while True:
    text = input("Indique o texto que pretendes formatar: ")
    n = False

    while not n:
        _n = input("Indique o número da coluna: ")
        if str(_n).isdigit():
            n = int(_n)
    
    try:
        print("\n"+"\n".join(justifica_texto(text,n)), end="\n\n")
    except:
        print('Erro.')
