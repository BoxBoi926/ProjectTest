#Team Bord: Austin Ngan (Gerald), Thomas Yu (Perry), Mark Zhu (Bob the Third Jr), Roshani Shrestha (Pete)
#SoftDev
#P00

#from flask import Flask             #facilitate flask webserving
#from flask import render_template   #facilitate jinja templating
#from flask import request           #facilitate form submission
#from flask import session           #facilitate session

from flask import Flask, render_template, request, session, redirect #, url_for
import os
import loginpage

app = Flask(__name__)    #create Flask object
app.secret_key=os.urandom(32) #secret key for flask to work

# not working
@app.route("/blog1", methods=['GET', 'POST'])
def blogPage():
    return render_template('indivBlog.html')
        

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()