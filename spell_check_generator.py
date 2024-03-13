# P310 9.20
import json
import re

print("loading...")

wrong_and_correct = {}

def swap_adjacent_letters(word: str) -> str: # the function to swap adjacent letters
    wrong_word_set = {word[: i] + word[i + 1] + word[i] + word[i + 2 :] for i in range(len(word) - 1)}
    return wrong_word_set

def repeated_adjacent_letters(word: str) -> str: # the function to repeat adjacent letters
    wrong_word_set = {word[: i] + word[i] + word[i] + word[i + 1 :] for i in range(len(word))}
    return wrong_word_set

def missing_single_letter(word: str) -> str: # the function to miss a single letter
    wrong_word_set = {word[: i] + word[i + 1 :] for i in range(len(word))}
    return wrong_word_set

def update_set_to_dict(wrong_word_set: set, correct_word: str) -> None:
    for wrong_word in wrong_word_set:
        if wrong_word != correct_word:
            wrong_and_correct[wrong_word] = correct_word # wrong -> correct
    wrong_and_correct[correct_word] = correct_word

filename = "dictionary.json" # the original dictionary
with open(filename, "r") as dictionary:
    dictionary_json = json.load(dictionary)
    # print(json.dumps(dictionary_json, indent=4))
    
word_pattern = r"[a-zA-Z]+" # filtering only words
words_set = {word["word"] for word in dictionary_json["words"] if re.fullmatch(word_pattern, word["word"])}
# print(words_set)

# code to clean dictionary.json
def update_dictionary() -> None:
    while True:
        new_word = input("Enter a new word(Ctrl+C to exit): ").strip()
        if re.fullmatch(word_pattern, new_word):
            break
        else:
            print("Invalid word")
    words_set.add(new_word)
    words_dict = {"words":[
        {"word": word}
        for word in words_set
    ]}
    with open("dictionary.json", "w") as dictionary:
        json.dump(words_dict, dictionary, indent=4)
        
def delete_word() -> None:
    while True:
        word_to_delete = input("Enter a word to delete(Ctrl+C to exit): ").strip()
        if re.fullmatch(word_pattern, word_to_delete):
            break
        else:
            print("Invalid word")
    try:
        words_set.remove(word_to_delete)
    except KeyError:
        print("word not found")
    else:
        words_dict = {"words":[
            {"word": word}
            for word in words_set
        ]}
        with open("dictionary.json", "w") as dictionary:
            json.dump(words_dict, dictionary, indent=4)
        print("word deleted")
        
def build_spell_check() -> None:
    for correct_word in words_set:
        update_set_to_dict(swap_adjacent_letters(correct_word), correct_word) # wrong_word -> correct_word
        update_set_to_dict(repeated_adjacent_letters(correct_word), correct_word) # wrong_word -> correct_word
        update_set_to_dict(missing_single_letter(correct_word), correct_word) # wrong_word -> correct_word
            
    words_dict = {"wrong_and_correct": [
        {"wrong_word": wrong_word, "correct_word": correct_word} 
        for wrong_word, correct_word in wrong_and_correct.items() 
        if wrong_word != correct_word
    ]} # make a dictionary that can be written to a json file

    target_filename = "spell_check.json"
    with open(target_filename, "w") as spell_check:
        json.dump(words_dict, spell_check, indent=4)
    # print(words_set)
    print("generate successfully")
    exit(0)

if __name__ == "__main__":
    while True:
        try:
            mode = int(input("Enter mode:\n1. Update dictionary\n2. Delete word\n3. Generate\n"))
        except ValueError:
            print("Invalid mode")
            continue
        
        if mode == 1:
            update_dictionary()
        elif mode == 2:
            delete_word()
        else:
            print("generating...")
            build_spell_check()