import random

def make_maze():

    maze = Maze([], Cell(True, 0, 1))

    for x in range(0, 10):
        maze.cell_list.append([])
        for y in range(0, 10):
            maze.cell_list[x].append(Cell(True, x, y))

    print(maze)

    visited_cells = []

    possible_to_visit = Stack()

    # initial cell.... for now. Know if there are ones which are unvisited by comparing lengths...
    # marked as visited
    # current cell is the head of the stack
    # x is vertical( rows) , y is across( columns )....

    # 1.

    visited_cells.append(maze.current_cell)

   # 2.

    for x in range(5):

        neighbours_list = []

        if maze.current_cell.x_cord + 2 < len(maze.cell_list):

            if maze.cell_list[maze.current_cell.x_cord + 2][maze.current_cell.y_cord] not in visited_cells:

                neighbours_list.append(maze.cell_list[maze.current_cell.x_cord + 2][maze.current_cell.y_cord])

        if maze.current_cell.x_cord - 2 > 0:

            if maze.cell_list[maze.current_cell.x_cord - 2][maze.current_cell.y_cord] not in visited_cells:

                neighbours_list.append(maze.cell_list[maze.current_cell.x_cord - 2][maze.current_cell.y_cord])

        if maze.current_cell.y_cord + 2 < len(maze.cell_list[0]):

            if maze.cell_list[maze.current_cell.x_cord][maze.current_cell.y_cord + 2] not in visited_cells:

                neighbours_list.append(maze.cell_list[maze.current_cell.x_cord][maze.current_cell.y_cord + 2])

        if maze.current_cell.x_cord - 2 > 0:

            if maze.cell_list[maze.current_cell.x_cord][maze.current_cell.y_cord - 2] not in visited_cells:

                neighbours_list.append(maze.cell_list[maze.current_cell.x_cord][maze.current_cell.y_cord - 2])

        if len(neighbours_list) != 0:

            random_chosen_cell = random.choice(neighbours_list)
            possible_to_visit.push(maze.current_cell)

            # Remove wall in between by doing the average of them + making the one we go to not a wall

            maze.cell_list[int(maze.current_cell.x_cord+random_chosen_cell.x_cord/2)][int(maze.current_cell.y_cord+random_chosen_cell.y_cord/2)].is_wall = False

            random_chosen_cell.is_wall = False

            maze.current_cell = random_chosen_cell
            visited_cells.append(maze.current_cell)

        else:

            popped_cell = possible_to_visit.pop()
            maze.current_cell = popped_cell

    print(maze)


class Cell:
    def __init__(self, is_wall, x_cord, y_cord):
        self.is_wall = is_wall
        self.x_cord = x_cord
        self.y_cord = y_cord

    def __repr__(self):
        if self.is_wall:
            return "#"
        else:
            return " "


class Maze:
    def __init__(self, cell_list, current_cell):
        self.cell_list = cell_list
        self.current_cell = current_cell

    def __repr__(self):
        return str(self.__dict__)


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


make_maze()
