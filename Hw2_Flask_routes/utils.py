from faker import Faker
import requests


def requirements():
    file = open('requirements.txt', "r")
    return file


def generate_users(length: int = 100):
    fake = Faker()
    users = [f'{fake.first_name()} {fake.email()}' for i in range(int(length))]
    return users


def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    number_of_astronauts = r.json()['number']
    return f"The number of astronauts in space right now: {number_of_astronauts}"

