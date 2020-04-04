import os

from creader.compressed import bzipped, gzipped

extension_map = {
    '.bz2':bzipped.opener,
    '.gz':gzipped.opener
}


class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        ##factory pattern
        ## wil return a built-in open  if extension is not in the map
        opener = extension_map.get(extension,open)
        self.f = opener(filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()



