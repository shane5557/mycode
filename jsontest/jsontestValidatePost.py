#!/usr/bin/python3

import requests
import jsontestIP
import time

# define the URL we want to use
POSTURL = "http://validate.jsontest.com/"
IPURL = "http://ip.jsontest.com/"

def main():
    # test data to validate as legal json
    # when a POST json= is replaced by the KEY "json"
    # the key "json" is mapped to a VALUE of the json to test
    # because the test item is a string, we can include whitespaces
    mydata = {"json": "{'fruit': ['apple', 'pear'], 'vegetable': ['carrot']}" }
    t = time.localtime()
    print(t)
    # use requests library to send an HTTP POST
    resp = requests.post(POSTURL, data=mydata)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")

      # use requests library to send an HTTP GET
    resp = requests.get(IPURL)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "ip"
    print(f"The current WAN IP is --> {respjson['ip']}")

    with open("myservers.txt") as my_servers:
        print(my_servers.read())


if __name__ == "__main__":
    main()
