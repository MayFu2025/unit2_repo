def count_letters(lexicon:dict, msg:str):
    for let in msg:
        if let in lexicon:
            lexicon[let] += 1
    print(lexicon)

# Check that it works:
count_letters({'w':0, 'l':0, 'c':0}, "hello world")
count_letters({'a':0, 'e':0, 'i':0, 'o':0, 'u':0}, "Why did I choose CS?")