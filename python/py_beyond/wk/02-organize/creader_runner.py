import creader

r = creader.Reader('test.txt')
print(r.read())
r = creader.Reader('test.gz')
print(r.read())