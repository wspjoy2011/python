import sys
import random
import secrets
import hmac
import hashlib
import math
from copy import deepcopy
from prettytable import PrettyTable


class GameEngine:
    def __init__(self):
        self._game_items = None
        self._random_comp_choice = None
        self._menu_options = None

    @staticmethod
    def check_game_arguments():
        arguments = sys.argv[1:]
        error = ''
        if len(arguments) < 3:
            error = 'The number of arguments must be at least three.'
        elif len(arguments) % 2 == 0:
            error = 'The number of arguments must be odd.'
        elif len(arguments) != len(set(arguments)):
            error = 'There are duplicates in the arguments.'
        if error:
            print(error)
            exit()
        return arguments

    def set_game_items(self):
        self._game_items = self.check_game_arguments()

    def set_random_comp_choice(self):
        self._random_comp_choice = random.choice(self._game_items)

    def set_menu_options(self):
        result = ''
        for i in range(len(self.get_game_items())):
            result += f'{i + 1} - {self._game_items[i]}\n'
        self._menu_options = result[:-1]

    def get_game_items(self):
        return self._game_items

    def get_random_comp_choice(self):
        return self._random_comp_choice

    def get_menu_options(self):
        return self._menu_options


class SecretKeyHMAC:
    def __init__(self):
        self._secret_key = None
        self._hmac = None

    def set_secret_key(self):
        self._secret_key = secrets.token_bytes(64).hex().upper()

    def set_hmac(self):
        byte_secret_key = self._secret_key.encode()
        byte_computer_choice = game_engine.get_random_comp_choice().encode()
        self._hmac = hmac.new(byte_secret_key, byte_computer_choice, hashlib.sha3_256).hexdigest()

    def get_hmac(self):
        return self._hmac

    def get_secret_key(self):
        return self._secret_key


class Rules:
    def __init__(self):
        self._rules = None

    def set_rules(self):
        rules = {key: {'draw': [], 'win': [], 'loss': []} for key in game_engine.get_game_items()}
        middle = math.ceil(len(game_engine.get_game_items()) / 2)
        copy_game_item = deepcopy(game_engine.get_game_items())
        for item in game_engine.get_game_items():
            rules[item]['draw'].append(copy_game_item[:1])
            rules[item]['win'].append(copy_game_item[1:middle])
            rules[item]['loss'].append(copy_game_item[middle:])
            copy_game_item.append(copy_game_item.pop(0))
        self._rules = rules

    def get_rules(self):
        return self._rules


class Help:
    def __init__(self):
        self._table = None

    def set_table(self):
        first_item = [key for key in rules.get_rules()][0]
        keys = list(rules.get_rules().keys())
        table = []
        temp = ['draw']
        for _ in range(len(rules.get_rules()[first_item]['win'][0])):
            temp.append('win')
        for _ in range(len(rules.get_rules()[first_item]['loss'][0])):
            temp.append('loss')
        for i in range(len(temp)):
            table.append(keys[i].upper())
            for item in temp:
                table.append(item)
            temp.insert(0, temp.pop())
        self._table = table

    def get_rules(self):
        th = [key for key in rules.get_rules().keys()]
        th.insert(0, 'Rules')
        td = self._table
        td_data = td[:]
        table = PrettyTable(th)
        for item in th:
            table.align[item] = 'l'
        columns = len(th)
        while td_data:
            table.add_row(td_data[:columns])
            td_data = td_data[columns:]
        return table


class Result:
    def __init__(self):
        self._user_choice = None

    def set_user_choice(self, choice):
        self._user_choice = int(choice)

    def get_user_choice(self):
        return self._user_choice

    def calculate_game_result(self):
        print(f'Your move: {game_engine.get_game_items()[self.get_user_choice() - 1]}')
        print(f'Computer move: {game_engine.get_random_comp_choice()}')
        user_choice = rules.get_rules()[game_engine.get_game_items()[self.get_user_choice() - 1]]
        for key in user_choice:
            if game_engine.get_random_comp_choice() in user_choice[key][0]:
                if key == 'draw':
                    print(key.title())
                else:
                    print(f'You {key}!')
                print(f'Secret key: {secret_key_hmac.get_secret_key()}')


def game_main_loop():
    while True:
        game_engine.set_random_comp_choice()
        secret_key_hmac.set_secret_key()
        secret_key_hmac.set_hmac()
        print(f'''HMAC: {secret_key_hmac.get_hmac()}
Available moves:
{game_engine.get_menu_options()}
0 - exit
? - help''')
        user_choice = input('Enter your move: ')
        if user_choice == '0':
            print('Bye!')
            exit()
        elif user_choice == '?':
            print(help.get_rules())
            input('Press enter to continue')
        else:
            try:
                result.set_user_choice(int(user_choice))
                result.calculate_game_result()
            except (IndexError, ValueError):
                pass


if __name__ == '__main__':
    game_engine = GameEngine()

    game_engine.set_game_items()
    game_engine.set_menu_options()

    secret_key_hmac = SecretKeyHMAC()

    rules = Rules()
    rules.set_rules()

    help = Help()
    help.set_table()

    result = Result()

    game_main_loop()
