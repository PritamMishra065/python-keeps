# Python Keeps 🐍📝

A secure, full-stack notes application built with **FastAPI** (Python backend) and **React** (frontend).

## ✨ Features

- 🔐 **Secure Authentication** with JWT tokens and bcrypt password hashing
- 📝 **Notes Management** - Create, read, edit, and delete personal notes
- 🎨 **Modern React Frontend** with Tailwind CSS
- 🚀 **FastAPI Backend** with SQLAlchemy ORM
- 🔒 **User-specific data** - Notes are isolated per user
- 📱 **Responsive Design** - Works on all devices

## 🏗️ Architecture

```
python_keeps/
├── backend/                 # FastAPI Python backend
│   ├── main.py             # Main application entry point
│   ├── auth.py             # Authentication logic
│   ├── database.py         # Database configuration
│   ├── models.py           # SQLAlchemy models
│   └── schemas.py          # Pydantic schemas
├── frontend/               # React frontend
│   ├── src/                # React source code
│   ├── public/             # Static assets
│   └── package.json        # Node.js dependencies
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- MySQL/PostgreSQL database

### Backend Setup

1. **Navigate to project directory**:
   ```bash
   cd python_keeps
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database** in `database.py`

5. **Start the server**:
   ```bash
   python -m uvicorn main:app --reload
   ```

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start development server**:
   ```bash
   npm start
   ```

4. **Open browser** at `http://localhost:3000`

## 🔧 Configuration

### Database

Update the database connection string in `database.py`:

```python
DATABASE_URL = "mysql+pymysql://username:password@localhost/database_name"
```

### Environment Variables

Create a `.env` file for sensitive configuration:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-database-url
```

## 📚 API Endpoints

### Authentication
- `POST /auth/` - User registration
- `POST /auth/token` - User login

### Notes
- `GET /notes` - Get user's notes
- `POST /notes/save` - Create new note
- `DELETE /notes/delete/{id}` - Delete note by ID

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation
- **JWT** - JSON Web Tokens for authentication
- **bcrypt** - Password hashing
- **PyMySQL** - MySQL database adapter

### Frontend
- **React 18** - JavaScript library for building user interfaces
- **Tailwind CSS** - Utility-first CSS framework
- **React Router** - Client-side routing
- **Axios** - HTTP client
- **Lucide React** - Beautiful icons

## 🔒 Security Features

- **JWT Authentication** with secure token handling
- **Password Hashing** using bcrypt
- **User Isolation** - Users can only access their own notes
- **Protected Routes** - Authentication required for sensitive endpoints

## 📱 Responsive Design

The frontend is fully responsive and optimized for:
- Desktop computers
- Tablets
- Mobile phones
- All modern browsers

## 🚀 Deployment

### Backend Deployment

1. **Build and deploy** to your preferred hosting service
2. **Set environment variables** for production
3. **Configure database** for production use

### Frontend Deployment

1. **Build the React app**:
   ```bash
   npm run build
   ```

2. **Deploy** the `build/` folder to your hosting service

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI community for the excellent framework
- React team for the amazing frontend library
- Tailwind CSS for the beautiful styling system

## 📞 Support

If you have any questions or need help:
- Create an issue in this repository
- Check the documentation
- Review the code examples

---

**Happy coding! 🎉**
