Este repositorio proporciona la configuración adecuada para conectarse desde una Raspberry Pi o sistema basado en Unix a una red con seguridad IPsec que utiliza una primera fase agresiva, con PSK, y soporta tanto conexiones con XAuth como sin XAuth. Las configuraciones han sido probadas exitosamente en una Raspberry Shake y una Raspberry Pi con módem SIM7600G-H.

# Requisitos Previos

En ambos casos, es necesario actualizar el sistema e instalar strongSwan:
```
sudo apt update && sudo apt upgrade
```
# Instalación de strongSwan

## Para Raspberry Shake (con soporte XAuth)

La Raspberry Shake requiere compilar strongSwan desde código fuente para incluir soporte XAuth:
```
wget https://download.strongswan.org/strongswan-5.9.13.tar.gz
tar xzf strongswan-5.9.13.tar.gz
cd strongswan-5.9.13

sudo apt install libgmp-dev libssl-dev flex bison

./configure --enable-fortinet-vendor-ids
make
sudo make install
```
## Para Raspberry Pi estándar
StrongSwan se puede descargar desde sudo apt:

```
sudo apt install strongswan strongswan-starter -y
```
# Configuración del Módem SIM7600G-H

Para conexiones bilaterales, es necesario configurar el módem en modo WAN y establecer el APN correspondiente. Utilice el script activar_wan_configurar_apn.py:
```
python3 activar_wan_configurar_apn.py
```
# Configuración IPsec

El repositorio incluye archivos de configuración que establecen la conexión IPsec. La configuración utiliza una subred específica para garantizar el correcto funcionamiento del geófono y sus canales en Raspberry Shake. En el caso de una Raspberry convencional el también se poseen archivos de configuración con algunos cambios en la configuración que son necesarios

## Estructura de configuración

- ipsec.conf: Configuración principal del túnel IPsec
- ipsec.secrets: Credenciales y claves PSK

## Notas importantes

- La configuración utiliza direccionamiento IP específico para asegurar compatibilidad
- Los archivos de secrets requieren permisos restrictivos (600)
- Se recomienda verificar la conectividad de red antes de iniciar el túnel

# Uso

Una vez configurado, inicie el servicio IPsec con:
```
sudo ipsec start
sudo ipsec up [NOMBRE_CONEXION]
```
Reemplace [NOMBRE_CONEXION] con el nombre específico de la conexión definida en su configuración.
