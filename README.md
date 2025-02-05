# Diablo



Escáner de Puertos Avanzado
Este es un escáner de puertos avanzado escrito en Python, diseñado para realizar escaneos de puertos TCP, SYN y UDP en direcciones IP específicas. El script permite obtener banners de servicios en los puertos abiertos y guardar los resultados en archivos JSON o de texto.

Características
Escaneo TCP, SYN y UDP: Soporta tres métodos de escaneo para detectar puertos abiertos en el objetivo.
Obtención de banners: Si se detecta un puerto abierto, se realiza un intento de obtener un banner del servicio que se esté ejecutando en ese puerto.
Multihilo: Utiliza múltiples hilos para realizar el escaneo de puertos de manera más rápida y eficiente.
Personalización de puertos: Puedes especificar un rango de puertos a escanear.
Salida de resultados: Los resultados del escaneo se guardan en un archivo JSON o de texto.
Logo personalizable: Incluye un logo ASCII al inicio del script.
Instalación
Este script requiere que tengas instalados los siguientes paquetes de Python:

scapy para realizar el escaneo de puertos y obtener banners.
Puedes instalarlo ejecutando:

pip install scapy
Uso
Para ejecutar el script, usa el siguiente comando en la terminal:

python3 diablo.py <IP objetivo> [opciones]
Opciones
target (requerido): La dirección IP del objetivo a escanear.
--ports (opcional): El rango de puertos a escanear. El valor predeterminado es 20-1024. Ejemplo: --ports 80-443.
--method (opcional): El método de escaneo que deseas utilizar. Los métodos disponibles son:
syn: Escaneo SYN.
tcp: Escaneo TCP.
udp: Escaneo UDP. El valor predeterminado es tcp.
--output (opcional): El nombre del archivo de salida. Si no se especifica, el script pedirá que ingreses un nombre para el archivo. Ejemplo: --output resultados.json.

python3 diablo.py <ip> --ports 80-443 --method tcp --output scan_results.json
Si no especificas el archivo de salida, el script te pedirá que ingreses un nombre para el archivo.

Ejemplo de salida
El archivo de resultados generado será un archivo JSON o TXT con la siguiente estructura:

[
    {
        "port": 80,
        "open": true,
        "banner": "HTTP/1.1 400 Bad Request ..."
    },
    {
        "port": 443,
        "open": true,
        "banner": "No banner"
    }
]
Contribuciones
Si deseas contribuir al desarrollo de este script, siéntete libre de hacer un fork del repositorio y enviar un pull request con tus mejoras.

Licencia
Este proyecto está bajo la licencia MIT.
