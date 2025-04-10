import os
import time
import threading
from flask import Blueprint, request, render_template, jsonify, redirect, url_for
from .data_handler import load_contacts, load_schedules, load_status, save_status
from .tasks import start_sending, stop_sending, is_sending

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    """Página inicial."""
    contacts = load_contacts()
    schedules = load_schedules()
    
    # Garante que o status tenha a estrutura correta
    status = load_status()
    if not status:
        status = {
            "general": {
                "is_running": False,
                "total_contacts": 0,
                "processed_contacts": 0,
                "success_count": 0,
                "error_count": 0
            },
            "contacts": {}
        }
    elif "general" not in status:
        status["general"] = {
            "is_running": False,
            "total_contacts": 0,
            "processed_contacts": 0,
            "success_count": 0,
            "error_count": 0
        }
    elif "contacts" not in status:
        status["contacts"] = {}
    
    return render_template(
        'index.html',
        contacts_count=len(contacts),
        contacts=contacts,
        schedules=schedules,
        contacts_progress=status
    )

@main_bp.route("/send_now", methods=["POST"])
def send_now():
    data = request.get_json()
    message_template = data.get("message", "").strip()
    if not message_template:
        return "Mensagem vazia!", 400

    contacts = load_contacts()
    if len(contacts) == 0:
        return "Não há contatos.", 400

    # Tenta iniciar o envio. Se retornar False, já existe um envio em andamento.
    if not start_sending(contacts, message_template):
        return "Já existe um envio em andamento.", 400

    return "Envio iniciado com sucesso!", 200

@main_bp.route("/stop", methods=["POST"])
def stop_route():
    """Define a flag de parada."""
    stop_sending()
    return "<p>Parada solicitada. <a href='/'>Voltar</a></p>"

@main_bp.route("/exit", methods=["POST"])
def exit_app():
    """Encerra o servidor."""
    def shutdown():
        time.sleep(1)
        os._exit(0)

    threading.Thread(target=shutdown).start()
    return "<p>Servidor encerrado, pode fechar a janela.</p>"

@main_bp.route("/status", methods=["GET"])
def get_status():
    """
    Retorna o status de envio dos contatos em JSON.
    """
    status = load_status()
    if not status:
        status = {
            "general": {
                "is_running": False,
                "total_contacts": 0,
                "processed_contacts": 0,
                "success_count": 0,
                "error_count": 0
            },
            "contacts": {}
        }
    elif "general" not in status:
        status["general"] = {
            "is_running": False,
            "total_contacts": 0,
            "processed_contacts": 0,
            "success_count": 0,
            "error_count": 0
        }
    elif "contacts" not in status:
        status["contacts"] = {}
    
    print(f"[DEBUG] Status route - status: {status}")
    return jsonify(status)

@main_bp.route("/clear_status", methods=["POST"])
def clear_status():
    """Limpa o status de envio."""
    # Cria um status vazio
    empty_status = {
        "general": {
            "is_running": False,
            "total_contacts": 0,
            "processed_contacts": 0,
            "success_count": 0,
            "error_count": 0
        },
        "contacts": {}
    }
    save_status(empty_status)
    return redirect(url_for('main.index'))
