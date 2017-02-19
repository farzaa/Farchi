from twilio.rest import TwilioRestClient


account_sid = "ACf9c87a70f6df3afa949cd02fab0d2b5f" # Your Account SID from www.twilio.com/console
auth_token  = "46f346035b4b588e0bbb6c20be3ca1de"  # Your Auth Token from www.twilio.com/console

def text_alerts():

    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(
        body="This is the Farchi Emergency System. The driver attched to this account is in peril. Ambulances are being called.",
        to="+19542572555",    # Replace with your phone number
        from_="+19542899840") # Replace with your Twilio number

    print(message.sid)

def call_ambulance():

    client = TwilioRestClient(account_sid, auth_token)

    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")

    print(resp)

    call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
    to="+19542572555",
    from_="+19542899840")