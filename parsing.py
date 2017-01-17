# -*- coding: utf-8 -*-
import re
from urllib.request import urlopen




class Professor(object):
    def __init__(self):
        self.name = ''
        self.phone = 0




def download(url):
    return str(urlopen(url).read(), 'utf-8').replace('\n', '')



def parsing(page):
    names = re.findall(r'(?<=class="g-pic\ person-avatar-small2"\ title=)"[\s\w]*"', page)
    phones = re.findall(r'<span>[\+\*\(\)\ \-\d]*</span>', page)

    professors = []
    for name, phone in zip(names, phones):
        object = Professor()
        object.name = name.replace('"', '')
        object.phone = phone[6:-7]
        professors.append(object)

    return professors



if __name__ == '__main__':
    page = download('https://www.hse.ru/org/persons')

    for professor in parsing(page):
        print (professor.name, professor.phone)