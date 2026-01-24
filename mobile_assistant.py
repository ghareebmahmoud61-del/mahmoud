#!/usr/bin/env python3
"""
Mobile-Optimized Cybersecurity Learning Assistant
עוזר למידה מותאם לנייד

Optimized for iPhone/iOS with Pythonista, Pyto, or other mobile Python apps.
Touch-friendly interface with minimal typing.
"""

try:
    from cyber_learning_assistant import CyberSecurityLearningAssistant
except ImportError as e:
    print("Error: Unable to import CyberSecurityLearningAssistant module.")
    print(f"Details: {e}")
    print("Please ensure cyber_learning_assistant.py is in the same directory.")
    exit(1)

import sys


def print_mobile_menu():
    """Display mobile-optimized menu"""
    print("\n" + "="*50)
    print("🎓 CYBER SECURITY ASSISTANT")
    print("📱 Mobile Edition")
    print("="*50)
    print("\n1. 📚 Lesson")
    print("2. 📝 Notes (writes for you!)")
    print("3. 📊 Summary")
    print("4. 🎥 YouTube")
    print("5. 📖 View Notes")
    print("6. 📈 Progress")
    print("7. 💾 Save")
    print("8. 📂 Load")
    print("9. ℹ️ Help")
    print("0. ❌ Exit")
    print("\n" + "="*50)


def show_mobile_topics(assistant):
    """Display topics in mobile-friendly format"""
    print("\n" + "="*50)
    print("📚 TOPICS")
    print("="*50 + "\n")
    
    topics = {
        "1": "information_security",
        "2": "network_security",
        "3": "cyber_threats",
        "4": "application_security",
        "5": "cryptography"
    }
    
    print("1. 🔐 Information Security")
    print("2. 🌐 Network Security")
    print("3. ⚠️  Cyber Threats")
    print("4. 💻 Application Security")
    print("5. 🔒 Cryptography")
    print("\nTip: Save often with option 7!")
    
    return topics


def mobile_lesson(assistant):
    """Generate a lesson with mobile-optimized flow"""
    topics = show_mobile_topics(assistant)
    print("\nChoose topic (1-5): ", end='')
    choice = input().strip()
    
    if choice in topics:
        topic = topics[choice]
        lesson = assistant.generate_lesson(topic)
        print(lesson)
        print("\n✅ Lesson complete!")
        print("💡 Tip: Use option 2 to save notes")
    else:
        print("\n❌ Invalid choice. Please choose 1-5.")


def mobile_notes(assistant):
    """Quick note-taking for mobile"""
    print("\n" + "="*50)
    print("📝 QUICK NOTES")
    print("="*50 + "\n")
    
    print("Title: ", end='')
    topic = input().strip()
    
    if not topic:
        topic = "Quick Note"
    
    print("\nWhat did you learn?")
    print("(Type 'done' when finished)\n")
    
    lines = []
    print("> ", end='')
    while True:
        line = input()
        if line.strip().lower() == 'done':
            break
        lines.append(line)
        print("> ", end='')
    
    content = ' '.join(lines)
    
    if content.strip():
        note = assistant.write_for_me(topic, content)
        print(note)
        print("✅ Note saved!")
    else:
        print("❌ No content entered.")


def mobile_summary(assistant):
    """Quick summary for mobile"""
    print("\n" + "="*50)
    print("📊 SUMMARY")
    print("="*50 + "\n")
    
    print("Title: ", end='')
    title = input().strip() or "Summary"
    
    print("\nWhat to summarize?")
    print("(Type 'done' when finished)\n")
    
    lines = []
    print("> ", end='')
    while True:
        line = input()
        if line.strip().lower() == 'done':
            break
        lines.append(line)
        print("> ", end='')
    
    content = ' '.join(lines)
    
    if content.strip():
        summary = assistant.create_summary(content, title)
        print(summary)
        print("✅ Summary created!")
    else:
        print("❌ No content provided.")


