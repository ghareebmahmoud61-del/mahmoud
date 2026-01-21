# How to Extend the Assistant / איך להרחיב את העוזר

## Overview / סקירה כללית

This guide shows you how to add new features, topics, and capabilities to the Cybersecurity Learning Assistant in the future.

The system is designed to be **modular** and **extensible** - you can easily add new things without breaking existing functionality!

---

## Adding New Topics / הוספת נושאים חדשים

### Method 1: Add to Existing System (Easy!)

The easiest way to add new topics is to extend the `_initialize_topics()` method:

```python
# Open cyber_learning_assistant.py and find the _initialize_topics method
# Add your new topic like this:

def _initialize_topics(self) -> Dict:
    """Initialize cybersecurity topics for learning"""
    return {
        # ... existing topics ...
        
        # ADD YOUR NEW TOPIC HERE:
        "cloud_security": {
            "title": "Cloud Security / אבטחת ענן",
            "subtopics": [
                "AWS Security",
                "Azure Security",
                "Cloud Access Control",
                "Cloud Data Protection",
                "Container Security"
            ]
        },
        
        "iot_security": {
            "title": "IoT Security / אבטחת אינטרנט של הדברים",
            "subtopics": [
                "Smart Device Security",
                "IoT Network Security",
                "Firmware Security",
                "IoT Authentication",
                "IoT Privacy"
            ]
        },
        
        # Add as many topics as you want!
    }
```

### Method 2: Create a Plugin File

Create a new file called `custom_topics.py`:

```python
"""
Custom Topics Plugin
Add your own cybersecurity topics here!
"""

CUSTOM_TOPICS = {
    "penetration_testing": {
        "title": "Penetration Testing / בדיקות חדירה",
        "subtopics": [
            "Reconnaissance",
            "Scanning and Enumeration",
            "Exploitation",
            "Post-Exploitation",
            "Reporting"
        ]
    },
    
    "incident_response": {
        "title": "Incident Response / תגובה לאירועים",
        "subtopics": [
            "Preparation",
            "Detection and Analysis",
            "Containment",
            "Eradication and Recovery",
            "Post-Incident Activities"
        ]
    },
    
    # Add your own topics below:
    "your_custom_topic": {
        "title": "Your Topic / הנושא שלך",
        "subtopics": [
            "Subtopic 1",
            "Subtopic 2",
            "Subtopic 3"
        ]
    }
}
```

Then load them in your code:

```python
from cyber_learning_assistant import CyberSecurityLearningAssistant
from custom_topics import CUSTOM_TOPICS

assistant = CyberSecurityLearningAssistant()

# Add custom topics
assistant.topics.update(CUSTOM_TOPICS)

# Now you can use them!
lesson = assistant.generate_lesson("penetration_testing")
```

---

## Adding New Languages / הוספת שפות חדשות

To add support for more languages in YouTube search:

```python
# Create a file: language_extensions.py

LANGUAGE_SEARCH_TERMS = {
    "information_security": {
        "Spanish": "seguridad de la información básica",
        "French": "sécurité de l'information de base",
        "German": "Informationssicherheit Grundlagen",
        "Russian": "основы информационной безопасности"
    },
    "network_security": {
        "Spanish": "seguridad de redes tutorial",
        "French": "tutoriel sécurité réseau",
        "German": "Netzwerksicherheit Tutorial",
        "Russian": "учебник по сетевой безопасности"
    },
    # Add more topics and languages...
}
```

---

## Adding New Features / הוספת תכונות חדשות

### Example: Add a Quiz Feature

Create a new file `quiz_extension.py`:

```python
"""
Quiz Extension for Learning Assistant
"""

import random

class QuizExtension:
    """Add quiz capabilities to the learning assistant"""
    
    def __init__(self):
        self.quiz_questions = {
            "information_security": [
                {
                    "question": "What does CIA stand for in information security?",
                    "options": [
                        "Confidentiality, Integrity, Availability",
                        "Central Intelligence Agency",
                        "Computer Internet Access",
                        "Certified Information Administrator"
                    ],
                    "correct": 0
                },
                {
                    "question": "What is encryption?",
                    "options": [
                        "Deleting data",
                        "Converting data into a secret code",
                        "Backing up data",
                        "Compressing data"
                    ],
                    "correct": 1
                }
            ],
            # Add more topics and questions...
        }
    
    def generate_quiz(self, topic: str, num_questions: int = 5):
        """Generate a quiz for a topic"""
        if topic not in self.quiz_questions:
            return f"No quiz available for {topic}"
        
        questions = random.sample(
            self.quiz_questions[topic],
            min(num_questions, len(self.quiz_questions[topic]))
        )
        
        quiz = f"\n{'='*60}\n"
        quiz += f"QUIZ: {topic}\n"
        quiz += f"{'='*60}\n\n"
        
        for i, q in enumerate(questions, 1):
            quiz += f"Question {i}: {q['question']}\n"
            for j, option in enumerate(q['options'], 1):
                quiz += f"  {j}. {option}\n"
            quiz += "\n"
        
        return quiz, questions
    
    def check_answers(self, questions, user_answers):
        """Check quiz answers"""
        score = 0
        for i, (question, answer) in enumerate(zip(questions, user_answers)):
            if answer == question['correct']:
                score += 1
        
        return score, len(questions)

# Usage:
# from quiz_extension import QuizExtension
# quiz = QuizExtension()
# quiz_text, questions = quiz.generate_quiz("information_security")
# print(quiz_text)
```

### Example: Add Flashcard Feature

Create `flashcard_extension.py`:

