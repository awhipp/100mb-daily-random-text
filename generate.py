import os
import random
from datetime import date
from string import digits, ascii_letters, punctuation

dt = date.today().strftime("%Y%m%d")
universe = digits + ascii_letters + punctuation

path = './releases'
isExist = os.path.exists(path)

if not isExist:
  os.makedirs(path)

file_name = '%s/random-%s.txt' % (path, dt)
with open(file_name, 'w') as f:
  print('Starting...')
  for i in range(1, 102400):
    f.write(''.join(random.choice(universe) for i in range(1024)))
    if i % 1024 == 0:
      print('Percent Complete: %s' % round(100*(i/102400), 2))