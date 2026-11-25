# Список парковочных сессий и платежей
sessions = []
payments = []

PRICE_PER_HOUR = 150
FREE_MINUTES = 15


def register_session(sessions, plate):
    """Создаёт парковочную сессию после проверки номера."""
    plate = plate.upper().replace(" ", "")

    if plate == "":
        return {"ok": False, "message": "Ошибка: номер автомобиля пуст."}

    # Проверяем, нет ли уже активной сессии для этой машины
    for session in sessions:
        if session["plate"] == plate and session["status"] == "активна":
            return {
                "ok": False,
                "message": "Ошибка: для автомобиля уже есть активная сессия."
            }

    session = {
        "plate": plate,
        "status": "активна",
        "amount": 0,
        "receipt": ""
    }
    sessions.append(session)

    return {
        "ok": True,
        "message": "Въезд зарегистрирован.",
        "session": session
    }


def calculate_cost(session, parked_minutes):
    """Рассчитывает стоимость по длительности парковки."""
    if session["status"] != "активна":
        return {"ok": False, "message": "Ошибка: сессия не активна."}

    if parked_minutes < 0:
        return {"ok": False, "message": "Ошибка: время не может быть отрицательным."}

    billable_minutes = parked_minutes - FREE_MINUTES

    if billable_minutes <= 0:
        amount = 0
    else:
        # Каждый начатый час оплачивается полностью
        hours = billable_minutes // 60
        if billable_minutes % 60 > 0:
            hours = hours + 1
        amount = hours * PRICE_PER_HOUR

    session["amount"] = amount

    return {
        "ok": True,
        "message": "Стоимость рассчитана.",
        "amount": amount
    }


def process_payment(session, payments, answer):
    """Имитирует платёж и сохраняет его результат."""
    if session["status"] != "активна":
        return {"ok": False, "message": "Ошибка: сессия не активна."}

    if answer != "да" and answer != "нет":
        return {"ok": False, "message": "Ошибка: введите «да» или «нет»."}

    if answer == "нет":
        payments.append({
            "plate": session["plate"],
            "amount": session["amount"],
            "status": "отклонён"
        })
        return {"ok": False, "message": "Оплата отменена."}

    payments.append({
        "plate": session["plate"],
        "amount": session["amount"],
        "status": "успешен"
    })
    session["status"] = "оплачена"

    return {"ok": True, "message": "Платёж прошёл успешно."}


def finalize_session(session, payments):
    """Завершает оплаченную сессию и формирует номер чека."""
    if session["status"] != "оплачена":
        return {
            "ok": False,
            "message": "Ошибка: нельзя завершить неоплаченную сессию."
        }

    receipt_number = "ЧЕК-" + str(len(payments))
    session["status"] = "завершена"
    session["receipt"] = receipt_number

    return {
        "ok": True,
        "message": "Парковочная сессия завершена.",
        "receipt": receipt_number
    }


# Консольный интерфейс: здесь находятся input() и print()
while True:
    print("\nСистема оплаты парковки")
    print("1. Зарегистрировать въезд")
    print("2. Рассчитать стоимость и оплатить")
    print("3. Проверить статус")
    print("4. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        plate = input("Введите номер автомобиля: ")
        result = register_session(sessions, plate)
        print(result["message"])

    elif choice == "2":
        plate = input("Введите номер автомобиля: ").upper().replace(" ", "")

        # Ищем активную сессию
        found_session = None
        for session in sessions:
            if session["plate"] == plate and session["status"] == "активна":
                found_session = session

        if found_session is None:
            print("Ошибка: активная сессия не найдена.")
        else:
            minutes_text = input("Сколько минут автомобиль стоял? ")

            if not minutes_text.isdigit():
                print("Ошибка: введите время целым положительным числом.")
            else:
                cost_result = calculate_cost(found_session, int(minutes_text))

                if cost_result["ok"]:
                    print("К оплате:", cost_result["amount"], "руб.")

                    paid = False
                    while not paid:
                        answer = input("Имитировать успешную оплату? (да/нет): ")
                        payment_result = process_payment(
                            found_session, payments, answer.lower()
                        )
                        print(payment_result["message"])

                        if payment_result["ok"]:
                            final_result = finalize_session(
                                found_session, payments
                            )
                            print(final_result["message"])
                            print("Номер чека:", final_result["receipt"])
                            paid = True
                        elif answer.lower() == "нет":
                            break
                else:
                    print(cost_result["message"])

    elif choice == "3":
        plate = input("Введите номер автомобиля: ").upper().replace(" ", "")
        found_session = None

        for session in sessions:
            if session["plate"] == plate:
                found_session = session

        if found_session is None:
            print("Ошибка: сессия не найдена.")
        else:
            print("Статус сессии:", found_session["status"])

    elif choice == "4":
        print("Программа завершена.")
        break

    else:
        print("Ошибка: выберите пункт меню от 1 до 4.")