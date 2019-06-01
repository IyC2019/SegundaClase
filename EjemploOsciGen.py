gen = Generador('USB0::0x0699::0x0346::C034198::INSTR')
gen.initialize()
osci = OsciloscopioTektronix1002B('USB0::0x0699::0x0363::C065092::INSTR')
osci.initialize()

gen.freqs = 10 #tiene el problema, de que el query ademas de hacer un write hace un read.

time, data = osci.pantalla()
xze, xin, yze, ymu, yoff = osci.escaleo2()
data = np.array([float(i) for i in data])
time = np.array([float(i) for i in time])
data = -yoff*ymu + data*ymu
time = xze + time * xin

plt.plot(time,data)

#Dependiendo que estamos levantando, grabar antes la data antes que se pise
rango = 10 #la cantidad de iteraciones que voy a tener.
paso = 100 # cada cuanto es el paso entre una frecuencia y la siguiente
times = np.zeros((rango,2500)) #La cantidad de columnas es la cantidad de datos que me tira el osci
datas = np.zeros((rango,2500)) # creo que era 2500, esto habria que chequearlo
for i in range(0,rango):
    gen.freqs = i*paso #tiene el problema, de que el query ademas de hacer un write hace un read.
    osci.timebase = (1/(i*paso))/5  #Que cada 5 cuadraditos del Osci, halla 1 onda completa. Se vera si se ajusta
    time, data = osci.pantalla() #levanto pantalla
    xze, xin, yze, ymu, yoff = osci.escaleo2()#levanto el escaleo
    datas = np.array([float(j) for j in data]) #transformo en float y en array
    times = np.array([float(j) for j in time])
    datas = -yoff*ymu + datas*ymu #hago la conversion del escaleo
    times = xze + times * xin
    mdata[:][i] = datas #Primer valor es fila, el segundo es columna
    mtime[:][i] = times
np.savetxt('Nombre barrido freq data',mdata, delimiter=' ')
np.savetxt('Nombre barrido freq tiempo',mtime, delimiter=' ')

rango = 10 #la cantidad de iteraciones que voy a tener.
paso = 100 # cada cuanto es el paso entre una frecuencia y la siguiente
times = np.zeros((rango,2500)) #La cantidad de columnas es la cantidad de datos que me tira el osci
datas = np.zeros((rango,2500)) # creo que era 2500, esto habria que chequearlo
for i in range(0,rango):
    gen.set_amp( i*paso)  #tiene el problema, de que el query ademas de hacer un write hace un read.
    osci.voltagescale = (1/(i*paso))/5  #Que cada 5 cuadraditos del Osci, halla 1 onda completa. Se vera si se ajusta
    time, data = osci.pantalla() #levanto pantalla
    xze, xin, yze, ymu, yoff = osci.escaleo2()#levanto el escaleo
    datas = np.array([float(j) for j in data]) #transformo en float y en array
    times = np.array([float(j) for j in time])
    datas = -yoff*ymu + datas*ymu #hago la conversion del escaleo
    times = xze + times * xin
    mdata[:][i] = datas #Primer valor es fila, el segundo es columna
    mtime[:][i] = times
np.savetxt('Nombre barrido amp data',mdata, delimiter=' ')
np.savetxt('Nombre barrido amp tiempo',mtime, delimiter=' ') 
