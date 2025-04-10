# WhatsApp Bot Web Interface

A Flask-based web application for managing and automating WhatsApp message sending with a user-friendly interface.

## Features

- 🌐 Web-based interface for easy management
- 📱 WhatsApp message automation
- 📋 Contact list management
- ⏱️ Scheduled message sending
- 🔄 Real-time sending progress tracking
- ⏱️ Elapsed time tracking
- ⏹️ Ability to stop ongoing message sending
- 🧹 Status clearing functionality
- 📊 JSON-based data storage
- 🧵 Thread-safe message sending

## Project Structure

```
pywhatsapp-bot/
├── app/
│   ├── __init__.py      # Flask application factory
│   ├── config.py        # Application configuration
│   ├── data_handler.py  # JSON data management
│   ├── routes.py        # Flask routes and views
│   ├── tasks.py         # Message sending logic
│   └── templates/       # HTML templates
├── data/
│   ├── contacts.json    # Contact list storage
│   ├── schedules.json   # Message schedules storage
│   └── status.json      # Message sending status storage
├── run.py              # Application entry point
└── requirements.txt    # Project dependencies
```

## Prerequisites

- Python 3.7 or higher
- WhatsApp Web access
- Chrome browser (for WhatsApp Web automation)
- Flask (web framework)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pywhatsapp-bot.git
cd pywhatsapp-bot
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

The application uses the following configuration (in `app/config.py`):
```python
SEND_INTERVAL = 10   # Seconds between each message
WAIT_TIME = 15      # Time pywhatkit waits before sending
CLOSE_TIME = 5      # Time until WhatsApp tab closes
```

## Usage

1. Start the web server:
```bash
python run.py
```

2. Open your browser and navigate to `http://localhost:5000`

3. Use the web interface to:
   - View and manage contacts
   - Send messages immediately
   - Schedule messages
   - Monitor sending progress in real-time
   - View elapsed time
   - Stop ongoing message sending
   - Clear sending status

## Data Management

### Contacts
Contacts are stored in `data/contacts.json`:
```json
[
    {"name": "Contact Name", "phone": "+5511999999999"},
    {"name": "Another Contact", "phone": "+5511999999999"}
]
```

### Schedules
Message schedules are stored in `data/schedules.json`

### Status
Message sending status is stored in `data/status.json`:
```json
{
  "general": {
    "is_running": false,
    "total_contacts": 10,
    "processed_contacts": 3,
    "success_count": 2,
    "error_count": 1,
    "start_time": 1234567890.123,
    "end_time": 1234567891.123,
    "elapsed_time": 1.0
  },
  "contacts": {
    "11999999999": {
      "status": "success",
      "name": "John Doe"
    }
  }
}
```

## Web Interface Features

1. **Dashboard**
   - View contact list
   - See sending progress
   - Check scheduled messages
   - Monitor elapsed time
   - View success/error counts

2. **Message Sending**
   - Send messages immediately
   - Use message templates
   - Monitor sending progress in real-time
   - Stop sending if needed
   - Clear sending status

3. **Status Tracking**
   - Real-time progress updates
   - Success/error counts
   - Elapsed time display
   - Individual contact status
   - Process completion status

4. **Contact Management**
   - View all contacts
   - Add new contacts
   - Edit existing contacts

## Best Practices

1. **Message Sending**:
   - Keep message intervals reasonable
   - Monitor sending progress
   - Use appropriate wait times
   - Check success/error counts

2. **Contact Management**:
   - Keep contact list updated
   - Use proper phone number format
   - Verify contacts before sending

3. **Web Interface**:
   - Don't close browser during sending
   - Monitor sending progress
   - Use stop button if needed
   - Clear status when starting new session

## Troubleshooting

1. **Web Interface Issues**:
   - Check if server is running
   - Verify port 5000 is available
   - Clear browser cache if needed

2. **Message Sending Problems**:
   - Ensure WhatsApp Web is open
   - Check internet connection
   - Verify contact numbers
   - Check success/error counts

3. **Data Issues**:
   - Check JSON file permissions
   - Verify file encoding
   - Ensure proper JSON format

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Acknowledgments

- Flask for the web framework
- pywhatkit for WhatsApp automation
- Python community for excellent tools