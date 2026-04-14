import socket

def main():
    # СОЗДАНИЕ СОКЕТА СЕРВЕРА
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # ЯВНО УКАЗЫВАЕМ localhost (127.0.0.1) и порт 8888
    host = '127.0.0.1'  # localhost - свой же компьютер
    port = 12345         # можно использовать любой свободный порт (1024-65535)
    
    # ПРИВЯЗКА К АДРЕСУ
    server_socket.bind((host, port))
    
    # НАЧАЛО ПРОСЛУШИВАНИЯ
    server_socket.listen(5)
    print(f"[СЕРВЕР] Запущен на {host}:{port}")
    print(f"[СЕРВЕР] Ожидание подключений...")
    
    try:
        while True:
            # ПРИНЯТИЕ КЛИЕНТА
            client_socket, client_address = server_socket.accept()
            print(f"\n[СЕРВЕР] Подключен клиент: {client_address[0]}:{client_address[1]}")
            
            try:
                while True:
                    # ПОЛУЧЕНИЕ ДАННЫХ
                    raw_data = client_socket.recv(1024)
                    
                    if not raw_data:
                        print(f"[СЕРВЕР] Клиент {client_address} отключился")
                        break
                    
                    received_message = raw_data.decode('utf-8').strip()
                    print(f"[СЕРВЕР] Получено: '{received_message}'")
                    
                    # ПРОВЕРКА КОМАНДЫ ВЫХОДА
                    if received_message.lower() in ('exit', 'quit'):
                        print(f"[СЕРВЕР] Клиент завершил сеанс")
                        client_socket.send(b"Goodbye! Connection closed.")
                        break
                    
                    # МОДИФИКАЦИЯ (эхо + верхний регистр)
                    modified_message = f"ECHO: {received_message.upper()}"
                    
                    # ОТПРАВКА ОБРАТНО
                    client_socket.send(modified_message.encode('utf-8'))
                    print(f"[СЕРВЕР] Отправлено: '{modified_message}'")
                    
            except Exception as e:
                print(f"[СЕРВЕР] Ошибка: {e}")
            finally:
                client_socket.close()
                
    except KeyboardInterrupt:
        print("\n[СЕРВЕР] Остановка сервера...")
    finally:
        server_socket.close()
        print("[СЕРВЕР] Сервер остановлен")

if __name__ == "__main__":
    main()