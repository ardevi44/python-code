import random

player_score = 0
computer_score = 0

options_to_play = ["🪩", "📄", "✂️"]
game_over = False
attempt = 0
max_attempt = 3

while not game_over:
  user_option = options_to_play[random.randint(0,2)]
  computer_option = options_to_play[random.randint(0,2)]

  user_wins = (user_option == "🪩" and computer_option == "✂️") or (user_option == "📄" and computer_option == "🪩") or (user_option == "✂️" and computer_option == "📄")

  if user_option == computer_option:
    print(f"\n😁 : {user_option}  vs  💻 : {computer_option} => 😑 ... 🔌 Draw, no body wins in this try 😶...")
  elif user_wins:
    player_score += 1
    print(f"\n😁 : {user_option}  vs  💻 : {computer_option} => 😁 has ... 🚨: {player_score} {"point" if player_score == 1 else "points"}")
  else:
    computer_score += 1
    print(f"\n😁 : {user_option}  vs  💻 : {computer_option} => 💻 has ... 🚨: {computer_score} {"point" if computer_score == 1 else "points"}")
  
  attempt += 1

  if ((attempt == max_attempt) or (player_score == 2) or (computer_score == 2)):
    game_over = True
    print(f"\nGame Over! 🚨🚨🚨 Player score:[{player_score}], 🚨🚨🚨 Console score:[{computer_score}]")
    if player_score == computer_score:
      print("\nYour finally ... Draw try another.")
    elif player_score > computer_score:
      print("\nThe player wins the game! 😁👍")
    else:
      print("\nThe console wins the game! 💻👍")
   