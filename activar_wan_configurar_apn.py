import serial
import time

def configurar_wan_apn(port='/dev/ttyUSB2', baudrate=115200, apn="internet.tigo.com.co"):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)
        
        commands = [
            "AT",
            "AT+CNCFG=0,1,\"" + apn + "\"",  # Configurar APN en perfil 0
            "AT+CNACT=0,1",                   # Activar perfil 0
            "AT+CNACT?",                      # Verificar activación
            "AT+CLANMODE=1",                  # Activar modo LAN/WAN
            "AT+CLANMODE?",                   # Verificar modo
            "AT+NETOPEN",                     # Abrir conexión red
            "AT+NETOPEN?",                    # Verificar conexión
            "AT+IPADDR"                       # Ver IP asignada
        ]
        
        for cmd in commands:
            ser.write((cmd + '\r\n').encode())
            time.sleep(3)
            response = ser.read(ser.in_waiting).decode()
            print(f"Enviando: {cmd}")
            print(f"Respuesta: {response}")
            print('-' * 50)
            
        ser.close()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    configurar_wan_apn()
