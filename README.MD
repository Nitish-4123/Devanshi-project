# AI Copilot prototype
designed to answer queries from structured data in the Email Conversations module stored in MongoDB.

---

# Tech Stack
- Backend: Flask (Python)  
- Database:MongoDB  
- Frontend: HTML, CSS  

# Features
- Dynamic Querying: Filter emails by "date, sender, receiver, subject, or delivery status".  
- Flexible Matching: Automatically recognizes and matches individual words in subjects, senders, and receivers.  
- Intuitive Interface: Built with Flask, offering a simple web interface for querying.

## Future Enhancements
To expand the current prototype into a full-fledged "AI Copilot", the following features can be added:
- Natural Language Processing (NLP): To interpret complex queries and extract meaningful intent.  
- Keyword Expansion with Embeddings: For smarter matching of related terms.  
- Machine Learning Model: To classify and prioritize emails based on importance or sentiment.  

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Devanshi-Munjal/RUNO-Assignment.git
cd flask-mongodb-app
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure MongoDB Atlas
1. Create a **MongoDB Atlas account** ([https://www.mongodb.com/atlas](https://www.mongodb.com/atlas)).
2. Set up a **cluster** and create a **database** named `CRM`.
3. Get your **MongoDB connection string** and update it in `app.py`:
   ```python
   client = MongoClient("mongodb+srv://your_username:your_password@cluster0.mongodb.net/CRM?retryWrites=true&w=majority")
   ```

### 4️⃣ Insert Sample Data
```bash
python insert_data.py
```

### 5️⃣ Run the Application
```bash
python app.py
```
Open `http://127.0.0.1:5000/` in your browser.


