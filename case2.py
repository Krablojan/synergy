def is_leap_year(year):
  """Проверяет, является ли год високосным."""
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
      return True
  return False

def get_day_of_week(day, month, year):
  """Определяет день недели для заданной даты (алгоритм Зеллера)."""
  if month < 3:
      month += 12
      year -= 1
  K = year % 100
  J = year // 100
  f = day + ((13 * (month + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)
  day_of_week = f % 7
  # Преобразуем день недели в нужный формат (0 - суббота, 1 - воскресенье, ..., 6 - пятница)
  day_of_week = (day_of_week + 6) % 7
  return day_of_week

def get_age(day, month, year):
  """Вычисляет текущий возраст пользователя."""
  current_day = 28
  current_month = 12
  current_year = 2024

  if (current_month < month) or (current_month == month and current_day < day):
      return current_year - year - 1
  return current_year - year

def print_styled_date(day, month, year):
  """Выводит дату в стилизованном формате."""
  styled_day = ''.join(['*****' if char.isdigit() else char for char in f'{day:02}'])
  styled_month = ''.join(['*****' if char.isdigit() else char for char in f'{month:02}'])
  styled_year = ''.join(['*****' if char.isdigit() else char for char in f'{year}'])
  print(f'{styled_day} {styled_month} {styled_year}')

def main():
  day = int(input("Введите день рождения (число): "))
  month = int(input("Введите месяц рождения (число): "))
  year = int(input("Введите год рождения (число): "))

  day_of_week = get_day_of_week(day, month, year)
  days = ["Суббота", "Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
  leap_year = is_leap_year(year)
  age = get_age(day, month, year)

  print(f"Ваша дата рождения: {day:02} {month:02} {year}")
  print(f"Это был {days[day_of_week]}.")
  if leap_year:
      print("Год был високосным.")
  else:
      print("Год не был високосным.")
  print(f"Вам сейчас {age} лет.")
  print("Ваша дата рождения в стилизованном формате:")
  print_styled_date(day, month, year)

if __name__ == "__main__":
  main()
