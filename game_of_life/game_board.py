from game_of_life.utils import add_coordinates, DEAD, LIVE


class GameBoard:
    standard_neighbor_list = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def __init__(self, board_seed, turn_count):
        self.row_count = len(board_seed)
        if self.row_count > 0:
            self.col_count = len(board_seed[0])
        self.board = []
        self.fields_map = {}
        self.states_map = {LIVE: [], DEAD: []}
        self.neighbors = {}
        self.turn_count = turn_count
        self.populate_board(board_seed)

    def populate_board(self, board_seed):
        row_idx = 0
        for row_of_values in board_seed:
            col_idx = 0
            board_row = []
            for col_value in row_of_values:
                position = (row_idx, col_idx)
                if col_value == '1':
                    board_row.append(1)
                    self.states_map[LIVE].append(position)
                    self.fields_map[position] = 1
                else:
                    board_row.append(0)
                    self.states_map[DEAD].append(position)
                    self.fields_map[position] = 0
                self.neighbors[position] = self.populate_neighbors(row_idx, col_idx)
                col_idx = col_idx + 1
            self.board.append(board_row)
            row_idx = row_idx + 1

    def populate_neighbors(self, x, y):
        neighbor_list = []
        for (a, b) in self.standard_neighbor_list:
            (temp_x, temp_y) = add_coordinates((a, b), (x, y))
            if 0 <= temp_x < self.row_count \
                    and 0 <= temp_y < self.col_count:
                neighbor_list.append((temp_x, temp_y))
        return neighbor_list

    def play(self):
        print("\nBefore Start: \n")
        self.print_board()
        self.print_dead_fields()
        self.print_live_fields()
        turn = 0
        while turn < self.turn_count:
            dead_in_this_turn = []
            live_in_this_turn = []
            for dead_position in self.states_map[DEAD]:
                position_neighbors = self.neighbors[dead_position]
                (live, dead) = self.state_counts_for_position(position_neighbors)
                if live == 3:
                    live_in_this_turn.append(dead_position)
                    self.fields_map[dead_position] = 1
                    self.board[dead_position[0]][dead_position[1]] = 1
            for live_position in self.states_map[LIVE]:
                position_neighbors = self.neighbors[live_position]
                (live, dead) = self.state_counts_for_position(position_neighbors)
                if live < 2:
                    dead_in_this_turn.append(live_position)
                    self.fields_map[live_position] = 0
                    self.board[live_position[0]][live_position[1]] = 0
                elif live > 3:
                    dead_in_this_turn.append(live_position)
                    self.fields_map[live_position] = 0
                    self.board[live_position[0]][live_position[1]] = 0
            self.remove_from_dead(live_in_this_turn)
            self.states_map[LIVE] = self.states_map[LIVE] + live_in_this_turn
            self.remove_from_live(dead_in_this_turn)
            self.states_map[DEAD] = self.states_map[DEAD] + dead_in_this_turn
            turn = turn + 1
            print("\n\n\n Board state after Turn: %d \n" % turn)
            print("To Dead from this iteration: " )
            print(dead_in_this_turn)
            print("To Live from this iteration: " )
            print(live_in_this_turn)
            self.print_board()
            self.print_dead_fields()
            self.print_live_fields()
            if len(self.states_map[LIVE]) == 0:
                break

    def state_counts_for_position(self, neighbors):
        dead_count = 0
        live_count = 0
        for neighbor in neighbors:
            if self.fields_map[neighbor] == 0:
                dead_count = dead_count + 1
            else:
                live_count = live_count + 1
        return live_count, dead_count

    def remove_from_dead(self, live_in_this_turn):
        for live in live_in_this_turn:
            self.states_map[DEAD].remove(live)

    def remove_from_live(self, dead_in_this_turn):
        for dead in dead_in_this_turn:
            self.states_map[LIVE].remove(dead)

    def print_board(self):
        print("\nCurrent Board:\n")
        for row in self.board:
            print(row)

    def print_dead_fields(self):
        print("\nDead List:\n")
        print(self.states_map[DEAD])

    def print_live_fields(self):
        print("\nLive List:\n")
        print(self.states_map[LIVE])
