#from flask import render_template, redirect, flash
from flask import render_template, redirect, flash, request, url_for, session
from app import app
from app.models.models import usuario, db
from werkzeug.security import generate_password_hash, check_password_hash
