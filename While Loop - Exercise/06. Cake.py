width = int(input())
lenght = int(input())
total_pieces = width * lenght
command = input()
while command != "STOP":
    current_pieces = int(command)
    total_pieces -= current_pieces
    if total_pieces < 0:
        break
    command = input()
if total_pieces >= 0:    # moje i command == "STOP"
    print(f"{total_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(total_pieces)} pieces more.")