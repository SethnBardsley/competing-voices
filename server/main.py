import uvicorn
from sys import argv
from os import environ

if __name__ == "__main__":
    subject, date, experiment, log_file = argv[1:5]
    environ["SUBJECT"] = subject
    environ["DATE"] = date
    environ["EXPERIMENT"] = experiment
    environ["LOG_FILE"] = log_file

    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)
