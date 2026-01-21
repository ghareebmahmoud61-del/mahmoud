"""
Professional Agent System with Open Mic Feature

This module provides a professional agent that can interact through an open mic system.
"""


class ProfessionalAgent:
    """A professional agent that handles interactions and communications."""
    
    def __init__(self, name="Agent", specialty="General"):
        """
        Initialize a professional agent.
        
        Args:
            name: The name of the agent
            specialty: The specialty or field of expertise
        """
        self.name = name
        self.specialty = specialty
        self.is_mic_open = False
        self.messages = []
    
    def open_mic(self):
        """Open the microphone for communication."""
        self.is_mic_open = True
        return f"{self.name}: Microphone is now open. Ready to listen."
    
    def close_mic(self):
        """Close the microphone."""
        self.is_mic_open = False
        return f"{self.name}: Microphone is now closed."
    
    def speak(self, message):
        """
        Agent speaks a message through the open mic.
        
        Args:
            message: The message to speak
            
        Returns:
            The formatted message or error if mic is closed
        """
        if not self.is_mic_open:
            return "Error: Microphone is closed. Please open mic first."
        
        formatted_message = f"{self.name} ({self.specialty}): {message}"
        self.messages.append(formatted_message)
        return formatted_message
    
    def listen(self, input_message):
        """
        Agent listens to input through the open mic.
        
        Args:
            input_message: The message received
            
        Returns:
            Acknowledgment message
        """
        if not self.is_mic_open:
            return "Error: Microphone is closed. Cannot listen."
        
        response = f"{self.name}: Received - '{input_message}'"
        self.messages.append(f"Listener: {input_message}")
        return response
    
    def get_message_history(self):
        """Get all messages in the conversation history."""
        return self.messages
    
    def introduce(self):
        """Agent introduces itself."""
        return f"Hello! I am {self.name}, a professional agent specializing in {self.specialty}."
