import subprocess


def convertCurl(curl):
    src = '/Users/katayama/Documents/Fun/NodeJS/Convert_Curl_to_Python/curl_to_python.js'
    cmd = src + ' --curl ' + curl
    # cmd = '{} --curl "{}"'.format(src, curl)
    out = subprocess.check_output(cmd, shell=True).decode('utf-8')
    return out


