import socket
import datetime

s1 = socket.socket() #Default of socket() is AF_NET and TCP
s2 = socket.socket()

host = "time-e-g.nist.gov"
host2 = "time-b-b.nist.gov"
port = 37

s1.connect((host, port))
s2.connect((host2, port))

IP_s1 = socket.gethostbyname(host)
IP_s2 = socket.gethostbyname(host2)

response1 = s1.recv(4096) #Recieving time in seconds since Jan 1 1900,
response2 = s2.recv(4096) #Time is given as 32-bit unsigned int in binary format

seconds1 = int.from_bytes(response1, 'big') #Converting byte data to integer
conversion = datetime.timedelta(seconds=seconds1)
dateof = datetime.datetime(1900, 1 , 1) #Date of reference for TIME protocol

time_s1 = dateof + conversion

seconds2 = int.from_bytes(response2, 'big')
conversion2 = datetime.timedelta(seconds=seconds2)

time_s2 = dateof + conversion2

print("IP Adress of server 1: ", IP_s1)
print("IP Adress of server 2: ", IP_s2)
print("Date and Time for server 1: ", time_s1)
print("Date and Time for server 2: ", time_s2)
print("Time difference: ", seconds2-seconds1)
