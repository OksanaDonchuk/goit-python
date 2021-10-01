from datetime import datetime
from datetime import date
from datetime import timedelta
from collections import defaultdict


def congratulate(birthdays_list):

    result_birthdays = defaultdict(list)

    current_date = datetime.now().date()
    current_date_2 = datetime.now().date().isocalendar()
    working_days = [1, 2, 3, 4, 5]
    weekend_days = [6, 7]

    for user in birthdays_list:

        user_date_birth = user['birthday'].date()
        user_date_birth2 = user['birthday'].date().isocalendar()

        birthday_weekday_name = user_date_birth.replace(
            current_date.year).strftime('%A')

        user_birth_week = user_date_birth.replace(
            current_date.year).isocalendar().week

        current_week = current_date_2.week

        user_birth_weekday = user_date_birth.replace(
            current_date.year).isocalendar().weekday

        if user_birth_week == current_week and user_birth_weekday in weekend_days:
            result_birthdays['Monday'].append(user['name'])

        elif user_birth_week == current_week + 1 and user_birth_weekday in working_days:
            result_birthdays[birthday_weekday_name].append(
                user['name'])

    return result_birthdays


def main():

    users = [
        {'name': 'Tanya', 'birthday': datetime.strptime(
            '15.05.1953', '%d.%m.%Y')},
        {'name': 'Oksana', 'birthday': datetime.strptime(
            '09.02.1980', '%d.%m.%Y')},
        {'name': 'Helen', 'birthday': datetime.strptime(
            '07.06.1984', '%d.%m.%Y')},
        {'name': 'Aleks', 'birthday': datetime.strptime(
            '06.05.1978', '%d.%m.%Y')},
        {'name': 'Vlad', 'birthday': datetime.strptime(
            '25.05.1999', '%d.%m.%Y')},
        {'name': 'Andrew', 'birthday': datetime.strptime(
            '19.05.1991', '%d.%m.%Y')},
        {'name': 'Den', 'birthday': datetime.strptime(
            '14.05.1975', '%d.%m.%Y')},
        {'name': 'Volodya', 'birthday': datetime.strptime(
            '20.05.1994', '%d.%m.%Y')}]

    result_birthdays = congratulate(users)

    week_days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    for day in week_days_list:

        for key, val in result_birthdays.items():
            if day == key and len(val) > 0:
                print(f'{key}: {", ".join(val)}')


if __name__ == '__main__':
    main()
