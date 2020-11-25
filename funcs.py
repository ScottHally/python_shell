from ftplib import FTP
import getpass
import fileinput
import sys
import os
import stat
import time

g_ftp = None
def parse_command(command):
	tokens = command.split(' ')
	print('Parsing command: ' + command)

	if(tokens[0].upper() == 'GET'):
		ret = cmd_get(tokens)
	elif(tokens[0].upper() == 'CONNECT'):
		ret = connect()
	elif(tokens[0].upper() == 'PUT'):
		ret = cmd_put(tokens)
	elif(tokens[0].upper() == 'LS'):
		ret = cmd_ls(tokens)
	elif(tokens[0].upper() == 'LLS'):
		ret = cmd_lls(tokens)
	else:
		ret = -1
	return ret

def cmd_lls(tokens):
	print('Listing local directory contents')
	#print(os.scandir())
	print('Mode\t\tLastWriteTIme\t\tLength Name')
	print('----\t\t-------------\t\t------ ----')
	for file in os.scandir():
		#print(file.stat().st_mode+'\t\t'+str(file.stat().st_mtime))

		mode = file.stat().st_mode
		mod_time = file.stat().st_ctime
		print(stat.filemode(mode)+'\t', end='')
		strtime = time.gmtime(mod_time)
		print(time.strftime('%Y-%m-%d  %I:%M %p', strtime))
	return None

def cmd_ls(tokens):
	print('Listing remote directory contents...')
	if(g_ftp is not None):
		print(g_ftp.retrlines('LIST'))
	else:
		print('Not connected to an FTP server. No directory to list')

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

def cmd_put(tokens):
	print('Processing PUT command...')
	if(g_ftp is not None):
		if(len(tokens) > 1):
			try:
				with open(tokens[1], 'rb') as fp:
					try:
						print(g_ftp.storbinary('STOR ' + tokens[1], fp))
					except:
						print("Could not find file specified")
			except:
				print("No file \"" + tokens[1] + "\" found in local directory")
		else:
			print("Usage: PUT filename")
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
		print("Login script detected. Using credentials...")
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
