#!/usr/bin/python

# Copyright (C) 2011 by Andrew Turley (aturley@acm.org)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import json
import sys

def usage(name):
    print "%s --KEY1 VALUE1 --KEY2 VALUE2 ..."%(name)
    sys.exit(0)

def main():
    group = lambda t, n: zip(*[t[i::n] for i in range(n)])
    obj = {}
    for arg in group(sys.argv[1:], 2):
        v = arg[1]
        try:
            v = float(v)
        except:
            pass
        obj[arg[0][2:]] = v
    print json.dumps(obj)

if __name__ == "__main__":
    if len(sys.argv) == 1 or (len(sys.argv[1:]) % 2) == 1:
        usage(sys.argv[0])
    main()
