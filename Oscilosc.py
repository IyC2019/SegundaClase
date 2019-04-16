
# coding: utf-8

# In[2]:



from lantz import Feat
from lantz.core import mfeats
from lantz import MessageBasedDriver
from lantz.core import log
from logging import DEBUG

import numpy as np
import matplotlib.pyplot as plt



class OsciloscopioTektronix1002B(MessageBasedDriver):

    MANUFACTURER_ID = '0x0699'
    MODEL_CODE = '0x0346'

    @Feat()
    def idn(self):
        return self.query('*IDN?')

    timebase = mfeats.QuantityFeat("HOR:MAI:SCA?","HOR:MAI:SCA {}", units = 's',limits=(0,10000))
    
    voltagescale = mfeats.QuantityFeat("CH1:SCA?","CH1:SCA {}", units = 'V',limits=(0,10))

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


# In[3]:


osci = OsciloscopioTektronix1002B('USB0::0x0699::0x0363::C108013::INSTR')


# In[4]:


osci.initialize()


# In[5]:


print(osci.timebase)
print(osci.idn)


# In[6]:


osci.timebase = 10.0


# In[45]:


print(osci.voltagescale)


# In[44]:


osci.voltagescale = 5

