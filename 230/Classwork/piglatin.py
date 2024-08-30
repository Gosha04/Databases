def word_to_pig(string):
    string_list = []
    if string.lower()[0] in ('a', 'i', 'o', 'u', 'e'):
        string_list = string.split()
        string_list.append('yay')  
        pig_string = ''.join(string_list)
    else:
        string_list = string.split()
        x = string_list[0]
        string_list.pop(0)
        string_list.append(x + 'ay')  
        pig_string = ' '.join(string_list)
    return pig_string

def pig_convert(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            words = content.split()
            pig_words = [word_to_pig(word) for word in words]
            pig = ' '.join(pig_words)

        with open(output_file, 'w') as file:
            file.write(pig)
        print("Conversion successful! Check '{}' for the piglatin text.".format(output_file))
    
    except FileNotFoundError:
        print("File not found.")


pig_convert('pig.txt', 'latin.txt')