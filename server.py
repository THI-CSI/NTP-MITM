import socket
import datetime
import time
import ntplib
import sys

DATE = "12:27:00 22.03.2023"


def get_ntp_data():
    padding = 2208988800
    dtime = datetime.datetime.strptime(DATE, "%H:%M:%S %d.%m.%Y").timetuple()
    utime = int(time.mktime(dtime) + padding)
    packet = ntplib.NTPPacket(3, 4, utime)
    packet.stratum = 1
    packet.recv_timestamp = utime
    packet.orig_timestamp = utime
    packet.ref_id = 133742069
    packet.ref_timestamp = utime
    return packet
    

def serve_ntp():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("localhost", 123))

    print("NTP server running...")
    while True:
        data, address = server.recvfrom(1024)
        print("[+] {} - {}:{}".format(datetime.datetime.now().time().strftime("%H:%M:%S"), address[0], address[1]))
        if data:
            ntp_data = get_ntp_data()
            server.sendto(ntp_data.to_data(), address)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        if sys.argv[1] in ["-d", "--datetime"]:
            try:
                datetime.datetime.strptime(sys.argv[2], "%H:%M:%S %d.%m.%Y")
                DATE = sys.argv[2]
            except:
                print("error: Date '{}' is not valid. Use format 'HH:MM:SS dd.mm.yyyy'.".format(sys.argv[2]))
                exit()
    serve_ntp()
