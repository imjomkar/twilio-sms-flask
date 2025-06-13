````markdown
# Twilio SMS Flask App

This is a simple Python Flask application that connects to Twilio to receive and respond to SMS messages. It's designed for developers who want a lightweight backend to test or build SMS bots, notification systems, or basic lead capture via SMS.

 

## Features

- Accepts incoming SMS messages using a Twilio webhook
- Sends automatic reply messages
- Simple Flask backend that's easy to modify
- Supports local testing via ngrok tunnel
- Can be tested using curl or a real phone number

 

## Requirements

- Python 3.7+
- A free Twilio trial account
- Flask
- Twilio Python SDK
- ngrok (for local tunneling)

 

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/imjomkar/twilio-sms-flask.git
cd twilio-sms-flask
````

### 2. Set up your environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, just run:

```bash
pip install flask twilio
pip freeze > requirements.txt
```

 

### 3. Start the Flask app

```bash
python app.py
```

The server will start on:

```
http://localhost:5000
```

 

### 4. Expose it to the internet using ngrok

```bash
ngrok http 5000
```

This will give you a public URL like:

```
https://abc123.ngrok.io
```

 

### 5. Configure Twilio webhook

1. Go to your Twilio Console
2. Open your phone number settings
3. Under **Messaging > A MESSAGE COMES IN**, set the webhook to:

```
https://abc123.ngrok.io/sms
```

4. Use `POST` as the method
5. Save

 

## Example curl Test

To simulate an incoming message without a phone:

```bash
curl -X POST https://abc123.ngrok.io/sms \
  -d "From=+1234567890" \
  -d "Body=Hello from curl"
```

 

## Sample Code: `app.py`

```python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=["POST"])
def sms_reply():
    incoming_msg = request.form.get("Body")
    sender = request.form.get("From")

    print(f"Message from {sender}: {incoming_msg}")

    resp = MessagingResponse()
    resp.message(f"You said: {incoming_msg}")
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```



## Notes

* This app is designed to work with your Twilio **trial** number (which will only send SMS to verified numbers).
* If you're using curl or Twilio's test tools, you can simulate SMS traffic easily without a phone.

 

## License

MIT License

 

## Author

[@imjomkar](https://github.com/imjomkar)
