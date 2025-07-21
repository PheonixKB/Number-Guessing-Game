import random
import time as t

# Global initialization
i = 0  # Used to display rules only once
high_score = {'Low': 0, 'Medium': 0, 'High': 0}   # Tracks best (least) number of attempts per difficulty
max_time = {'Low': 0, 'Medium': 0, 'High': 0}     # Tracks fastest time per difficulty


class NumberGuessingGame():
    def __init__(self):
        global high_score, max_time, i

        # Game settings
        self.levels = ['Low', 'Medium', 'High']
        self.max_attempts = [10, 5, 3]  # Corresponds to Low, Medium, High difficulty
        self.hints = [7, 3, 2]          # Attempt number when hint will be shown
        self.attempts = 0
        self.start = t.time()          # Start time of the game

        # Game introduction
        print('Greetings!')
        print("Welcome to the number guessing game.")

        if i == 0:
            # Display rules only once
            print('In this game, the computer has guessed a number between 1 and 100.')
            print('You have to guess that number.')
            print("You will be able to choose the difficulty levels for the game.")
            print('1. Easy\n2. Medium\n3. Hard')
            i += 1
        else:
            print('All the rules have already been explained.')

        print("\nNow, let's start the game.")
        print(f'Your highest scores are: {high_score}')
        print(f'Your fastest time taken (in seconds) are: {max_time}')

        # User selects difficulty level
        try:
            self.level = int(input("Enter difficulty level (1-3): ")) - 1
            assert 0 <= self.level <= 2
        except (ValueError, AssertionError):
            print("Invalid input. Defaulting to Easy level.")
            self.level = 0

        # Random target number between 1 to 100
        self.target = random.randint(1, 100)
        print('Computer has chosen the number.')

    def game(self):
        # Prompt the user for a guess
        try:
            prompt_text = 'Guess the number: ' if self.attempts == 0 else 'Guess the number again: '
            self.guess = int(input(prompt_text))
        except ValueError:
            print("Please enter a valid number.")
            return self.game()  # Retry on invalid input

        self.attempts += 1

        # Check the guess
        if self.guess > self.target:
            print('You guessed high. Guess lower.')
        elif self.guess < self.target:
            print('You guessed low. Guess higher.')
        else:
            # Correct guess
            self.end = t.time()
            self.duration = self.end - self.start
            print(f'\nCongratulations! You guessed it right in {self.attempts} attempts.')
            print(f'You took {self.duration:.2f} seconds.')

            # Update high score if it's better
            level_name = self.levels[self.level]
            if self.attempts < high_score[level_name] or high_score[level_name] == 0:
                high_score[level_name] = self.attempts

            # Update best time
            if self.duration < max_time[level_name] or max_time[level_name] == 0:
                max_time[level_name] = self.duration

            # Show updated stats
            print(f'Best attempts in {level_name} level: {high_score[level_name]}')
            print(f'Fastest time (in seconds) in {level_name} level: {max_time[level_name]:.2f}')
            return

        # Provide hint if allowed on current attempt
        if self.attempts == self.hints[self.level]:
            low = max(1, self.target - random.randint(1, 5))
            high = min(100, self.target + random.randint(1, 5))
            print(f'Hint: The number is between {low} and {high}')

        # End game if max attempts reached
        if self.attempts == self.max_attempts[self.level]:
            self.end = t.time()
            self.duration = self.end - self.start
            print('\nYou have reached your maximum number of attempts.')
            print(f'You took {self.duration:.2f} seconds.')
            print(f'The correct number was: {self.target}')
            print('Better luck next time.')
            return

        # Continue the game
        self.game()


# Main game loop
again = 'y'
while again in ['y', 'yes']:
    NumberGuessingGame().game()
    print("\n" + "=" * 40 + "\n")
    again = input('Do you want to play again (y/n): ').lower()

# Final summary after exiting
print("\nGame Summary:")
print("-" * 40)
for level in ['Low', 'Medium', 'High']:
    print(f"- {level:<6} | Best Attempts: {high_score[level]:<2} | Fastest Time: {max_time[level]:>6.2f} sec")
print("-" * 40)
