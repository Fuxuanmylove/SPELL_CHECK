import json

print("loading...")
wrong_to_correct = {}
with open("spell_check.json", "r") as spell_check:
    spell_check_dict = json.load(spell_check)
    # print(json.dumps(spell_check_dict, indent=4))
    for wrong_and_correct in spell_check_dict["wrong_and_correct"]:
        wrong_word = wrong_and_correct["wrong_word"]
        correct_word = wrong_and_correct["correct_word"]
        wrong_to_correct[wrong_word] = correct_word
        wrong_to_correct[correct_word] = correct_word
  
if __name__ == "__main__":
    while True:
        try:
            word = input("enter a word(ctrl+C to exit): ").lower()
        except KeyboardInterrupt:
            print("exit successfully")
            break
        if word in wrong_to_correct:
            if word == wrong_to_correct[word]:
                print("correct spell")
            else:
                print(f"Did you mean {wrong_to_correct[word]}?")
        else:
            print("cannot find the word in the dictionary")