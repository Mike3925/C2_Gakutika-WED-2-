# 

import numpy as np
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pprint

import csv
import re


def get_data(url):
  reList = []
  options = Options()
  options.add_argument('--headless')
  driver = webdriver.Chrome(options=options)

  CHUTE_Q = "body > form > ol > font > li"
  CHUTE_A = "body > table > tbody > tr"
  HONTE_Q = "body > form > font:nth-child(3) > ol > li"
  HONTE_A = "body > table > tbody > tr"

  try:
    driver.get(url)
    wait = WebDriverWait(driver,1)
    print(driver.title)
    if "f0" in url:
      driver.switch_to.frame("frame1")
      elements = driver.find_elements(By.CSS_SELECTOR,CHUTE_Q)
      for item in elements:
        # print(item.text)
        pattern = "[^［ ]+"
        repatter = re.compile(pattern)
        result = repatter.search(item.text)
        print(result.group(0))
        reList.append(result.group(0))
    else:
      elements = driver.find_elements(By.CSS_SELECTOR,CHUTE_A)
      for item in elements:
        pattern = "○|×"
        repatter = re.compile(pattern)
        result = repatter.search(item.text)
        reList.append(result.group(0))
  finally:
    driver.quit()
  return reList


def output(data,index):
  path = r"Car_Solve_AI\raw_data\data" + str(index) + ".csv"
  with open(path, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)



def main():
  data = []
  MAXPAGE = 4
  count = 1
  INDEX = 12

  for i in range(1,MAXPAGE + 1):
    url = 'https://www.takaragaike.co.jp/se_q/chute_f0' + str(i) + 't.html'
    A = get_data(url)
    url = 'https://www.takaragaike.co.jp/se_q/chute_a0' + str(i) + '.html'
    B = get_data(url)

    for i in range(len(A)):
      data.append([count, A[i], B[i]])
      count += 1
    print(data)

  output(data,INDEX)
  pprint.pprint(data)

if __name__ == "__main__":
  main()