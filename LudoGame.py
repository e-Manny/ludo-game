# Author: Manuel Espinoza
# GitHub username: e-Manny
# Date: 8/3/2022
# Description: Portfolio project - Ludo Game. Wrote a program comprised of 2 classes used to evaluate the outcome of
# playing the game Ludo after being given a list of players (A, B, C, or D) and a list of rolls for each player.
# Included a decision algorithm that would determine which token (p or q) would move from each player based on given
# priority rules. Also accounted for the given game rules in the ReadMe such as being stacked, landing on an opponent,
# etc.


class Player:
    """Represents a Player object who plays the game at a certain position"""

    def __init__(self, pos):
        """Takes a string position as a parameter and creates a player object with the following data members:
        1. the position the player chooses (a, B, C, or D)
        2. the start and end space for this player based on the position chosen
        3. the current position of the player's 2 tokens (home yard, ready to go, on board, finished)
        4. current state of the player (won the game and finished or still playing)
        5. stacked state of player"""
        self._pos = pos
        if pos == "A":
            self._start = 1
        elif pos == "B":
            self._start = 15
        elif pos == "C":
            self._start = 29
        elif pos == "D":
            self._start = 43
        if pos == "A":
            self._end = 50
        elif pos == "B":
            self._end = 8
        elif pos == "C":
            self._end = 22
        elif pos == "D":
            self._end = 36
        # current position of the player's 2 tokens [home yard (H), ready to go (R), on board (B), finished (F)]
        self._curPosition = {
            "p": "H",
            "q": "H"
                            }
        self._steps = {
            "p": -1,
            "q": -1
        }
        self._curState = "Playing"   #Won, Finished, Playing
        self._stacked = "No"

    def get_curState(self):
        return self._curState

    def set_curState(self, state):
        self._curState = state

    def get_stacked(self):
        return self._stacked

    def set_stacked(self, y_or_n):
        self._stacked = y_or_n

    def set_curPosition_p(self, position):
        self._curPosition["p"] = position

    def set_curPosition_q(self, position):
        self._curPosition["q"] = position

    def set_p_steps(self, steps):
        self._steps["p"] = steps

    def set_q_steps(self, steps):
        self._steps["q"] = steps

    def get_curPosition(self):
        return self._curPosition

    def get_completed(self):
        """Takes no parameters and returns True or False if the player has finished or not finished the game"""
        if self._curState == "Won":
            return True
        else:
            return False

    def get_token_p_step_count(self):
        """Takes no parameters and returns the total steps the token p has taken on the board. Steps = -1 for
        home yard position and steps = 0 for ready to go position. The total step should not be larger than
        57. If the token is bounced back in the home squares, this bounced aprt should be subtracted from the
        step count."""
        return self._steps["p"]

    def get_token_q_step_count(self):
        """Takes no parameters and returns the total steps the token p has taken on the board. Steps = -1 for
        home yard position and steps = 0 for ready to go position. The total step should not be larger than
        57. If the token is bounced back in the home squares, this bounced aprt should be subtracted from the
        step count."""
        return self._steps["q"]

    def get_space_name(self, total_steps):
        """takes as a parameter the total steps of the token and returns the name of the space the token
        has landed on the board as a string. It can return the home yard position (‘H’) and the ready
        to go position (‘R’) as well."""
        if total_steps == -1:
            return "H"
        elif total_steps == 0:
            return "R"
        elif total_steps == 57:
            return "E"
        elif 51 <= total_steps <= 56:
            return self._pos + str(total_steps - 50)
        elif self._pos == "A":
            return str(total_steps)
        elif self._pos == "B":
            if 1 <= total_steps <= 42:
                return str(total_steps + 14)
            elif 43 <= total_steps <= 50:
                return str(total_steps - 42)
        elif self._pos == "C":
            if 1 <= total_steps <= 28:
                return str(total_steps + 28)
            elif 29 <= total_steps <= 50:
                return str(total_steps - 28)
        elif self._pos == "D":
            if 1 <= total_steps <= 14:
                return str(total_steps + 42)
            elif 15 <= total_steps <= 50:
                return str(total_steps - 14)

    def get_pos(self):
        return self._pos


