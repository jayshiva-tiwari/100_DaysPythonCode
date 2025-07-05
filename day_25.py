#  Day 25 of python with programming paglu🎀

# OOP Quiz Game with Score

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        print("🧠 Welcome to the Python Quiz Game!")
        for i, q in enumerate(self.questions, start=1):
            print(f"\nQuestion {i}:")
            print(q.prompt)
            user_ans = input("Your answer: ").strip().lower()
            if user_ans == q.answer.lower():
                print("✅ Correct!")
                self.score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q.answer}")
        self.show_score()

    def show_score(self):
        print("\n🎉 Quiz Completed!")
        print(f"Your final score is: {self.score} out of {len(self.questions)}")
        if self.score == len(self.questions):
            print("🏆 You're a Python Pro!")
        elif self.score >= len(self.questions)//2:
            print("👏 Good job! Keep practicing.")
        else:
            print("📚 Don't worry, keep learning!")

# 🚀 Questions
question_list = [
    Question("What is the output of 3 + 2?\n(a) 5\n(b) 6\n(c) 7", "a"),
    Question("Which keyword is used to define a function in Python?\n(a) func\n(b) define\n(c) def", "c"),
    Question("What does 'len()' do?\n(a) Add numbers\n(b) Return length\n(c) Print output", "b"),
    Question("Which data type is immutable?\n(a) List\n(b) Tuple\n(c) Set", "b")
]

# 🎮 Start Quiz
quiz_game = Quiz(question_list)
quiz_game.start()