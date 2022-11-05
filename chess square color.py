chess_square = input("Please enter chess square: ")
coordinate1 = ord(chess_square[0])
coordinate2 = int(chess_square[1])

if coordinate1 % 2 == 1 and coordinate2 % 2 ==1:
    print(str(chess_square) + " is black.")
elif coordinate1 % 2 == 1 and coordinate2 % 2 == 0:
    print(str(chess_square) + " is white.")
elif coordinate1 % 2 == 0 and coordinate2 % 2 == 0:
    print(str(chess_square) + " is black.")
elif coordinate1 % 2 == 0 and coordinate2 % 2 == 1:
    print(str(chess_square) + " is white.")

