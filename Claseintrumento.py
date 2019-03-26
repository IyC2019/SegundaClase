import visa # Install pyvisa: pip install pyvisa
import time

class instrument(object):
    
    ##################################
    # Generic instrument class
    ##################################
    
    def __init__(self, name=None, port=None):
        # Initialization function:        
        # Args
        # name: name of the instrument
        # port: connection port. Can be either GPIB or serial.

        
        
        self.rm = visa.ResourceManager()
        rm.list_resources()
        if not port:
            Generador = rm.list_resources()
            GeneradorID= Generador[0]
            self.port = GeneradorID
        else:
            self.port = port
        if not name:
            self.name =  inst.query("*IDN?")
        else:
            self.name = name
        print("Opening VISA session...")
        print(port)
        self.instr = self.rm.open_resource(port)
        print("VISA session successfully opened!")
        
    def __repr__(self):
        
         # Representation of object
         return """Instrument %s \navailable at port: %s \nwaiting for commands...""" %(self.port, self.name)
        
    def close_instrument(self):
        
        # Close VISA session (Close instrument connection)
        print("Killing")
        self.rm.close()
        print("Communication with instrument %s at port %s will be closed..." %(self.name, self.port))
        print("VISA session closed!")

rm = visa.ResourceManager()
rm.list_resources()
Generador = rm.list_resources()
GeneradorID = Generador[0]
rm.close()

gen = instrument()
gen.close_instrument()
print(gen.name)