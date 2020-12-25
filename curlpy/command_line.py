#!/usr/bin/env python3
from . import convertCurl
import argparse
import os

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('curl_cmd', help='the curl command to convert into python syntax')
    ap.add_argument('-o', '--output', default=False, help='save output to file')
    args = ap.parse_args()

    curl_cmd = args.curl_cmd
    out_file = args.output

    py_src = convertCurl(curl_cmd)
    if not out_file:
        print(py_src)
    else:
        with open(os.path.abspath(out_file), 'w') as f:
            f.write(py_src)
