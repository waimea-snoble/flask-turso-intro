from flask          import Flask
from flask          import render_template
from libsql_client  import create_client_sync
from dotenv         import load_dotenv
import os

# Load Turso environment variables from the .env file
load_dotenv()
TURSO_URL = os.getenv("TURSO_URL")
TURSO_KEY = os.getenv("TURSO_KEY")

# Create the Flask app
app = Flask(__name__)


# Track the DB connection
client = None

#-----------------------------------------------------------
# Connect to the Turso DB and return the connection
#-----------------------------------------------------------
def connect_db():
    global client
    # Not connected yet?
    if client == None:
        # No, so make the connection to Turso
        client = create_client_sync(url=TURSO_URL, auth_token=TURSO_KEY)
    # Pass the connection back
    return client


#-----------------------------------------------------------
# Home Page with list of things
#-----------------------------------------------------------
@app.get("/")
def home():

    # TODO: Switch from SupaBase to Turso queries!
    # response = supabase.table("things").select().order("name").execute()
    # records = response.data

    return render_template("pages/home.jinja", things=???)


#-----------------------------------------------------------
# Thing details page
#-----------------------------------------------------------
@app.get("/thing/<int:id>")
def showThing(id):

    return render_template("pages/thing.jinja", thing=???)


#-----------------------------------------------------------
# Thing deletion
#-----------------------------------------------------------
@app.get("/delete/<int:id>")
def deleteThing(id):

    # TODO!!!!

    return


#-----------------------------------------------------------
# 404 error handler
#-----------------------------------------------------------
@app.errorhandler(404)
def notFound(error):
    return render_template("pages/404.jinja")
