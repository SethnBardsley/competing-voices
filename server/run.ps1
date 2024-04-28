param([Int32]$subject=1,[String]$date="$(Get-Date -format 'yyyy-MM-ddThh-mm-ss')",[String]$experiment="default") 

Set-Location $PSScriptRoot

./.venv/Scripts/activate

$logs = ".\logs\$($date)_Subject_$($subject)_Experiment_$($experiment).txt"

python main.py $subject $date $experiment $logs