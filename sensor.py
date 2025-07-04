import serial
import serial.tools.list_ports
import time

# Lista portas e escolhe manualmente
print("Portas encontradas:")
for p in serial.tools.list_ports.comports():
    print(f"  {p.device} -> {p.description}")

# Ajuste aqui para a porta correta
porta = 'COM5'
baud  = 9600

# Tenta abrir
try:
    ser = serial.Serial(porta, baud, timeout=1)
    time.sleep(2)
    print(f"Conectado em {porta} a {baud} bps")
    # Exemplo de comando
    ser.write(b'F')
    ser.close()
except Exception as e:
    print("Erro ao abrir porta serial:", e)


    