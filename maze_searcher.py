import random

class MazeSearcher:

    def make_maze():

        maze = Maze([], Cell(True, 1, 1))

        for x in range(0, 11):
            maze.cell_list.append([])
            for y in range(0, 51):
                maze.cell_list[x].append(Cell(True, x, y))

        # current cell is the head of the stack
        # x is vertical( rows) , y is across( columns )....

        maze.current_cell.is_wall = False

        expanded_maze = MazeSearcher.explore_neighbours(maze)

        for i in range(len(expanded_maze.cell_list)):
            print(*expanded_maze.cell_list[i])

    def explore_neighbours(maze):

        visited_cells = [maze.current_cell]

        possible_to_visit = Stack()
        possible_to_visit.push(maze.current_cell)

        while possible_to_visit.size() != 0:
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

            if maze.current_cell.y_cord - 2 > 0:

                if maze.cell_list[maze.current_cell.x_cord][maze.current_cell.y_cord - 2] not in visited_cells:
                    neighbours_list.append(maze.cell_list[maze.current_cell.x_cord][maze.current_cell.y_cord - 2])

            if len(neighbours_list) != 0:

                random_chosen_cell = random.choice(neighbours_list)
                possible_to_visit.push(maze.current_cell)

                # Remove wall in between by doing the average of them + making the one we go to not a wall

                maze.cell_list[int((maze.current_cell.x_cord + random_chosen_cell.x_cord) / 2)][
                    int((maze.current_cell.y_cord + random_chosen_cell.y_cord) / 2)].is_wall = False

                random_chosen_cell.is_wall = False

                maze.current_cell = random_chosen_cell
                visited_cells.append(maze.current_cell)

                neighbours_list.clear()

            else:

                maze.current_cell = possible_to_visit.pop()

        return maze


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

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


MazeSearcher.make_maze()
