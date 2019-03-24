import sys
import ereader

r = ereader.Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()