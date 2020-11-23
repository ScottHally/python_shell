def parse_command(command):
	tokens = command.split(' ')
	print('Parsing command: ' + command)
	if(tokens[0].upper() == 'GET'):
		cmd_get(tokens)

def cmd_get(tokens):
	print('Processing GET command...')

	
