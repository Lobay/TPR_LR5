from SimplexSolve import Simplex, MAX, MIN


def main():

    matrix = [
        [14, 5, 9, 1, 17],
        [4, 6, 10, 18, 4],
        [2, 5, 13, 11, 0],
        [0, 6, 14, 1, 16],
    ]

    na = len(matrix)  # количество для игрока A
    nb = len(matrix[0])  # количество для игрока B

    a_a = [[-matrix[i][j] for i in range(na)] for j in range(nb)]
    b_a = [-1 for _ in range(nb)]
    c_a = [1 for _ in range(na)]
    game_a = Simplex(a_a, b_a, c_a, MIN, 'u', 'W')

    a_b = [[matrix[i][j] for j in range(nb)] for i in range(na)]
    b_b = [1 for _ in range(na)]
    c_b = [1 for _ in range(nb)]
    game_b = Simplex(a_b, b_b, c_b, MAX, 'v', 'Z')

    game_a.table.PrintTask()
    game_a.solve()
    solve_a = game_a.table.GetSolve()

    game_b.table.PrintTask()
    game_b.solve()
    solve_b = game_b.table.GetSolve()

    print("\nResults")
    solve_a.PrintGame("x", "g")
    solve_b.PrintGame("y", "h")


if __name__ == '__main__':
    main()
