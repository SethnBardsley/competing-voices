param([Int32]$subject=1,[String]$date="$(Get-Date -format 'yyyy-MM-ddThh-mm-ss')",[String]$experiment="default") 

# Move to current directory
Set-Location $PSScriptRoot

# Activate venv
./.venv/Scripts/activate

# Setup ENV Variables for the runtime
$Env:SUBJECT = $subject
$Env:DATE = $date
$Env:EXPERIMENT = $experiment
$Env:PYLSL_LIB = '.\liblsl\bin\lsl.dll'

# Run the server
python -m uvicorn main:app --host 0.0.0.0 --port 5001