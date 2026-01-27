"""
Simple stop function implementation.
"""
import sys


def stop(exit_code=0):
    """
    Stop function that terminates program execution.
    
    Args:
        exit_code (int): The exit code to return (default: 0)
    
    This function gracefully stops the program by calling sys.exit().
    """
    print("Stopping...")
    sys.exit(exit_code)


if __name__ == "__main__":
    stop()
