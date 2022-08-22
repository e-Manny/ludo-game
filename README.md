<a id="back-to-top"></a> 

# Simplified Ludo CS162 Portfolio Project

> This was the submission for my CS162 final project. The requirements were to build a playable game where 2 - 4 players
> could input their rolls and have them evaluated by the program to determine the final position of each players' tokens.
> I will go over my thought process in writing the most significant portions of the program's components.

---

## Program Overview

The program consists of two classes that help evaluate the rolls received when the game is initiated with the play_game
method. All the rolls made during the game must be entered at one time in a list because the game is concluded after 
the play_game method finishes running. To see the full requirements of the program, please reference the project 
requirements file.

#### Classes

- Player
- Ludo Game

[Back To The Top](#read-me)

---

## The Player Class and significant methods

This class represents the player who plays at a certain position.

### Initializing the self._start and self._end Data Members

Initializing those data members for the Player was one of my challenges. I considered using a dictionary to store the
values of those data members for all potential positions of a player and building my get_methods to only access the
correct values based on the player's positions. 

In retrospect, this seems to be the more efficient option, but I decided to use conditional statements. I made this 
decision to avoid potential for mistakes from having all the start and end points available to all the players. With my 
approach, once the class determines the position of the player, the correct data members values are initialized and the
object is unable to access the values of other positions.


###get_space_name Method

Another challenge I faced was returning the name of the space that a token landed on for use in logical functions of 
other methods. The "Home" "Ready" and "End" square names were easy since the step count is the same for all the
players regardless of starting position. However, all the other square names are different even with the same step
count. My solution was to implement some conditional statements with simple math to produce the correct name for the
square. 

My only issue with this part is that the code seems a bit repetitive and I feel like there must be a more efficient way 
to write it which I haven't found yet.

[Back To The Top](#back-to-top)

---

## The LudoGame Class and significant methods

This class represents the game as it is played under the simplified rules.

###play_game Method

The initial and guiding method of the program. This was the first method I wrote which served as a guide
for which other methods I was going to need and what those methods needed to do. I broke the required functions of this 
method into three parts:
- Add the participating players to the game
- Iterate through the rolls in the order given and determine which token will move where
- Return the final space names that each player's tokens occupy

###decision_algorithm Method

This method is responsible for determining which token is going to move by considering the move-priority requirements 
given for the project. This method calls the move_token method to actually change the position of the token.

###move_token Method
The most significant method in the program. This method is responsible for actually moving the token which the 
decision_algorithm method determines needs to be moved. This was a very challenging method because moving a token may come
with certain consequences which may affect the position of other tokens based on the game rules. My solution to this was
to have a post-validation section within the method where the method would recursively call itself to handle any
consequences that affect the position of any other token that is affected which is not initially determined by the 
decision_algorithm. There may be a scenario where the movement of that second token affects a third token, this is also
handled thanks to this recursive implementation.

[Back To The Top](#back-to-top)


---

## Future of the project
I would ultimately like to implement a GUI and change the functionality of this program to allow for a more traditional
Ludo gameplay experience. Currently, this program better serves as a validation tool to verify the final token
locations for all the participating players after finishing playing the game under the simplified rules. 
My intent is to make this a turn-based game with more traditional Ludo rules while keeping the same board layout.

[Back To The Top](#back-to-top)

---

## How to use

As a simple example, the program could be used as follows:

```
players = ['A', 'B']
turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]
game = LudoGame()
current_tokens_space = game.play_game(players, turns)
player_A = game.get_player_by_position('A')
print(player_A.get_completed())
print(player_A.get_token_p_step_count())
print(current_tokens_space)
player_B = game.get_player_by_position('B')
print(player_B.get_space_name(55))

And the output will be:
False
28
[‘28’, ‘28’, ‘21’, ‘H’]
B5

```
[Back To The Top](#back-to-top)
