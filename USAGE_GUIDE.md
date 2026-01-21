# Usage Guide / מדריך שימוש

## For Users with Dyslexia / למשתמשים עם דיסלקציה

This guide is written in simple, clear language to help you use the Cybersecurity Learning Assistant.

---

## What Does This Assistant Do? / מה העוזר הזה עושה?

The assistant helps you learn cybersecurity by:

1. **Writing for you** - You don't need to take notes yourself! Just tell the assistant what you learned, and it will write and organize the notes for you.

2. **Creating lessons** - Get clear, structured lessons on any cybersecurity topic.

3. **Making summaries** - The assistant can summarize complex information into simple points.

4. **Finding videos** - Search YouTube for educational videos in Hebrew, Arabic, or English.

5. **Tracking progress** - See how much you've learned and how many notes you've taken.

---

## How to Use / איך להשתמש

### Option 1: Interactive Mode (Easiest!) / מצב אינטראקטיבי (הכי קל!)

This is the easiest way to use the assistant. Just run:

```bash
python3 interactive_assistant.py
```

Then follow the menu:
- Press `1` to generate a lesson
- Press `2` to have the assistant write notes for you
- Press `3` to create a summary
- Press `4` to search YouTube videos
- Press `5` to see all your notes
- Press `6` to check your progress
- Press `7` to save your work
- Press `8` to load previous work
- Press `9` to exit

### Option 2: As a Python Module / כמודול פייתון

If you know Python, you can use it in your own programs:

```python
from cyber_learning_assistant import CyberSecurityLearningAssistant

# Create assistant
assistant = CyberSecurityLearningAssistant(user_name="Mahmoud")

# Example 1: Generate a lesson
lesson = assistant.generate_lesson("information_security")
print(lesson)

# Example 2: Have the assistant write notes for you
note = assistant.write_for_me(
    "What I learned today",
    "Firewalls are like guards for your network. They check who can come in and go out."
)
print(note)

# Example 3: Create a summary
summary = assistant.create_summary(
    "Today I learned about encryption. It's like a secret code that protects data.",
    "Day 1: Encryption"
)
print(summary)

# Example 4: Search YouTube
videos = assistant.search_youtube_resources("network_security")
for video in videos[:3]:
    print(video['url'])

# Example 5: Check progress
progress = assistant.get_learning_progress()
print(progress)

# Example 6: Save your work
assistant.save_session("my_learning.json")
```

---

## Learning Topics / נושאי למידה

### 1. Information Security / אבטחת מידע

Learn about:
- How to protect information
- Passwords and user accounts
- Encryption (secret codes)
- Who can access what

To start: `assistant.generate_lesson("information_security")`

### 2. Network Security / אבטחת רשתות

Learn about:
- Firewalls (network guards)
- VPN (secure connections)
- Protecting WiFi
- Network monitoring

To start: `assistant.generate_lesson("network_security")`

### 3. Cyber Threats / איומי סייבר

Learn about:
- Computer viruses
- Phishing (fake emails)
- Hackers and attacks
- Ransomware

To start: `assistant.generate_lesson("cyber_threats")`

### 4. Application Security / אבטחת יישומים

Learn about:
- Secure programming
- Web application security
- Common vulnerabilities
- Safe coding

To start: `assistant.generate_lesson("application_security")`

### 5. Cryptography / קריפטוגרפיה

Learn about:
- Encryption methods
- Secret codes
- Digital signatures
- Secure communication

To start: `assistant.generate_lesson("cryptography")`

---

## Tips for Success / טיפים להצלחה

### 1. Take It Slow / לאט לאט
- Learn one topic at a time
- Don't rush
- The assistant is here to help you go at your own pace

### 2. Use the Note-Taking Feature / השתמש בכתיבת הערות
- Let the assistant write for you
- Just tell it what you learned in your own words
- It will organize everything nicely

### 3. Watch Videos / צפה בסרטונים
- Use the YouTube search feature
- Videos are great for visual learning
- Available in multiple languages

### 4. Review Your Progress / בדוק את ההתקדמות
- Check your progress regularly
- See how much you've learned
- Celebrate your achievements!

### 5. Save Your Work / שמור את העבודה
- Save your session often
- You can come back anytime
- All your notes are safe

---

## Examples / דוגמאות

### Example 1: First Day Learning

```python
# Day 1: Start with basics
assistant = CyberSecurityLearningAssistant(user_name="Mahmoud")

# Get a lesson
lesson = assistant.generate_lesson("information_security")
print(lesson)

# The assistant writes notes for you
note = assistant.write_for_me(
    "CIA Triad",
    "CIA stands for: Confidentiality (keeping secrets), "
    "Integrity (keeping data correct), "
    "Availability (making sure data is available when needed)"
)
print(note)

# Save your work
assistant.save_session("day1.json")
```

### Example 2: Continuing Learning

```python
# Load previous session
assistant = CyberSecurityLearningAssistant()
assistant.load_session("day1.json")

# Continue learning
lesson = assistant.generate_lesson("network_security")
print(lesson)

# Add more notes
note = assistant.write_for_me(
    "Firewalls",
    "A firewall checks all traffic going in and out of a network. "
    "It blocks bad traffic and allows good traffic."
)
print(note)
```

### Example 3: Finding Videos

```python
assistant = CyberSecurityLearningAssistant(user_name="Mahmoud")

# Search for videos in different languages
videos = assistant.search_youtube_resources("cryptography")

print("Videos to watch:")
for video in videos:
    print(f"- {video['query']} ({video['language']})")
    print(f"  {video['url']}\n")
```

---

## Keyboard Shortcuts in Interactive Mode / קיצורי מקלדת

- `1` - New lesson
- `2` - Write notes
- `3` - Create summary
- `4` - Search videos
- `5` - View notes
- `6` - Check progress
- `7` - Save
- `8` - Load
- `9` - Exit

---

## Troubleshooting / פתרון בעיות

### Problem: Python not found
**Solution:** Install Python 3.6 or higher from python.org

### Problem: Can't run the script
**Solution:** Make sure you're in the right directory:
```bash
cd /path/to/mahmoud
python3 interactive_assistant.py
```

### Problem: Lost my session
**Solution:** Load your saved session:
```python
assistant.load_session("learning_session.json")
```

---

## Need Help? / צריך עזרה?

- Read this guide again slowly
- Try the interactive mode - it's the easiest
- Start with simple topics
- Don't worry about making mistakes - the assistant is here to help!

---

## Remember / זכור

✅ The assistant writes FOR YOU - you don't have to struggle with writing
✅ Take your time - learning is not a race
✅ Use videos - they're great for visual learning
✅ Save often - don't lose your work
✅ You can do this! 🎯

---

Made with ❤️ to help everyone learn, especially those with dyslexia.
