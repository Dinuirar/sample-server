from flask import Flask, escape, request

app = Flask(__name__)

from src import server
