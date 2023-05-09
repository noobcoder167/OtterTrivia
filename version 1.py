import random
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

# Trivia questions and answers
questions = {
   "What is the capital of France?": "Paris",
   "What is the largest planet in our solar system?": "Jupiter",
   "Who wrote the Harry Potter series?": "J.K. Rowling",
   "What is the tallest mammal in the world?": "Giraffe",
   "What is the currency of Japan?": "Yen",
   "What is a group of geese called?": "Gander",
   "What is the most important mineral for strong bones & teeth?": "Calcium",
   "What is 'bountiful mother' in latin?": "Alma Mater",
   "Lake Vanern is the largest lake in which country?": "Sweden",
   "What country covers an entire continent?": "Australia",
   "An atom is comprised of these 3 subatomic particles: electron, neutron, & _____?": "Proton",
   "What school does Harry Potter attend?": "Hogwarts",
   "Who said 'ask not what your country can do for you, but what you can do for your country'?": "JFK",
   "Michelle and Julia are songs by which group?": "The Beatles",
   "Who holds the nhl record for the most goals scored during a regular season?": "Wayne Gretzky",
   "What does UFC stand for?": "Ultimate Fighting Championships",
   "The koala eats the leaves from this tree?": "Eucalyptus",
   "Who recorded the album 'the cry of love' in 1970?": "jimi hendrix",
   "Which animal uses white ear spots as identification marks?": "tiger",
   "What is the main flavour of aioli?": "garlic",
   "Which of tea leaves or coffee beans have more caffeine?": "tea leaves",
   "What is the official state food of Texas?": "chili",
   "Who wrote about Willie Wonka and the Chocolate Factory?": "roald dahl",
   "In Greek mythology Cronos and Rhea were the parents of who?": "Zeus",
   "What sort of drink is barbancourt?": "rum",
   "In which country did Turkeys originate?": "USA",
   "Nashville is the capital of ______?": "tennessee",
   "What is the nickname for Texas?": "lone star state",
}
class TriviaGame:
   def __init__(self, master):
       self.master = master
       self.master.title("Trivia Game")
       self.master.geometry("700x250")
       self.master.configure(bg="#FFE5B4")

       # Initialize variables
       self.player1_score = 0
       self.player2_score = 0
       self.current_question = ""
       self.correct_answer = ""
       self.current_player = 1
       self.questions_answered = 0


       # Create widgets
       self.lbl_player = tk.Label(self.master, text=f"Player {self.current_player}'s turn", font=("Helvetica", 12, 'bold'), bg="#FFE5B4")
       self.lbl_player.pack(pady=10)
       self.lbl_question = tk.Label(self.master, text="", font=("Helvetica", 12, 'bold'), bg="#FFE5B4")
       self.lbl_question.pack(pady=10)
       self.entry_answer = tk.Entry(self.master, font=("Helvetica", 12))
       self.entry_answer.pack(pady=10)
       self.btn_answer = ttk.Button(self.master, text="Submit", command=self.check_answer)
       self.btn_answer.pack(pady=10)

       # Choose first question
       self.choose_question()

   def choose_question(self):
       self.current_question, self.correct_answer = get_random_question()
       self.lbl_question.config(text=self.current_question)
       self.lbl_player.config(text=f"Player {self.current_player}'s turn")

   def check_answer(self):
       player_answer = self.entry_answer.get().strip()
       if check_answer(player_answer, self.correct_answer):
           if self.current_player == 1:
               self.player1_score += 1
               self.master.configure(bg='green')  # Set the background to green for correct answer
           else:
               self.player2_score += 1
               self.master.configure(bg='green')  # Set the background to green for correct answer
           self.master.after(1000, lambda: self.master.configure(bg="#FFE5B4"))  # Reset color after 1 second
           self.questions_answered += 1
           if self.questions_answered < 5:
               self.current_player = 2 if self.player1_score > self.player2_score else 1
               self.choose_question()
               self.entry_answer.delete(0, tk.END)
           else:
               self.show_result()
       else:
           self.questions_answered += 1
           self.choose_question()
           self.entry_answer.delete(0, tk.END)
           self.master.configure(bg='red')  # Set the background to red for incorrect answer
           self.master.after(1000, lambda: self.master.configure(bg="#FFE5B4"))  # Reset color after 1 second

   def show_result(self):
       if self.player1_score > self.player2_score:
           result = "Congratulations, Player 1 wins!"
       elif self.player2_score > self.player1_score:
           result = "Congratulations, Player 2 wins!"
       else:
           result = "It's a tie!"
       messagebox.showinfo("Game Over", f"Final Scores: Player 1 = {self.player1_score}, Player 2 = {self.player2_score}\n{result}")
       self.master.destroy()




# Function to choose a random question
def get_random_question():
   question = random.choice(list(questions.keys()))
   answer = questions[question]
   return question, answer




# Function to check the player's answer
def check_answer(player_answer, correct_answer):
   return player_answer.lower() == correct_answer.lower()

# Main function to start the game
def main():
   root = tk.Tk()
   style = ttk.Style()
   style.configure('TButton', font=('Helvetica', 20, 'bold'), borderwidth='0')
   app = TriviaGame(root)
   root.mainloop()


if __name__ == "__main__":
   main()
