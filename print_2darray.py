from typing import List


def print_2darray(array: List[List[float]], headers: List, indexes: List, ljust_len: int = 25):
  '''Print 2d list with index labels and headers.'''
  index_ljust_len = max(len(str(index)) for index in indexes)
  print(" " * index_ljust_len, end="")
  for header in headers:
    print(str(header).ljust(ljust_len, " "), end="")
  print()

  for i in range(len(array)):
    print(str(indexes[i]).ljust(index_ljust_len, " "), end="")
    for j in range(len(array[0])):
      print(str(array[i][j]).ljust(ljust_len, " "), end="")
    print()