import random

class MathCalculator:
    """A random math calculator with multiple difficulty levels."""
    
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.difficulty_ranges = {
            1: (1, 10),
            2: (1, 100),
            3: (1, 1000)
        }
        self.operations = ['+', '-', '*', '/']
    
    def get_difficulty(self):
        """Get difficulty level from user."""
        print("\n" + "=" * 50)
        print("Select Difficulty Level:")
        print("1. Easy (1-10)")
        print("2. Medium (1-100)")
        print("3. Hard (1-1000)")
        print("=" * 50)
        
        while True:
            try:
                choice = int(input("Enter your choice (1-3): "))
                if choice in [1, 2, 3]:
                    return choice
                else:
                    print("Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input! Please enter a number.")
    
    def get_number_of_questions(self):
        """Get number of questions from user."""
        while True:
            try:
                num = int(input("\nHow many questions do you want to solve? "))
                if num > 0:
                    return num
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input! Please enter a number.")
    
    def generate_problem(self, difficulty):
        """Generate a random math problem based on difficulty."""
        min_val, max_val = self.difficulty_ranges[difficulty]
        
        num1 = random.randint(min_val, max_val)
        num2 = random.randint(min_val, max_val)
        operation = random.choice(self.operations)
        
        # Ensure division problems are solvable (no division by zero)
        if operation == '/':
            num2 = random.randint(1, max_val)
            # Make sure result is a whole number for simplicity
            num1 = num2 * random.randint(1, 10)
        
        return num1, num2, operation
    
    def calculate_answer(self, num1, num2, operation):
        """Calculate the correct answer."""
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return num1 // num2  # Integer division
    
    def solve_problem(self, num1, num2, operation, question_number):
        """Present a problem and check the answer."""
        print(f"\nQuestion {question_number}: {num1} {operation} {num2} = ?")
        
        correct_answer = self.calculate_answer(num1, num2, operation)
        
        while True:
            try:
                user_answer = int(input("Your answer: "))
                
                if user_answer == correct_answer:
                    print("✅ Correct!")
                    self.score += 1
                    return True
                else:
                    print(f"❌ Wrong! The correct answer is {correct_answer}")
                    return False
                    
            except ValueError:
                print("Invalid input! Please enter a number.")
    
    def display_score(self):
        """Display the final score."""
        percentage = (self.score / self.total_questions) * 100
        print("\n" + "=" * 50)
        print("QUIZ COMPLETE!")
        print(f"Your Score: {self.score}/{self.total_questions}")
        print(f"Percentage: {percentage:.1f}%")
        
        if percentage == 100:
            print("🏆 Perfect score! You're a math wizard!")
        elif percentage >= 80:
            print("🌟 Excellent! Great job!")
        elif percentage >= 60:
            print("👍 Good! Keep practicing!")
        else:
            print("📚 Keep practicing to improve!")
        print("=" * 50)
    
    def run_quiz(self):
        """Run the complete math calculator quiz."""
        print("\n" + "=" * 50)
        print("Welcome to Random Math Calculator!")
        print("=" * 50)
        
        difficulty = self.get_difficulty()
        num_questions = self.get_number_of_questions()
        self.total_questions = num_questions
        
        print(f"\nGreat! Starting {num_questions} problems at difficulty level {difficulty}...")
        
        for question_num in range(1, num_questions + 1):
            num1, num2, operation = self.generate_problem(difficulty)
            self.solve_problem(num1, num2, operation, question_num)
        
        self.display_score()
    
    def play(self):
        """Main game loop with replay option."""
        while True:
            self.score = 0
            self.total_questions = 0
            
            self.run_quiz()
            
            while True:
                play_again = input("\nDo you want to play again? (yes/no): ").lower()
                if play_again in ['yes', 'y']:
                    break
                elif play_again in ['no', 'n']:
                    print("\nThanks for playing! Goodbye! 👋")
                    return
                else:
                    print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    calculator = MathCalculator()
    calculator.play()
