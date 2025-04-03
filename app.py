from flask import Flask, render_template, request
from pymongo import MongoClient
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# MongoDB connection
MONGO_URI = os.getenv("MONGODB_URI", "mongodb+srv://devanshi:test123@crm-cluster.8ixgwc0.mongodb.net/")
client = MongoClient(MONGO_URI)
db = client["CRM"]
collection = db["Email Conversations"]

unique_subject_words = set()
unique_senders = set()
unique_receivers = set()

for email in collection.find({}, {"subject": 1, "sender": 1, "receiver": 1}):
    # Extract subject words
    subject = email.get("subject", "")
    unique_subject_words.update(word.lower() for word in subject.split())
    
    # Extract senders and receivers
    if email.get("sender"):
        unique_senders.add(email["sender"].lower())
    if email.get("receiver"):
        unique_receivers.add(email["receiver"].lower())

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    user_query = ""

    if request.method == "POST":
        user_query = request.form.get("query")

        filters = {}

        # Filtering based on time of email sent - last week or last month
        if "last week" in user_query:
            week_ago = datetime.now() - timedelta(days=7)
            filters["timestamp"] = {"$gte": week_ago.isoformat()}

        if "last month" in user_query:
            today = datetime.now()
            first_day = datetime(today.year, today.month - 1, 1)
            last_day = datetime(today.year, today.month, 1)
            filters["timestamp"] = {
                "$gte": first_day.isoformat(),
                "$lt": last_day.isoformat()
            }

        # Subject filtering based on dynamic subject words
        for word in unique_subject_words:
            if word in user_query:
                filters["subject"] = {"$regex": word, "$options": "i"}
                break
        
        # Sender filtering
        if "sent by" in user_query or "sender" in user_query:
            for sender in unique_senders:
                if sender in user_query:
                    filters["sender"] = sender
                    break
        
        # Receiver filtering
        if "sent to" in user_query or "received by" in user_query or "receiver" in user_query:
            for receiver in unique_receivers:
                if receiver in user_query:
                    filters["receiver"] = receiver
                    break
        
        # Status filtering
        if "undelivered" in user_query or "not delivered" in user_query or "bounced" in user_query or "failed" in user_query:
            filters["status"] = {"$ne": "sent"}

        
        if "delivered" in user_query or "sent" in user_query or "successful" in user_query:
            filters["status"] = "sent"

        # Execute the query
        emails = collection.find(filters)

        for email in emails:
            results.append({
                "sender": email.get("sender"),
                "receiver": email.get("receiver"),
                "subject": email.get("subject"),
                "timestamp": email.get("timestamp"),
                "status": email.get("status")
            })

    return render_template("index.html", results=results, user_query=user_query)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
