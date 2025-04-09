import pywhatkit
import time

# Lista de contatos com nome e telefone (adicione ou remova conforme necessário)
contatos = [
    {"nome": "Fulano", "telefone": "+5511999999999"},
    {"nome": "Ciclano", "telefone": "+5511999999999"},
    {"nome": "Beltrano", "telefone": "+5511999999999"}
]

# Mensagem base com um placeholder para inserir o nome
mensagem_base = "Olá {nome}, tudo bem? Esta é apenas uma mensagem de teste!"

# Envia a mensagem para cada contato da lista
for contato in contatos:
    nome = contato["nome"]
    telefone = contato["telefone"]
    
    # Cria a mensagem personalizada
    mensagem_personalizada = mensagem_base.format(nome=nome)
    
    # Envia a mensagem instantaneamente (sem precisar agendar horário)
    # Observações:
    #  - Após abrir o WhatsApp Web, o script aguarda alguns segundos (wait_time)
    #  - tab_close=True fecha a aba do WhatsApp Web automaticamente depois do envio
    #  - close_time define quantos segundos depois do envio a aba será fechada
    pywhatkit.sendwhatmsg_instantly(
        phone_no=telefone,
        message=mensagem_personalizada,
        wait_time=15,   # Tempo de espera para o envio (ajuste conforme a conexão)
        tab_close=True, # Fecha aba depois do envio
        close_time=5    # Tempo até fechar a aba após o envio
    )
    
    # Adicione uma pausa para evitar problemas de envio (ajuste conforme necessário)
    time.sleep(10)
