from ftplib import FTP
import getpass

def parse_command(command):
	tokens = command.split(' ')
	print('Parsing command: ' + command)

	if(tokens[0].upper() == 'GET'):
		ret = cmd_get(tokens)
	elif(tokens[0].upper() == 'CONNECT'):
		ret = connect()
	return ret

def cmd_get(tokens):
	print('Processing GET command...')
	return None

def connect():
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
	return ftp
