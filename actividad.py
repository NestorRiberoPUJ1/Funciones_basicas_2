def cuentaRegresiva(num):
    list=[]
    for x in range(num+1):
        list.append(num-x)
    return list
print(cuentaRegresiva(8))

def imprimir_y_devolver(list):
    print(list[0])
    return list[1]
print(imprimir_y_devolver([0,20]))

def primero_mas_longitud(list):
    return len(list)+list[0]
print(primero_mas_longitud([1,2,3,4,5]))

def valores_mayores_que_el_segundo(list):
    if(len(list)<2):
        return False
    auxList=[]
    for x in list:
        if(x>list[1]):
            auxList.append(x)
    print(len(auxList))

    return auxList
print(valores_mayores_que_el_segundo([5,2,3,2,1,4]))
print(valores_mayores_que_el_segundo([3]))

def length_and_value(length,value):
    list=[]
    for x in range(length):
        list.append(value)
    return list
print(length_and_value(4,7))
print(length_and_value(6,2))

