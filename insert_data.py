import json
from pymongo import MongoClient

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://devanshi:test123@crm-cluster.8ixgwc0.mongodb.net/")
db = client["CRM"] 
collection = db["Email Conversations"]  

# Load JSON file
with open("e:/misc/runo chatbot/Devanshi/emails_sample.json", "r") as file:
    data = json.load(file)

# Insert data into MongoDB
collection.insert_many(data)

print("✅ Sample data inserted successfully!")
