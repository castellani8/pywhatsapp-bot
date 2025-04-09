import pywhatkit
import time
import json

BASE_MSG = "Olá {name}, tudo bem? Esta é apenas uma mensagem de teste!"

def main(): 
    contacts = load_contacts()

    for contact in contacts:
        name = contact["name"]
        phone = contact["phone"]

        msg = BASE_MSG.format(name=name)
        print(f"Sending message to {name} ({phone})")
        send_message(phone, msg)

        time.sleep(10)

def load_contacts():
    try:
        return json.load(open('data/contacts.json'))
    except FileNotFoundError:
        print("Arquivo de contatos não encontrado. Criando arquivo padrão.")
        return []
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo de contatos. Criando arquivo padrão.")
        return []
    
def send_message(phone, msg):
    pywhatkit.sendwhatmsg_instantly(
        phone_no=phone,
        message=msg,
        wait_time=15,
        tab_close=True,
        close_time=5
    )
    
if __name__ == "__main__":
    main()
