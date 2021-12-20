from fastapi import APIRouter

mat = APIRouter()
matriz = [[2,1,2],[2,2,1],[1,3,1]]
matriz1 = [[0,0,0],[0,0,0],[0,0,0]]

cont = [0,1,2,3,4,5,6,7,8,9]

@mat.get('/nuevaMat')
def nuevaMat():
    for i in range(1,10):
        cont.append(i)
    return 'Matriz con'+ str(cont)

@mat.get('/pide')
def mandamat():   
    return str(matriz)

@mat.get('/pide2')
def mandamat():   
    return str(matriz1)

@mat.get('/pos')
def pos():                
    if (cont[-1] == 9):                 
        cont.pop()
        return str([0,0])
    if (cont[-1] == 8):
        cont.pop()
        return str([0,1])
    if (cont[-1] == 7):
        cont.pop()
        return str([0,2])
    if (cont[-1] == 6):                 
        cont.pop()
        return str([1,0])
    if (cont[-1] == 5):
        cont.pop()
        return str([1,1])
    if (cont[-1] == 4):
        cont.pop()
        return str([1,2])
    if (cont[-1] == 3):                 
        cont.pop()
        return str([2,0])
    if (cont[-1] == 2):
        cont.pop()
        return str([2,1])
    if (cont[-1] == 1):
        cont.pop()
        return str([2,2])
    else:
        return "No hay posisiones a calcular"
    
@mat.post('/actualizamat/{pos}/{res}')
def actualiza(pos, res):   
    if pos == '0':
        matriz1[0][0] = res
    elif pos == '1':
        matriz1[0][1] = res
    elif pos == '2':
        matriz1[0][2] = res
    elif pos == '3':
        matriz1[1][0] = res
    elif pos == '4':
        matriz1[1][1] = res
    elif pos == '5':
        matriz1[1][2] = res
    elif pos == '6':
        matriz1[2][0] = res
    elif pos == '7':
        matriz1[2][2] = res
    
    return 'Datos recibidos'