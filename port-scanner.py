import socket
import sys


def scan(url, port_start, port_end):
    try:
        ip = socket.gethostbyname(url)
        for port in range(port_start,port_end):  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port "+ str(port) +" : open")
            sock.close()

    except KeyboardInterrupt:
        print("")
        print("Bye !")
        sys.exit()


def main():
    url = input("Enter the URL (or IP) you want to scan (Without 'http' or 'https'): ")
    while "http" in url:
        print("You don't need to specify 'http' or 'https' in the URL : ")
        url = input("Enter the URL (or IP) you want to scan (Without 'http' or 'https'): ")

    port_start = int(input("Enter the port where you want the scan to start : "))
    port_end = int(input("Enter the port where you want the scan to end : "))
    while port_start > port_end:
        print("The first port can't be superior to the last one, try again.")
        port_start = int(input("Enter the port where you want the scan to start : "))
        port_end = int(input("Enter the port where you want the scan to end : "))

    print("Scan is starting ... (Ctrl + C to quit)")
    print("")
    print("Host : " + url)
    print("Port range : " + str(port_start) + " - " + str(port_end))
    print("")
    scan(url, port_start, port_end)


if __name__ == "__main__":
    main()