class LudoGame:
    """Represents the Ludo game as played"""

    def __init__(self):
        """Creates a Ludo Game object with information about the players and the board"""
        self._player_position_list = []

    def add_player(self, player_object):
        self._player_position_list.append(player_object)

    def get_player_by_position(self, player_position):
        """Takes a parameter representing the player’s position as a string and returns the
        player object. For an invalid string parameter, it will return 'Player not found!'"""
        for player in self._player_position_list:
            if player.get_pos() == player_position:
                return player
        return "Player not found!"

    def move_token(self, player_object, token_name, steps):
        """Takes three parameters, the player object, the token name (‘p’ or ‘q’) and the steps the token
        will move on the board (int). This method will take care of one token moving on the board. It will
        also update the token’s total steps, and it will take care of kicking out other opponent tokens as
        needed. The play_game method will use this method."""

        if token_name == "p":
            if player_object.get_token_p_step_count() == 57:
                pass
            elif player_object.get_token_p_step_count() + steps > 57:
                player_object.set_p_steps(57 - (player_object.get_token_p_step_count() + steps - 57))
            elif player_object.get_space_name(player_object.get_token_p_step_count()) == "H":
                player_object.set_p_steps(0)
            elif player_object.get_space_name(player_object.get_token_p_step_count()) == "E":
                player_object.set_p_steps(57)
            else:
                player_object.set_p_steps(player_object.get_token_p_step_count() + steps)
        elif token_name == "q":
            if player_object.get_token_q_step_count() == 57:
                pass
            elif player_object.get_token_q_step_count() + steps > 57:
                player_object.set_q_steps(57 - (player_object.get_token_q_step_count() + steps - 57))
            elif player_object.get_space_name(player_object.get_token_q_step_count()) == "H":
                player_object.set_q_steps(0)
            elif player_object.get_space_name(player_object.get_token_q_step_count()) == "E":
                player_object.set_q_steps(57)
            else:
                player_object.set_q_steps(player_object.get_token_q_step_count() + steps)

        # If token lands on friendly token and are not already stacked, it will become stacked.
        if player_object.get_space_name(player_object.get_token_p_step_count()) == player_object.get_space_name(
                player_object.get_token_q_step_count()) and player_object.get_stacked() == "No"\
                and player_object.get_space_name(player_object.get_token_p_step_count()) not in ("H", "R"):
            player_object.set_stacked("Yes")

        # Post-move validations:
        if token_name == "p":
            player_object.set_curPosition_p(player_object.get_space_name(player_object.get_token_p_step_count()))
            # if player is stacked and tokens are not already in same square, move tokens to same square
            if player_object.get_stacked() == "Yes" and player_object.get_space_name(
                    player_object.get_token_p_step_count()) \
                    != player_object.get_space_name(player_object.get_token_q_step_count()):
                self.move_token(player_object, "q", steps)
            # if token lands on enemy token, it will move enemy token to their Home
            for player in self._player_position_list:
                if player_object != player and (player_object.get_space_name(
                        player_object.get_token_p_step_count()) not in ("H", "R")) and \
                        player_object.get_space_name(player_object.get_token_p_step_count()) == \
                        player.get_space_name(player.get_token_p_step_count()):
                    self.move_token(player, "p", (-1 - player.get_token_p_step_count()))
                    # if enemy landed on is stacked, send both enemy tokens to home and unstack them
                    if player.get_stacked() == "Yes":
                        player.set_stacked("No")
                # if token lands on enemy token, it will move enemy token to their Home
                elif player_object != player and (player_object.get_space_name(
                        player_object.get_token_p_step_count()) not in ("H", "R")) and \
                        player_object.get_space_name(player_object.get_token_p_step_count()) == \
                        player.get_space_name(player.get_token_q_step_count()):
                    self.move_token(player, "q", (-1 - player.get_token_q_step_count()))
                    # if enemy landed on is stacked, send both enemy tokens to home and unstack them
                    if player.get_stacked() == "Yes":
                        player.set_stacked("No")
        elif token_name == "q":
            player_object.set_curPosition_q(player_object.get_space_name(player_object.get_token_q_step_count()))
            # if player is stacked and tokens are not already in same square, move tokens to same square
            if player_object.get_stacked() == "Yes" and player_object.get_space_name(
                    player_object.get_token_p_step_count()) != player_object.get_space_name(
                    player_object.get_token_q_step_count()):
                self.move_token(player_object, "p", steps)
            # if token lands on enemy token, it will move enemy token to their Home
            for player in self._player_position_list:
                if player_object != player and (player_object.get_space_name(
                        player_object.get_token_q_step_count()) not in ("H", "R")) and \
                        player_object.get_space_name(player_object.get_token_q_step_count()) == \
                        player.get_space_name(player.get_token_p_step_count()):
                    self.move_token(player, "p", (-1 - player.get_token_p_step_count()))
                    # if enemy landed on is stacked, send both enemy tokens to home and unstack them
                    if player.get_stacked() == "Yes":
                        player.set_stacked("No")
                # if token lands on enemy token, it will move enemy token to their Home
                elif player_object != player and (player_object.get_space_name(
                        player_object.get_token_q_step_count()) not in ("H", "R")) and \
                        player_object.get_space_name(player_object.get_token_q_step_count()) == \
                        player.get_space_name(player.get_token_q_step_count()):
                    self.move_token(player, "q", (-1 - player.get_token_q_step_count()))
                    # if enemy landed on is stacked, send both enemy tokens to home and unstack them
                    if player.get_stacked() == "Yes":
                        player.set_stacked("No")

    def play_game(self, players_list, turns_list):
        """Takes two parameters: the players list, and the turns list. The players list is the list of positions
        players choose, like [‘A’, ‘C’] means two players will play the game at position A and C. Turns list is a
        list of tuples with each tuple a roll for one player. For example, [('A', 6), ('A', 4), ('C', 5)] means
        player A rolls 6, then rolls 4, and player C rolls 5. This method will create the player list first using
        the players list pass in, and then move the tokens according to the turns list following the priority rule
        and update the tokens position and the player’s game state (whether finished the game or not). After all
        the moving is done in the turns list, the method will return a list of strings representing the current
        spaces of all the tokens for each player in the list after moving the tokens following the rules
        described above. ‘H’ for home yard, ‘R’ for ready to go position, ‘E’ for finished position, and other
        letters/numbers for the space the token has landed on."""
        # Create new players from players_list
        for new_player in players_list:
            self.add_player(Player(new_player))

        # run the tuple containing info about roll and player move through the decision algorithm. This algo will decide
        # which token will move and call move_token method
        for info_tup in turns_list:
            self.decision_algorithm(self.get_player_by_position(info_tup[0]), info_tup[1])
            player_object = self.get_player_by_position(info_tup[0])
            # if a player wins, set their state as "Won"
            if player_object.get_token_p_step_count() and player_object.get_token_q_step_count() == 57:
                player_object.set_curState("Won")

        current_token_space = []
        for player in self._player_position_list:
            current_token_space.append(player.get_space_name(player.get_token_p_step_count()))
            current_token_space.append(player.get_space_name(player.get_token_q_step_count()))
            if player.get_curState() != "Won":
                player.set_curState("Finished")
        return current_token_space

    def decision_algorithm(self, player_object, steps):
        """Calls the move_token method after determining which move should be made based on passed parameters and
        move priority. This method also updates the moved token's current position"""
        if player_object.get_space_name(player_object.get_token_p_step_count()) == "H" and \
                player_object.get_space_name(player_object.get_token_q_step_count()) == "H":
            if steps != 6:
                return None
            if steps == 6:
                self.move_token(player_object, "p", steps)
        elif player_object.get_space_name(player_object.get_token_p_step_count()) != "H" and \
                player_object.get_space_name(player_object.get_token_q_step_count()) == "H":
            if steps == 6:
                self.move_token(player_object, "q", steps)
            elif steps != 6:
                self.move_token(player_object, "p", steps)
        elif player_object.get_space_name(player_object.get_token_q_step_count()) != "H" and \
                player_object.get_space_name(player_object.get_token_p_step_count()) == "H":
            if steps == 6:
                self.move_token(player_object, "p", steps)
            elif steps != 6:
                self.move_token(player_object, "q", steps)
        # If roll will take a token that is in home stretch to "E"
        elif (player_object.get_space_name(player_object.get_token_p_step_count()) or
                player_object.get_space_name(player_object.get_token_q_step_count())) in \
                ((player_object.get_pos() + "1"),
                 (player_object.get_pos() + "2"),
                 (player_object.get_pos() + "3"),
                 (player_object.get_pos() + "4"),
                 (player_object.get_pos() + "5"),
                 (player_object.get_pos() + "6")) and \
                (steps + player_object.get_token_p_step_count() == 57 or steps +
                 player_object.get_token_q_step_count() == 57):
            if steps + player_object.get_token_p_step_count() == 57:
                self.move_token(player_object, "p", steps)
            elif steps + player_object.get_token_q_step_count() == 57:
                self.move_token(player_object, "q", steps)
        # If roll will land on enemy token
        elif player_object.get_space_name(player_object.get_token_p_step_count()) != "H" and \
                player_object.get_space_name(player_object.get_token_q_step_count()) != "H":
            for player in self._player_position_list:
                if player is not player_object:
                    if player_object.get_space_name((steps + player_object.get_token_p_step_count())) in \
                            (player.get_space_name(player.get_token_p_step_count()) or
                             player.get_space_name(player.get_token_q_step_count())):
                        self.move_token(player_object, "p", steps)
                        return
                    elif player_object.get_space_name((steps + player_object.get_token_q_step_count())) in \
                            (player.get_space_name(player.get_token_p_step_count()) or
                             player.get_space_name(player.get_token_q_step_count())):
                        self.move_token(player_object, "q", steps)
                        return
            # move whichever is farther away from "E"
            if player_object.get_token_p_step_count() <= player_object.get_token_q_step_count():
                self.move_token(player_object, "p", steps)
            elif player_object.get_token_p_step_count() >= player_object.get_token_q_step_count():
                self.move_token(player_object, "q", steps)


# players = ['A', 'B']
# turns = [('A', 6),('A', 4),('A', 5),('A', 4),('A', 4),('A', 4),('A', 5),('A', 4),('A', 5),('A', 5),('A', 3),('A', 5),('A', 5),('A', 6),('A', 5),('A', 5),('A', 3),('B', 6),('B', 3),('A', 4)]
# game = LudoGame()
# current_tokens_space = game.play_game(players, turns)
# player_A = game.get_player_by_position('A')
# print(player_A.get_completed())
# print(player_A.get_token_p_step_count())
# print(current_tokens_space)
# player_B = game.get_player_by_position('B')
