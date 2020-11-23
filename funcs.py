from ftplib import FTP
import getpass
import fileinput
import sys

g_ftp = None
def parse_command(command):
	tokens = command.split(' ')
	print('Parsing command: ' + command)

	if(tokens[0].upper() == 'GET'):
		ret = cmd_get(tokens)
	elif(tokens[0].upper() == 'CONNECT'):
		ret = connect()
	else:
		ret = -1
	return ret

def cmd_get(tokens):
	print('Processing GET command...')
	if(g_ftp is not None):
		if(len(tokens) > 1):
			with open(tokens[1], 'wb') as fp:
				try:
					print(g_ftp.retrbinary('RETR ' + tokens[1], fp.write))
				except:
					print("Could not find file specified")
		else:
			print("Usage: GET filename")
	else:
		print("Connect to a valid FTP server before issuing commands")
	return None

def connect():
	if(len(sys.argv) == 1):
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
			exit()
	else:
		filein = fileinput.FileInput(files=(sys.argv[1]))
		print('\nEnter host IP or address:')
		hostname = filein.readline()[:-1]
		print("Connecting to " + hostname + "...")
		#print(hostname)
		try:
			ftp = FTP(hostname)
		except:
			print("Could not connect to specified host. Quiting.")
			exit()

		username = filein.readline()
		passwd = getpass.getpass('Password:')

		try:
			login = ftp.login(username, passwd)
		except:
			print("Invalid credentials")
			exit()

		filein.close()
	print(login)

	global g_ftp
	g_ftp = ftp
