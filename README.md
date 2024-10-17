# Squid CAPTCHA

- In each step, select the row of squids that ""feels"" the most random
- Real humans usually end up picking them correctly
- Just go by vibes
- Get 3 or more correct to pass

## Usage

Open `localhost:5000`


## Installation

### Docker
Build locally:
```commandline
docker build -t squid-captcha:1.0 .
```
Pre-built image:
```commandline
docker pull naarkie/squid-captcha:1.0
```

```commandline
docker run --rm -it -p 5000:5000 --name squid-captcha squid-captcha:1.0
```
------
or,
### Python virtualenv

Requires `python>=3.10, <3.14`

```commandline
pip install --no-cache-dir -r requirements.txt
python app.py
```
------
or,

### Pyinstaller binary
There's no way this works anywhere other than on my own PC but apparently there's supposed to be a prebuilt windows binary
```commandline
.\dist\app\app.exe
```
Creating a new pyinstaller binary from a working local copy:
```commandline
 pyinstaller --add-data "templates;templates" --add-data "static;static" --add-data "make_captcha;make_captcha" --clean .\app.py
```