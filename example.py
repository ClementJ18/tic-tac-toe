from ttt import TicTacToe

#two players
game = TicTacToe(X="Bob", O="John")

while not game.game_over():
    value = input(">>> ")
    while not game.validate(value):
        value = input(">>> ")
    game.play("Bob", value)

    print(game.print_board())

    value = input(">>> ")
    while not game.validate(value):
        value = input(">>> ")
    game.play("John", value)

    print(game.print_board())

print(game.print_board())
print(game.winner + " is the winner")

#ai game
game = TicTacToe(X="Bob", O="ai")

while not game.game_over():
    value = input(">>> ")
    while not game.validate(value):
        value = input(">>> ")
    game.play("Bob", value)

    print(game.print_board())

    game.play("ai")
    
    print(game.print_board())

print(game.print_board())
print(game.winner + " is the winner")

