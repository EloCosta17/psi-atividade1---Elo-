from flask import Blueprint
import routes.py

reviews_bp = (Blueprint("reviews", __name__,template_folder="templates"))