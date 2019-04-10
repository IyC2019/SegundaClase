import visa  # Install pyvisa: pip install pyvisa
import numpy as np
import matplotlib.pyplot as plt
rm = visa.ResourceManager()
print(rm.list_resources())


class OsciloscopioTektronix1002B():
    def __init__(self, serialno):
        self.serialno = serialno
        self.inst = rm.open_resource(self.serialno)
        print(self.serialno)

    def idn(self):
        return self.inst.query("*IDN?")

    def set_timebase(self, seconds):
        print('HOR: MAI: SCA {}'.format(seconds))
        self.inst.write('HOR:MAI:SCA {}'.format(seconds))
        # return self.inst.write('HOR:MAI?')

    def close_instrument(self):
        # Close VISA session (Close instrument connection)
        print("Killing")
        self.inst.close()
        print("VISA session closed!")

    def pantalla(self):
        self.inst.write('DAT:ENC RPB')
        self.inst.write('DAT: WID 1')
        data = self.inst.query_binary_values('CURV?', datatype='B',  is_big_endian=True)
        time = np.arange(len(data))
        return time, data

    def escaleo(self):
        #self.inst.write('DAT:ENC ASCIi')
        #self.inst.write('DAT: WID 1')
        print(self.inst.query('WFMP?'))

        #xze, xin, yze, ymu, yoff = self.inst.query_ascii_values('WFMPRE:XZE?;XIN?;YZE?;YMU?;YOFF?;')
        # return xze, xin, yze, ymu, yoff

    def escaleo2(self):
        self.inst.write('DAT:ENC RPB')
        self.inst.write('DAT: WID 1')
        xze, xin, yze, ymu, yoff = self.inst.query_binary_values(
            'WFMPRE:XZE?;XIN?;YZE?;YMU?;YOFF?;')
        return xze, xin, yze, ymu, yoff


osc = OsciloscopioTektronix1002B('USB0::1689::867::C108011::0::INSTR')
# osc = OsciloscopioTektronix1002B('USB0::1689::872::C017051::0::INSTR')
# osc.set_timebase(10)
# osc.pantalla()
t, y = osc.pantalla()
plt.plot(t, y)
plt.show()
osc.close_instrument()
# gen = rm.open_resource('USB0::1689::872::C017051::0::INSTR')
# print(gen.query("*IDN?"))
