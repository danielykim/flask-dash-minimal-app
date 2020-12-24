from waitress import serve
serve(wsgiapp, listen='*:8080')
