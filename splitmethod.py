#making my own split method

def mysplit(str):
    #
    # put your code here
    #
    lista = []
    strTemp =''
    for char in str:
        
        if not (char.isspace()):
               strTemp += char
        elif (len(strTemp) > 0):
            lista.append(strTemp)
            strTemp =''
            
    if (len(strTemp) > 0):
            lista.append(strTemp)
        
    return lista

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
