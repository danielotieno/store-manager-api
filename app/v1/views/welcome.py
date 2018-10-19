"""Welcome resource."""
from flask_restful import Resource
from flask import redirect


class Welcome(Resource):
    """Displays the app documentation"""

    def get(self):
        """Display the documentation of the api from postman"""
        return redirect("https://documenter.getpostman.com/view/616287/RWaRMjfq", code=302)
