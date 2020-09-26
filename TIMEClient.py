import socket
import datetime

s = socket.socket()
s2 = socket.socket()

host = "time.nist.gov"
port = 37
host2 = "ut1-wwv.nist.gov"

s.connect((host, port))
s2.connect((host2, port))

print("IP Adress of server 1: ",socket.gethostbyname(host))
print("IP Adress of server 2: ",socket.gethostbyname(host2))


s.send(b'')
response_str = s.recv(4096)

seconds = int.from_bytes(response_str, 'big')

conversion = datetime.timedelta(seconds=seconds)
converted_time = str(conversion)

s2.sendall(b'')
response2_str = s2.recv(4096)

seconds2 = int.from_bytes(response2_str, 'big')

conversion2 = datetime.timedelta(seconds=seconds2)
converted_time2 = str(conversion2)


print("Time Passed for server 1: ",converted_time)
print("Time Passed for server 2: ",converted_time2)
print("Time difference: ", seconds2-seconds)