from ftplib import FTP
import getpass
#test
#ftp = FTP('10.0.0.235') 
#my local IP, using windows FTP server

print("Scott Haligowski")
print("My own FTP client")
print("2020")
print('v0.1.1')

print('\nEnter host IP or address:')
hostname = input()
print("Connecting to " + hostname + "...")
try:
	ftp = FTP(hostname)
except:
	print("Could not connect to specified host. Quiting.")
	exit()

username = input("Username:")
passwd = getpass.getpass('Password:')

try:
	login = ftp.login(username, passwd)
except:
	print("Invalid credentials")
print(login)

#test
#with open('hello','wb') as fp:
#	ftp.retrbinary('RETR hello',fp.write)
command = input('>>>')
while(command != 'quit'):
	command = input('>>>')
ftp.quit()

