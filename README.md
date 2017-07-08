# boto3-sendemail-sample

This repository is a sample of boto3 sendemail

## Requirements

* AWS knowledge
* aws configure
* AWS SES setting
* AWS IAM setting

## How to use

```python

$ pip install -r requirements.txt
$ vim main.py

change this area

  fr = 'from address'
  to = 'dest address'
  title = "title"
  body = "<html><body><p>content</p></body></html>"
  send_mail(fr, to, title, body)

$ python main.py

```
