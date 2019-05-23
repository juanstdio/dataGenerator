#Invente Roman Invente by Juanstdio
# Mayo 2019

import xlsxwriter #Modulo requerido
import time  # Modulo incluido en python
import names #Modulo requerido 
import random #Modulo incluido en python

excel = xlsxwriter.Workbook('Usuarios.xlsx')
renglon1 = excel.add_worksheet('Empleados')
renglon2 = excel.add_worksheet('Trabajadores en Actividad')
Cargos = ['Asistente','Administrador','Editor']
Zona = ['San Martin','Concordia','Buenos Aires']
Fechas = ['22/05/2019','23/04/2019','20/04/2020']

renglon1.write('A1', 'Nombre')
renglon1.write('B1', 'Apellido')
renglon1.write('C1', 'Zona')
renglon1.write('D1', 'Cargo')
renglon1.write('E1', 'Edad')
renglon1.write('F1', 'Fecha de Ingreso')
for x in xrange(2,152):
   renglon1.write('A'+str(x),names.get_first_name())
   valor = random.randint(0, 2)
   renglon1.write('B'+str(x),names.get_last_name())
   renglon1.write('C'+str(x),Zona[valor])
   valor = random.randint(0,2)
   renglon1.write('D'+str(x),Cargos[valor])
   valor = random.randint(0,2)
   renglon1.write('E'+str(x),random.randint(18,65))
   renglon1.write('F'+str(x),Fechas[valor])

Bonos = ['Si','No','No disponible']

renglon2.write('A1', 'ID Empleado')
renglon2.write('B1', 'Area de Trabajo')
renglon2.write('C1', 'Cuando debe ir?')
renglon2.write('D1', 'Bono Comidas')
renglon2.write('E1', 'Distancia recorrida')
renglon2.write('F1', 'Categoria sueldo')
for x in xrange(2,152):
    #ID Empleado va aqui
    renglon2.write('A'+str(x),str(x-1))
    valor = random.randint(0,2)
    renglon2.write('B'+str(x),Cargos[valor])
    valor = random.randint(0,2)
    renglon2.write('C'+str(x),Fechas[valor])
    valor = random.randint(0,2)
    renglon2.write('D'+str(x),Bonos[valor])
    renglon2.write('E'+str(x),random.randint(1,180))
    renglon2.write('F'+str(x),random.randint(1,4))

excel.close()
