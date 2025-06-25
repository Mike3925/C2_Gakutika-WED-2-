import csv

NUM = 12

def main(num):
 
  arrayCsv = []
  page = 1
  count = 1

  for i in range(1,num + 1):
    print(f"Now Loading ... data{i}.csv")
    with open(r"Car_Solve_AI\raw_data\data" + str(i) + ".csv") as f:
        reader = csv.reader(f)

        for row in reader:
          lineCsvArray = []
          if (row != []):
            if (row[0] == "Q1"):
              page += 1
            print(f"{row[0]} ({page}) : {row[1]}")
            lineCsvArray.append("Q" + str(count))
            count += 1
            lineCsvArray.append(row[1])
            lineCsvArray.append(row[2])
            arrayCsv.append(lineCsvArray)
  
  with open(r'.\Car_Solve_AI\raw_data\data.csv',mode='w',newline='',encoding="UTF-8") as f:
    writer = csv.writer(f)
    writer.writerows(arrayCsv)



if __name__ == "__main__" :
  main(NUM)