
def load_numbers_sorted(txt):
    with open(txt) as f:
        numbers = sorted(map(lambda e: int(e), f))
    return numbers
