import tkinter as tk
from tkinter import messagebox
import random

# Define a set of questions (you can expand this list)
questions = [
    {
        'question': 'What is the capital of France?',
        'choices': ['Berlin', 'Madrid', 'Paris', 'Lisbon'],
        'answer': 'Paris'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'choices': ['Earth', 'Mars', 'Jupiter', 'Saturn'],
        'answer': 'Mars'
    },
    {
        'question': 'What is the largest mammal?',
        'choices': ['Elephant', 'Whale', 'Shark', 'Giraffe'],
        'answer': 'Whale'
    },
    {
        'question': 'Which is the largest ocean?',
        'choices': ['Atlantic Ocean', 'Indian Ocean', 'Pacific Ocean', 'Arctic Ocean'],
        'answer': 'Pacific Ocean'
    },
    {
        'question': 'Who wrote the play "Romeo and Juliet"?',
        'choices': ['William Shakespeare', 'Charles Dickens', 'Jane Austen', 'George Orwell'],
        'answer': 'William Shakespeare'
    }
]

# Shuffle the questions
random.shuffle(questions)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        
        self.score = 0
        self.current_question = 0
        
        # Label for question display
        self.question_label = tk.Label(root, text="", font=("Arial", 14), width=50, height=3)
        self.question_label.pack(pady=20)
        
        # Radio buttons for answer choices
        self.var = tk.StringVar()
        self.choice1 = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Arial", 12))
        self.choice1.pack(fill='x')
        self.choice2 = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Arial", 12))
        self.choice2.pack(fill='x')
        self.choice3 = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Arial", 12))
        self.choice3.pack(fill='x')
        self.choice4 = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Arial", 12))
        self.choice4.pack(fill='x')
        
        # Button to submit the answer
        self.submit_button = tk.Button(root, text="Submit Answer", command=self.check_answer, font=("Arial", 12))
        self.submit_button.pack(pady=10)
        
        # Button to next question
        self.next_button = tk.Button(root, text="Next Question", command=self.next_question, font=("Arial", 12))
        self.next_button.pack(pady=10)
        self.next_button.config(state=tk.DISABLED)  # Disable until answer is submitted
        
        # Display the first question
        self.display_question()
    
    def display_question(self):
        """Display the current question and choices"""
        question = questions[self.current_question]
        
        # Set the question text
        self.question_label.config(text=question['question'])
        
        # Set the answer choices
        self.choice1.config(text=question['choices'][0], value=question['choices'][0])
        self.choice2.config(text=question['choices'][1], value=question['choices'][1])
        self.choice3.config(text=question['choices'][2], value=question['choices'][2])
        self.choice4.config(text=question['choices'][3], value=question['choices'][3])
        
        # Reset the selected choice
        self.var.set(None)
        
        # Enable the submit button and disable next question button
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)
    
    def check_answer(self):
        """Check if the selected answer is correct"""
        question = questions[self.current_question]
        selected_answer = self.var.get()
        
        if selected_answer == question['answer']:
            self.score += 1
            messagebox.showinfo("Correct!", "That's the correct answer!")
        else:
            messagebox.showinfo("Incorrect!", f"Oops! The correct answer was: {question['answer']}")
        
        # Disable the submit button and enable the next question button
        self.submit_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)
    
    def next_question(self):
        """Move to the next question or display results"""
        self.current_question += 1
        
        if self.current_question < len(questions):
            self.display_question()  # Show the next question
        else:
            self.show_results()  # No more questions, show results
    
    def show_results(self):
        """Display the final score"""
        messagebox.showinfo("Quiz Over", f"Your final score is: {self.score}/{len(questions)}")
        self.root.quit()  # Close the application after displaying results

# Create the Tkinter root window
root = tk.Tk()

# Create the QuizApp instance
app = QuizApp(root)

# Run the Tkinter event loop
root.mainloop()
