import tkinter as tk
import random 
import pandas as pd

def load_flashcards(file_path):
    df = pd.read_excel(file_path)
    return dict(zip(df['Question'], df['Answer']))

flashcards = load_flashcards('C:/Users/You/flashcards.xlsx')
print(flashcards)

class FlashcardApp:
    def __init__ (self, window):
        self.window = window
        window.title("Flashcard App")
        window.geometry ("500x300")
        
        self.question_label = tk.Label(window, text=" ", font=("Helvetica", 20))
        self.question_label.pack(pady=20)

        self.reveal_button = tk.Button(window, text = "Reveal Answer", command=self.reveal_answer) 
        self.reveal_button.pack()

        self.answer_label = tk.Label(window, text=" ", font=("Helvetica", 20))
        self.answer_label.pack(pady=20)

        self.next_button = tk.Button(window, text="Next", command=self.next_flashcard)
        self.next_button.pack()

        self.flashcard_list = list(flashcards.items())
        random.shuffle(self.flashcard_list)
        self.current_index = 0 
        self.next_flashcard()

    def next_flashcard(self):
        self.answer_label.config(text="")
        if self.current_index >= len(self.flashchard_list):
            random.shuffle(self.flashcard_list)
            self.current_index = 0
        self.current_question, self.current_answer = self.flashcard_list[self.current_index]
        self.question_label.config(text=self.current_question)
        self.current_index += 1
    
    def reveal_answer(self): 
        self.answer_label.config(text=self.current_answer)


window = tk.Tk()
app = FlashcardApp (window)
window.mainloop()
