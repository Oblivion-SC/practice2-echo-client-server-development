import socket

def main():
    # СОЗДАНИЕ СОКЕТА КЛИЕНТА
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # ТОТ ЖЕ АДРЕС И ПОРТ, ЧТО И У СЕРВЕРА
    host = '127.0.0.1'  # localhost
    port = 12345         # должен совпадать с портом сервера
    
    try:
        # ПОДКЛЮЧЕНИЕ К СЕРВЕРУ
        client_socket.connect((host, port))
        print(f"[КЛИЕНТ] Подключен к серверу {host}:{port}")
        print("[КЛИЕНТ] Введите сообщения. Для выхода введите 'exit' или 'quit'\n")
        
        while True:
            # ВВОД СООБЩЕНИЯ
            user_input = input("Вы: ")
            
            # ПРОВЕРКА ВЫХОДА
            if user_input.lower() in ('exit', 'quit'):
                print("[КЛИЕНТ] Завершение работы...")
                client_socket.send(user_input.encode('utf-8'))
                break
            
            # ОТПРАВКА
            client_socket.send(user_input.encode('utf-8'))
            print(f"[КЛИЕНТ] Отправлено: '{user_input}'")
            
            # ПОЛУЧЕНИЕ ОТВЕТА
            raw_response = client_socket.recv(1024)
            if not raw_response:
                print("[КЛИЕНТ] Сервер разорвал соединение")
                break
                
            response_message = raw_response.decode('utf-8')
            print(f"[КЛИЕНТ] Ответ сервера: '{response_message}'\n")
            
    except ConnectionRefusedError:
        print("[КЛИЕНТ] ОШИБКА: Сервер не запущен!")
        print("[КЛИЕНТ] Сначала запустите echo_server.py")
    except Exception as e:
        print(f"[КЛИЕНТ] Ошибка: {e}")
    finally:
        client_socket.close()
        print("[КЛИЕНТ] Соединение закрыто")

if __name__ == "__main__":
    main()