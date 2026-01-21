#!/usr/bin/env python3
"""
Cybersecurity Learning Assistant
עוזר למידה לאבטחת מידע

A smart assistant designed to help learn cybersecurity concepts,
especially helpful for users with dyslexia.

Features:
- Lesson generation
- Summary creation
- YouTube video search
- Note-taking assistance
- Writing support
"""

import json
import os
from datetime import datetime
from typing import List, Dict


class CyberSecurityLearningAssistant:
    """Smart assistant for cybersecurity education"""
    
    def __init__(self, user_name: str = "Student"):
        self.user_name = user_name
        self.notes = []
        self.lessons_completed = []
        self.topics = self._initialize_topics()
        
    def _initialize_topics(self) -> Dict:
        """Initialize cybersecurity topics for learning"""
        return {
            "information_security": {
                "title": "Information Security Basics / יסודות אבטחת מידע",
                "subtopics": [
                    "CIA Triad (Confidentiality, Integrity, Availability)",
                    "Authentication and Authorization",
                    "Encryption Basics",
                    "Access Control",
                    "Security Policies"
                ]
            },
            "network_security": {
                "title": "Network Security / אבטחת רשתות",
                "subtopics": [
                    "Firewalls",
                    "VPN (Virtual Private Networks)",
                    "IDS/IPS Systems",
                    "Network Protocols Security",
                    "Wireless Security"
                ]
            },
            "cyber_threats": {
                "title": "Cyber Threats / איומי סייבר",
                "subtopics": [
                    "Malware Types",
                    "Phishing and Social Engineering",
                    "DDoS Attacks",
                    "Ransomware",
                    "Zero-Day Vulnerabilities"
                ]
            },
            "application_security": {
                "title": "Application Security / אבטחת יישומים",
                "subtopics": [
                    "OWASP Top 10",
                    "SQL Injection",
                    "Cross-Site Scripting (XSS)",
                    "Secure Coding Practices",
                    "API Security"
                ]
            },
            "cryptography": {
                "title": "Cryptography / קריפטוגרפיה",
                "subtopics": [
                    "Symmetric Encryption",
                    "Asymmetric Encryption",
                    "Hash Functions",
                    "Digital Signatures",
                    "PKI (Public Key Infrastructure)"
                ]
            }
        }
    
    def generate_lesson(self, topic: str) -> str:
        """
        Generate a lesson on a specific cybersecurity topic
        יצירת שיעור בנושא אבטחת מידע מסוים
        """
        if topic in self.topics:
            lesson = f"\n{'='*60}\n"
            lesson += f"LESSON: {self.topics[topic]['title']}\n"
            lesson += f"{'='*60}\n\n"
            
            lesson += f"Hello {self.user_name}! 👋\n\n"
            lesson += f"Today we'll learn about: {self.topics[topic]['title']}\n\n"
            
            lesson += "Topics covered in this lesson:\n"
            for i, subtopic in enumerate(self.topics[topic]['subtopics'], 1):
                lesson += f"  {i}. {subtopic}\n"
            
            lesson += "\n" + "="*60 + "\n"
            
            # Add to completed lessons
            self.lessons_completed.append({
                "topic": topic,
                "title": self.topics[topic]['title'],
                "date": datetime.now().isoformat()
            })
            
            return lesson
        else:
            return f"Topic '{topic}' not found. Available topics: {', '.join(self.topics.keys())}"
    
    def create_summary(self, content: str, title: str = "Summary") -> str:
        """
        Create a summary of learning content
        יצירת סיכום של תוכן למידה
        """
        summary = f"\n{'='*60}\n"
        summary += f"SUMMARY / סיכום: {title}\n"
        summary += f"{'='*60}\n\n"
        summary += f"Created for: {self.user_name}\n"
        summary += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        summary += "Content Summary:\n"
        summary += f"{content}\n\n"
        summary += "="*60 + "\n"
        
        return summary
    
    def search_youtube_resources(self, topic: str, languages: List[str] = None) -> List[Dict]:
        """
        Generate YouTube search queries for cybersecurity topics
        חיפוש משאבים ב-YouTube
        
        Returns search queries that can be used on YouTube
        """
        if languages is None:
            languages = ["English", "Hebrew", "Arabic"]
        
        search_queries = []
        
        # Base search terms
        base_terms = {
            "information_security": [
                "information security basics",
                "אבטחת מידע יסודות",
                "أساسيات أمن المعلومات"
            ],
            "network_security": [
                "network security tutorial",
                "אבטחת רשתות הדרכה",
                "تعليم أمن الشبكات"
            ],
            "cyber_threats": [
                "cyber threats explained",
                "איומי סייבר הסבר",
                "شرح التهديدات السيبرانية"
            ],
            "application_security": [
                "application security basics",
                "אבטחת יישומים",
                "أمن التطبيقات"
            ],
            "cryptography": [
                "cryptography explained",
                "קריפטוגרפיה הסבר",
                "شرح التشفير"
            ]
        }
        
        if topic in base_terms:
            for i, query in enumerate(base_terms[topic]):
                search_queries.append({
                    "query": query,
                    "language": languages[i % len(languages)],
                    "url": f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
                })
        
        # Add general searches
        general_queries = [
            f"{topic} tutorial",
            f"{topic} for beginners",
            f"learn {topic}",
            f"{topic} explained simply"
        ]
        
        for query in general_queries:
            search_queries.append({
                "query": query,
                "language": "English",
                "url": f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
            })
        
        return search_queries
    
    def write_for_me(self, topic: str, notes: str = "") -> str:
        """
        Write and organize notes for the user
        כתיבה וארגון הערות עבור המשתמש
        """
        note = {
            "id": len(self.notes) + 1,
            "topic": topic,
            "content": notes,
            "date": datetime.now().isoformat(),
            "user": self.user_name
        }
        
        self.notes.append(note)
        
        formatted_note = f"\n{'='*60}\n"
        formatted_note += f"NOTE #{note['id']}: {topic}\n"
        formatted_note += f"{'='*60}\n\n"
        formatted_note += f"Written for: {self.user_name}\n"
        formatted_note += f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        formatted_note += f"{notes}\n\n"
        formatted_note += "="*60 + "\n"
        
        return formatted_note
    
    def get_all_notes(self) -> str:
        """Get all saved notes"""
        if not self.notes:
            return "No notes saved yet."
        
        all_notes = f"\n{'='*60}\n"
        all_notes += f"ALL NOTES FOR {self.user_name}\n"
        all_notes += f"{'='*60}\n\n"
        
        for note in self.notes:
            all_notes += f"Note #{note['id']}: {note['topic']}\n"
            all_notes += f"Date: {note['date']}\n"
            all_notes += f"{note['content']}\n\n"
            all_notes += "-"*60 + "\n\n"
        
        return all_notes
    
    def get_learning_progress(self) -> str:
        """Get learning progress report"""
        report = f"\n{'='*60}\n"
        report += f"LEARNING PROGRESS FOR {self.user_name}\n"
        report += f"{'='*60}\n\n"
        report += f"Lessons Completed: {len(self.lessons_completed)}\n"
        report += f"Notes Created: {len(self.notes)}\n\n"
        
        if self.lessons_completed:
            report += "Completed Lessons:\n"
            for lesson in self.lessons_completed:
                report += f"  - {lesson['title']} ({lesson['date'][:10]})\n"
        
        report += "\n" + "="*60 + "\n"
        
        return report
    
    def save_session(self, filename: str = "learning_session.json"):
        """Save the learning session to a file"""
        session_data = {
            "user_name": self.user_name,
            "notes": self.notes,
            "lessons_completed": self.lessons_completed,
            "last_saved": datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)
        
        return f"Session saved to {filename}"
    
    def load_session(self, filename: str = "learning_session.json"):
        """Load a learning session from a file"""
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                session_data = json.load(f)
            
            self.user_name = session_data.get("user_name", self.user_name)
            self.notes = session_data.get("notes", [])
            self.lessons_completed = session_data.get("lessons_completed", [])
            
            return f"Session loaded from {filename}"
        else:
            return f"File {filename} not found"


