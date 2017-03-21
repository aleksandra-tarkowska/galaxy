from __future__ import print_function

import sys

import requests

def stop_err( msg ):
    sys.stderr.write( msg )
    sys.exit()


def __main__():
    image_id = sys.argv[1]

    url = "http://idr-demo.openmicroscopy.org/webclient/api/annotations/"

    payload = {"type": "map", "image": image_id}
    r = requests.get(url, params=payload)
    print(r)
    print(r.json())

if __name__ == "__main__":
    __main__()
