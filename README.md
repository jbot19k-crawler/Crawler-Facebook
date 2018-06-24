# Facebook Crawler
A simple [Facebook fanpage](https://www.facebook.com/) crawler.

## Environment:
- Windows 10 Home
- Python 3.6.4

## Preparation
- install python 3.x (32bit)
  1. download from https://www.python.org/downloads/
  2. remember to tick the checkbox "add python 3.x to path" and "pip"
- install requests, beautifulsoup, pandas
  1. run command line as administrator
  2. input instructions below
  ```
  pip3 install requests
  pip3 install beautifulsoup4
  pip3 install pandas
  ```
- install SQLiteStudio (optional)
  1. download from https://sqlitestudio.pl/index.rvt

## How to use
- Get the token
  1. Go to [Graph API Explorer](https://developers.facebook.com/tools/explorer/).
  2. Click "Get Token".
  3. Copy the token and paste it in the main.py.
  ```
  token = <your_token>
  ```
  > If token is expired, click "Get token" again.
- Get the fanpage id
  1. Paste the url of the fanpage right after "GET → / vx.x /"
  2. Click submit and it will show the id of the fanpage.
  3. Copy the id and paste it in the main.py.
- Set the number of page that will be crawled.
  ```
  page = <# of page>
  ```
- Run
  ```
  python main.py
  ```
---
If you have any problem, please [email](mailto:eugene87222@gmail.com) to me or open an issue.
