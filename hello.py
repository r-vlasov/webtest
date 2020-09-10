from cgi import parse_qsl

def application(environ, start_response):
	d = parse_qsl(environ['QUERY_STRING'])
	output = '';
	if environ['REQUEST_METHOD'] == 'GET':
		for ch in d:
			output += ('='.join(ch))
			output += ('\n')
	output_len = sum(len(line) for line in output)	
	status = '200 Ok'
	response_headers = [('Content-type', 'text/plain'),
						('Content-Length', str(output_len))]

	start_response(status, response_headers)
	return [output.encode('utf-8')]
	
