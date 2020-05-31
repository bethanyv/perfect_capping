"""
Used for calculating honor needed
"""
# perfect_cap.csv
import csv

# this is styled as control_distance: (min_speed, max_speed) all in km/km per hour
LEVELS = [48,49,50,51,52,53,54,55,56,57,58,59,60]

RANKS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

TABLE = []

def create_table(csv_file):
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
    print(TABLE)

# up to 3 people
def calculate_honor(honor_needed):
  return honor_needed

if __name__ == "__main__":
  create_table('perfect_cap.csv')
  calculate_honor(350)