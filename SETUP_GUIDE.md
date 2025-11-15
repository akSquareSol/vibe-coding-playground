# 🎯 Setup Guide - Get Started in 5 Minutes!

## ⚡ Quick Setup (TL;DR)

```bash
# 1. Install Node packages
npm install

# 2. Start dev server
npm run dev

# 3. Open browser to http://localhost:3000
```

That's it! 🎉

---

## 📋 Detailed Setup Instructions

### Step 1: Check Prerequisites

Make sure you have these installed:

- **Node.js** (v18+) - [Download here](https://nodejs.org/)
- **Python** (3.8+, optional for Flask) - [Download here](https://www.python.org/)
- **Git** (optional) - [Download here](https://git-scm.com/)

**Check versions:**

```bash
node --version
npm --version
python --version
```

### Step 2: Install JavaScript Dependencies

Open your terminal in the project folder and run:

```bash
npm install
```

This will install:
- ✅ Vite (dev server)
- ✅ React & React DOM
- ✅ Three.js (3D graphics)
- ✅ Tone.js (audio)
- ✅ p5.js (creative coding)
- ✅ Other utilities

**Wait for it to finish** (usually takes 1-2 minutes).

### Step 3: Start the Development Server

```bash
npm run dev
```

You should see:

```
VITE v5.x.x  ready in XXX ms

➜  Local:   http://localhost:3000/
➜  Network: use --host to expose
```

### Step 4: Open in Browser

Open your browser and go to: **http://localhost:3000**

You'll see a beautiful landing page with all the projects! 🎨

---

## 🐍 Optional: Python Flask Setup

If you want to use the Python Flask backend:

### Windows:

```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# Install packages
pip install -r requirements.txt

# Run Flask server
python python-flask/app.py
```

### Mac/Linux:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install packages
pip install -r requirements.txt

# Run Flask server
python python-flask/app.py
```

Flask will run on: **http://localhost:5000**

---

## 🎮 Testing Each Project

### 1. Vanilla JavaScript

- Click "Vanilla JS" on the homepage
- Or visit: `http://localhost:3000/vanilla/`
- Try the counter, color generator, and todo list!

### 2. React App

- Click "React" on the homepage
- Or visit: `http://localhost:3000/react-app/`
- Interact with the React components!

### 3. p5.js Creative

- Click "p5.js Creative" on the homepage
- Or visit: `http://localhost:3000/p5-creative/`
- Try the different visual effects!

### 4. Three.js 3D

- Click "Three.js 3D" on the homepage
- Or visit: `http://localhost:3000/three-3d/`
- Switch between different 3D shapes!

### 5. Audio/Visual

- Click "Audio/Visual" on the homepage
- Or visit: `http://localhost:3000/audio-visual/`
- Make some music!

### 6. Python Flask

- Start the Flask server (see Python setup above)
- Visit: `http://localhost:5000`
- Test the API endpoints!

---

## ❓ Common Issues & Solutions

### Issue: "npm: command not found"

**Solution:** Install Node.js from [nodejs.org](https://nodejs.org/)

### Issue: "Port 3000 is already in use"

**Solution:**

```bash
# Windows - Kill process on port 3000
netstat -ano | findstr :3000
taskkill /PID <PID_NUMBER> /F

# Mac/Linux - Kill process on port 3000
lsof -ti:3000 | xargs kill -9
```

Or use a different port:

```bash
npm run dev -- --port 3001
```

### Issue: "Module not found" errors

**Solution:**

```bash
# Delete and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Issue: Python "venv not found"

**Solution:** Make sure you're using the right Python command:

```bash
# Try python3 instead of python
python3 -m venv venv

# Or use py on Windows
py -m venv venv
```

### Issue: "Failed to fetch" in browser

**Solution:**
- Make sure the dev server is running (`npm run dev`)
- Check that you're using the correct URL
- Try clearing browser cache (Ctrl+Shift+R or Cmd+Shift+R)

### Issue: Hot reload not working

**Solution:**

```bash
# Stop the server (Ctrl+C)
# Clear Vite cache
rm -rf node_modules/.vite
# Restart
npm run dev
```

---

## 🎨 Editor Setup (Optional but Recommended)

### VS Code Extensions

Install these for the best experience:

1. **ES7+ React/Redux/React-Native snippets** - React shortcuts
2. **Prettier - Code formatter** - Auto-format on save
3. **ESLint** - Catch errors as you type
4. **Live Server** - Alternative dev server
5. **Path Intellisense** - File path autocomplete

### Enable Format on Save

1. Open VS Code Settings (Ctrl/Cmd + ,)
2. Search for "format on save"
3. Check the box ✅

Now your code will auto-format when you save!

---

## 🚀 Next Steps

Once everything is set up:

1. **Explore each project** - Click around and see what they do
2. **Read the code** - Open the files and see how things work
3. **Make changes** - Edit something and see it update instantly!
4. **Build something new** - Use these as templates for your own ideas

---

## 📱 Quick Reference

### Start Development

```bash
npm run dev
```

### Stop Server

Press `Ctrl + C` in the terminal

### Restart Server

```bash
# Stop first (Ctrl+C), then:
npm run dev
```

### Format Code

```bash
npm run format
```

### Build for Production

```bash
npm run build
```

---

## 🎉 You're All Set!

Everything should be working now! If you run into any issues:

1. Check the error message carefully
2. Look in the troubleshooting section above
3. Search online (Stack Overflow is your friend!)
4. Read the full README.md for more details

**Happy coding!** 🚀✨

