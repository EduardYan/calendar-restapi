# Calendars Restapi.

__This is a retapi with python-flask, for get calendars of year, months and holidays of months.__

## Installation.

```bash
git clone https://github.com/EduardYan/calendars-restapi.git
cd calendars-restapi/
```

### Dependencies.

Install with pip or other as well, with the requeirements file.

```bash
pip3 install -r requirements.txt
```

## Run.

```bash
python3 index.py
```

## Routes.

__For get a month of a year.__
* /year/month

The month is a numeric values as 1, 2, 3 or January, February, December, etc.

-------------------------------

__For get a year complete.__
* /year/all

-------------------------------

__For get holidays of a month.__
* /get-holidays/month
