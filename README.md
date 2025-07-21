
## Prerequisites

- Python 3.11+
- Node.js 22+
- npm or yarn
- [WhoisXML API key](https://whois.whoisxmlapi.com/)

##  Setup Instructions

### 1. Clone the repository
git clone https://github.com/your-username/whois-lookup.git
cd whois-lookup

### 2. Create virtual environment
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

### 3. Create virtual environment
pip install -r requirements.txt

### 4. Set environment variables
#Create a .env file in backend/ and add:
WHOIS_API_KEY=at_Q6gTqKMRP3czcx7JHQ0ZNOP4u7Iym

### 5. Run migrations
python manage.py migrate

### 6. Start the server
python manage.py runserver

### 7. Install frontend dependencies
cd ../frontend
npm install

### 4. Set environment variables
#Create a .env file in frontend/ and add:
REACT_APP_API_URL=http://localhost:8000/api

### 8. Start the development server
npm start

