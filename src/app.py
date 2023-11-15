from flask import Flask


app = Flask(__name__, template_folder='../frontend/public')
#app.secret_key = getenv("TODO")