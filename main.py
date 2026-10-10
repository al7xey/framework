from datetime import date, datetime

TEACHER_NAME = "Иванова Мария Сергеевна"
SUBJECT = "Математика"
PRICE_PER_HOUR = 1500
WORK_START = 10
WORK_END = 20


def calculate_price(hours, is_first_lesson):
    price = hours * PRICE_PER_HOUR
    if is_first_lesson:
        price = price * 0.8
    elif hours >= 2:
        price = price * 0.9
    return round(price, 2)


def check_time(lesson_date, start_hour, hours):
    if lesson_date < date.today():
        return "Нельзя записаться на прошедшую дату"
    if lesson_date.weekday() == 6:
        return "В воскресенье преподаватель не работает"
    if start_hour < WORK_START or start_hour + hours > WORK_END:
        return f"Занятие должно быть с {WORK_START}:00 до {WORK_END}:00"
    return "ok"


def get_booking_status(subject, balance, price, time_result):
    if subject.lower() != SUBJECT.lower():
        return f"Преподаватель ведет только предмет: {SUBJECT}"
    if time_result != "ok":
        return time_result
    if balance < price:
        return f"Недостаточно средств, не хватает {price - balance} руб."
    return "Запись подтверждена"


print(f"Преподаватель: {TEACHER_NAME}")
print(f"Предмет: {SUBJECT}")
print(f"Стоимость часа: {PRICE_PER_HOUR} руб.")
print()

student_name = input("Ваше имя: ")
subject = input("Предмет: ")
date_text = input("Дата занятия (ДД.ММ.ГГГГ): ")
start_hour = int(input("Час начала (например, 15): "))
hours = int(input("Сколько часов: "))
first_answer = input("Это первое занятие? (да/нет): ")
balance = float(input("Баланс на счете, руб.: "))

lesson_date = datetime.strptime(date_text, "%d.%m.%Y").date()
is_first_lesson = first_answer.lower() == "да"

price = calculate_price(hours, is_first_lesson)
time_result = check_time(lesson_date, start_hour, hours)
status = get_booking_status(subject, balance, price, time_result)

print()
print(f"Ученик: {student_name}")
print(f"Дата: {lesson_date.strftime('%d.%m.%Y')}")
print(f"Время: {start_hour}:00, часов: {hours}")
print(f"К оплате: {price} руб.")
print(status)
