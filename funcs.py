import requests

def thais_func(num):
  if num > 10:
    print(num, 'is bigger than 10!')
  elif num > 5:
    print(num, 'is bigger than 5 but not bigger than 10!')
  else:
    print(num, 'is not bigger than 5!')
  thais_list = ['hi'] * num
  print('thais_list', thais_list)
  for word in thais_list:
    print('word', word)
  for i, w in enumerate(thais_list):
    print('i', i, 'w', w)

def get_stuff(url):
  r = requests.get(url)
  return r.text

stuff = get_stuff('http://www.google.com')
print(stuff)