```python
"""
Flashcard Extension for Learning Assistant
"""

class FlashcardExtension:
    """Add flashcard study capabilities"""
    
    def __init__(self):
        self.flashcards = {
            "information_security": [
                {
                    "front": "What is Confidentiality?",
                    "back": "Ensuring that information is accessible only to authorized users"
                },
                {
                    "front": "What is Integrity?",
                    "back": "Ensuring that information is accurate and hasn't been tampered with"
                },
                {
                    "front": "What is Availability?",
                    "back": "Ensuring that information and resources are available when needed"
                }
            ]
        }
    
    def create_flashcard(self, topic: str, front: str, back: str):
        """Create a new flashcard"""
        if topic not in self.flashcards:
            self.flashcards[topic] = []
        
        self.flashcards[topic].append({
            "front": front,
            "back": back
        })
        
        return f"Flashcard created for {topic}!"
    
    def get_flashcards(self, topic: str):
        """Get all flashcards for a topic"""
        if topic in self.flashcards:
            return self.flashcards[topic]
        return []

# Usage:
# from flashcard_extension import FlashcardExtension
# flashcards = FlashcardExtension()
# cards = flashcards.get_flashcards("information_security")
# for card in cards:
#     print(f"Q: {card['front']}")
#     input("Press Enter to see answer...")
#     print(f"A: {card['back']}\n")
```

---

## Creating a Complete Plugin / יצירת תוסף מלא

Here's how to create a complete plugin:

```python
# my_custom_plugin.py

"""
My Custom Security Learning Plugin
"""

class MyCustomPlugin:
    """Add your custom features here"""
    
    def __init__(self, assistant):
        """Initialize with the main assistant"""
        self.assistant = assistant
        self.name = "My Custom Plugin"
        self.version = "1.0.0"
    
    def my_custom_feature(self, param):
        """Your custom feature"""
        result = f"Custom feature executed with {param}"
        
        # You can access the assistant's methods:
        # self.assistant.write_for_me(...)
        # self.assistant.notes
        # etc.
        
        return result
    
    def get_info(self):
        """Plugin information"""
        return {
            "name": self.name,
            "version": self.version,
            "features": ["my_custom_feature"]
        }

# Usage:
# from cyber_learning_assistant import CyberSecurityLearningAssistant
# from my_custom_plugin import MyCustomPlugin
#
# assistant = CyberSecurityLearningAssistant()
# plugin = MyCustomPlugin(assistant)
# result = plugin.my_custom_feature("test")
# print(result)
```

---

## Example: Complete Extension System

Create `extension_manager.py`:

```python
"""
Extension Manager for Loading Plugins
"""

import importlib
import os

class ExtensionManager:
    """Manage extensions and plugins"""
    
    def __init__(self, assistant):
        self.assistant = assistant
        self.extensions = {}
    
    def load_extension(self, extension_name):
        """Load an extension by name"""
        try:
            module = importlib.import_module(extension_name)
            extension_class = getattr(module, f"{extension_name.title()}Extension")
            self.extensions[extension_name] = extension_class(self.assistant)
            return f"Extension '{extension_name}' loaded successfully!"
        except Exception as e:
            return f"Failed to load extension '{extension_name}': {e}"
    
    def list_extensions(self):
        """List all loaded extensions"""
        return list(self.extensions.keys())
    
    def get_extension(self, name):
        """Get a specific extension"""
        return self.extensions.get(name)

# Usage:
# from cyber_learning_assistant import CyberSecurityLearningAssistant
# from extension_manager import ExtensionManager
#
# assistant = CyberSecurityLearningAssistant()
# manager = ExtensionManager(assistant)
# manager.load_extension("quiz")
# quiz = manager.get_extension("quiz")
```

---

## Templates for Common Extensions / תבניות להרחבות נפוצות

### Template 1: Adding a New Content Type

```python
class ContentTypeExtension:
    """Template for adding new content types"""
    
    def __init__(self, assistant):
        self.assistant = assistant
    
    def create_content(self, topic, **kwargs):
        """Create new type of content"""
        content = f"New content for {topic}"
        # Your logic here
        return content
```

### Template 2: Adding External API Integration

```python
class APIIntegration:
    """Template for integrating external APIs"""
    
    def __init__(self, assistant, api_key=None):
        self.assistant = assistant
        self.api_key = api_key
    
    def fetch_data(self, query):
        """Fetch data from external API"""
        # Your API call logic here
        pass
```

### Template 3: Adding Data Export Features

```python
class ExportExtension:
    """Template for exporting data in different formats"""
    
    def __init__(self, assistant):
        self.assistant = assistant
    
    def export_to_pdf(self, filename):
        """Export notes to PDF"""
        pass
    
    def export_to_markdown(self, filename):
        """Export notes to Markdown"""
        pass
```

---

## Best Practices / שיטות עבודה מומלצות

1. **Keep it modular** - Each extension should do one thing well
2. **Document your code** - Add comments so you remember what it does
3. **Test before using** - Make sure your extension works
4. **Save backups** - Keep copies before making big changes
5. **Start small** - Add one feature at a time

---

## Quick Reference / מדריך מהיר

### Adding a Topic:
```python
assistant.topics["new_topic"] = {
    "title": "New Topic",
    "subtopics": ["Sub 1", "Sub 2"]
}
```

### Adding a Language:
```python
# In search_youtube_resources, add your language
languages = ["English", "Hebrew", "Arabic", "Spanish"]
```

### Creating a Plugin:
```python
class MyPlugin:
    def __init__(self, assistant):
        self.assistant = assistant
    
    def my_feature(self):
        # Your code here
        pass
```

---

## Need Help? / צריך עזרה?

- Look at the existing code for examples
- Start with simple additions
- Test each change before adding more
- Keep the original files as backup

---

**Remember:** The system is designed for YOU to customize! Don't be afraid to experiment and add what you need. 🚀
