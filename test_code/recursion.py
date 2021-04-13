menu1 = [
    {
        'label': 'Yii framework',
        'url': 'https://yii.ru'
    },
    {
        'label': 'More frameworks',
        'items': [
            {'label': 'Laravel', 'url': 'http://laravel.com',
             'items': [
                 {'label': 'Google', 'url': 'http://google.com'}
             ]
             },
            {'label': 'Slim', 'url': 'http://slimframework.com'}
        ]
    },
    {
        'label': 'Symfony',
        'url': 'http://symfony.com'
    }
]


def build_menu(menu):
    result = ''
    for i in range(len(menu)):
        for key, value in enumerate(menu[i]):
            if value == 'label':
                result += f'{value}: {menu[i][value]}\n'
            elif value == 'url':
                result += f'{value}: {menu[i][value]}\n\n'
            elif value == 'items':
                result += build_menu(menu[i][value])
    return result


print(build_menu(menu1))


def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])


print(list_sum([random.randint(1, 255) * x for x in range(20)]))

