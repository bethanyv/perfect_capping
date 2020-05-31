"""
Used for calculating honor needed
"""
import csv

LEVELS = [48,49,50,51,52,53,54,55,56,57,58,59,60]

RANKS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

def create_table(csv_file):
  TABLE = []
  with open(csv_file, encoding="utf-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      TABLE.append([])
      for column in row:
        if column in (None, ""):
          continue
        TABLE[line_count].append(column)
      line_count += 1
  return TABLE

# up to 3 people
def calculate_honor(honor_needed):
  '''
  honor needed should return dictionary of 1, 2, 3 people and a list of lists 
  of all possible people
  ex: {1: [[1,4], [2,5]] 2: [] 3: []}
  '''
  TABLE = create_table('perfect_cap.csv')
  possibilities = {1: [], 2: [], 3: []}
  # for 1 kills
  for i in range(13): # 13 rows
    row = 0
    for point_amt in TABLE[i]:
      point_amt = int(point_amt)
      # print(point_amt)
      if point_amt == honor_needed:
        possibilities[1].append(["Level " + str(LEVELS[i]),"Rank " + str(RANKS[row])])
      row += 1

  # for 2 kills
  for i in range(13): # 13 rows
    row = 0
    for point_amt in TABLE[i]:
      point_amt = int(point_amt)
      # print(point_amt)
      for k in range(13): # 13 rows
        row_to_add = 0
        for point_amt_to_add in TABLE[k]:
          point_amt_to_add = int(point_amt_to_add)
          # print(point_amt)
          if point_amt + point_amt_to_add == honor_needed:
            if (["Level " + str(LEVELS[k]),"Rank " + str(RANKS[row_to_add]), "Level " + str(LEVELS[i]),"Rank " + str(RANKS[row])] not in possibilities[2]):
              possibilities[2].append(["Level " + str(LEVELS[i]),"Rank " + str(RANKS[row]), "Level " + str(LEVELS[k]),"Rank " + str(RANKS[row_to_add])])
          row_to_add += 1
      row += 1
  # for 3 kills
  for i in range(13): # 13 rows
    row = 0
    for point_amt in TABLE[i]:
      point_amt = int(point_amt)
      # print(point_amt)
      for k in range(13): # 13 rows
        row_to_add = 0
        for point_amt_to_add in TABLE[k]:
          point_amt_to_add = int(point_amt_to_add)
          # print(point_amt)
          for j in range(13): # 13 rows
            row_to_add_2 = 0
            for point_amt_to_add_2 in TABLE[j]:
              point_amt_to_add_2 = int(point_amt_to_add_2)
              # print(point_amt)
              if point_amt + point_amt_to_add + point_amt_to_add_2 == honor_needed:
                if ((["Level " + str(LEVELS[k]),"Rank " + str(RANKS[row_to_add]), "Level " + str(LEVELS[i]),"Rank " + str(RANKS[row]), "Level " + str(LEVELS[j]),"Rank " + str(RANKS[row_to_add_2])] not in possibilities[3])\
                  and ((["Level " + str(LEVELS[k]),"Rank " + str(RANKS[row_to_add]), "Level " + str(LEVELS[j]),"Rank " + str(RANKS[row_to_add_2]), "Level " + str(LEVELS[i]),"Rank " + str(RANKS[row])] not in possibilities[3])\
                  and (["Level " + str(LEVELS[i]),"Rank " + str(RANKS[row]), "Level " + str(LEVELS[k]),"Rank " + str(RANKS[row_to_add]), "Level " + str(LEVELS[j]),"Rank " + str(RANKS[row_to_add_2])] not in possibilities[3])\
                  and (["Level " + str(LEVELS[i]),"Rank " + str(RANKS[row]), "Level " + str(LEVELS[j]),"Rank " + str(RANKS[row_to_add_2]), "Level " + str(LEVELS[k]),"Rank " + str(RANKS[row_to_add])] not in possibilities[3]))\
                  and (["Level " + str(LEVELS[j]),"Rank " + str(RANKS[row_to_add_2]), "Level " + str(LEVELS[k]),"Rank " + str(RANKS[row_to_add]), "Level " + str(LEVELS[i]),"Rank " + str(RANKS[row])] not in possibilities[3])\
                  and (["Level " + str(LEVELS[j]),"Rank " + str(RANKS[row_to_add_2]), "Level " + str(LEVELS[i]),"Rank " + str(RANKS[row]), "Level " + str(LEVELS[k]),"Rank " + str(RANKS[row_to_add])] not in possibilities[3])):
                    possibilities[3].append(["Level " + str(LEVELS[i]),"Rank " + str(RANKS[row]), "Level " + str(LEVELS[k]),"Rank " + str(RANKS[row_to_add]), "Level " + str(LEVELS[j]),"Rank " + str(RANKS[row_to_add_2])])
              row_to_add_2 += 1
          row_to_add += 1
      row += 1

  return possibilities

if __name__ == "__main__":
  print(calculate_honor(100))