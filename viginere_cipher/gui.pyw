from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from string import ascii_lowercase as alphabet
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread

LETTER_FREQUENCY = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.36, 0.15, 1.974, 0.074]
N = len(LETTER_FREQUENCY)

class Window(Frame):
    def __init__(self, frequency, master=Tk()):
        self.master = master

        # Self variables
        self.shift_value = 0
        n = sum(frequency)
        self.frequency = [i/n for i in frequency]
        self.txt_shift_value = StringVar()

        def shift(number):
            self.shift_value = (self.shift_value + number) % N
            self.txt_shift_value.set("Shift value: " + str(self.shift_value))

            new_index = []
            for i in range(N):
                new_index += [(self.shift_value + i) % N]
                self.ith_char_plot[i].set_height(
                    self.frequency[(self.shift_value + i) % N]
                )
            self.canvas.draw()

        def enter():
            self.master.quit()

        button_frame = Frame(master)
        Label(button_frame, textvariable=self.txt_shift_value).pack(side=LEFT)
        Button(button_frame, text='→',command=lambda:shift(-1)).pack(side=LEFT)
        Button(button_frame, text='←',command=lambda:shift(1)).pack(side=LEFT)
        Button(button_frame, text='Enter', command=enter).pack(side=LEFT)
        button_frame.pack()

        ind = np.arange(N)  # the x locations for the groups
        width = 0.2         # the width of the bars

        fig, ax = plt.subplots(figsize=(15,15))
        rects1 = ax.bar(ind, [i/100 for i in LETTER_FREQUENCY], width, color='r')

        self.ith_char_plot = ax.bar(ind + width, [i for i in self.frequency], width, color='b')

        # add some text for labels, title and axes ticks
        ax.set_ylabel('Percentage')
        ax.set_xlabel('Letter')
        ax.set_title('Frequency of letter')
        ax.set_xticks(ind + width / 2)
        ax.set_xticklabels(tuple(alphabet))

        ax.legend((rects1[0], self.ith_char_plot[0]), ('English', 'ith char'))

        self.canvas = FigureCanvasTkAgg(fig, master=master)
        self.canvas.get_tk_widget().pack()

        self.master.title("Hack viginere")
        self.master.mainloop()

    def get_shift(self):
        # We need to trace backward, so we actually need the
        # negative of the shift value. (mod N obviously)
        return -self.shift_value % N
