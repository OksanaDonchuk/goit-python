EXIT_COMMANDS = {
    'exit': '',
    'close': '',
    'good': ''
}

phone_book = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print('Invalid command. Try again...')
            return back_to_choice
        except IndexError:
            print('Give me name and phone, please.')
            return back_to_choice(*args, **kwargs)
        except ValueError:
            print('Give me name and phone, please.')
            return back_to_choice(*args, **kwargs)
    return wrapper


def back_to_choice(*args, **kwargs):
    return f''


def parser(user_input):
    return user_input.split(' ')


def hello(*args):
    return f'How can I help you?'


@ input_error
def get_handler(command):
    return COMMANDS[command]


@ input_error
def add(data):
    if data[1] in phone_book:
        return f'The contact in the phone book. Use the command "change"...'
    else:
        phone_book[data[1]] = data[2]
    return f'Contact {data[1]} has been saved.'


@ input_error
def change(data):
    phone_book.update({data[1]: data[2]})
    return f'Contact {data[1]} has been changed.'


@ input_error
def phone(data):
    if data[1] in phone_book:
        return f'{data[1]}: {phone_book.get(data[1])}'
    else:
        return f'The contact is not in the phone book.'


def show_all(*args):
    show_result = ''
    for key, value in phone_book.items():
        show_result += f'{key}: {value}'
    return show_result


def bye(*args):
    return f'Good bye!'


COMMANDS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show_all': show_all


}


def main():
    while True:
        user_input = input(
            'Enter your command (hello, add, change, phone, show_all or exit):...')
        data = parser(user_input)
        if data[0].lower() in EXIT_COMMANDS:
            print(bye())
            break
        else:
            print(get_handler(data[0].lower())(data))


if __name__ == "__main__":
    main()
