# competing-voices

Please ensure python version is >3.12

## Client

### Installation

```
cd client
yarn install
```

### Running

```
./run.ps1
```

GOTO localhost:3000


## Server

### Installation

```
cd server
python3.11 -m venv .venv
./.venv/Scripts/activate
pip install -r requirements.txt
```


### Running

To run an experiment run the following command in the top level directory of the project on windows:

```
./run.ps1 -subject 1 -experiment "Test"
```