import visa
from lantz import Feat
from lantz.core import mfeats
from lantz import MessageBasedDriver
from lantz.core import log
from logging import DEBUG

import numpy as np
import matplotlib.pyplot as plt


from lantz import Feat
from lantz.core import mfeats
from lantz import MessageBasedDriver
from lantz.core import log
from logging import DEBUG
import numpy as np
import time


class OsciloscopioTektronix1002B(MessageBasedDriver):

    MANUFACTURER_ID = '0x0699'
    MODEL_CODE = '0x0346'

    @Feat()
    def idn(self):
        return self.query('*IDN?')

    timebase = mfeats.QuantityFeat("HOR:MAI:SCA?","HOR:MAI:SCA {}", units = 's',limits=(0,10000))

    voltagescale = mfeats.QuantityFeat("CH1:SCA?","CH1:SCA {}", units = 'V',limits=(0,10))

    def pantalla(self):
        self.write('DAT:ENC RPB')
        self.write('DAT: WID 1')
        data = self.resource.query_binary_values('CURV?', datatype='B',  is_big_endian=True)
        time = np.arange(len(data))
        return time, data

    def escaleo(self):
        #self.inst.write('DAT:ENC ASCIi')
        #self.inst.write('DAT: WID 1')
        print(self.query('WFMP?'))

        #xze, xin, yze, ymu, yoff = self.inst.query_ascii_values('WFMPRE:XZE?;XIN?;YZE?;YMU?;YOFF?;')
        # return xze, xin, yze, ymu, yoff

    def escaleo2(self):
        self.write('DAT:ENC RPB')
        self.write('DAT: WID 1')
        xze, xin, yze, ymu, yoff = self.resource.query_ascii_values(
            'WFMP:XZE?;XIN?;YZE?;YMU?;YOF?;', separator=";")
        return xze, xin, yze, ymu, yoff
