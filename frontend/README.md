# Python Keeps - React Frontend

A modern, responsive React frontend for the Python Keeps notes application. Built with React 18, Tailwind CSS, and modern web technologies.

## Features

- 🔐 **User Authentication**: Secure login and registration with JWT tokens
- 📝 **Notes Management**: Create, read, edit, and delete personal notes
- 🎨 **Modern UI**: Beautiful, responsive design with Tailwind CSS
- 🔒 **Protected Routes**: Secure access to authenticated features
- 📱 **Mobile Responsive**: Optimized for all device sizes
- ⚡ **Fast Performance**: Built with React 18 and optimized rendering

## Tech Stack

- **Frontend Framework**: React 18
- **Styling**: Tailwind CSS
- **Routing**: React Router DOM
- **HTTP Client**: Axios
- **Icons**: Lucide React
- **State Management**: React Context API
- **Build Tool**: Create React App

## Prerequisites

- Node.js 16+ and npm
- Python Keeps backend running on `http://localhost:8000`

## Installation

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm start
   ```

4. **Open your browser** and navigate to `http://localhost:3000`

## Project Structure

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── Dashboard.js      # Main notes management interface
│   │   ├── Login.js          # User login form
│   │   ├── Navbar.js         # Navigation bar
│   │   └── Register.js       # User registration form
│   ├── contexts/
│   │   └── AuthContext.js    # Authentication state management
│   ├── services/
│   │   └── api.js           # API communication layer
│   ├── App.js               # Main application component
│   ├── index.js             # Application entry point
│   └── index.css            # Global styles with Tailwind
├── package.json
├── tailwind.config.js
└── postcss.config.js
```

## API Integration

The frontend communicates with your FastAPI backend through the following endpoints:

- **Authentication**:
  - `POST /auth/` - User registration
  - `POST /auth/token` - User login
  - `GET /` - Get current user info

- **Notes**:
  - `GET /notes` - Fetch user's notes
  - `POST /notes/save` - Create new note
  - `DELETE /notes/delete/{note_id}` - Delete note by ID
  - `DELETE /notes/delete/{title}` - Delete note by title

## Key Components

### AuthContext
Manages authentication state, JWT tokens, and user information across the application.

### Dashboard
The main interface for managing notes, including:
- Display notes in a responsive grid
- Create new notes with inline forms
- Edit existing notes
- Delete notes with confirmation

### Login/Register
Secure authentication forms with:
- Form validation
- Error handling
- Password visibility toggle
- Responsive design

## Styling

The application uses Tailwind CSS for styling with:
- Custom color scheme (primary blues)
- Responsive grid layouts
- Hover effects and transitions
- Consistent spacing and typography
- Mobile-first responsive design

## Development

### Available Scripts

- `npm start` - Start development server
- `npm build` - Build for production
- `npm test` - Run tests
- `npm eject` - Eject from Create React App

### Environment Variables

The API base URL is configured in `src/services/api.js`. You can modify the `API_BASE_URL` constant to point to your backend server.

## Deployment

1. **Build the application**:
   ```bash
   npm run build
   ```

2. **Serve the build folder** using any static file server (nginx, Apache, etc.)

3. **Update the API base URL** in production to point to your deployed backend

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is part of the Python Keeps application suite.

## Support

For issues or questions, please check the main Python Keeps repository or create an issue there.
