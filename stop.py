"""
Simple stop function implementation.
"""
import sys


def stop(exit_code=0, message="Stopping..."):
    """
    Stop function that terminates program execution.
    
    Args:
        exit_code (int): The exit code to return (default: 0)
        message (str): Optional message to print before stopping (default: "Stopping...")
    
    This function gracefully stops the program by calling sys.exit().
    """
    if message:
        print(message)
    sys.exit(exit_code)


if __name__ == "__main__":
    stop()
