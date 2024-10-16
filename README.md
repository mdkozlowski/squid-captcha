# Squid CAPTCHA

- In each step, select the row of squids that ""feels"" the most random
- Real humans usually end up picking them correctly
- Just go by vibes
- Get 3 or more correct to pass

## Usage

Open `localhost:5000`


## Installation

### Python virtualenv

Requires `python>=3.10, <3.14`

```commandline
python -m pip install -r requirements.txt
python app.py
```

or

### Docker

```commandline
docker build -t squid-captcha .
docker run --rm -it -p 5000:5000 --name squid-captcha squid-captcha
```

or 

### Pyinstaller binary
There's no way this works anywhere other than on my own PC but apparently there's supposed to be a windows binary
```commandline
./dist/app/app.exe
```