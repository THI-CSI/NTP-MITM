import ntplib
from time import ctime

def get_ntp_time(server='localhost'):
    try:
        client = ntplib.NTPClient()
        response = client.request(server, version=3)
        print(vars(response))
        return response.tx_time
    except Exception as e:
        print("Error:", e)
        return None

def main():
    ntp_time = get_ntp_time()
    if ntp_time:
        print("NTP Time:", ctime(ntp_time))

if __name__ == "__main__":
    main()
