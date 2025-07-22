# WHOIS Lookup Tool

A full-stack web application for performing WHOIS domain lookups with a modern React frontend and Django backend.

## 🚀 Features

- Fast and accurate WHOIS domain lookups
- Clean, responsive user interface
- RESTful API backend
- Real-time domain information retrieval
- Powered by WhoisXML API

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.11+**
- **Node.js 22+**
- **npm** or **yarn**
- **WhoisXML API key** - [Get your free API key here](https://whois.whoisxmlapi.com/)

## 🛠️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/whois-lookup.git
cd whois-lookup
```

### Step 2: Backend Setup

#### 2.1 Navigate to Backend Directory
```bash
cd backend
```

#### 2.2 Create Virtual Environment
```bash
python -m venv venv
```

#### 2.3 Activate Virtual Environment
```bash
# On Linux/macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

#### 2.4 Install Dependencies
```bash
pip install -r requirements.txt
```

#### 2.5 Configure Environment Variables
Create a `.env` file in the `backend/` directory:

```env
WHOIS_API_KEY=at_Q6gTqKMRP3czcx7JHQ0ZNOP4u7Iym
```

> ⚠️ **Important**: Replace the API key with your own WhoisXML API key

#### 2.6 Run Database Migrations
```bash
cd myproject
python manage.py migrate
```

#### 2.7 Start the Backend Server
```bash
python manage.py runserver
```

The backend API will be available at `http://localhost:8000`

### Step 3: Frontend Setup

#### 3.1 Navigate to Frontend Directory
```bash
cd ../frontend
```

#### 3.2 Install Dependencies
```bash
npm install
```

#### 3.3 Configure Environment Variables
Create a `.env` file in the `frontend/` directory:

```env
REACT_APP_API_URL=http://localhost:8000/api
```

#### 3.4 Start the Development Server
```bash
npm start
```

The frontend application will be available at `http://localhost:3000`

## 🌐 Usage

1. Open your web browser and navigate to `http://localhost:3000`
2. Enter a domain name in the search field
3. Click the lookup button to retrieve WHOIS information
4. View detailed domain information including registration details, nameservers, and more

## 📁 Project Structure

```
whois-lookup/
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env
│   └── ...
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── .env
│   └── ...
└── README.md
```

## 🔧 Configuration

### Backend Configuration

- **API Key**: Set your WhoisXML API key in `backend/.env`
- **Port**: Backend runs on port 8000 by default

### Frontend Configuration

- **API URL**: Configure the backend API URL in `frontend/.env`
- **Port**: Frontend runs on port 3000 by default

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/your-username/whois-lookup/issues) page
2. Create a new issue if your problem isn't already reported
3. Provide detailed information about your environment and the issue

