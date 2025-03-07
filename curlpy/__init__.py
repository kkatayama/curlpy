import subprocess


def convertCurl(curl, verbose):
    src = '/Users/katayama/Documents/Fun/NodeJS/Convert_Curl_to_Python/curl_to_python.js'
    cmd = src + ' --curl ' + curl
    # cmd = '{} --curl "{}"'.format(src, curl)

    if verbose:
        print(f'src = {src}')
        print(' --curl ')
        print(f'cmd = {cmd}')

    #out = subprocess.check_output(cmd, shell=True).decode('utf-8')
    out = subprocess.run([src,'--curl', curl], shell=True, capture_output=True, text=True).stdout
    return out


