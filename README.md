🚀 MASIKA- The Generation That Talks Period.

MASIKA is a Flask-based web application designed to collect, store, and manage user feedback efficiently.
It powers the contact and interaction layer of the MASIKA platform by capturing user inputs and storing them in a structured Excel database.

📌 Features
📩 Contact Form Handling – Collects user details and messages
📊 Excel Data Storage – Stores all submissions in a structured .xlsx file
🕒 Timestamp Logging – Automatically records date & time of each entry
🌐 Multi-page Routing – Includes team pages and additional routes
📱 PWA Support – Serves manifest.json for progressive web app capability
⚡ Lightweight & Scalable – Built using Flask with minimal dependencies
🧠 Tech Stack
Backend: Flask (Python)
Data Handling: Pandas
Storage: Excel (openpyxl)
Frontend: HTML (Jinja Templates)
📂 Project Structure
MASIKA/
│
├── app.py
├── masika_feedback.xlsx
├── templates/
│   ├── index.html
│   ├── comingsoon.html
│   ├── tapaswinipadhi.html
│   ├── vishmapasayat.html
│   ├── amritasaini.html
│   └── ...
│
├── static/
│   └── manifest.json
│
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/masika.git
cd masika
2️⃣ Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install flask pandas openpyxl
4️⃣ Run the application
python app.py

👉 App will run on:

http://127.0.0.1:5000/
🔄 How It Works
User submits the contact form
Flask captures form data via /contact route
Data is structured with timestamp
Stored in masika_feedback.xlsx using Pandas
Success response is returned to UI
🧾 Data Stored

Each submission includes:

Date & Time
Name (Identity)
Email / Signal
Contact Frequency
Message (Transmission Data)
⚠️ Important Notes
❗ Ensure masika_feedback.xlsx is closed before submitting data
⚠️ Running in debug=True is only for development
🔒 Add validation & security (CSRF, sanitization) for production
🔮 Future Improvements
Database integration (PostgreSQL / MongoDB)
Authentication system
Admin dashboard for viewing feedback
API-based architecture
AI-based feedback analysis
👨‍💻 Team
Vishma Pasayat
Tapaswini Padhi
Amrita Saini
Paramjeet Singh
Dr. Bikramaditya Das
📜 License

This project is for educational and research purposes.
For commercial usage, please contact the authors.

🌟 Contribution

Contributions, issues, and feature requests are welcome!
