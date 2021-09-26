from flask import Flask
app = Flask(__name__)
import codeitsuisse.routes.square
import codeitsuisse.routes.asteroid
import codeitsuisse.routes.parasite
import codeitsuisse.routes.tictactoe
import codeitsuisse.routes.decoder
import codeitsuisse.routes.fixed_race
import codeitsuisse.routes.stock_hunter

