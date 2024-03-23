import ntplib
import sys
from time import ctime

SERVER='localhost'

def get_ntp_time(server='localhost'):
    try:
        client = ntplib.NTPClient()
        response = client.request(server, version=3)
        print(vars(response))
        print(response.to_data().hex())
        return response.tx_time
    except Exception as e:
        print("Error:", e)
        return None

def main():
    ntp_time = get_ntp_time(SERVER)
    if ntp_time:
        print("NTP Time:", ctime(ntp_time))

if __name__ == "__main__":
    if len(sys.argv) > 2:
        if sys.argv[1] in ["-s", "--server"]:
            SERVER=sys.argv[2]
    main()
