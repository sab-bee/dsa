def locate_card(cards, query):
  low, high = 0, len(cards) - 1
  while low <= high:
    mid = (low + high) // 2
    mid_number = cards[mid]

    if mid_number == query:
      return mid
    elif mid < query:
      high = mid - 1
    else:
      low = mid + 1
  return -1

# test cases
tests = []

#t1
tests.append ({
  'input' : {
    'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
    'query' : 7
  },
  'output' : 3
})

#t2
tests.append ({
  'input' : {
    'cards' : [4, 2, 1, -1],
    'query' : 4
  },
  'output' : 0
})

#t3
tests.append ({
  'input' : {
    'cards' : [3, -1,  -9, -127],
    'query' : -127
  },
  'output' : 3
})

#4
tests.append ({
  'input' : {
    'cards' : [6],
    'query' : 6
  },
  'output' : 0
})

#5
tests.append ({
  'input' : {
    'cards' : [9, 7, 5, 2, -9,],
    'query' : 4
  },
  'output' : -1
})

#6
tests.append ({
  'input' : {
    'cards' : [8, 8, 6, 6, 6, 6, 6, 6, 2, 2, 2, 0, 0, 0],
    'query' : 6
  },
  'output' : 2
})

#7
tests.append ({
  'input' : {
    'cards' : [],
    'query' : 7
  },
  'output' : -1
})


for i in range(len(tests)):
  print(f'test case #{i}')
  result = locate_card(**tests[i]['input'])
  print(result)
  if result == tests[i]['output']:
    print('passed')
  else:
    print('failed')
  print('\n')