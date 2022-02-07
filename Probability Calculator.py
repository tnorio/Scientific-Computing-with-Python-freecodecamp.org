import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []

    for k in kwargs.keys():
      for v in range(0,kwargs.get(k)):
        self.contents.append(str(k))
    
  def draw(self,nballs):
    removed = []
    if nballs > len(self.contents):
      return self.contents 
    else:
      for i in range(nballs):
       randchoice = random.choice(self.contents)
       removed.append(randchoice)
       self.contents.pop(self.contents.index(randchoice))
    return removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  pcount = 0 # n times of sucess

  for num in range(num_experiments):
    copyhat = copy.deepcopy(hat)
    taken_balls = copyhat.draw(num_balls_drawn) #taken_balls is the list result
    taken_balls_dict = {}
    contains_all = True

    #taken_balls do dict
    for i in taken_balls:
      if i not in taken_balls_dict:
        taken_balls_dict.setdefault(i,1)
      else:
        taken_balls_dict.update({i:taken_balls_dict.get(i)+1})

    for k,v in expected_balls.items():
      if k not in taken_balls_dict.keys() or taken_balls_dict.get(k) < expected_balls.get(k):
        contains_all = False
        break
 
    if contains_all == True:
      pcount +=1

  probability = pcount/num_experiments
  print("Probability: ",probability)
  return probability
