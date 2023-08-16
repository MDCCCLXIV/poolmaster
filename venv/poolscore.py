balls_sequence = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2]

balls = []
score = 0
players = []

def addPlayer(name):
    players.append({"name": name, "score": 0})

def displayPlayers():
    print("\nPlayers:")
    for idx, player in enumerate(players):
        print(f"{idx + 1}. {player['name']}: {player['score']} points")

for i in range(1, 16):
    balls.append(i)

print("Pool Game Killer Score Tracker")
print("Balls present are:", ", ".join(str(b) for b in balls))
print("Player registration")

while len(players) < 5:
    if len(players) < 2:
        player_name = input("Enter player name: ")
        addPlayer(player_name)
    elif 2 <= len(players) < 5:
        add_another = input("Do you wish to add more players? (Yes/No): ")
        if add_another.lower() == "yes":
            extra = int(input("How many extra? "))
            for i in range(extra):
                player_name = input("Enter player name: ")
                addPlayer(player_name)
        else:
            break
    else:
        print("Maximum number of players (5) reached.")
        break

if len(players) < 2:
    print("No players available. Please add players to start the game.")
elif len(players) > 5:
    print("Maximum number of players reached.")
else:
    game = True
    player_idx = 0

    last_player_scored = False
    rightBall = False
    white = False
    last_player_name = None

    while game:
        try:
            displayPlayers()
            selected_player = players[player_idx % len(players)]

            if selected_player['name'] == last_player_name:
                print(f"\n{selected_player['name']}, to play Again!")
            else:
                print(f"\n{selected_player['name']}, to play!")

            last_player_name = selected_player['name']

            if len(balls_sequence) > 0:
                selected_ball = balls_sequence[0]
                if selected_ball not in balls:
                    balls_sequence.pop(0)
                    continue 
                print(f"Play ball number: {selected_ball}")

                rightBall = int(input("Enter Ball played : "))
                if rightBall == selected_ball:
                    white_input = input("White in? (Yes/No): ")
                    white = white_input.lower() == "yes"
                    scored_ball = input("Is the ball in? (Yes/No): ")
                    scored = scored_ball.lower() == "yes"
                
                    if scored:
                        balls_sequence.pop(0)

                    if last_player_scored and rightBall and not white:
                        scored = True

                    if selected_ball in balls:
                        if 2 < selected_ball < 7:
                            value = 6
                        elif selected_ball == 1:
                            value = 16
                        elif selected_ball == 2:
                            value = 17
                        else:
                            value = selected_ball
                        rightballvalue = value
                        if white and rightBall and scored:

                            pass
                        elif not white and rightBall and scored:
                            selected_player['score'] += rightballvalue
                            last_player_scored = True
                        elif not white and not rightBall and scored:
                            selected_player['score'] -= rightballvalue
                        elif not white and not rightBall and not scored:
                            selected_player['score'] -= rightballvalue
                        elif not white and rightBall and not scored:
                            selected_player['score'] -= rightballvalue
                        elif white and rightBall and not scored:
                            selected_player['score'] -= 6
                        elif white and not rightBall and not scored:
                            selected_player['score'] -= 6

                        if scored:
                            balls.remove(selected_ball)
                        
                        else:
                            print("Ball not scored. Play will continue for this ball.")

                        other_balls_scored = input("Enter other balls scored (comma-separated, e.g., 4,7): ")
                        other_balls = [int(ball.strip()) for ball in other_balls_scored.split(",")]
                        for ball in other_balls:
                            if ball in balls_sequence:
                                if 2 < ball < 7:
                                    value = 6
                                elif ball == 1:
                                    value = 16
                                elif ball == 2:
                                    value = 17
                                else:
                                    value=ball
                                ball_sequence_value = value
                                balls_sequence.remove(ball)
                                # if white
                                    # selected_player['score']-6
                                selected_player['score'] += ball_sequence_value


                else:
                    if rightBall in balls_sequence:
                        if 2 < rightBall < 7:
                            value = 6
                        elif rightBall == 1:
                            value = 16
                        elif rightBall == 2:
                            value = 17
                        else:
                            value = rightBall
                        ball_sequence_value = value
                        selected_player['score'] -= ball_sequence_value

                        wrongBallHitSomeEnter = input("Hit the wrong ball and in the process scored the following balls (comma-separated, e.g., 4,7): ")
                        wrongBallHitSomeEnter = [int(ball.strip()) for ball in wrongBallHitSomeEnter.split(",")]

                        for ball in wrongBallHitSomeEnter:
                            if ball in balls_sequence:
                                if 2 < ball < 7:
                                    value = 6
                                elif ball == 1:
                                    value = 16
                                elif ball == 2:
                                    value = 17
                                else:
                                    value = ball
                                ball_sequence_value = value
                                balls_sequence.remove(ball)
                                selected_player['score'] += ball_sequence_value
                            else:
                                print(str(ball) + " already played")

                    

                print(balls_sequence)
                print(f"{selected_player['name']} has redeemed : {selected_player['score']} points")

                displayPlayers()
            else:
                print("Ball not found")

            if last_player_scored and rightBall and not white:
                last_player_scored = False
            else:
                player_idx = (player_idx + 1) % len(players)

        except ValueError:
            print("Invalid input. Please enter a valid ball number or 0 to exit.")

    if len(balls) == 0:
        print("No balls left. Game Over!")





