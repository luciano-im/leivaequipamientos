def navMenu(request):
	urlpath = request.path.strip('/').split("/")
	navMenu = urlpath[0]
	
	return {'navMenu': navMenu}