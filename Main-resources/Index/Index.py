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
MEDIDAS ="1 PLAZA ", "1 PLZA ½", "2 PLAZAS ","PLAZAS ½"
TIPO = "RESORTES", "ESPUMA"
CANTIDAD = "700-10.000", "10.000 A 15.000", "MAS DE 15.000"
PRECIO = "40.000 A 70.000", "70.000 A 100.000", "MAS DE 100.000"

#index
MARCA = input('ingrese marca')
print ('usted quiere, ' + marca)
MEDIDAS= input('ingrese medidas')
print ('usted quiere, ' + medidas)
TIPO =input('ingrese tipo')
print ('usted quiere, ' + tipo)
CANTIDAD = input('ingrese cantidad')
print ('usted quiere, ' + cantidad)

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