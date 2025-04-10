import os
import time
import threading
from flask import Blueprint, request, render_template, redirect, url_for

from .data_handler import load_contacts, load_schedules, save_schedules
from .tasks import start_sending, stop_sending, is_sending

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    contacts = load_contacts()
    schedules = load_schedules()
    return render_template(
        'index.html',
        contacts_count=len(contacts),
        contacts=contacts,
        schedules=schedules
    )


@main_bp.route("/send_now", methods=["POST"])
def send_now():
    """Inicia o envio imediato de mensagens (em uma thread) usando o template passado."""
    message_template = request.form.get("message", "").strip()
    if not message_template:
        return "<p>Mensagem vazia. <a href='/'>Voltar</a></p>"

    contacts = load_contacts()
    if len(contacts) == 0:
        return "<p>Não há contatos. <a href='/'>Voltar</a></p>"

    # Tenta iniciar o envio. Se retornar False, já existe um envio em andamento.
    if not start_sending(contacts, message_template):
        return "<p>Já existe um envio em andamento! <a href='/'>Voltar</a></p>"

    return """
    <p>Envio iniciado em segundo plano. 
    <a href="/">Voltar</a></p>
    """

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
