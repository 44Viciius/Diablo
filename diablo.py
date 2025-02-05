import argparse
import socket
import threading
import json
import random
import time
from scapy.all import *

def print_logo():
    logo = r"""
 _______   __            __        __
|       \ |  \          |  \      |  \
| $$$$$$$\ \$$  ______  | $$____  | $$  ______
| $$  | $$|  \ |      \ | $$    \ | $$ /      \
| $$  | $$| $$  \$$$$$$\| $$$$$$$\| $$|  $$$$$$\
| $$  | $$| $$ /      $$| $$  | $$| $$| $$  | $$
| $$__/ $$| $$|  $$$$$$$| $$__/ $$| $$| $$__/ $$
| $$    $$| $$ \$$    $$| $$    $$| $$ \$$    $$
 \$$$$$$$  \$$  \$$$$$$$ \$$$$$$$  \$$  \$$$$$$

                  By 44Viciius<3
    """
    print(logo)

def get_output_filename():
    filename = input("Ingrese el nombre del archivo de salida (.json, .txt): ")
    if not filename:
        filename = "scan_results.json"
    return filename

def syn_scan(target, port):
    src_port = RandShort()
    syn_pkt = IP(dst=target)/TCP(sport=src_port, dport=port, flags="S")
    response = sr1(syn_pkt, timeout=1, verbose=0)

    if response and response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
        send(IP(dst=target)/TCP(sport=src_port, dport=port, flags="R"), verbose=0)
        return True
    return False

def tcp_scan(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((target, port)) == 0:
                return True
    except:
        pass
    return False

def udp_scan(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2)
        sock.sendto(b"Hello", (target, port))
        sock.recvfrom(1024)
        return True
    except:
        pass
    return False

def banner_grab(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((target, port))
            s.send(b'HEAD / HTTP/1.1\r\nHost: example.com\r\n\r\n')
            return s.recv(1024).decode().strip()
    except:
        return "No banner"

def format_banner(banner):
    return banner.replace("\r\n", "\n").replace("\n", " ").strip()

def scan(target, port, method):
    result = {"port": port, "open": False, "banner": None}

    if method == "syn":
        result["open"] = syn_scan(target, port)
    elif method == "tcp":
        result["open"] = tcp_scan(target, port)
    elif method == "udp":
        result["open"] = udp_scan(target, port)

    if result["open"]:
        result["banner"] = banner_grab(target, port)
        result["banner"] = format_banner(result["banner"])

    return result

def threaded_scan(target, ports, method, output_file):
    results = []
    threads = []

    def thread_func(port):
        result = scan(target, port, method)
        if result["open"]:
            results.append(result)
        time.sleep(random.uniform(0.5, 1.5))

    for port in ports:
        t = threading.Thread(target=thread_func, args=(port,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    with open(output_file, "w") as f:
        json.dump(results, f, indent=4, separators=(",", ": "), ensure_ascii=False)
    print(f"Escaneo finalizado. Resultados guardados en {output_file}")

def main():
    print_logo()

    parser = argparse.ArgumentParser(description="Escáner de Puertos Avanzado")
    parser.add_argument("target", type=str, help="Dirección IP objetivo")
    parser.add_argument("--ports", type=str, default="20-1024", help="Rango de puertos a escanear (ej. 20-1024)")
    parser.add_argument("--method", type=str, choices=["syn", "tcp", "udp"], default="tcp", help="Método de escaneo")
    parser.add_argument("--output", type=str, help="Archivo de salida (ej. result.json)")

    args = parser.parse_args()

    if not args.output:
        output_filename = get_output_filename()
    else:
        output_filename = args.output

    start, end = map(int, args.ports.split("-"))
    ports = range(start, end + 1)
    threaded_scan(args.target, ports, args.method, output_filename)

if __name__ == "__main__":
    main()

