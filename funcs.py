import requests

# def thais_func(num):
#   thais_list = [num] * num
#   print('thais_list', thais_list)

def get_stuff(url):
  r = requests.get(url)
  return r.text

stuff = get_stuff('http://www.google.com')
print(stuff)
