def is_pangram(sentence):
    ALPHABET_SIZE = 26

    sentence_chars = filter(str.isalpha, sentence.lower())

    letters = set(sentence_chars)

    return len(letters) == ALPHABET_SIZE
