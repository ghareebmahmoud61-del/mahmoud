# mahmoud

## ineed - A Simple Need/Requirement Tracker

`ineed` is a lightweight command-line tool for tracking your needs, requirements, or tasks.

## Features

- ✅ Add new needs with priority levels
- 📋 List active and completed needs
- ✓ Mark needs as completed
- 🗑️ Remove needs
- 💾 Persistent storage in JSON format

## Installation

```bash
# Clone the repository
git clone https://github.com/ghareebmahmoud61-del/mahmoud.git
cd mahmoud

# Make the script executable (Unix/Linux/Mac)
chmod +x ineed.py
```

## Usage

### Add a new need

```bash
python3 ineed.py add "Learn Python" -p high
python3 ineed.py add "Buy groceries"
```

### List needs

```bash
# List active needs
python3 ineed.py list

# List all needs (including completed)
python3 ineed.py list --all
```

### Complete a need

```bash
python3 ineed.py complete 1
```

### Remove a need

```bash
python3 ineed.py remove 2
```

## Options

### Priority Levels
- `low` - Low priority
- `medium` - Medium priority (default)
- `high` - High priority

## Examples

```bash
# Add a high-priority need
$ python3 ineed.py add "Finish project report" -p high
Added need #1: Finish project report (priority: high)

# Add a normal need
$ python3 ineed.py add "Call dentist"
Added need #2: Call dentist (priority: medium)

# List all active needs
$ python3 ineed.py list
ID    Status       Priority   Description
----------------------------------------------------------------------
1     ○ Pending    high       Finish project report
2     ○ Pending    medium     Call dentist

# Complete a need
$ python3 ineed.py complete 1
Completed need #1: Finish project report

# List with completed needs
$ python3 ineed.py list --all
ID    Status       Priority   Description
----------------------------------------------------------------------
1     ✓ Completed  high       Finish project report
2     ○ Pending    medium     Call dentist
```

## Data Storage

Needs are stored in a `needs.json` file in the current directory. This file is automatically created when you add your first need.

## Requirements

- Python 3.6 or higher
- No external dependencies required

## License

This project is open source and available under the MIT License.