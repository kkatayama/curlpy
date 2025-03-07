#!/usr/bin/env python3
from . import convertCurl
import argparse
import shlex
import os


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-v', '--verbose', default=False, help='verbose mode')
    ap.add_argument('-o', '--output', default=False, help='save output to file')
    ap.add_argument('curl_cmd', nargs=argparse.REMAINDER, help='the curl command to convert into python syntax')
    args = ap.parse_args()

    verbose = args.verbose
    out_file = args.output
    curl_cmd = ''.join(args.curl_cmd) if len(args.curl_cmd) == 1 else ' '.join(args.curl_cmd)
    # curl_cmd = args.curl_cmd
    # if curl_cmd[0] == "'":
    #     curl_cmd = curl_cmd.replace('"', '\\"').replace("'", '"')

    py_src = convertCurl(curl_cmd, verbose)
    if not out_file:
        print(py_src)
    else:
        with open(os.path.abspath(out_file), 'w') as f:
            f.write(py_src)


if __name__ == '__main__':
    main()
