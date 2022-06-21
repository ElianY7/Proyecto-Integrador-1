def mayor_num(num1,num2,num3,num4,num5):
   
    lista=[num1,num2,num3,num4,num5]

    mayor=0

    for i in range (len(lista)):
     if lista[i]>mayor:
     mayor=lista[i]

    print(mayor)

