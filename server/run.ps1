param([Int32]$subject=1,[String]$date="$(Get-Date -format 'yyyy-MM-ddThh-mm-ss')",[String]$experiment="default") 

Set-Location $PSScriptRoot

./.venv/Scripts/activate

$logs = ".\logs\$($date)_Subject_$($subject)_Experiment_$($experiment).txt"

$Env:LOG_FILE = $logs
$Env:SUBJECT = $subject
$Env:DATE = $date
$Env:EXPERIMENT = $experiment
$Env:PYLSL_LIB = '.\liblsl\bin\lsl.dll'

python -m uvicorn main:app --host 0.0.0.0 --port 5001