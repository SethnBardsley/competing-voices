import sys
from os import environ

# Import dependencues
from experiment import load_experiment
from routes import create_experiment_app

# Read in environment variables
subject = environ["SUBJECT"]
experiment_date = environ["DATE"]
experiment_name = environ["EXPERIMENT"]

experiment = load_experiment(experiment_name)

app = create_experiment_app(experiment, subject, experiment_date)
