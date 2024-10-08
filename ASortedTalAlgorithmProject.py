## utils.py TAB

import csv

# This code loads the current book
# shelf data from the csv file
def load_books(filename):
  bookshelf = []
  with open(filename) as file:
      shelf = csv.DictReader(file)
      for book in shelf:
          # add your code here
          book['author_lower'] = book['author'].lower()
          book['title_lower'] = book['title'].lower()
          
          bookshelf.append(book)
  return bookshelf

## sorts.py TAB

import random

def bubble_sort(arr, comparison_function):
  swaps = 0
  sorted = False
  while not sorted:
    sorted = True
    for idx in range(len(arr) - 1):
      if comparison_function(arr[idx], arr[idx +1]):# arr[idx] > arr[idx + 1]:
        sorted = False
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        swaps += 1
  print("Bubble sort: There were {0} swaps".format(swaps))
  return arr

def quicksort(list, start, end, comparison_function):
  if start >= end:
    return
  pivot_idx = random.randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  less_than_pointer = start
  for i in range(start, end):
    if comparison_function(pivot_element, list[i]):# pivot_element > list[i]:
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  quicksort(list, start, less_than_pointer - 1, comparison_function)
  quicksort(list, less_than_pointer + 1, end, comparison_function)

## script.py

import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

for book in bookshelf:
  print(book['title'])


print(ord("a"))
print(ord(" "))
print(ord("A"))

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)

for book in sort_1:
  print(book['title'])

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

bookshelf_v1 = bookshelf.copy()

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)

print(sort_2)

bookshelf_v2 = bookshelf.copy()

sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

print(bookshelf_v2)

def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])


long_bookshelf = utils.load_books('books_large.csv')

#sorts.bubble_sort(long_bookshelf, by_total_length)
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)