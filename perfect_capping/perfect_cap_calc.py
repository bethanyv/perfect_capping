"""
Used for calculating honor needed
"""
# perfect_cap.csv
import csv

# this is styled as control_distance: (min_speed, max_speed) all in km/km per hour
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
  ex: {1: [[1,4], [2,5]]}
  '''
  TABLE = create_table('perfect_cap.csv')
  possibilities = {1: [], 2: [], 3: []}
  # for 1 person
  for i in range(13): # 13 rows
    row = 0
    for point_amt in TABLE[i]:
      point_amt = int(point_amt)
      # print(point_amt)
      if point_amt == honor_needed:
        print("HERE")
        possibilities[1].append(["Level " + str(LEVELS[i]),"Rank " + str(RANKS[row])])
      row += 1

  return possibilities

if __name__ == "__main__":
  print(calculate_honor(51))