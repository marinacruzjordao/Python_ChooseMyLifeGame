# Choose My Life Game
# Write a question and obtain a random answer

from random import randint


class Choose:

    def __init__(self):
        self.answers=['Yes.', 'No.', 'Sure, why not?', 'Sure, you should do that.', 'I do not know.',
                      'Do it.','Do not do this.','Yes, is the right time to do it.']

    def question(self):
        q=input('Write a Question:')

    def answer(self):
        value= randint(1,len(self.answers))
        ans=self.answers[value]

        return ans

c=Choose()
c.question()
print(c.answer())