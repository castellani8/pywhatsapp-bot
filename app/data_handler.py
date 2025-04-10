import json
import os

# Caminhos para os arquivos de dados
CONTACTS_FILE = os.path.join('data', 'contacts.json')
SCHEDULES_FILE = os.path.join('data', 'schedules.json')
STATUS_FILE = os.path.join('data', 'status.json')

def load_contacts():
    """Carrega contatos de um JSON."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    try:
        with open(CONTACTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def load_schedules():
    """Carrega agendamentos de um JSON."""
    if not os.path.exists(SCHEDULES_FILE):
        return []
    try:
        with open(SCHEDULES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_schedules(schedules):
    """Salva lista de agendamentos em JSON."""
    with open(SCHEDULES_FILE, 'w', encoding='utf-8') as f:
        json.dump(schedules, f, ensure_ascii=False, indent=2)

def load_status():
    """Carrega o status de envio dos contatos."""
    if not os.path.exists(STATUS_FILE):
        return {}
    try:
        with open(STATUS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_status(status):
    """Salva o status de envio dos contatos."""
    with open(STATUS_FILE, 'w', encoding='utf-8') as f:
        json.dump(status, f, ensure_ascii=False, indent=2)
