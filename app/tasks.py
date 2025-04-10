import time
import threading
import pywhatkit
from .config import INTERVALO_ENVIO, WAIT_TIME, CLOSE_TIME

# Variáveis globais para controle de envio
sending_thread = None  # Thread que faz o envio
stop_flag = False      # Sinal para parar envio em andamento

def start_sending(contacts, message_template):
    """Inicia o envio em uma thread separada."""
    global sending_thread, stop_flag

    # Se já houver um envio em andamento, não inicia outro
    if sending_thread and sending_thread.is_alive():
        return False  # Indica que já há um envio em andamento

    # Reseta o stop_flag antes de iniciar
    stop_flag = False

    def envio_thread():
        total = len(contacts)
        for i, c in enumerate(contacts, start=1):
            if stop_flag:
                print("[INFO] Envio interrompido pelo usuário.")
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
                time.sleep(INTERVALO_ENVIO)
            except Exception as e:
                print("[ERRO]", e)

        print("[INFO] Envio finalizado!")

    sending_thread = threading.Thread(target=envio_thread)
    sending_thread.daemon = True
    sending_thread.start()
    return True

def stop_sending():
    """Define a flag de parada."""
    global stop_flag
    stop_flag = True

def is_sending():
    """Retorna True se estiver enviando mensagens no momento."""
    global sending_thread
    return sending_thread is not None and sending_thread.is_alive()
