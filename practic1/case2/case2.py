def get_user_birthday():
    date_str = input("Введите дату вашего рождения (в формате ДД.ММ.ГГГГ): ")
    day, month, year = map(int, date_str.split('.'))
    return day, month, year

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_week(day, month, year):
    days = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if month < 3:
        year -= 1
    return days[(year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7]

def calculate_age(day, month, year):
    # Вместо использования datetime, просто сравниваем с текущей датой
    current_year = 2025
    current_month = 1
    current_day = 7
    age = current_year - year - ((current_month, current_day) < (month, day))
    return age

def print_digital_date(day, month, year):
    digits = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "    *", " *** ", "*    ", "*****"],
        '3': [" *** ", "    *", " *** ", "    *", " *** "],
        '4': ["*   *", "*   *", "*****", "    *", "    *"],
        '5': ["*****", "*    ", " *** ", "    *", " *** "],
        '6': [" *** ", "*    ", "**** ", "*   *", " *** "],
        '7': ["*****", "    *", "   * ", "  *  ", " *   "],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " ****", "    *", " *** "],
    }

    def render_number(number):
        return [digits[d] for d in str(number)]

    def print_lines(lines):
        for line in lines:
            print(line)

    day_lines = render_number(f"{day:02}")
    month_lines = render_number(f"{month:02}")
    year_lines = render_number(f"{year}")

    combined_lines = [
        ''.join(parts) for parts in zip(
            *day_lines, ["   "] * 5, *month_lines, ["   "] * 5, *year_lines
        )
    ]

    print_lines(combined_lines)

if __name__ == "__main__":
    day, month, year = get_user_birthday()

    week_day = day_of_week(day, month, year)
    leap = is_leap_year(year)
    age = calculate_age(day, month, year)

    print(f"Это была {week_day}.")
    print(f"{year} год был {'високосным' if leap else 'не високосным'}.")
    print(f"Сейчас вам {age} лет.")

    print("Ваш день рождения в цифровом формате:")
    print_digital_date(day, month, year)
