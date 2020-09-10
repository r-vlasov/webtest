def application(environ, start_response):
	status = '200 Ok'
	response_headers = [('Content-type', 'text/plain')]
						

	start_response(status, response_headers)
	return [(i + '\n').encode('utf-8') for i in environ['QUERY_STRING'].split('&')]
	
