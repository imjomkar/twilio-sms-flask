from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=["POST"])
def sms_reply():
    print("Webhook was hit!")

    incoming_msg = request.form.get("Body")
    sender = request.form.get("From")

    print(f"Message from {sender}: {incoming_msg}")

    resp = MessagingResponse()
    resp.message(f"You said: {incoming_msg}")
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)
