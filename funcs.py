from ftplib import FTP
import getpass

g_ftp = 0
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
	with open(tokens[1], 'wb') as fp:
		print(g_ftp.retrbinary('RETR ' + tokens[1], fp.write))
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

	global g_ftp
	g_ftp = ftp
