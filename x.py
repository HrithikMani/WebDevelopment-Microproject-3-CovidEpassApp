from twilio.rest import Client
ac_id = "AC3fd163862ee1582da8856cf01e8c5232"
auth = "fd1909be4570b0c79169a5ea8b254074"
client = Client(ac_id, auth)

body = "Your Epass has been Booked successfully, Here is your pass :\n\n xxxx \n\n Happy Journey!"

msg = client.messages.create(to="whatsapp:+919652608434",
                             from_="whatsapp:+14155238886", body=body)
print(msg.sid)
