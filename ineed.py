#!/usr/bin/env python3
"""
ineed - A simple utility to manage and track needs/requirements

This module provides functionality to:
- Add new needs/requirements
- List existing needs
- Mark needs as completed
- Remove needs
"""

import json
import os
import sys
from datetime import datetime
from typing import List, Dict, Optional


class INeed:
    """Main class for managing needs/requirements"""
    
    def __init__(self, data_file: str = "needs.json"):
        """Initialize the INeed manager
        
        Args:
            data_file: Path to the JSON file storing needs
        """
        self.data_file = data_file
        self.needs: List[Dict] = []
        self.load_needs()
    
    def load_needs(self) -> None:
        """Load needs from the data file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.needs = json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading needs: {e}", file=sys.stderr)
                self.needs = []
        else:
            self.needs = []
    
    def save_needs(self) -> None:
        """Save needs to the data file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.needs, f, indent=2)
        except IOError as e:
            print(f"Error saving needs: {e}", file=sys.stderr)
    
    def add_need(self, description: str, priority: str = "medium") -> Dict:
        """Add a new need
        
        Args:
            description: Description of the need
            priority: Priority level (low, medium, high)
            
        Returns:
            The created need dictionary
            
        Raises:
            ValueError: If priority is not one of low, medium, high
        """
        # Validate priority
        valid_priorities = ["low", "medium", "high"]
        if priority not in valid_priorities:
            raise ValueError(f"Priority must be one of {valid_priorities}, got '{priority}'")
        
        # Calculate next ID based on max existing ID
        next_id = max([need["id"] for need in self.needs], default=0) + 1
        
        need = {
            "id": next_id,
            "description": description,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().isoformat(),
            "completed_at": None
        }
        self.needs.append(need)
        self.save_needs()
        return need
    
    def list_needs(self, show_completed: bool = False) -> List[Dict]:
        """List all needs
        
        Args:
            show_completed: Whether to include completed needs
            
        Returns:
            List of needs
        """
        if show_completed:
            return self.needs
        return [need for need in self.needs if not need["completed"]]
    
    def complete_need(self, need_id: int) -> Optional[Dict]:
        """Mark a need as completed
        
        Args:
            need_id: ID of the need to complete
            
        Returns:
            The updated need or None if not found
        """
        for need in self.needs:
            if need["id"] == need_id:
                need["completed"] = True
                need["completed_at"] = datetime.now().isoformat()
                self.save_needs()
                return need
        return None
    
    def remove_need(self, need_id: int) -> bool:
        """Remove a need
        
        Args:
            need_id: ID of the need to remove
            
        Returns:
            True if removed, False if not found
        """
        for i, need in enumerate(self.needs):
            if need["id"] == need_id:
                self.needs.pop(i)
                self.save_needs()
                return True
        return False


def main():
    """Command-line interface for INeed"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="ineed - Manage your needs/requirements"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new need")
    add_parser.add_argument("description", help="Description of the need")
    add_parser.add_argument(
        "-p", "--priority",
        choices=["low", "medium", "high"],
        default="medium",
        help="Priority level"
    )
    
    # List command
    list_parser = subparsers.add_parser("list", help="List needs")
    list_parser.add_argument(
        "-a", "--all",
        action="store_true",
        help="Show completed needs as well"
    )
    
    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a need as completed")
    complete_parser.add_argument("id", type=int, help="ID of the need to complete")
    
    # Remove command
    remove_parser = subparsers.add_parser("remove", help="Remove a need")
    remove_parser.add_argument("id", type=int, help="ID of the need to remove")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    manager = INeed()
    
    if args.command == "add":
        try:
            need = manager.add_need(args.description, args.priority)
            print(f"Added need #{need['id']}: {need['description']} (priority: {need['priority']})")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    
    elif args.command == "list":
        needs = manager.list_needs(show_completed=args.all)
        if not needs:
            print("No needs found.")
        else:
            print(f"{'ID':<5} {'Status':<12} {'Priority':<10} {'Description'}")
            print("-" * 70)
            for need in needs:
                status = "✓ Completed" if need["completed"] else "○ Pending"
                print(f"{need['id']:<5} {status:<12} {need['priority']:<10} {need['description']}")
    
    elif args.command == "complete":
        need = manager.complete_need(args.id)
        if need:
            print(f"Completed need #{need['id']}: {need['description']}")
        else:
            print(f"Need #{args.id} not found.", file=sys.stderr)
            sys.exit(1)
    
    elif args.command == "remove":
        if manager.remove_need(args.id):
            print(f"Removed need #{args.id}")
        else:
            print(f"Need #{args.id} not found.", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
