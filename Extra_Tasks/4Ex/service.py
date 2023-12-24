import re
import csv
import ssl

import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

adres_request = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry/").read().decode()
pattern = r"(?:class=\"org-widget-header__title-link\">)(?P<services>[^<]+)(?:[^0]+)(?:location\">[\s]+)(?P<street>[^<]+\b)(?:[^0-9]+)(?:value\">)(?P<number>[^<]+\b)(?:[^0-9,]+)(?:value\">)(?P<time>[^<]+)"
matches = re.findall(pattern, adres_request)

with open('data.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Сервис', 'Адрес', 'Контакт', 'Расписание'])
    for match in matches:
        match = list(match)
        filter_match = [match[j] for j in range(len(match)) if len(match[j].split()) != 0]
        '''print(filter_match)
        for j in range(len(i)):
            if len(i[j].split()) == 0:
                i[j] = ''
        i = list(filter(None, a))'''
        writer.writerow(filter_match)
