function httpRequest(args) {
	var request = new XMLHttpRequest()
	function get(ks) {
		var ks = ks.split(' '), res = []; 
		for (var i=0; i<ks.length; i+=1) { res[i] = args[ks[i]]; delete args[ks[i]] }
		return ks.length==1 ? res[0] : res
	}
	for (var k in args) if (k in request) request[k] = get(k)
	var [method='get', url, async=true, usr=null, pwd=null, header, body=null] = get('method url async usr pwd header body')
	request.open(method, url, async, usr, pwd)
	if (header) for (var k in header) request.setRequestHeader(k, header[k])
	if (Object.keys(args).length) {
		switch (method) {
		case 'post':
			if (!body) body = new FormData()
			if (body instanceof FormData) {
				for (var k in args) body.append(k, args[k])
				break
			}
		default:
			var qs = ''; for (var k in args) qs += (qs ? '&' : '') + encodeURIComponent(k) + '=' + encodeURIComponent(args[k])
			url += (url.indexOf('?') == -1 ? '?' : '&') + qs
		}
	}
	var requestSend = request.send
	request.send = function () { requestSend.call(request, body) }
	return request
}
