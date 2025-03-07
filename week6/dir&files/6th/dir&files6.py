def file_generator():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in letters:
        filename = f"{letter}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f'file: {filename}')
        print("File successfully created")
file_generator()