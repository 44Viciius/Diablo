# GoodLuck - Escáner de Puertos 🚀

**GoodLuck** es tu nuevo mejor amigo para auditar redes y encontrar puertos abiertos como un profesional. Con este script, podrás detectar vulnerabilidades, obtener banners de servicios y hacer todo un análisis de seguridad en tus objetivos, todo de manera rápida y eficiente. Ya sea que seas un pentester, un admin de sistemas o simplemente un hacker ético, **GoodLuck** está diseñado para ofrecerte lo mejor en escaneos de puertos, ¡y lo hace con estilo! 😎

## Características 🔧

- **Escaneo Poderoso**: Escoge entre **SYN**, **TCP** o **UDP** para detectar puertos abiertos.
- **Banner Grabbing**: ¿Qué hay detrás de ese puerto abierto? **GoodLuck** agarra los banners para que sepas qué servicio está corriendo y qué versión tiene. 🖥️
- **Multihilo**: Escanea varios puertos al mismo tiempo, ¡nada de esperar horas! ⚡
- **Salida en JSON o TXT**: Guarda los resultados en formato limpio, listo para analizar o compartir. 💾
- **Totalmente Flexible**: Define el rango de puertos, elige el método de escaneo y, si te hace falta, personaliza el archivo de salida. 🔄

## Requisitos 📋

- **Python 3.x** 🐍
- Paquete **Scapy** (sí, es el rey para manipular paquetes en redes)

Instálalo fácil con `pip`:

```bash
pip install scapy

Cómo Usarlo 💻

python goodluck.py <target> --ports <port_range> --method <scan_method> --output <output_file>


<target>: La IP o dominio que vas a escanear. 🌍
--ports <port_range>: Rango de puertos a escanear (por ejemplo, 20-1024).
--method <scan_method>: Método de escaneo:
syn: Escaneo SYN (súper rápido). ⚡
tcp: Conexión TCP completa. 🌐
udp: Paquete UDP. 📦
--output <output_file>: Archivo donde se guardan los resultados. Si no lo defines, el nombre por defecto es scan_results.json.

Ejemplo
Para escanear puertos en una IP objetivo, usando TCP y guardar todo en resultados.json, solo tienes que correr:
python goodluck.py <tu ip> --ports 0-65535 --method tcp --output resultados.json

Lo que Hace el Código 🧑‍💻
Escaneo de Puertos: Escoge el método de escaneo que prefieras (SYN, TCP o UDP) y GoodLuck lo ejecutará de manera eficiente, buscando puertos abiertos en el rango que determines.
Banner Grabbing: Cuando encuentres un puerto abierto, el script intenta obtener el banner del servicio. Así podrás saber qué está corriendo y qué versión tiene. ¡Perfecto para identificar posibles vulnerabilidades! 🔍
Escaneo Multihilo: No pierdas tiempo escaneando puerto por puerto. GoodLuck utiliza múltiples hilos para escanear en paralelo y obtener resultados más rápidos. 🚀
Exportación de Resultados: Los resultados se guardan automáticamente en un archivo JSON o TXT, fácil de leer, analizar o compartir con otros. 📂

Contribuciones 🤝
Si quieres mejorar el proyecto, haz un fork y envía tu pull request! Si encuentras un bug o tienes alguna sugerencia, abre un issue en el repositorio y lo miramos.


