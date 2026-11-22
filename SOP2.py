from datetime import datetime
from math import ceil

sessions = {}
price_per_hour = 150

def register_session(plate):
    plate = plate.upper().replace(" ", "")
    sessions[plate] = {"entry": datetime.now(), "paid": False}


def calculate_cost(plate):
    session = sessions[plate]
    minutes = int((datetime.now() - session["entry"]).total_seconds() / 60)
    hours = ceil(minutes / 60)
    return hours * price_per_hour


def process_payment(plate, approved):
    if approved:
        sessions[plate]["paid"] = True
        return True
    return False

def register_session_screen():
    plate = input("Номер автомобиля: ")
    register_session(plate)
    print("Въезд зарегистрирован.")


def process_payment_screen():
    plate = input("Номер автомобиля: ").upper().replace(" ", "")

    if plate not in sessions:
        print("Автомобиль не найден.")
        return

    amount = calculate_cost(plate)
    print(f"К оплате: {amount} руб.")

    answer = input("Оплатить? (да/нет): ").lower()
    if process_payment(plate, answer == "да"):
        print("Оплата прошла успешно.")
    else:
        print("Оплата отменена.")

while True:
    print("\n1. Зарегистрировать въезд")
    print("2. Оплатить парковку")
    print("3. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        register_session_screen()
    elif choice == "2":
        process_payment_screen()
    elif choice == "3":
        break
    else:
        print("Неверный пункт меню.")