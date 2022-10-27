def locate_card(cards, query):
  position = 0

  while len():
    if cards[position] == query:
      return position
    
    position += 1

    if position == len(cards):
      return -1


# test cases
tests = []
tests.append ({
  'input' : {
    'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
    'query' : 7
  },
  'output' : 3
})

tests.append ({
  'input' : {
    'cards' : [4, 2, 1, -1],
    'query' : 4
  },
  'output' : 0
})

tests.append ({
  'input' : {
    'cards' : [3, -1,  -9, -127],
    'query' : -127
  },
  'output' : 3
})
tests.append ({
  'input' : {
    'cards' : [6],
    'query' : 6
  },
  'output' : 0
})

tests.append ({
  'input' : {
    'cards' : [9, 7, 5, 2, -9,],
    'query' : 4
  },
  'output' : -1
})

tests.append ({
  'input' : {
    'cards' : [8, 8, 6, 6, 6, 2, 2, 2, 0, 0, 0],
    'query' : 6
  },
  'output' : 2
})

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