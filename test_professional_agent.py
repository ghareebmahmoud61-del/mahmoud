"""
Unit tests for the Professional Agent System
"""

import unittest
from professional_agent import ProfessionalAgent


class TestProfessionalAgent(unittest.TestCase):
    """Test cases for the ProfessionalAgent class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.agent = ProfessionalAgent(name="TestAgent", specialty="Testing")
    
    def test_initialization(self):
        """Test agent initialization."""
        self.assertEqual(self.agent.name, "TestAgent")
        self.assertEqual(self.agent.specialty, "Testing")
        self.assertFalse(self.agent.is_mic_open)
        self.assertEqual(len(self.agent.messages), 0)
    
    def test_open_mic(self):
        """Test opening the microphone."""
        result = self.agent.open_mic()
        self.assertTrue(self.agent.is_mic_open)
        self.assertIn("open", result.lower())
    
    def test_close_mic(self):
        """Test closing the microphone."""
        self.agent.open_mic()
        result = self.agent.close_mic()
        self.assertFalse(self.agent.is_mic_open)
        self.assertIn("closed", result.lower())
    
    def test_speak_with_closed_mic(self):
        """Test speaking when microphone is closed."""
        result = self.agent.speak("Hello")
        self.assertIn("Error", result)
        self.assertIn("closed", result.lower())
    
    def test_speak_with_open_mic(self):
        """Test speaking when microphone is open."""
        self.agent.open_mic()
        result = self.agent.speak("Hello World")
        self.assertIn("TestAgent", result)
        self.assertIn("Hello World", result)
        self.assertEqual(len(self.agent.messages), 1)
    
    def test_listen_with_closed_mic(self):
        """Test listening when microphone is closed."""
        result = self.agent.listen("Test input")
        self.assertIn("Error", result)
        self.assertIn("closed", result.lower())
    
    def test_listen_with_open_mic(self):
        """Test listening when microphone is open."""
        self.agent.open_mic()
        result = self.agent.listen("User message")
        self.assertIn("Received", result)
        self.assertIn("User message", result)
    
    def test_introduce(self):
        """Test agent introduction."""
        result = self.agent.introduce()
        self.assertIn("TestAgent", result)
        self.assertIn("Testing", result)
    
    def test_message_history(self):
        """Test message history tracking."""
        self.agent.open_mic()
        self.agent.speak("Message 1")
        self.agent.listen("Input 1")
        self.agent.speak("Message 2")
        
        history = self.agent.get_message_history()
        self.assertEqual(len(history), 3)
    
    def test_multiple_agents(self):
        """Test multiple agents can coexist."""
        agent1 = ProfessionalAgent(name="Agent1", specialty="Sales")
        agent2 = ProfessionalAgent(name="Agent2", specialty="Support")
        
        agent1.open_mic()
        agent2.open_mic()
        
        msg1 = agent1.speak("From Agent 1")
        msg2 = agent2.speak("From Agent 2")
        
        self.assertIn("Agent1", msg1)
        self.assertIn("Agent2", msg2)
        self.assertNotEqual(msg1, msg2)


if __name__ == "__main__":
    unittest.main()
