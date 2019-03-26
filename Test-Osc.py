import visa
from matplotlib import pyplot as plt
import numpy as np
rm = visa.ResourceManager()
rm.list_resources()
Osciloscopio = rm.list_resources()
#print(Osciloscopio[0])
OsciloscopioID = Osciloscopio[0]
inst = rm.open_resource(OsciloscopioID)

print(inst.query("*IDN?"))

print(inst.query('DAT:SOU?'))
#print(inst.query('CURVe?'))
#help(query())
#inst.write('DAT:ENC ASCI')
xze, xin, yze, ymu, yoff = inst.query_ascii_values('WFMPRE:XZE?;XIN?;YZE?;YMU?;YOFF?;', separator=';')
#inst.write('DAT:ENC ASCI')
#inst.write('DAT:WID 1')
#print(inst.query_binary_values('CURVe?',datatype='f'))

#print(inst.query_ascii_values('CURV?'))

#inst.write('CURV?')
#print(inst.read())
inst.write('DAT:ENC RPB') #pasa a binario
inst.write('DAT:WID 1')

# Adquiere los datos del canal 1 y los devuelve en un array de numpy
data = -yoff*ymu + inst.query_binary_values('CURV?', datatype='B', container=np.array)*ymu #hay que ver la magia de aca...
print(yze)
print(ymu)
print(yoff*ymu)
tiempo = xze + np.arange(len(data)) * xin

plt.plot(tiempo, data);
plt.xlabel('Tiempo [s]');
plt.ylabel('Voltaje [V]');
plt.show()
# parameters = inst.acquire_parameters()
# inst.data_setup() 
# inst.send('DAT:STAR 1')
# inst.send('DAT:STOP 100')
# data = inst.query('CURV?')
# data = data[6:].split(',')
# data = array(list(map(float, data)))
# ydata = (data - parameters['YOF']) * parameters['YMU']\
#         + parameters['YZE']
# xdata = arange(len(data))*parameters['XIN'] + parameters['XZE']
# return list(xdata), list(ydata)