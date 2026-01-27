# mahmoud

A simple repository with a stop function implementation.

## Usage

```python
from stop import stop

# Call the stop function with default message
stop()

# Call with custom message
stop(message="Goodbye!")

# Call with no message
stop(message=None)

# Call with exit code
stop(exit_code=1, message="Error occurred!")
```