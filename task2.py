import calendar
import re
from datetime import datetime
import sys
import os
import re
import click
from collections import Counter

@click.command()
@click.option('--calendars', '-c')
@click.option('--durationinminutes', '-d')
@click.option('--minimumpeople', '-m')
def main(calendars, durationinminutes, minimumpeople) :
  path=os.getcwd()
  path_to_calendars = path + "/" + calendars + "/"
  free_people = {}
  flag=0
  i=0
  j=0
  list1 = []
  listoffreetimes = 0
  listofdates = []
  listofsums = []
  first_key = "key"
  for filename in os.listdir(path_to_calendars):
    with open(os.path.join(calendars, filename), 'r') as f:
      i=i+1
      free_time = 0
      #print(filename)
      Lines = f.readlines()
      for line in Lines:
        match_day_start = re.search(r'(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})', line)
        match_day_end = re.search(r'( )(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})', line)
        match_day_only = re.search(r'\d{4}-\d{2}-\d{2}', line)
        date_only = datetime.strptime(match_day_only.group(), '%Y-%m-%d').date()
        #date_only=str(date_only)
        try:
          date = datetime.strptime(match_day_start.group(), '%Y-%m-%d %H:%M:%S')
          casual_start = date.replace(hour=8,minute=0,second=0)
          #print(date)
        except:
          match_day_only = re.search(r'\d{4}-\d{2}-\d{2}', line)
          date = datetime.strptime(match_day_only.group(), '%Y-%m-%d').date()
          #print(date, "8:00:00")

        try:
          date_end = datetime.strptime(match_day_end.group(), ' %Y-%m-%d %H:%M:%S')
          casual_end = date_end.replace(hour=16,minute=0,second=0)
          #print(date_end)
          free_time = (casual_end - casual_start - (date_end - date)).total_seconds()/60.0
          #print("He has ",free_time, " minutes of free time")
          free_time = int(free_time)
          durationinminutes = int(durationinminutes)
          if j==0 or list1[len(list1)-2]!=date_only:
            list1.append(date_only)
            j=j+1
            if free_time>durationinminutes:
              list1.append(1)
          # else:
          #   a = listoffreetimes[-1] - int((date_end - date).total_seconds()/60.0)
          #   list1[-1] = a
          # listoffreetimes.append(free_time)

        except:
          free_time=0
            #print(date_only, "16:00:00")
            #print("He has no free time")
      #print(list1)
  result = Counter(list1)
  minimumpeople=int(minimumpeople)
  for key in result:
    if result[key]>=minimumpeople and key!=1:
      print("Given amount of people is available on: ",key)
      quit()
  #print(result)


          

  

if __name__ == "__main__":
  main()

  