# 🎨 Vibe Coding Playground

A complete development environment with everything you need for creative coding! Includes vanilla JS, React, Python Flask, p5.js, Three.js, and audio/visual projects.

## 🚀 Quick Start

### 1. Install Node.js Dependencies

```bash
npm install
```

### 2. Install Python Dependencies (Optional)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

### 3. Start Development Server

```bash
npm run dev
```

Visit `http://localhost:3000` to see the main menu!

---

## 📁 Project Structure

```
vibe-coding-playground/
├── index.html              # Main landing page
├── styles/                 # Global styles
├── vanilla/               # Pure HTML/CSS/JS
├── react-app/             # React with Vite
├── p5-creative/           # p5.js creative coding
├── three-3d/              # Three.js 3D graphics
├── audio-visual/          # Tone.js audio/visual
├── python-flask/          # Python Flask backend
├── package.json           # Node dependencies
├── requirements.txt       # Python dependencies
└── vite.config.js         # Vite configuration
```

---

## 🎯 What's Included

### 🌟 Vanilla JavaScript

**Location:** `/vanilla/`

Pure HTML, CSS & JavaScript with no frameworks. Perfect for learning fundamentals.

**Features:**
- Interactive counter
- Random color generator
- Todo list with localStorage
- Clean, modern UI

**Start:**

```bash
npm run dev
# Navigate to http://localhost:3000/vanilla/
```

### ⚛️ React App

**Location:** `/react-app/`

Modern React setup with Vite for lightning-fast hot reload.

**Features:**
- Component-based architecture
- React hooks (useState, useEffect)
- Modular components
- Beautiful UI with animations

**Start:**

```bash
npm run dev
# Navigate to http://localhost:3000/react-app/
```

### 🎨 p5.js Creative Coding

**Location:** `/p5-creative/`

Generative art and interactive animations with p5.js.

**Features:**
- Particle system
- Animated spirals
- Wave patterns
- Interactive mouse controls

**Start:**

```bash
npm run dev
# Navigate to http://localhost:3000/p5-creative/
```

### 🎮 Three.js 3D Graphics

**Location:** `/three-3d/`

3D graphics and WebGL with Three.js.

**Features:**
- Multiple 3D shapes (cube, sphere, torus)
- Dynamic lighting
- Camera controls
- Smooth animations

**Start:**

```bash
npm run dev
# Navigate to http://localhost:3000/three-3d/
```

### 🎵 Audio/Visual with Tone.js

**Location:** `/audio-visual/`

Music and sound synthesis with Tone.js.

**Features:**
- Synthesizer keyboard
- Pattern sequencer
- Audio effects (reverb)
- Real-time visualizer

**Start:**

```bash
npm run dev
# Navigate to http://localhost:3000/audio-visual/
```

### 🐍 Python Flask Backend

**Location:** `/python-flask/`

REST API backend with Python Flask.

**Features:**
- RESTful API endpoints
- CORS enabled
- Todo CRUD operations
- Random quote generator

**Start:**

```bash
# Make sure virtual environment is activated
python python-flask/app.py
# Visit http://localhost:5000
```

**API Endpoints:**
- `GET /api/hello` - Test endpoint
- `GET /api/quote` - Random quote
- `GET /api/todos` - Get all todos
- `POST /api/todos` - Create todo
- `PUT /api/todos/:id` - Update todo
- `DELETE /api/todos/:id` - Delete todo

---

## 🛠️ Available Scripts

```bash
# Start main dev server (Vite)
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Format code with Prettier
npm run format

# Run p5.js project
npm run p5

# Run audio project
npm run audio
```

---

## 📦 Dependencies Installed

### JavaScript/Node.js

- **vite** - Lightning fast dev server
- **react** & **react-dom** - UI library
- **three** - 3D graphics
- **tone** - Audio synthesis
- **p5** - Creative coding
- **axios** - HTTP client
- **gsap** - Animation library
- **prettier** - Code formatter

### Python

- **Flask** - Web framework
- **flask-cors** - CORS support
- **requests** - HTTP library
- **python-dotenv** - Environment variables

---

## 💡 Tips for Vibe Coding

### 1. Hot Reload is Your Friend

All projects have hot reload enabled. Just save your file and see changes instantly!

### 2. Experiment Freely

Don't be afraid to break things! That's how you learn. Use Git to save your progress:

```bash
git init
git add .
git commit -m "Initial setup"
```

### 3. Use the Browser DevTools

- **Console** - See logs and errors
- **Elements** - Inspect HTML/CSS
- **Network** - Monitor API calls
- **Performance** - Profile your code

### 4. Keyboard Shortcuts

- `Ctrl/Cmd + S` - Save file (triggers hot reload)
- `Ctrl/Cmd + Shift + P` - Command palette
- `F12` - Open DevTools

### 5. Learn by Doing

- Start small, build up gradually
- Comment your code
- Break complex tasks into smaller steps
- Look up documentation when stuck

---

## 🎨 Customization Ideas

### Vanilla JS

- Add local storage to save counter state
- Create a dark mode toggle
- Build a calculator
- Make a weather app with API

### React

- Add routing with React Router
- Implement global state with Context
- Create a form with validation
- Build a mini dashboard

### p5.js

- Create your own generative art
- Add mouse/keyboard interactions
- Build a simple game
- Make data visualizations

### Three.js

- Add camera controls
- Create custom materials
- Load 3D models
- Build a mini game scene

### Audio/Visual

- Create custom melodies
- Add more effects (delay, distortion)
- Build a drum machine
- Make a music visualizer

### Flask

- Connect to a database (SQLite)
- Add user authentication
- Create a chat API
- Build a file upload system

---

## 🐛 Troubleshooting

### Port Already in Use

```bash
# Kill process on port 3000 (Windows)
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# Kill process on port 3000 (Mac/Linux)
lsof -ti:3000 | xargs kill
```

### Module Not Found

```bash
# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

### Python Module Not Found

```bash
# Make sure virtual environment is activated
# Then reinstall
pip install -r requirements.txt
```

### Vite Not Starting

```bash
# Clear cache
rm -rf node_modules/.vite
npm run dev
```

---

## 📚 Resources & Documentation

### JavaScript

- [MDN Web Docs](https://developer.mozilla.org/)
- [JavaScript.info](https://javascript.info/)

### React

- [React Docs](https://react.dev/)
- [React Hooks](https://react.dev/reference/react)

### p5.js

- [p5.js Reference](https://p5js.org/reference/)
- [p5.js Examples](https://p5js.org/examples/)

### Three.js

- [Three.js Docs](https://threejs.org/docs/)
- [Three.js Examples](https://threejs.org/examples/)

### Tone.js

- [Tone.js Docs](https://tonejs.github.io/)
- [Tone.js Examples](https://tonejs.github.io/examples/)

### Flask

- [Flask Docs](https://flask.palletsprojects.com/)
- [Flask Quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/)

---

## 🎉 Have Fun!

Remember: The best way to learn coding is by doing. Don't worry about making mistakes - they're part of the process!

**Happy vibe coding!** 🚀✨

---

## 📝 License

MIT - Feel free to use this for learning and personal projects!

