class PuzzleNode:
    def __init__(self, puzzle, parent=None, move=None):
        self.puzzle = puzzle
        self.parent = parent
        self.move = move

    def __eq__(self, other):
        return self.puzzle == other.puzzle

    def __hash__(self):
        return hash(str(self.puzzle))


def find_blank(puzzle):
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                return i, j


def is_valid_move(i, j):
    return 0 <= i < 3 and 0 <= j < 3


def get_neighbors(node):
    neighbors = []
    i, j = find_blank(node.puzzle)
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for move in moves:
        ni, nj = i + move[0], j + move[1]
        if is_valid_move(ni, nj):
            neighbor_puzzle = [list(row) for row in node.puzzle]
            neighbor_puzzle[i][j], neighbor_puzzle[ni][nj] = neighbor_puzzle[ni][nj], neighbor_puzzle[i][j]
            neighbors.append(PuzzleNode(neighbor_puzzle, parent=node, move=move))
    return neighbors


def dfs(initial_state, goal_state):
    visited = set()
    stack = [PuzzleNode(initial_state)]
    
    while stack:
        current_node = stack.pop()
        visited.add(tuple(map(tuple, current_node.puzzle)))  # Store the puzzle state as a tuple of tuples

        if current_node.puzzle == goal_state:
            return current_node

        neighbors = get_neighbors(current_node)
        for neighbor in neighbors:
            if tuple(map(tuple, neighbor.puzzle)) not in visited:
                stack.append(neighbor)

    return None


def print_solution(node):
    if node is None:
        print("No solution found.")
        return

    moves = []
    while node.parent is not None:
        moves.append(node.move)
        node = node.parent

    moves.reverse()
    for move in moves:
        if move == (1, 0):
            print("Move Down")
        elif move == (-1, 0):
            print("Move Up")
        elif move == (0, 1):
            print("Move Right")
        elif move == (0, -1):
            print("Move Left")


if __name__ == "__main__":
    initial_state = [
        [1, 2, 3],
        [4, 0, 5],
        [7, 8, 6]
    ]

    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    solution_node = dfs(initial_state, goal_state)
    print_solution(solution_node)
