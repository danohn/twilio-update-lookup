import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

incoming_phone_numbers = client.incoming_phone_numbers.list()

for number in incoming_phone_numbers:
    client.incoming_phone_numbers(number.sid).update(voice_caller_id_lookup=False)
    print(f"Disabling Voice Caller ID Lookup for {number.phone_number} - {number.sid}")
