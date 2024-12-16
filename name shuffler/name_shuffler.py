def name_shuffler(s: str):
    return ' '.join(reversed(list(s.split(' '))))
print(name_shuffler('Mirkomil Rashidov'))