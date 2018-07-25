

def make_maze():

    maze = Maze([])

    for x in range(0, 20):
        maze.cell_list.append([])
        for y in range(0, 20):
            maze.cell_list[x].append(Cell(True, x, y))

    print(maze)

    visited_cells = []

    possible_to_visit = Stack()

    # initial cell.... for now. Know if there are ones which are unvisited by comparing lengths...

    visited_cells.append(maze.cell_list[0][1])

    # current cell is the head of the stack
    # x is vertical( rows) , y is across( columns )....

    possible_to_visit.push(maze.cell_list[0][1])

    while sum(len(x) for x in maze.cell_list) != len(visited_cells):
        if possible_to_visit.peek().x_cord + 2 < len(maze.cell_list):

            if maze.cell_list[possible_to_visit.peek().x_cord + 2][possible_to_visit.peek().y_cord] not in visited_cells:

                possible_to_visit.push(
                    maze.cell_list[possible_to_visit.peek().x_cord + 2][possible_to_visit.peek().y_cord])
        if possible_to_visit.peek().x_cord - 2 > 0:

            if maze.cell_list[possible_to_visit.peek().x_cord - 2][possible_to_visit.peek().y_cord] not in visited_cells:
                
                possible_to_visit.push(
                    maze.cell_list[possible_to_visit.peek().x_cord + 2][possible_to_visit.peek().y_cord])
        if possible_to_visit.peek().y_cord + 2 < len(maze.cell_list[0]):
            if maze.cell_list[possible_to_visit.peek().x_cord][possible_to_visit.peek().y_cord + 2] not in visited_cells:
                print()
        if possible_to_visit.peek().x_cord - 2 > 0:
            if maze.cell_list[possible_to_visit.peek().x_cord][possible_to_visit.peek().y_cord - 2] not in visited_cells:
                print()



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
    def __init__(self, cell_list):
        self.cell_list = cell_list

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
