from datetime import datetime
from math import ceil

sessions = {}
price_per_hour = 150
free_minutes = 15


def register_session():
    plate = input("Номер автомобиля: ").upper().replace(" ", "")
    sessions[plate] = {
        "entry": datetime.now(),
        "paid": False
    }
    print("Въезд зарегистрирован.")


def calculate_cost(plate):
    session = sessions[plate]
    parked_minutes = int((datetime.now() - session["entry"]).total_seconds() / 60)
    billable_minutes = max(61, parked_minutes - free_minutes)
    hours = ceil(billable_minutes / 60)
    return hours * price_per_hour


def process_payment():
    plate = input("Номер автомобиля: ").upper().replace(" ", "")

    if plate not in sessions:
        print("Автомобиль не найден.")
        return

    amount = calculate_cost(plate)
    print(f"К оплате: {amount} руб.")

    if input("Оплатить? (да/нет): ").lower() == "да":
        sessions[plate]["paid"] = True
        print("Оплата прошла успешно. Чек выдан.")
    else:
        print("Оплата отменена.")


def finalize_session():
    plate = input("Номер автомобиля: ").upper().replace(" ", "")

    if plate not in sessions:
        print("Сессия не найдена.")
        return

    status = "оплачена" if sessions[plate]["paid"] else "не оплачена"
    print(f"Статус парковки: {status}")


while True:
    print("\n1. Зарегистрировать въезд")
    print("2. Оплатить парковку")
    print("3. Проверить статус")
    print("4. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        register_session()
    elif choice == "2":
        process_payment()
    elif choice == "3":
        finalize_session()
    elif choice == "4":
        break
    else:
        print("Выберите пункт от 1 до 4.")
