#!/usr/bin/env python3
"""
Interactive Cybersecurity Learning Assistant CLI
עוזר למידה אינטראקטיבי לאבטחת מידע

An interactive command-line interface for the learning assistant.
"""

from cyber_learning_assistant import CyberSecurityLearningAssistant
import sys


def print_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("CYBERSECURITY LEARNING ASSISTANT - MAIN MENU")
    print("עוזר למידה לאבטחת מידע - תפריט ראשי")
    print("="*60)
    print("\n1. 📚 Generate a Lesson (יצירת שיעור)")
    print("2. 📝 Write Notes for Me (כתיבת הערות בשבילי)")
    print("3. 📊 Create a Summary (יצירת סיכום)")
    print("4. 🎥 Search YouTube Videos (חיפוש סרטוני YouTube)")
    print("5. 📖 View All My Notes (צפייה בכל ההערות)")
    print("6. 📈 Check Learning Progress (בדיקת התקדמות)")
    print("7. 💾 Save Session (שמירת סשן)")
    print("8. 📂 Load Session (טעינת סשן)")
    print("9. ❌ Exit (יציאה)")
    print("\n" + "="*60)


def show_topics(assistant):
    """Display available topics"""
    print("\n" + "="*60)
    print("AVAILABLE TOPICS / נושאים זמינים")
    print("="*60 + "\n")
    
    for i, (key, value) in enumerate(assistant.topics.items(), 1):
        print(f"{i}. {key}")
        print(f"   {value['title']}")
        print(f"   Subtopics:")
        for subtopic in value['subtopics']:
            print(f"     • {subtopic}")
        print()


def interactive_lesson(assistant):
    """Generate a lesson interactively"""
    show_topics(assistant)
    print("\nEnter topic key (e.g., 'information_security'): ", end='')
    topic = input().strip()
    
    if topic in assistant.topics:
        lesson = assistant.generate_lesson(topic)
        print(lesson)
        print("\n✅ Lesson generated successfully!")
    else:
        print(f"\n❌ Topic '{topic}' not found.")


def interactive_notes(assistant):
    """Take notes interactively"""
    print("\n" + "="*60)
    print("NOTE TAKING / כתיבת הערות")
    print("="*60 + "\n")
    
    print("Enter topic/title: ", end='')
    topic = input().strip()
    
    print("\nEnter your notes (or what you want me to write about):")
    print("(Type END on a new line when done)\n")
    
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    
    content = '\n'.join(lines)
    
    if content.strip():
        note = assistant.write_for_me(topic, content)
        print(note)
        print("✅ Note saved successfully!")
    else:
        print("❌ No content provided.")


def interactive_summary(assistant):
    """Create a summary interactively"""
    print("\n" + "="*60)
    print("SUMMARY CREATION / יצירת סיכום")
    print("="*60 + "\n")
    
    print("Enter summary title: ", end='')
    title = input().strip()
    
    print("\nEnter content to summarize:")
    print("(Type END on a new line when done)\n")
    
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    
    content = '\n'.join(lines)
    
    if content.strip():
        summary = assistant.create_summary(content, title)
        print(summary)
        print("✅ Summary created successfully!")
    else:
        print("❌ No content provided.")


def interactive_youtube(assistant):
    """Search YouTube interactively"""
    show_topics(assistant)
    print("\nEnter topic key to search (e.g., 'network_security'): ", end='')
    topic = input().strip()
    
    print("\nSearching YouTube resources...\n")
    resources = assistant.search_youtube_resources(topic)
    
    print("="*60)
    print(f"YOUTUBE SEARCH RESULTS FOR: {topic}")
    print("="*60 + "\n")
    
    if resources:
        print(f"Found {len(resources)} search queries:\n")
        for i, resource in enumerate(resources, 1):
            print(f"{i}. Query: '{resource['query']}' ({resource['language']})")
            print(f"   URL: {resource['url']}\n")
        print("\n💡 Tip: Copy and paste the URLs into your browser to watch videos!")
    else:
        print("❌ No resources found for this topic.")


def interactive_save(assistant):
    """Save session interactively"""
    print("\nEnter filename (press Enter for default 'learning_session.json'): ", end='')
    filename = input().strip()
    
    if not filename:
        filename = "learning_session.json"
    
    result = assistant.save_session(filename)
    print(f"\n✅ {result}")


def interactive_load(assistant):
    """Load session interactively"""
    print("\nEnter filename (press Enter for default 'learning_session.json'): ", end='')
    filename = input().strip()
    
    if not filename:
        filename = "learning_session.json"
    
    result = assistant.load_session(filename)
    print(f"\n✅ {result}")


def main():
    """Main interactive loop"""
    print("\n" + "="*60)
    print("WELCOME TO CYBERSECURITY LEARNING ASSISTANT!")
    print("ברוכים הבאים לעוזר למידה לאבטחת מידע!")
    print("="*60)
    
    print("\nThis assistant helps you learn cybersecurity.")
    print("It's especially designed for people with dyslexia.")
    print("The assistant will write notes for you!\n")
    
    print("Enter your name: ", end='')
    user_name = input().strip()
    
    if not user_name:
        user_name = "Student"
    
    assistant = CyberSecurityLearningAssistant(user_name=user_name)
    
    print(f"\n✅ Welcome, {user_name}! Let's start learning!\n")
    
    while True:
        try:
            print_menu()
            print("Choose an option (1-9): ", end='')
            choice = input().strip()
            
            if choice == '1':
                interactive_lesson(assistant)
            elif choice == '2':
                interactive_notes(assistant)
            elif choice == '3':
                interactive_summary(assistant)
            elif choice == '4':
                interactive_youtube(assistant)
            elif choice == '5':
                notes = assistant.get_all_notes()
                print(notes)
            elif choice == '6':
                progress = assistant.get_learning_progress()
                print(progress)
            elif choice == '7':
                interactive_save(assistant)
            elif choice == '8':
                interactive_load(assistant)
            elif choice == '9':
                print("\n" + "="*60)
                print("Thank you for using the Cybersecurity Learning Assistant!")
                print("תודה שהשתמשת בעוזר למידה לאבטחת מידע!")
                print("Keep learning and stay secure! 🔒")
                print("="*60 + "\n")
                break
            else:
                print("\n❌ Invalid option. Please choose 1-9.")
            
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
