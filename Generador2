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
