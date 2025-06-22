import csv
import pprint
from B2_wakati import wakatiSentence as wk
import re

arrayCsv = []
count = 1
page = 0

def readCsvToWakati(num):
  global count
  global page

  with open(r"Car_Solve_AI\raw_data\data" + str(num) + ".csv") as f:
    reader = csv.reader(f)
    for row in reader:
      lineCsvArray = []
      if (row != []):
        if (row[0] == "Q1"):
          page += 1

        pattern = r"標識|標示"
        repatter = re.compile(pattern)
        result = repatter.search(row[1])
        print(f"{row[0]} ({page}) : {row[1]}")

        if (result == None):
          wks = wk(row[1])
          print(wks)
          lineCsvArray.append(f'{count}')
          lineCsvArray.append(wks)
          if row[2] == "○":
            lineCsvArray.append(1)
          else:
            lineCsvArray.append(0)
          count += 1
          arrayCsv.append(lineCsvArray)
        else:
          print("Skipped")
        print()

  # with open(r"Car_Solve_AI\wakati_data\wakati_data" + str(num) + ".csv", "w") as f:
  #   writer = csv.writer(f)
  #   writer.writerows(arrayCsv)

def writeWakatiTo1Csv():
  with open(r'.\Car_Solve_AI\data\data.csv',mode='w',newline='',encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerows(arrayCsv)

def main():
  for i in range(1,11):
    readCsvToWakati(i)
  writeWakatiTo1Csv()
  


  
  

if __name__ == "__main__":
  main()
