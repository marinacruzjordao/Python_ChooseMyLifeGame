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


        layout=[[sg.Text('Write a Question:'), sg.Input(key='question')],
                [sg.Button('Generate')],
                [sg.Text('Answer'),]#sg.Output(size=(80,10))]#, sg.Output(size=(80, 10))],
                ]
        #create a window in GUI
        self.w1=sg.Window('Choos My Life Game').layout(layout)



    def answer(self):
        num= randint(1,len(self.answers))
        ans=self.answers[num]
        print(ans)

    def cicle(self):
        while True:

            self.event, self.value = self.w1.read()

            if self.event == sg.WINDOW_CLOSED: # validates if the window is closed
                break

            if self.event == 'Generate':
                print(c.answer())




c=Choose()