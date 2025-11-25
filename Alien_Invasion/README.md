# Alien Invasion

**Alien Invasion** is a classic arcade-style shooter built in Python using the Pygame library.  
You control a ship at the bottom of the screen and must shoot down descending alien fleets before they reach the bottom or collide with your ship.

This project is based on the exercises in *Python Crash Course* (Eric Matthes) and is a great introduction to game development.

---

## 🚀 Features

- Player-controlled ship that moves left and right  
- Projectile bullets fired upward  
- Waves of aliens arranged in a dynamic fleet  
- Increasing difficulty as levels progress  
- Collision detection between bullets and aliens  
- Tracking score, level, and remaining ships  
- Ability to restart after a game over  
- Clean, modular, object-oriented architecture  

---

## 📦 Installation

### 1. Install Python 3

Use Python 3.10+ for best compatibility.

Check your version:

```bash
python3 --version
```
2. Create and activate a virtual environment (recommended)
Copy code
```bash
python3 -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```
3. Install dependencies
```bash
pip install pygame-ce
```
(pygame-ce is a community edition with better macOS compatibility.)

▶️ Running the Game
From the project root directory:

```bash
python alien_invasion.py
```
A game window should open immediately.
### Controls

| Key   | Action                               |
| ----- | ------------------------------------ |
| ← / → | Move ship left/right                 |
| SPACE | Fire bullet                          |
| Q     | Quit game                            |
| ESC   | Also quit depending on configuration |


🎮 How the Game Works
The main game loop runs continuously:
1. Handle events
     - Keyboard input
     - Mouse clicks
     - Window close events

2. Update game objects

    - Move the ship
     - Move bullets
     - Update the fleet
    - Detect collisions and game over conditions

3. Draw everything
    - Clear the screen
    - Draw the ship, bullets, aliens, and UI
    - Update the display

This loop runs ~60 times per second.