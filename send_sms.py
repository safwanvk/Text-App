
"""
from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twilio

# Find these values at https://twilio.com/user/account
client = TwilioRestClient(account_sid, auth_token)

my_msg = "Your message goes here..."

message = client.messages.create(to=my_cell, from_=my_twilio,
                                     body=my_msg)
"""



from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC16ccd28fbb5cc9a92e4140355485c8fb"
# Your Auth Token from twilio.com/console
auth_token  = "a0e430627bfcc8eb61a54aeb1c0e5b90"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919497575968",
    from_="+12408396516",
    body="Hello!")

print(message.sid)
