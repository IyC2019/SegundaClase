
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-
"""
    lantz.drivers.tektronix.afg3021b
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Implements the drivers to control a signal generator.
    :copyright: 2015 by Lantz Authors, see AUTHORS for more details.
    :license: BSD, see LICENSE for more details.
"""

from lantz import Feat
from lantz.core import mfeats
from lantz import MessageBasedDriver
from lantz.core import log
from logging import DEBUG



class Generador(MessageBasedDriver):

    MANUFACTURER_ID = '0x0699'
    MODEL_CODE = '0x0346'

    @Feat()
    def idn(self):
        return self.query('*IDN?')
    
    @Feat(units = 'Hz',limits=(0,10000))
    def freq(self):
        self.log
        return float(self.query("SOUR1:FREQ:FIX?"))
        
    @freq.setter
    def freq(self, hertz):
        self.write("SOUR1:FREQ:FIX {}".format(hertz))
    
    freqs = mfeats.QuantityFeat("SOUR1:FREQ:FIX?","SOUR1:FREQ:FIX {}", units = 'Hz',limits=(0,10000))
        
    def set_amp(self, volts):
        self.write("SOUR1:VOLT:AMPL {}".format(volts))
   
    def waveform_shape(self, channel = 1, shape = 'SIN'):
        # Formas posibles: SIN, SQU, PULS, RAMP
        # PRNoise, DC|SINC|GAUSsian|LORentz|ERISe|EDECay|
        # HAVersine
        self.write('SOUR{}:FUNC:SHAPE {}'.format(channel, shape))
        
    def waveform_phase(self, radians, channel = 1):
        self.write('SOUR{}:PHAS {})'.format(channel, radians))
    
    def close_instrument(self):
        # Close VISA session (Close instrument connection)
        print("Killing")
        self.close()
        print("VISA session closed!")
    
    def freq_sweep(self, freq_inicial, freq_final, step, stop = 1, channel = 1):
        # Hace un barrido de frecuencias desde freq_inicial hasta freq_final
        # con un step. Entre cada cambio de frecuencia dejamos 1 segundo de
        # stop.
        frecuencias = np.arange(freq_inicial, freq_final, step)
        for elemento in frecuencias:
            self.write('SOUR{}:FREQ:FIX {}'.format(channel, elemento))
            time.sleep(stop)
            

#with AFG3021b('USB0::0x0699::0x0346::C036492::INSTR') as inst:
 #   print(inst.idn)

        


# In[2]:


import visa
rm = visa.ResourceManager()
data = rm.list_resources()
data


# In[3]:


osci = Generador('USB0::0x0699::0x0346::C036492::INSTR')


# In[4]:


osci.initialize()


# In[5]:


print(osci.freqs)


# In[6]:


osci.freq = 10


# In[161]:


log.log_to_socket(DEBUG)


# In[156]:


with 


# In[120]:


osci.finalize()

