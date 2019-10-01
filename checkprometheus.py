#
# importing the requests library
import requests
import argparse
import sys

def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d myprometheus.com")
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-d', '--domain', help="the url of prometheus domain",type=str, required=True)
    parser.add_argument('-t', '--timeout', help="timeout of reponse",type=int, default=30,required=False)
    return parser.parse_args()
args = parse_args()

# defining the api-endpoint
PROMETHEUS_ENDPOINT = args.domain
TIMEOUT = args.timeout
RELOAD = '/-/reload'
URL = PROMETHEUS_ENDPOINT + RELOAD
def main ():
    r = requests.post(url = PROMETHEUS_ENDPOINT, timeout=TIMEOUT)
    print (r.status_code)
    if r.status_code == 200:
        print ('Your setting is correct! ')
        exit()
    else:
        print ('Check your setting! ')



if __name__ == '__main__':
    main()
