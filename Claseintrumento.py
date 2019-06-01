import visa  # Install pyvisa: pip install pyvisa


class instrument(object):
    def __init__(self, name=None, port=None):
        self = visa.ResourceManager()
        self.list_resources()
        if not port:
            Generador = self.list_resources()
            GeneradorID = Generador[0]
            self.port = GeneradorID
        else:
            self.port = port
        print("Opening VISA session...")
        inst = self.open_resource(self.port)
        print("VISA session successfully opened!")
        if not name:
            self.name = inst.query("*IDN?")
        else:
            self.name = name

        print(self.port)

    def __repr__(self):
        # Representation of object
        return """Instrument %s \navailable at port: %s
        \nwaiting for commands...""" % (self.port, self.name)

    def close_instrument(self):

        # Close VISA session (Close instrument connection)
        print("Killing")
        self.close()
        print("""Communication with instrument %s at port %s will be closed...""" %
              (self.name, self.port))
        print("VISA session closed!")


gen = instrument()
gen.close_instrument()
print(gen.name)
