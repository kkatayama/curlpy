#!/usr/bin/env python3
from . import convertCurl
import argparse
import os


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('curl_cmd', help='the curl command to convert into python syntax')
    ap.add_argument('-o', '--output', default=False, help='save output to file')
    args = ap.parse_args()

    out_file = args.output
    curl_cmd = args.curl_cmd
    if curl_cmd[0] == "'":
        curl_cmd = curl_cmd.replace('"', '\\"').replace("'", '"')

    py_src = convertCurl(curl_cmd)
    if not out_file:
        print(py_src)
    else:
        with open(os.path.abspath(out_file), 'w') as f:
            f.write(py_src)


if __name__ == '__main__':
    main()
