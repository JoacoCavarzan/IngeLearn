from pymodbus.client import ModbusTcpClient

cliente = ModbusTcpClient("192.168.5.20")

cliente.connect()

#cliente.write_coll(1, True)

lectura = cliente.read_discrete_inputs(0,1)
print("El estado de entrada es", lectura.bits[0])

cliente.close()
