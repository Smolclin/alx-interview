#!/usr/bin/python3

"""
Chess grandmaster Judit Polgár, the strongest female chess player of all time
"""
import sys


def backtrack(a, i, cols, pos, neg, board):
    """
    """
    if a == i:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return
    for c in range(i):
        if c in cols or (a + c) in pos or (a - c) in neg:
            continue

        cols.add(c)
        pos.add(a + c)
        neg.add(a - c)
        board[a][c] = 1

        backtrack(a+1, i, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(a + c)
        neg.remove(a - c)
        board[a][c] = 0


def nqueens(n):
    """
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)

    if __name__ == "__main__":
        n = sys.argv
        if len(n) != 2:
            print("Usage: nqueens N")
            sys.exit(1)
        try:
            nn = int(n[1])
            if nn < 4:
                print("N must be at least 4")
                sys.exit(1)
            nqueens(nn)
        except ValueError:
            print("N must be a number")
            sys.exit(1)
