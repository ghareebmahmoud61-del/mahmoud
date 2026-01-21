# Cybersecurity Learning Assistant / עוזר למידה לאבטחת מידע

A smart assistant designed to help learn cybersecurity concepts, with special support for users with dyslexia.

## Features / תכונות

- **📚 Lesson Generation** - Automatic lesson creation on cybersecurity topics
- **📝 Note Taking** - Smart assistant writes notes for you
- **📊 Summary Creation** - Generates clear summaries of learning materials
- **🎥 YouTube Search** - Finds educational videos in multiple languages (English, Hebrew, Arabic)
- **📈 Progress Tracking** - Monitors your learning journey
- **💾 Session Saving** - Save and load your learning sessions

## For Users with Dyslexia / למשתמשים עם דיסלקציה

This assistant is designed to help by:
- Writing and organizing notes automatically
- Creating clear, structured summaries
- Breaking down complex topics into simple concepts
- Providing visual organization of information
- Supporting multiple languages

## Quick Start / התחלה מהירה

### Installation / התקנה

```bash
# Clone the repository
git clone https://github.com/ghareebmahmoud61-del/mahmoud.git
cd mahmoud

# No installation needed - uses Python standard library only!
```

### Usage / שימוש

Run the assistant:

```bash
python3 cyber_learning_assistant.py
```

### Using as a Module / שימוש כמודול

```python
from cyber_learning_assistant import CyberSecurityLearningAssistant

# Create your personal assistant
assistant = CyberSecurityLearningAssistant(user_name="Your Name")

# Generate a lesson
lesson = assistant.generate_lesson("information_security")
print(lesson)

# Take notes (assistant writes for you)
note = assistant.write_for_me(
    "Encryption Basics",
    "Encryption protects data by converting it into unreadable format."
)
print(note)

# Create a summary
summary = assistant.create_summary(
    "Today I learned about firewalls and network security.",
    "Network Security - Day 1"
)
print(summary)

# Search YouTube for learning resources
videos = assistant.search_youtube_resources("cryptography")
for video in videos[:3]:
    print(f"Search: {video['query']}")
    print(f"URL: {video['url']}\n")

# Check your progress
progress = assistant.get_learning_progress()
print(progress)

# Save your session
assistant.save_session("my_learning.json")
```

## Available Topics / נושאים זמינים

1. **Information Security** / אבטחת מידע
   - CIA Triad
   - Authentication and Authorization
   - Encryption Basics
   - Access Control
   - Security Policies

2. **Network Security** / אבטחת רשתות
   - Firewalls
   - VPN
   - IDS/IPS Systems
   - Network Protocols Security
   - Wireless Security

3. **Cyber Threats** / איומי סייבר
   - Malware Types
   - Phishing and Social Engineering
   - DDoS Attacks
   - Ransomware
   - Zero-Day Vulnerabilities

4. **Application Security** / אבטחת יישומים
   - OWASP Top 10
   - SQL Injection
   - Cross-Site Scripting (XSS)
   - Secure Coding Practices
   - API Security

5. **Cryptography** / קריפטוגרפיה
   - Symmetric Encryption
   - Asymmetric Encryption
   - Hash Functions
   - Digital Signatures
   - PKI

## Key Methods / מתודות עיקריות

- `generate_lesson(topic)` - Generate a lesson on a specific topic
- `write_for_me(topic, notes)` - Take notes for you automatically
- `create_summary(content, title)` - Create a summary
- `search_youtube_resources(topic, languages)` - Find YouTube videos
- `get_learning_progress()` - View your progress
- `save_session(filename)` - Save your learning session
- `load_session(filename)` - Load a previous session

## Dyslexia-Friendly Features / תכונות ידידותיות לדיסלקציה

✅ Clear, structured output
✅ Automatic note-taking (no need to write yourself)
✅ Simple language and explanations
✅ Visual separation with formatting
✅ Multi-language support
✅ Progress tracking to stay organized

## Requirements / דרישות

- Python 3.6 or higher
- No external dependencies required!

## License / רישיון

Open source - Feel free to use and modify!

## Support / תמיכה

For questions or issues, please open an issue on GitHub.

---

Made with ❤️ to help everyone learn cybersecurity, especially those with dyslexia.