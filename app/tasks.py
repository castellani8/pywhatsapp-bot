# tasks.py
import time
import threading
import pywhatkit
from .config import SEND_INTERVAL, WAIT_TIME, CLOSE_TIME
from .data_handler import load_status, save_status

# Variáveis globais para controle de envio
sending_thread = None
stop_flag = False

def start_sending(contacts, message_template):
    """Inicia o envio em uma thread separada."""
    global sending_thread, stop_flag

    # Se já houver um envio em andamento, não inicia outro
    if sending_thread and sending_thread.is_alive():
        return False  # Indica que já há um envio em andamento

    # Inicializa o status no arquivo JSON
    status = {
        "general": {
            "is_running": True,
            "total_contacts": len(contacts),
            "processed_contacts": 0,
            "success_count": 0,
            "error_count": 0
        },
        "contacts": {}
    }
    
    # Inicializa o status de cada contato
    for c in contacts:
        phone = c.get("phone", "")
        if phone:
            status["contacts"][phone] = {
                "status": "pending",
                "name": c.get("name", "SemNome")
            }
    
    save_status(status)
    print(f"[DEBUG] Initial status saved: {status}")

    # Reseta o stop_flag antes de iniciar
    stop_flag = False

    def envio_thread():
        total = len(contacts)
        for i, c in enumerate(contacts, start=1):
            if stop_flag:
                print("[INFO] Envio interrompido pelo usuário.")
                # Atualiza o status geral para parado
                status = load_status()
                status["general"]["is_running"] = False
                save_status(status)
                break

            name = c.get("name", "SemNome")
            phone = c.get("phone", "")
            msg_final = message_template.replace("{name}", name)

            print(f"[INFO] Enviando {i}/{total} -> {name} ({phone})")
            if not phone:
                print("[ERRO] Telefone vazio!")
                continue

            try:
                pywhatkit.sendwhatmsg_instantly(
                    phone_no=phone,
                    message=msg_final,
                    wait_time=WAIT_TIME,
                    tab_close=True,
                    close_time=CLOSE_TIME
                )
                # Atualiza o status no arquivo JSON
                status = load_status()
                status["contacts"][phone]["status"] = "success"
                status["general"]["processed_contacts"] += 1
                status["general"]["success_count"] += 1
                save_status(status)
                print(f"[DEBUG] Updated status for {phone}: success")
                time.sleep(SEND_INTERVAL)
            except Exception as e:
                print("[ERRO]", e)
                # Atualiza o status no arquivo JSON
                status = load_status()
                status["contacts"][phone]["status"] = "error"
                status["general"]["processed_contacts"] += 1
                status["general"]["error_count"] += 1
                save_status(status)
                print(f"[DEBUG] Updated status for {phone}: error")

        # Atualiza o status geral para finalizado
        status = load_status()
        status["general"]["is_running"] = False
        save_status(status)
        print(f"[DEBUG] Final status: {load_status()}")

    sending_thread = threading.Thread(target=envio_thread)
    sending_thread.daemon = True
    sending_thread.start()
    return True

def stop_sending():
    """Define a flag de parada."""
    global stop_flag
    stop_flag = True
    # Atualiza o status geral para parado
    status = load_status()
    if status and "general" in status:
        status["general"]["is_running"] = False
        save_status(status)

def is_sending():
    """Retorna True se estiver enviando mensagens no momento."""
    global sending_thread
    return sending_thread is not None and sending_thread.is_alive()
