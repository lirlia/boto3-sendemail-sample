import boto3

def send_mail(fr, to, title, body):
    '''
    fr : from address
    to : dest address
    title : title
    body : content
    '''

    client = boto3.client('ses')

    #
    # API reference
    # https://boto3.readthedocs.io/en/latest/reference/services/ses.html#SES.Client.send_email
    #
    response = client.send_email(
        Source=fr,
        Destination={'ToAddresses': [to]},
        Message={
            'Subject': {
                'Data': title
            },
            'Body': {
                'Html': {
                    'Data': body
                }
            }
        }
    )
def main():
    fr = 'from address'
    to = 'dest address'
    title = "title"
    body = "<html><body><p>content</p></body></html>"
    send_mail(fr, to, title, body)

if __name__ == '__main__':
    main()
