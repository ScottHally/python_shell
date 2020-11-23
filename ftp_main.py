from ftplib import FTP
import getpass
import funcs
#test
#ftp = FTP('10.0.0.235') 
#my local IP, using windows FTP server

print("Scott Haligowski")
print("My own FTP client")
print("2020")
print('v0.1.2')




#test
#with open('hello','wb') as fp:
#	ftp.retrbinary('RETR hello',fp.write)
command = input('>>>')

while(command != 'quit'):
	funcs.parse_command(command)
	command = input('>>>')
if(funcs.ftp is not None):
	funcs.ftp.quit()

