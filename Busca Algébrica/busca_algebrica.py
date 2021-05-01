
lista_nao_prog = [5,13,7,8,9,11,12,25,556,779,2656,7989,56,497,94,96,59,79,1,3,2,96,974,79,9,749,7,97,9,74,19,4,49,888,4444,777889,87979797]
def busca_algebrica(lista_np, term_encontrar):
    try:
        tam_np = len(lista_np)
        lista_p = [x for x in range(0,tam_np)]
        relation = {}
        for i in range(0,tam_np):
            relation[lista_np[i]] = lista_p[i]
        razao = 1
        prim_term = lista_p[0]
        n = int((1/razao)*(relation[term_encontrar] - prim_term))
        pos_term = n
        if(pos_term <= tam_np):
            return pos_term
    except KeyError:
        print("Termo não encontrado ou não está na lista!")
        return -1
    
print(busca_algebrica(lista_nao_prog,7))