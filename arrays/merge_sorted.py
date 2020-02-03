
def find_duplicate_files(paths):
    duplicates = []
    mapping = {}

    for path in paths:
        info = path.split()
        path = info.pop(0)

        for detail in info:
            file_detail = detail.split('(')
            file_name = path + '/' + file_detail[0]
            file_text = file_detail[1]
            if file_text not in mapping:
                mapping[file_text] = [file_name]
            elif file_text in mapping:
                mapping[file_text].append(file_name)
        print(mapping)

    for text in mapping:
        if len(mapping[text]) > 1:
            duplicates.append(mapping[text])

    return duplicates

def word_puzzles(words, puzzles):
    valid_words = []
    count = 0

    curr_puzz_set = {}
    curr_first_char = None

    for puzzle in puzzles:
        curr_puzz_set = set(puzzle)
        curr_first_char = puzzle[0]

        for word in words:
            if word[0] == curr_first_char:
                is_valid = True
                word_uniques = set(word)
                for char in word_uniques:
                    print(char)
                    if char not in curr_puzz_set:
                        is_valid = False
                if is_valid:
                    count += 1

        valid_words.append(count)
        count = 0


    return valid_words
