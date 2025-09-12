
import csv
from list import list as list_of_word

# For each word in the list, i want to check all the others words as the first one is the result and get the 

result = {word : 0 for word in list_of_word}
answer = {
  '0': [0, [], []],
  '1': [0, [], []],
  '2': [0, [], []],
  '3': [0, [], []],
  '4': [0, [], []]
}

def check_possibility(attempt, answer):
  res = 0
  lettre_tried = []
  for i in range(len(attempt)):
    if attempt[i] == answer[i]:
      res += 2
  
    elif attempt[i] in answer and attempt[i] not in lettre_tried:
      # TODO : check if the letter is in the word at the right place
      lettre_tried.append(attempt[i])
      res += 1
    else : 
      res -= 1

  return res
    
def check_all(answer):
  for word in list_of_word:
    result[word] += check_possibility(word, answer)

def extract_to_csv(result):
  with open('result.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['word', 'result'])
    for word, result in sorted(result.items(), key=lambda x: x[1]):
      writer.writerow([word, result])

def get_from_file():
  f = open('./response')
  response = [res.split('.') for res in f.read().split('\n')]
  f.close()
  for w,p in response:
    for i in range(5):
      match p[i]:
        case 'X':
          answer[str(i)][1].append(w[i])
        case 'O':
          answer[str(i)][2].append(w[i])
        case 'V':
          answer[str(i)][0] = w[i]
  return answer

def getList():
  new_list = []
  included = []
  excluded = []
  for i in range(5):
    included.extend(answer[str(i)][2])
    excluded.extend(answer[str(i)][1])
  for word in filter(lambda x: all(letter not in x for letter in excluded), list_of_word):
    new_list.append(word)
    for i in range(5):
      if answer[str(i)][0] != 0 and word[i] != answer[str(i)][0]:
        new_list.remove(word)
        break
    
  print(new_list)
  return new_list


get_from_file()

for word in getList():
  check_all(word)
print(sorted(result.items(), key=lambda x: x[1]))

extract_to_csv(result)



