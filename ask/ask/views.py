from django.http import HttpResponse

def page_test(request, *args, **kwargs):
	return HttpResponse('Ok')
