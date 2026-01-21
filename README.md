# mahmoud

## Professional Agent System with Open Mic Feature

A Python-based professional agent system that enables communication through an open microphone interface.

### Features

- **Professional Agent**: Create and manage professional agents with customizable names and specialties
- **Open Mic**: Control microphone access for speaking and listening
- **Message History**: Track all communications in a conversation history
- **Error Handling**: Proper validation to ensure mic is open before communication

### Installation

No external dependencies required. Uses Python 3 standard library only.

### Usage

#### Basic Example

```python
from professional_agent import ProfessionalAgent

# Create a professional agent
agent = ProfessionalAgent(name="Mahmoud", specialty="Customer Service")

# Introduce the agent
print(agent.introduce())

# Open the microphone
print(agent.open_mic())

# Speak through the open mic
print(agent.speak("How can I help you today?"))

# Listen to input
print(agent.listen("I have a question"))

# Close the microphone
print(agent.close_mic())
```

#### Running Tests

```bash
python3 test_professional_agent.py
```

### API Reference

#### ProfessionalAgent Class

- `__init__(name, specialty)`: Initialize a new professional agent
- `open_mic()`: Open the microphone for communication
- `close_mic()`: Close the microphone
- `speak(message)`: Agent speaks a message (requires open mic)
- `listen(input_message)`: Agent listens to input (requires open mic)
- `get_message_history()`: Retrieve all messages in the conversation
- `introduce()`: Agent introduces itself

### Requirements

The original requirements addressed:
1. **Professional Agent** ("profshinal agent"): Implemented as the `ProfessionalAgent` class with full agent capabilities
2. **Open Mic**: Implemented with `open_mic()` and `close_mic()` methods for controlled communication

### License

MIT License