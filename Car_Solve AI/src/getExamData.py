import numpy as np
import pandas as pd
import requests
import pprint
from bs4 import BeautifulSoup
import csv
import time


def get_data(page,index):
  returnList = []

  for i in range(1, page + 1):
    url = 'https://www.car-license.co.jp/feature/question/challenge' + str(index) +'-' + str(i) + '.html'
    r = requests.get(url)
    # print(r.content)

    soup = BeautifulSoup(r.content, 'html.parser')  
    number = soup.select("dl.question-box > dt")
    # del number[2]
    question = soup.select("dl.question-box > dd > p")
    # del question[2]
    answer = soup.select("dl.answer-box > dt")
    for j in range(len(number)):
      returnList.append([number[j].text, question[j].text, answer[j].text])
    print("Over [" + str(index) + "] : Page " + str(i))
    time.sleep(1)
  return returnList

def output(data,index):
  path = r"C:\Users\yousa\Program\C2_Gakutika(WED 2)\MyProject\data\data" + str(index) + ".csv"
  with open(path, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)


def main():
  MAXPAGE = 9
  for i in range(7,11):
    data = get_data(MAXPAGE,i)
    output(data, i)
    pprint.pprint(data)

if __name__ == "__main__":
  main()