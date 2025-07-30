import time
import random

def get_random_sentence():
    """
    Returns a random sentence from a predefined list.
    """
    sentences = [
        "You are winning Felix Sindani",
        "You are a big thinker Felix, so think big about everything",
        "You look good Felix and feel good, stay that way",
        "You have the ability to do a first calss job so do a first class job",
        "Discipline is not weakness",
        "You were a great fello yestarday, and are going to be an even greater fellow today",
        "Now go to it Felix, go forward",
    ]
    return random.choice(sentences)

def calculate_wpm(start_time, end_time, typed_text):
    """
    Calculates Words Per Minute (WPM).
    WPM = (Number of characters / 5) / Time taken in minutes
    """
    time_taken_seconds = end_time - start_time
    time_taken_minutes = time_taken_seconds / 60
    words_typed = len(typed_text.split()) # Count words based on spaces
    
    if time_taken_minutes <= 0:
        return 0
    
    wpm = words_typed / time_taken_minutes
    return round(wpm)

def calculate_accuracy(original_text, typed_text):
    """
    Calculates typing accuracy as a percentage.
    Compares character by character.
    """
    correct_characters = 0
    min_length = min(len(original_text), len(typed_text))

    for i in range(min_length):
        if original_text[i] == typed_text[i]:
            correct_characters += 1
    
    if len(original_text) == 0:
        return 0
        
    accuracy = (correct_characters / len(original_text)) * 100
    return round(accuracy, 2)

def typing_test_game():
    """
    Main function to run the typing test game.
    """
    print("Lets do this Felix")
    print("You will be given a sentence to type. Type it as fast and accurately as you can.")
    input("Finya Enter Mkuu...")

    while True:
        sentence_to_type = get_random_sentence()
        print("\n----------------------------------------------------")
        print("Type this sentence:")
        print(f"\"{sentence_to_type}\"")
        print("----------------------------------------------------")

        start_time = time.time()
        user_input = input("Your typing: ")
        end_time = time.time()

        wpm = calculate_wpm(start_time, end_time, user_input)
        accuracy = calculate_accuracy(sentence_to_type, user_input)

        print("\n--- Results ---")
        print(f"Time taken: {round(end_time - start_time, 2)} seconds")
        print(f"Words Per Minute (WPM): {wpm}")
        print(f"Accuracy: {accuracy}%")
        print("---------------")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    typing_test_game()
