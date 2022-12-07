#!/usr/bin/python3

from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from flask import render_template

#app = Flask(__name__)

#app.secret_key= "random random RANDOM!"

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]



#@app.route("/<str:name>")
def create_list(groups):
    return render_template('template.txt',name = groups)

def main():
    create_list(groups)

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port= 2224)
    main()
    


