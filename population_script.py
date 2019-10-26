import os
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dressCode.settings')

import django
django.setup()

from codeforgood.models import NewsArticle


def populate():

    # dummy News articles
    news = {"title": "News Article ", "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "picture": "cat.jpg"}
    for i in range(1, 10):
        n = NewsArticle.objects.get_or_create(title=news["title"]+str(i), description=news["description"], picture=news["picture"], date=timezone.now())

if __name__ == '__main__':
    print("Starting codeforgood population script..")
    populate()