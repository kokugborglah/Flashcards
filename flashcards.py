import random
import time

# Dictionary to store flashcards (German to English)
flashcards = {
    'Der Schauspieler': 'The actor',
    'Das Bett': 'The Bed',
    'Der Garten': 'The Garden',
    'Das Spiel': 'The Game',
    'Das Buch': 'The Book',
    'Das Bücherregal': 'The Bookcase',
    'Der Schreibtischer': 'The Writer',
    'Der Kellner': 'The Waiter',
    'Der Kellnerin': 'The Waitress',
    'Der Mensch': 'The Man',
    'Die Frau': 'The Woman',
    'Der Hund': 'The Dog',
    'Der Mann': 'The Man',
    'Die Frau': 'The Woman',
    'Der Koffer': 'The Bag',
    'Der Schrank': 'The Dresser',
    'Der Kühlschrank': 'The Refrigerator',
    'Der Tisch': 'The Table',
    'Der Küchenkellner': 'The Cook',
    'Der Küchenkellnerin': 'The Cook',
    'Der Eisenbahn': 'The Railway',
    'Der Boden': 'The Ground',
    'Die Tür': 'The Door',
    'Der Hof': 'The Garden',
    'Der Wald': 'The Forest',
    'Der Baum': 'The Tree',
    'Die Wiese': 'The Valley',
    'Der See': 'The Sea',
    'Die Erde': 'The Earth',
    'Der Himmel': 'The Sky',
    'Die Erde': 'The Earth',
    'Die Luft': 'The Air',
    'Die Berg': 'The Mountain',
    'Der Ort': 'The Place',
    'Der Tag': 'The Day',
    'Der Nacht': 'The Night',
    'Die Sonne': 'The Sun',
    'Der Wald': 'The Forest',
    'Das Wasser': 'The Water',
    'Das Auto': 'The Car',
    'Der Freund': 'The Friend',
    'Die Liebe': 'The Love'
    
}

# Variables to track performance
correct_answers = 0
total_questions = 0


# Function to add a new flashcard, checking for duplicates
def add_flashcard():
    german_word = input("Enter the German word: ").capitalize()
    
    # Check if the German word already exists in the flashcards
    if german_word in flashcards:
        print(f'The word "{german_word}" already exists with the translation "{flashcards[german_word]}".')
    else:
        english_word = input("Enter the English translation: ").capitalize()
        flashcards[german_word] = english_word
        print(f'Flashcard added: {german_word} - {english_word}')

# Function to test the user with a random flashcard
def test_flashcards():
    if flashcards:  # Ensure there are flashcards available
        german_word = random.choice(list(flashcards.keys()))
        answer = input(f'What is the English translation of "{german_word}"? ')
        
        if answer.lower() == flashcards[german_word].lower():
            print("Correct!")
        else:
            print(f'Wrong! The correct translation is "{flashcards[german_word]}"')
    else:
        print("No flashcards available! Please add some first.")
        
# Function to calculate performance percentage
def calculate_performance():
    if total_questions > 0:
        percentage = (correct_answers / total_questions) * 100
        print(f'\nPerformance: {correct_answers} correct out of {total_questions} ({percentage:.2f}%)')
    else:
        print("\nNo flashcards tested yet.")

# Function to display the menu when requested
def display_menu():
    print("\nFlashcard Menu:")
    print("1. Add new flashcard")
    print("2. Test yourself")
    print("3. Exit")

# Main function to wait for user's request to show menu
def main():
    # Start timer
    start_time = time.time()

    while True:
        user_input = input("\nType 'menu' to view options or 'exit' to quit: ").lower()
        
        if user_input == 'menu':
            display_menu()
            while True:
                choice = input("Choose an option (1, 2, or 3): ")
                if choice == '1':
                    add_flashcard()
                elif choice == '2':
                    test_flashcards()
                elif choice == '3':
                    # End timer and calculate total usage time
                    end_time = time.time()
                    total_time = end_time - start_time
                    minutes, seconds = divmod(total_time, 60)
                    
                    # Display performance and total time used
                    calculate_performance()
                    print(f'Total time spent: {int(minutes)} minutes and {int(seconds)} seconds.')
                    print("Goodbye!")
                    return  # Exit the program
                else:
                    print("Invalid choice. Please choose 1, 2, or 3.")
            # Exit menu loop, go back to waiting for 'menu' or 'exit'
        elif user_input == 'exit':
            # End timer and calculate total usage time
            end_time = time.time()
            total_time = end_time - start_time
            minutes, seconds = divmod(total_time, 60)
            
            # Display performance and total time used
            calculate_performance()
            print(f'Total time spent: {int(minutes)} minutes and {int(seconds)} seconds.')
            print("Goodbye!")
            break
        else:
            print("Invalid command. Type 'menu' to view options or 'exit' to quit.")


# Entry point of the program
if __name__ == '__main__':
    main()