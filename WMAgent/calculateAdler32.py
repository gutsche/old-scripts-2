#!/usr/bin/env python

import sys

def readAdler32(filename):
    """
    _readAdler32_

    Get the adler32 checksum of a file. Return None on error

    Process line by line and adjust for known signed vs. unsigned issues
      http://docs.python.org/library/zlib.html

    """
    try:
        from zlib import adler32
        sum = 1L
        f = open(filename, 'rb')
        while True:
            line = f.readline(4096) #limit so binary files don't blow up
            if not line:
                break
            sum = adler32(line, sum)
        f.close()
        return '%x' % (sum & 0xffffffffL) # +ve values and convert to hex
    except StandardError, e:
        print('Error computing Adler32 checksum of %s. %s' % (filename, str(e)))

if __name__ == '__main__' :
    print readAdler32(sys.argv[1])

