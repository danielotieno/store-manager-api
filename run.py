""" This is an entry point to start our app. """
import os

from app.v2 import create_app

config = os.getenv('APP_SETTINGS')
app = create_app(config)

# The value of __name__  attribute is set to '__main__'  when module run as main program. Otherwise the value of __name__  is set to contain the name of the module.
if __name__ == "__main__":
    app.run(debug=True)
