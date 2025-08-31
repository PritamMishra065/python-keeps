import axios from 'axios';

const API_BASE_URL = 'https://web-production-3c0b4.up.railway.app/';

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Auth API service
export const authAPI = {
  setAuthToken: (token) => {
    api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
  },
  
  removeAuthToken: () => {
    delete api.defaults.headers.common['Authorization'];
  },

  register: async (username, password) => {
    const response = await api.post('/auth/', {
      username,
      password,
    });
    return response.data;
  },

  login: async (username, password) => {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    
    const response = await api.post('/auth/token', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  },

  getCurrentUser: async () => {
    const response = await api.get('/');
    return response.data;
  },
};

// Notes API service
export const notesAPI = {
  getNotes: async () => {
    const response = await api.get('/notes');
    return response.data;
  },

  createNote: async (title, content) => {
    const response = await api.post('/notes/save', {
      title,
      content,
    });
    return response.data;
  },

  deleteNote: async (noteId) => {
    const response = await api.delete(`/notes/delete/${noteId}`);
    return response.data;
  },

  deleteNoteByTitle: async (title) => {
    const response = await api.delete(`/notes/delete/${title}`);
    return response.data;
  },
};

export default api;
