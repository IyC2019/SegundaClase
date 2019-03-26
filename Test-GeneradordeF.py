import visa
rm = visa.ResourceManager()
rm.list_resources()
Generador = rm.list_resources()
print(Generador[0])
GeneradorID = Generador[0]
inst = rm.open_resource(GeneradorID)

print(inst.query("*IDN?"))
inst.write("*IDN?")
print(inst.read())
inst.write('SOURCE:FREQ 100')
inst.write('SOUR:VOLT:AMPL 1')

inst.write('SOUR:VOLTage:LEVel:IMMediate:OFFSet 250mV')
inst.write('SOUR:PHAS:ADJ 10 DEG')



#print("valor %.1f %.1f" % (4.3, 4))