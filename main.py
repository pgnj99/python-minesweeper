# Minesweeper by Peter Giordano
# August 13, 2024
# Based on Microsoft Minesweeper

from play import play

print('MINESWEEPER')
print('1: Beginner (5x5, 7 mines)')
print('2: Easy (8x8, 10 mines)')
print('3: Medium (16x16, 40 mines)')
print('4: Hard (25x25, 70 mines)')
print('5: Custom')

# This loop will run for as long as the player wants to continue playing
while True:
    choice = input('Enter a number to select your difficulty or enter 0 to exit.')
    if choice == "1":
        play(1)
    elif choice == "2":
        play(2)
    elif choice == "3":
        play(3)
    elif choice == "4":
        play(4)
    elif choice == "5":
        play(5)
    elif choice.lower() == "papegay":
        play('Papegay')
    elif choice == "0":
        print("Thank you for playing!")
        break
    else:
        print("Invalid choice.")