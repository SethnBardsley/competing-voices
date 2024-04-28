import sys
from os import environ

from experiment import load_experiment
from routes import create_experiment_app

subject = environ["SUBJECT"]
experiment_date = environ["DATE"]
experiment_name = environ["EXPERIMENT"]

experiment = load_experiment(experiment_name)


with open(environ["LOG_FILE"], "a") as sys.stdout:
    app = create_experiment_app(experiment, subject, experiment_date)
