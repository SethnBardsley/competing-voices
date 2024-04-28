param([Int32]$subject=1,[String]$date="$(Get-Date -format 'yyyy-MM-ddThh-mm-ss')",[String]$experiment="default") 

"Experiment $experiment on $date with subject $subject started"

$DIR = $PWD 
Start-Job -ScriptBlock {
    Invoke-Expression "$using:DIR\client\run.ps1 > $using:DIR\client\logs.txt"
}


Start-Job -ScriptBlock {
    Invoke-Expression "$using:DIR\server\run.ps1 -subject $using:subject -date $using:date -experiment $using:experiment"
}


While (Get-Job -State Running) {
    Start-Sleep -Seconds 1
}

Get-Job | Receive-Job