def mobile_youtube(assistant):
    """YouTube search optimized for mobile"""
    topics = show_mobile_topics(assistant)
    print("\nTopic (1-5): ", end='')
    choice = input().strip()
    
    topic_map = {
        "1": "information_security",
        "2": "network_security",
        "3": "cyber_threats",
        "4": "application_security",
        "5": "cryptography"
    }
    
    if choice in topic_map:
        topic = topic_map[choice]
        print("\n🔍 Searching YouTube...\n")
        resources = assistant.search_youtube_resources(topic)
        
        print("="*50)
        print(f"🎥 VIDEOS: {topic.replace('_', ' ').title()}")
        print("="*50 + "\n")
        
        # Show first 5 for mobile
        for i, resource in enumerate(resources[:5], 1):
            print(f"{i}. {resource['query']}")
            print(f"   {resource['url']}\n")
        
        print("\n💡 Tap URL to open in browser")
    else:
        print("\n❌ Invalid choice.")


def mobile_help():
    """Show help for mobile users"""
    print("\n" + "="*50)
    print("ℹ️  HELP - MOBILE TIPS")
    print("="*50 + "\n")
    
    print("📱 MOBILE FEATURES:")
    print("  • Simple number menus (1-9)")
    print("  • Auto-save capability")
    print("  • Works offline")
    print("  • Touch-friendly")
    print("\n💡 TIPS:")
    print("  • Use option 2 for quick notes")
    print("  • Save often (option 7)")
    print("  • Landscape = better typing")
    print("  • Portrait = better reading")
    print("\n🎯 BEST FOR MOBILE:")
    print("  • Short learning sessions")
    print("  • Quick note-taking")
    print("  • Progress tracking")
    print("  • YouTube searches")
    print("\n📖 FULL GUIDE:")
    print("  • See IPHONE_GUIDE.md")
    print("  • Troubleshooting included")
    print("  • App recommendations")
    
    print("\n" + "="*50)


def main():
    """Main mobile-optimized loop"""
    print("\n" + "="*50)
    print("🎓 WELCOME!")
    print("📱 Cybersecurity Learning Assistant")
    print("   Mobile Edition")
    print("="*50)
    
    print("\n💡 Optimized for iPhone/iOS")
    print("   Touch-friendly interface\n")
    
    print("Your name: ", end='')
    user_name = input().strip()
    
    if not user_name:
        user_name = "Student"
    
    assistant = CyberSecurityLearningAssistant(user_name=user_name)
    
    print(f"\n✅ Welcome, {user_name}!")
    print("💡 Tip: Type 'help' anytime for tips\n")
    
    while True:
        try:
            print_mobile_menu()
            print("Choose (0-9): ", end='')
            choice = input().strip()
            
            if choice == '1':
                mobile_lesson(assistant)
            elif choice == '2':
                mobile_notes(assistant)
            elif choice == '3':
                mobile_summary(assistant)
            elif choice == '4':
                mobile_youtube(assistant)
            elif choice == '5':
                notes = assistant.get_all_notes()
                print(notes)
            elif choice == '6':
                progress = assistant.get_learning_progress()
                print(progress)
            elif choice == '7':
                print("\nFilename (or press Enter): ", end='')
                filename = input().strip()
                if not filename:
                    filename = "mobile_session.json"
                result = assistant.save_session(filename)
                print(f"\n✅ {result}")
            elif choice == '8':
                print("\nFilename (or press Enter): ", end='')
                filename = input().strip()
                if not filename:
                    filename = "mobile_session.json"
                result = assistant.load_session(filename)
                print(f"\n✅ {result}")
            elif choice == '9':
                mobile_help()
            elif choice == '0':
                print("\n" + "="*50)
                print("👋 Thanks for learning!")
                print("   Stay secure! 🔒")
                print("="*50 + "\n")
                break
            else:
                print("\n❌ Choose 0-9 only")
            
            if choice != '9':  # Don't pause after help
                print("\n📱 Tap to continue...", end='')
                input()
            
        except KeyboardInterrupt:
            print("\n\n👋 Exiting...")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("\n📱 Tap to continue...", end='')
            input()


if __name__ == "__main__":
    main()
