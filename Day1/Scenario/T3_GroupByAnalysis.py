# *Tasks*  
# Write a Python program to find the most repeated word in a given paragraph. 
# Write a Python program to find the least repeated word in a given paragraph. 
# Write a Python program to remove duplicate words from a paragraph while maintaining 
# the original order of words. 
# Write a Python program to count the number of uppercase letters, lowercase letters, 
# digits, and special characters present in a paragraph. 
# Write a Python program to reverse the complete paragraph. 
# Write a Python program to reverse each word in a paragraph without changing the order 
# of the words. 


paragraph = "Rain tapped against the café window as Mira scribbled furiously in her leather-bound notebook. Between the aroma of fresh espresso and the low hum of conversation, she was lost in a puzzle only she could see. On the page, a strange sequence sprawled across the lines: Δ-42#moonrise@17:45!key=Ω7* if(x>99){unlock:door_3} $path→north-east; code=5&7&13 To anyone else, it looked like a jumble of symbols, numbers, and nonsense. But to Mira, each mark was a breadcrumb. The Δ meant “change,” the Ω was “end,” and the numbers—42, 17:45, 5, 7, 13—were coordinates in a hidden map she’d been building for months. Her heart raced as she underlined the final line: @dawn=truth%found. She knew that if she could solve the last equation before sunrise, the café’s old grandfather clock—its pendulum swinging like a heartbeat—would reveal the secret compartment she’d been chasing. Outside, lightning flashed, illuminating her reflection in the glass. She smiled faintly. The world thought she was just another customer sipping coffee. But in her mind, she was already halfway through the door that no one else could see."


words = paragraph.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
most_repeated_word = max(word_count, key=word_count.get)
print(f"Most repeated word: '{most_repeated_word}' with {word_count[most_repeated_word]} occurrences.")



least_repeated_word = min(word_count, key=word_count.get)
print(f"Least repeated word: '{least_repeated_word}' with {word_count[least_repeated_word]} occurrences.")


    
seen = set()
unique_words = []
for word in words:
    if word not in seen:
        seen.add(word)
        unique_words.append(word)
print("Paragraph without duplicate words:", ' '.join(unique_words))


    
uppercase_count = sum(1 for char in paragraph if char.isupper())
lowercase_count = sum(1 for char in paragraph if char.islower())
digit_count = sum(1 for char in paragraph if char.isdigit())
special_char_count = sum(1 for char in paragraph if not char.isalnum() and not char.isspace())


print(f"Uppercase letters: {uppercase_count}")
print(f"Lowercase letters: {lowercase_count}")
print(f"Digits: {digit_count}")
print(f"Special characters: {special_char_count}")



    
reversed_paragraph = paragraph[::-1]
print("Reversed paragraph:", reversed_paragraph)



    
reversed_words = ' '.join(word[::-1] for word in words)
print("Paragraph with each word reversed:", reversed_words)