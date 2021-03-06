import random


class MazeSearcher:

    def initialise_filled_maze(height, width, start_point_x, start_point_y):

        maze = Maze([], Cell(True, False, start_point_x, start_point_y))

        for x in range(0, height):
            maze.cell_list.append([])
            for y in range(0, width):
                maze.cell_list[x].append(Cell(True, False, x, y))

        # current cell is the head of the stack
        # x is vertical( rows) , y is across( columns )....

        maze.current_cell.is_wall = False

        expanded_maze = MazeSearcher.recursive_backtrack(maze)
        vertices = MazeSearcher.find_vertices(expanded_maze)
        vertices_with_edge_info = MazeSearcher.find_edges(maze, vertices)

        for vertex in vertices_with_edge_info:
            print(str(vertex.x_cord) + ", " + str(vertex.y_cord) + ", " + str(vertex.edges))

        for i in range(len(expanded_maze.cell_list)):
            print(*expanded_maze.cell_list[i])

    def recursive_backtrack(maze):

        visited_cells = [maze.current_cell]

        possible_to_visit = Stack()
        possible_to_visit.push(maze.current_cell)

        while possible_to_visit.size() != 0:
            neighbours_list = []

            x_coord = maze.current_cell.x_cord
            y_coord = maze.current_cell.y_cord

            if x_coord + 2 < len(maze.cell_list):

                if maze.cell_list[x_coord + 2][y_coord] not in visited_cells:
                    neighbours_list.append(maze.cell_list[x_coord + 2][y_coord])

            if x_coord - 2 > 0:

                if maze.cell_list[x_coord - 2][y_coord] not in visited_cells:
                    neighbours_list.append(maze.cell_list[x_coord - 2][y_coord])

            if y_coord + 2 < len(maze.cell_list[0]):

                if maze.cell_list[x_coord][y_coord + 2] not in visited_cells:
                    neighbours_list.append(maze.cell_list[x_coord][y_coord + 2])

            if maze.current_cell.y_cord - 2 > 0:

                if maze.cell_list[x_coord][y_coord - 2] not in visited_cells:
                    neighbours_list.append(maze.cell_list[x_coord][y_coord - 2])

            if len(neighbours_list) != 0:

                random_chosen_cell = random.choice(neighbours_list)
                possible_to_visit.push(maze.current_cell)

                # Remove wall in between by doing the average of them + making the one we go to not a wall

                maze.cell_list[int((x_coord + random_chosen_cell.x_cord) / 2)][
                    int((y_coord + random_chosen_cell.y_cord) / 2)].is_wall = False

                random_chosen_cell.is_wall = False

                maze.current_cell = random_chosen_cell
                visited_cells.append(maze.current_cell)

                neighbours_list.clear()

            else:

                maze.current_cell = possible_to_visit.pop()

        return maze

    def find_vertices(maze):
        # Corners are vertices in the Dijkstra algorithm
        vertices_list = []

        for row in maze.cell_list:
            for cell in row:
                if not cell.is_wall:
                    vertices = MazeSearcher.corner_information(maze, cell)
                    if vertices:
                        vertices_list.append(vertices)
                        cell.is_vertices = True

        return vertices_list

    def corner_information(maze, cell):

        valid_corner_codes = ["UL", "UR", "DL", "RD", "URD", "RDL", "UDL", "URL", "U", "R", "D", "L"]

        corner_code = ""

        if maze.cell_list[cell.x_cord-1][cell.y_cord].is_wall:
            corner_code += "U"
        if maze.cell_list[cell.x_cord][cell.y_cord+1].is_wall:
            corner_code += "R"
        if maze.cell_list[cell.x_cord+1][cell.y_cord].is_wall:
            corner_code += "D"
        if maze.cell_list[cell.x_cord][cell.y_cord-1].is_wall:
            corner_code += "L"

        if corner_code in valid_corner_codes:
            print(corner_code)
            return Vertex(False, True, cell.x_cord, cell.y_cord, [], corner_code)

        else:
            return False

    def find_edges(maze, vertices):

        for vertex in vertices:

            # then must have an edge upwards
            if "U" not in vertex.corner_type:
                vertex.edges.append(MazeSearcher.search_direction(maze, -1, 0, vertex))
            if "R" not in vertex.corner_type:
                vertex.edges.append(MazeSearcher.search_direction(maze, 0, 1, vertex))
            if "D" not in vertex.corner_type:
                vertex.edges.append(MazeSearcher.search_direction(maze, 1, 0, vertex))
            if "L" not in vertex.corner_type:
                vertex.edges.append(MazeSearcher.search_direction(maze, 0, -1, vertex))

        return vertices

    def search_direction(maze, x_direction, y_direction, vertex):
        found = False

        while not found:
            current_cell = maze.cell_list[vertex.x_cord + x_direction][vertex.y_cord + y_direction]
            if current_cell.is_vertices:
                found
                return current_cell
            else:
                if x_direction > 0:
                    x_direction += 1
                if x_direction < 0:
                    x_direction -= 1
                if y_direction > 0:
                    y_direction += 1
                if y_direction < 0:
                    y_direction -= 1


class Cell:
    def __init__(self, is_wall, is_vertices, x_cord, y_cord):
        self.is_wall = is_wall
        self.is_vertices = is_vertices
        self.x_cord = x_cord
        self.y_cord = y_cord

    def __repr__(self):
        if self.is_wall:
            return "#"
        if self.is_vertices:
            return "."
        else:
            return " "


class Vertex(Cell):

    # Edges is a set of tuples, representing an edge from a vertex, and its cost to reach it.
    # corner type allows more efficiency when searching for connecting vertices
    # corner type list follows following code U = Up cell is wall, L = Left cell is wall etc...
    # so code URL means Up right and Left occupied (clockwise from Up)

    def __init__(self, is_wall, is_vertices, x_cord, y_cord, edges, corner_type):
        Cell.__init__(self, is_wall, is_vertices, x_cord, y_cord)
        self.edges = edges
        self.corner_type = corner_type

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


MazeSearcher.initialise_filled_maze(111, 111, 1, 1)
