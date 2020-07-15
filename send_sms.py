from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Your Account Sid"
# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+Your Cell Number",
    from_="+Your Twilio Number",
    body="Hello!")

print(message.sid)
