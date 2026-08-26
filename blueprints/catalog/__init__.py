from flask import Blueprint
import routes.py

catalog_bp = (Blueprint("catalog", __name__,template_folder="templates"))