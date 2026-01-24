"""
Example Plugin: Quiz Feature
This is an example of how to extend the Cybersecurity Learning Assistant
"""

import random
from datetime import datetime


class QuizPlugin:
    """Add quiz capabilities to the learning assistant"""
    
    def __init__(self, assistant):
        self.assistant = assistant
        self.quiz_history = []
        self.questions_bank = self._initialize_questions()
    
    def _initialize_questions(self):
        """Initialize quiz questions for different topics"""
        return {
            "information_security": [
                {
                    "question": "What does the 'C' in CIA Triad stand for?",
                    "options": ["Confidentiality", "Computer", "Central", "Cryptography"],
                    "correct": 0,
                    "explanation": "CIA stands for Confidentiality, Integrity, and Availability"
                },
                {
                    "question": "What is the purpose of encryption?",
                    "options": [
                        "To delete data",
                        "To protect data by converting it into a secret code",
                        "To backup data",
                        "To compress data"
                    ],
                    "correct": 1,
                    "explanation": "Encryption protects data by making it unreadable without the decryption key"
                }
            ]
        }
    
    def generate_quiz(self, topic: str, num_questions: int = 3):
        """Generate a quiz for a specific topic"""
        if topic not in self.questions_bank:
            return f"No quiz available for topic: {topic}", []
        
        available_questions = self.questions_bank[topic]
        selected_questions = random.sample(
            available_questions,
            min(num_questions, len(available_questions))
        )
        
        quiz_text = f"\n{'='*60}\n"
        quiz_text += f"QUIZ: {topic.replace('_', ' ').title()}\n"
        quiz_text += f"{'='*60}\n\n"
        
        for i, q in enumerate(selected_questions, 1):
            quiz_text += f"Question {i}: {q['question']}\n\n"
            for j, option in enumerate(q['options'], 1):
                quiz_text += f"  {j}. {option}\n"
            quiz_text += "\n"
        
        return quiz_text, selected_questions


# Example usage
if __name__ == "__main__":
    print("Quiz Plugin Example - See EXTENDING.md for usage details")
