def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print(f'\nInvalid command. Try again...')
            return back_to_main
        except IndexError:
            print('\nGive me name and phone, please.')
            return back_to_main(*args, **kwargs)
    return inner


@input_error
def add(user_input):
    if user_input[1] in phone_book:
        return f'\nThe contact is already in the phone book. To change the number, use the command "change".'
    else:
        phone_book[user_input[1]] = user_input[2]
    return f'\nContact {user_input[1]} has been added.'


def back_to_main(*args, **kwargs):
    return f''


def bye(*args):
    return f'\nGood bye!'


@input_error
def change(user_input):
    phone_book.update({user_input[1]: user_input[2]})
    return f'\nContact {user_input[1]} has been updated.'


@input_error
def get_handler(command):
    return COMMANDS[command]


def hello(*args):
    return f'\nHow can I help you?'


def parser(string):
    return string.split(' ')


@input_error
def phone(user_input):
    if user_input[1] in phone_book:
        return f'\n{user_input[1]}: {phone_book.get(user_input[1])}'
    else:
        return f'\nThe contact is not in the phone book.'


def show_all(*args):
    result = ''
    for key, value in phone_book.items():
        result += f'\n{key}: {value}'
    return result


COMMANDS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show_all': show_all

}

EXIT_COMMANDS = {
    'exit': '',
    'close': '',
    'good bye': ''
}

phone_book = {}


def main():
    while True:
        string = input(
            '\nEnter your command (hello, add, change, phone, show_all or exit/close/good bye):\n')
        user_input = parser(string)
        if user_input[0].lower() in EXIT_COMMANDS:
            print(bye())
            break
        else:
            print(get_handler(user_input[0].lower())(user_input))


if __name__ == "__main__":
    main()