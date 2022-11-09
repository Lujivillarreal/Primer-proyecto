###############################################
# Primer commit main APP-Prueba
# Subir a Github
# Index.py
# ejecutacle.exe
# release: 26/10/2022
# devolper: Villarreal Maria Lujan
###############################################

#main-recurces
MARCA = "CANNON", "PIERO", "SIMMONS", "KING KOIL",  "INDUCOL", "SERTA", "BEDTIME", "TELGO", "SEALY", "SUAVESTAR"
MEDIDAS ="1 PLAZA ", "1 PLZA ½", "2 PLAZAS "," 2 PLAZAS ½"
TIPO = "RESORTES", "ESPUMA"
CANTIDAD = "700-10.000", "10.000 A 15.000", "MAS DE 15.000"
PRECIO = "40.000 A 70.000", "70.000 A 100.000", "MAS DE 100.000"

#index
#MARCA = input('ingrese marca')
#print ('usted quiere, ' + MARCA)

#MEDIDAS= input('ingrese medidas')
print ('usted quiere, ' + MEDIDAS)

#TIPO =input('ingrese tipo')
print ('usted quiere, ' + TIPO)

#CANTIDAD = input('ingrese cantidad')
print ('usted quiere, ' + CANTIDAD)

while True:
        MARCA = input('ingrese marca')
        if MARCA != "CANNON":
            print( "Pone una marca valida")
        else:
            print ("Genial")
            break
        continue

while True:
        MEDIDAS = int (input('ingrese medidas') )
        if  MEDIDAS!="1 PLAZA " :
            print ("elija una medida valida")
        else:
            print ("Bien")
            break
        continue
    
while True:
        CANTIDAD = int (input('ingrese tipo')) 
        if  CANTIDAD!="700-10.000":
            print ("elija una cantidad valida")
        else:
            print ("Bien")
            break
        continue

while True:
        TIPO = input('ingrese tipo') 
        if  TIPO!="RESORTES":
            print ("elija un tipo valido")
        else:
            print ("Bien")
            break
        continue
   
  
while True:
        PRECIO = int (input('ingrese precio') )
        if PRECIO!= "40.000 A 70.000":
         print ("elija un precio valido")
        else:
            print ("Bien")
            break
        continue


#VARUSUARIO
#variableUsuario

#definimos la forma de importacion
from csv import excel
import openpyxl

#definimos la ubicación del archivo
wb = openpyxl.load_workbook("/C:\Desarrollo\vigilante-aventura\excel.xlsx")

print(wb.sheetnames)

"import" 
ws = wb.get_sheet_byname(name = 'emails-clientes')






   