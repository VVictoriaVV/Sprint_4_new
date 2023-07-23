import random as r

def random_name():
    names =['Виктория', 'Арсений', 'Колумб', 'Светлана', 'Гарри']
    r_name = r.choice(names)
    return r_name


def random_surname():
    surnames = ['Тестеров', 'Петров', 'Иванов', 'Сухов', 'Сидоров']
    r_surname = r.choice(surnames)
    return r_surname

def random_address():
    addresses = ['ул. Крутицкий Вал 2', 'ул. Петровская 3', 'ул.Ленинский проспект 432', 'ул. Каргопольская 1', 'ул. Декабристов 48']
    r_address = r.choice(addresses)
    return r_address

def random_telephone():
    region_id = '+7'
    operator_id = r.randint(900, 999)
    number = r.randint(100000, 999999)
    r_telephone = region_id + str(operator_id) + str(number)
    return r_telephone

def random_comment():
    comments = ['Набирайте домофон!', 'за час позвонить',
                'нужна сдача', 'бонусы,будут?', 'хочу скидку']
    r_comment = r.choice(comments)
    return r_comment