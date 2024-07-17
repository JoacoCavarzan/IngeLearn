import paho.mqtt.client as mqtt
import time
from pymodbus.client import ModbusTcpClient

PLC = ModbusTcpClient("192.168.5.20")
PLC.conect()

servidor = "broker.mqtt.cool"
cliente = mqtt.Client(protocol=mqtt.MQTTv5)

cliente.connect(servidor, 1883)

# --------------------------------------------------------------
try:
    while True:
        lectura = PLC.read_discrete_inputs(0, 1)
        estadoEntrada = lectura.bita[0]
        cliente.publish("EntradaPLC", estadoEntrada)
        time.sleep(0.2)

except:
    PLC.close()