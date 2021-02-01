# Choose My Life Game
# Write a question and obtain a random answer

from random import randint
from PySimpleGUI import PySimpleGUI as sg

class Choose:

    def __init__(self):
        self.answers=['Yes.', 'No.', 'Sure, why not?', 'Sure, you should do that.', 'I do not know.',
                      'Do it.','Do not do this.','Yes, is the right time to do it.']
        #create layout
        sg.theme('Reddit')


        layout=[[sg.Text('Write a Question:'), sg.Input(key='question')], #line1
                [sg.Button('Generate')], #line 2
                [sg.Text('Answer'),sg.Output(size=(80,10))]#Line 3
                ]
        #create a window in GUI
        self.w1=sg.Window('Choose My Life Game').layout(layout)


    def answer(self):
        num= randint(1,len(self.answers)) #generate a answer
        ans=self.answers[num]
        return ans

    def data(self):
        self.event, self.value = self.w1.read()
        return self.event, self.value


c=Choose()
#c.cicle()

while True:

    event, value = c.data()

    if event == 'Generate':
        print(c.answer())

    if event == sg.WINDOW_CLOSED: # validates if the window is closed
        break


