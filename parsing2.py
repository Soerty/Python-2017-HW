# -*- coding: utf-8 -*-
import re
from io import StringIO
from urllib.request import urlopen

from lxml import etree




class Professor(object):
    def __init__(self):
        self.name = ''
        self.pnone = ''
        self.email = ''




def download(url):
    return str(urlopen(url).read(), 'utf-8')



def clean_email(email):
    return ''.join(re.findall('[a-zA-Z@.]', email.replace('-at-', '@')))



def teachers_with_etree(parsed_page):
    professors = []

    # Через iterfind()
    for person in parsed_page.iterfind('//div[@class="post person"]'):
        professor = Professor()

        professor.name = person.xpath('.//div[@class="g-pic person-avatar-small2"]/@title')[0]
        professor.phone = [i for i in person.xpath('.//div[@class="l-extra small"]/span/text()')]
        professor.email = [clean_email(i) for i in person.xpath('.//div[@class="l-extra small"]/a/@data-at')]

        professors.append(professor)

    return professors



def teachers_with_xpath(parsed_page):
    professors = []

    # Через XPath
    for person in parsed_page.xpath('//div[@class="post person"]'):
        professor = Professor()

        professor.name = person.xpath('.//div[@class="g-pic person-avatar-small2"]/@title')[0]
        professor.phone = [i for i in person.xpath('.//div[@class="l-extra small"]/span/text()')]
        professor.email = [clean_email(i) for i in person.xpath('.//div[@class="l-extra small"]/a/@data-at')]

        professors.append(professor)

    return professors





if __name__ == '__main__':
    url = 'https://www.hse.ru/org/persons/'

    page = StringIO(download(url))
    parser = etree.HTMLParser()
    tree = etree.parse(page, parser)

    teachers_with_etree(tree)
    teachers_with_xpath(tree)
