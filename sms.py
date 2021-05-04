from twilio.rest import Client 
 
account_sid = 'CODE' 
auth_token = 'CODE' 
client = Client(account_sid, auth_token) 
 
message = client.messages \
                .create(
                     body="ce faci?",
                     from_='+15017122661',
                     to='+15558675310'
                 )
 
print(message.sid)