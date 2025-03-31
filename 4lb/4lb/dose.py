import datetime

class MedicationReminder:
    def __init__(self):
        self.schedule = []
        self.missed_meds = []

    def add_med(self, name, times, before_meal, after_meal):
        for time in times:
            self.schedule.append({'name': name, 'time': time, 'before_meal': before_meal, 'after_meal': after_meal})

    def check_reminders(self):
        current_time = datetime.datetime.now()
        reminders = []
        future_reminders = []

        for med in self.schedule:
            med_time = datetime.datetime.strptime(med['time'], '%H:%M').replace(year=current_time.year,
                                                                                month=current_time.month,
                                                                                day=current_time.day)

            # Напоминание за 30 минут до приема пищи
            if med['before_meal'] and med_time - datetime.timedelta(minutes=30) <= current_time < med_time:
                reminders.append((med['name'], med['time'], f"Примите {med['name']} за 30 минут до еды."))

            # Напоминание через 1 час после окончания приема пищи
            if med['after_meal'] and med_time < current_time < med_time + datetime.timedelta(hours=1):
                reminders.append((med['name'], med['time'], f"Примите {med['name']} через 1 час после еды."))

            # Напоминание в установленное время
            if not med['before_meal'] and not med['after_meal'] and med_time <= current_time < med_time + datetime.timedelta(minutes=30):
                reminders.append((med['name'], med['time'], f"Примите {med['name']} в установленное время."))

            # Пропущенный прием
            if current_time > med_time + datetime.timedelta(minutes=30):
                response = input(f"Вы пропустили приём {med['name']} в {med['time']}. Вы его приняли? (да/нет): ")
                if response.lower() == 'нет':
                    self.missed_meds.append(med)
                reminders.append((med['name'], med['time'], f"Вы пропустили приём {med['name']}."))

            # Будущие напоминания
            elif current_time < med_time:
                future_reminders.append((med['name'], med['time'], f"Будущее напоминание: {med['name']}."))

        return reminders, future_reminders

    def get_missed_meds(self):
        return self.missed_meds


def main():
    reminder_system = MedicationReminder()

    while True:
        cat_name = input("Введите название лекарства (или 'всё' для выхода): ")
        if cat_name.lower() == 'всё':
            break

        cat_times = input("Введите время приёма (в формате HH:MM, разделяя запятыми для нескольких времён): ")
        cat_times = [time.strip() for time in cat_times.split(',')]

        cat_before_meal = input("Принимается до еды? (да/нет): ") == 'да'
        cat_after_meal = input("Принимается после еды? (да/нет): ") == 'да'

        reminder_system.add_med(cat_name, cat_times, cat_before_meal, cat_after_meal)

    reminders, future_reminders = reminder_system.check_reminders()

    print("\nСписок напоминаний:")
    print(f"{'Название':<20} {'Время':<10} {'Напоминание'}")
    print("-" * 50)
    if reminders:
        for name, time, reminder in reminders:
            print(f"{name:<20} {time:<10} {reminder}")
    else:
        print("На данный момент нет напоминаний.")

    print("\nБудущие напоминания:")
    print(f"{'Название':<20} {'Время':<10} {'Напоминание'}")
    print("-" * 50)
    if future_reminders:
        for name, time, reminder in future_reminders:
            print(f"{name:<20} {time:<10} {reminder}")
    else:
        print("На данный момент нет будущих напоминаний.")

    missed_meds = reminder_system.get_missed_meds()
    if missed_meds:
        print("\nПропущенные лекарства:")
        for med in missed_meds:
            print(f"{med['name']} в {med['time']} (пропущено)")

if __name__ == "__main__":
    main()
