import random
import time

import requests
from faker import Faker


def main():
    urls = ['http://localhost/', 'http://localhost/random_page', 'http://localhost/admin', 'http://localhost/profile/1']
    while True:
        fake = Faker()
        agent = fake.user_agent()
        headers = {'User-Agent': agent}
        url = random.choice(urls)
        response = requests.get(url=url, headers=headers)
        print(response.status_code)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
