# cloud-function-caller.py
# Erik Fredericks, 2021

# This script calls a simple Cloud Function multiple times in parallel
# to demonstrate local to cloud interactions.

import multiprocessing as mpc
import requests
import pprint

url = 'YOUR-CLOUD-FUNCTION-URL'

def makeRequest(x):
  resp = requests.post(url, json={'message':'hey there cis680 [{0}]!'.format(x)})
  return "[{0}]: {1}".format(resp.status_code, resp.content)

if __name__ == "__main__":
  with mpc.Pool(5) as p:
    pprint.pprint(p.map(makeRequest, range(50)))

