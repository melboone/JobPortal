import requests
from bs4 import BeautifulSoup

#job = input('Enter job Tilte:')
#location = input('Enter Location:')

#print(job)



#url = 'https://www.indeed.co.in/jobs?q=python+developer&l=Bengaluru&sort=date'

#url ='https://www.indeed.co.in/jobs?q='+job+'&l='+location+'&sort=date'



titles  =[]
links = []
companies = []
summaries  = []

dates =[]


def job_data(url,items):

    res = requests.get(url).content
    soup = BeautifulSoup(res,'html.parser')
    data = soup.find_all('div',class_='jobsearch-SerpJobCard')

    for i in data:

        title = i.find('h2',class_='title')

        if items[0] in title.text:
            company = i.find('span',class_='company')
            link = title.find('a')
            summary  =i.find('div',class_='summary')

            date = i.find('span',class_='date')

            titles.append(title.text.strip())
            links.append('https://www.indeed.co.in'+link['href'])
            companies.append(company.text.strip())
            dates.append(date.text.strip())
            summaries.append(summary.text.strip())

            # print('\nJob Title:',title.text)
            # #print('posted:',date.text)
            # print('Company Name:',company.text)
            # print('Job Summary:',summary.text)
            # print('posted:',date.text)
            # print('https://www.indeed.co.in'+link['href'])
            # print(10*'*****')

    return titles,companies,summaries,dates,links

#job_data(url)

























































































'''
j = 'python developer'.strip().title()
items = j.split(' ')

job = 'python developer'.replace('+',' ').strip()

location ='Bengaluru'.replace('+',' ').strip()


url = 'https://www.indeed.co.in/jobs?q=python+developer&sort=date'

url = 'https://www.indeed.co.in/jobs?q='+job+'&l='+location+'&sort=date'


res = requests.get(url).content

soup = BeautifulSoup(res,'html.parser')

data = soup.find_all('div',class_='jobsearch-SerpJobCard')

for i in data:
    title = i.find('h2',class_='title')
    if items[0] in title.text.strip():
        link = title.find('a')

        sal = i.find('span',class_='salaryText')
        day = i.find('span',class_='date')
        company = i.find('span',class_='company')
        summary = i.find('div',class_='summary')

        print('\n',title.text)
        print(sal)
        print(day.text)
        print(company.text)
        print(summary.text)
        print('https://www.indeed.co.in'+link['href'])



'''








