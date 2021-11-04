import time
from random import randint

#Llenar la matriz con numeros random entre 1 y 9
#Retornar la suma de concentraciones de los bloques extraidos




def inicio(arrayList,p):
  aux2=[]
  x=0

  for j in range(p):
    aux2.insert(j,0)

  aux=arrayList.pop(p-1)
  arrayList.insert(p-1,aux2)

  for i in range(len(aux)):
    x=x+aux[i]


  return x
#esta funcion sirve para botar la ultima fila y guardar su valor


#----------------------------------------------------------------
def count(arrayList,p,q):
  x=0
  for i in range(0,len(arrayList)-1):
    if arrayList[i+1][q]==0:
      x=x+1
  return x
#sirve para contar los ceros en la respectiva columna
#----------------------------------------------------------------
def caer(arrayList,p,q):
  x=0
  if ((arrayList[p][q] <= count(arrayList,p,q)) and (arrayList[p+1][q]==0) ):
    x=arrayList[p][q]
    arrayList[p][q]=0
  return x
#sirve para botar el cuadro en que se encuentra en caso de ser necesario
#----------------------------------------------------------------

def count2(arrayList,p,q):
  x=0

  if q==0:
    for i in range(0,len(arrayList)-1):
      if arrayList[i+1][q]==0:
        x=x+1
    if arrayList[p+1][q+1]==0:
      x=x+1
  elif q==len(arrayList)-1:
    for i in range(0,len(arrayList)-1):
      if arrayList[i+1][q]==0:
        x=x+1
    if arrayList[p+1][q-1]==0:
      x=x+1
  else:
    for i in range(0,len(arrayList)-1):
      if arrayList[i+1][q]==0:
        x=x+1
    if arrayList[p+1][q-1]==0:
      x=x+1
    if arrayList[p+1][q+1]==0:
      x=x+1
  
  
  return x
 
#contador para caso 2
#----------------------------------------------------------------

def caer2(arrayList,p,q):
  x=0
  if ((arrayList[p][q] <= count2(arrayList,p,q)) and (arrayList[p+1][q]==0) ):
    x=arrayList[p][q]
    arrayList[p][q]=0
  return x
#sirve para botar el cuadro en que se encuentra en caso de ser necesario



#----------------------------------------------------------------
p=int(input("Ingrese dimension de la matriz: "))
print("ingrese la opcion deseada\n [1]caso en que se evalua solo los bloques verticalmente abajon\n [2]caso se evalua bloques verticalmente abajo y los bloques directamente diagonales")
u=int(input())

t_eje=time.time()

arrayList = []
for i in range(p):
  s=[]

  for j in range(p):
    s.insert(j,randint(1,9))#rango de numeros random
  arrayList.insert(i,s)
  
   
for q in range(p):
  print(arrayList[q])

print("-------------------------------------------")

suma =inicio(arrayList,p)

if u==1:#opcion caso 1
  for k in range(len(arrayList)-2,-1,-1):
    for l in range(len(arrayList)):
      suma =suma + caer(arrayList,k,l)
      for q in range(p):
        print(arrayList[q])
      print("-------------------------------------------")

if u==2:#opcion caso 2
  for k in range(len(arrayList)-2,-1,-1):
    for l in range(len(arrayList)):
      suma =suma + caer2(arrayList,k,l)
      for q in range(p):
        print(arrayList[q])
      print("-------------------------------------------")

for q in range(p):
  print(arrayList[q])
print("el total minado es de",suma)
print(time.time()-t_eje,"segundos")

#cuerpo del programa
#------------------------------------------------------------------