
word = input("Enter a word: ").upper()
symbol = input("Enter a symbol: ")

if len(symbol) > 1:
    print("Error! Please type only one charater as the symbol!")
    while len(symbol) > 1:
        symbol = input("Enter a symbol: ")
        print("Error! Please type only one charater as the symbol!")


border_length = len(word) + 4

print(symbol * border_length)
print(f"{symbol} {word} {symbol}")
print(symbol * border_length)