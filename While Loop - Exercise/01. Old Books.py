book_name = input()
current_book = input()
book_count = 0
is_book_found = False
while current_book != "No More Books":
    if current_book == book_name:
        is_book_found = True
        break
    else:
        book_count += 1
        current_book = input()

if is_book_found:
    print(f"You checked {book_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_count} books.")