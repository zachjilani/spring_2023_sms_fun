import json

QUESTIONS = {}
with open('RevisedQuestions.json', 'r') as myfile:
  QUESTIONS = json.loads(myfile.read())


class Player:
  def __init__(self, number, score=0):
    self.number = number
    self.score = score
    self.questions_asked = []


  def save_player(self, question):
    self.questions_asked.append(question)

  def exists(self):
    print("player object exists")

  def questions(self, input):
    out = []
    for next_question in QUESTIONS[self.state]['next_state']:
      if input.lower() == next_question['input'].lower():
        self.state = next_question['next_state']
        if 'point' in next_question['point']:
          self.score += next_question['point']
          out.append(self.score)
    while True:
      out.append(QUESTIONS[self.state]['content'])
      if 'next_state' not in QUESTIONS[self.state]:
        break
      self.state = QUESTIONS[self.state]['next_state']

    return out
