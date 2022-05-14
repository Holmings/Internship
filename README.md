# Internship

#### Task 2
Commands:\
--calendars\
adds to path name of the directory with .txt files\
I used my own directiory which is available in a repository as calendars.zip\
It is meant to be extracted in the same place as task2.py file\
I wrote my code on Linux so i use "/" to define path\
--durationinminutes\
defines how many minutes people should be available\
--minimumpeople\
defines number amount of people that must be available\
\
Example use:\
python task2.py --calendars calendars --durationinminutes 200 --minimumpeople 2\
\
Program is reading all files in given directiory and finding a pattern od date using re directory and converts it to datatype using datetime directory.\
For each line it counts amount of free time and if it is >= durationinminutes, it adds the date to a list. If the same date repeats for the same person it was supposed to count it properly but it returns error so I commented that part of the code.\
Counter(list1) counts how many times date repeats.\
If the same date repeats >= minimumpeople times then it is our result.