def main():
    """Main function to demonstrate the assistant"""
    print("\n" + "="*60)
    print("CYBERSECURITY LEARNING ASSISTANT")
    print("עוזר למידה לאבטחת מידע")
    print("="*60 + "\n")
    
    # Create assistant
    assistant = CyberSecurityLearningAssistant(user_name="Student")
    
    print("Welcome! This assistant will help you learn cybersecurity.")
    print("It's designed to be helpful for people with dyslexia.\n")
    
    # Show available topics
    print("Available Topics:")
    for key, value in assistant.topics.items():
        print(f"  - {key}: {value['title']}")
    
    print("\n" + "="*60)
    print("EXAMPLE: Generating a lesson on Information Security")
    print("="*60)
    lesson = assistant.generate_lesson("information_security")
    print(lesson)
    
    print("\n" + "="*60)
    print("EXAMPLE: Creating a summary")
    print("="*60)
    summary = assistant.create_summary(
        "Learned about CIA Triad: Confidentiality, Integrity, and Availability. "
        "These are the three main principles of information security.",
        "Information Security - Day 1"
    )
    print(summary)
    
    print("\n" + "="*60)
    print("EXAMPLE: YouTube Resources for Network Security")
    print("="*60)
    youtube_resources = assistant.search_youtube_resources("network_security")
    print(f"\nFound {len(youtube_resources)} YouTube search queries:\n")
    for i, resource in enumerate(youtube_resources[:5], 1):
        print(f"{i}. Search: '{resource['query']}' ({resource['language']})")
        print(f"   URL: {resource['url']}\n")
    
    print("\n" + "="*60)
    print("EXAMPLE: Taking notes (writing for you)")
    print("="*60)
    note = assistant.write_for_me(
        "Firewalls",
        "A firewall is a security system that monitors and controls network traffic. "
        "It acts as a barrier between trusted and untrusted networks."
    )
    print(note)
    
    print("\n" + "="*60)
    print("EXAMPLE: Learning Progress")
    print("="*60)
    progress = assistant.get_learning_progress()
    print(progress)
    
    # Save session
    print("\nSaving session...")
    result = assistant.save_session()
    print(result)
    
    print("\n✅ Assistant is ready to help you learn!")
    print("💡 You can use this tool to generate lessons, create summaries,")
    print("   search for YouTube videos, and take notes automatically.\n")


if __name__ == "__main__":
    main()
