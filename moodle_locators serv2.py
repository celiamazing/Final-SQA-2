from faker import Faker
fake = Faker(locale='en_CA')
moodle_url = 'http://52.33.5.136/'
moodle_login_url = 'http://52.33.5.136/login/index.php'
moodle_username = 'admin'
moodle_password = 'Moodle$erver002!#'
moodle_dashboard_url = 'http://52.33.5.136/my/'
new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
moodle_net_profile = f'https://moodle.net/{new_username}'
moodle_users_main_page='http://52.33.5.136/admin/user.php'
city = fake.city()
#country = fake.country()
description = fake.sentence(nb_words=100)
pic_desc = new_username
phonetic_firstname = fake.first_name()
phonetic_middle = fake.first_name()
phonetic_lastname = fake.last_name()
phonetic_alternate = fake.last_name()
list_of_interests = [new_username, new_password, first_name, city, email]
id = fake.pyint(11111111, 99999999)
institution = fake.pyint(111111, 999999)
department = fake.lexify(text='????')
phone1 = fake.phone_number()
phone2 = fake.phone_number()
address = fake.address()
address = fake.address().replace("\n", "")
full_name = f'{first_name} {last_name}'

