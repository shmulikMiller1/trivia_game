import json
import random
import argparse

print("Welcome to the TRIVIA GAME!")


parser = argparse.ArgumentParser(description="TRIVIA GAME")
parser.add_argument('num_players', type=int, help='Number of players')
parser.add_argument('game_level', choices=['easy', 'medium', 'hard'], help='Level of the game')
parser.add_argument('player_names', nargs='+', help='Names of the players')
args = parser.parse_args()

if len(args.player_names) != args.num_players:
    print("Number of player names provided does not match the number of players specified.")
    exit()


with open("questions.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    easy = data["easy"]
    medium = data["medium"]
    hard = data["hard"]

players_dic = {name: 0 for name in args.player_names}
players_list = args.player_names
game_level = args.game_level


def ask_questions(questions):
    for i in range(4):
        for player in players_list:
            question = random.choice(questions)
            print(f"\n{player}, here's your question:")
            print(f"Question: {question['question']}")
            for idx, answer in enumerate(question['answers'], 1):
                print(f"\t{idx}. {answer}")
            player_answer = int(input(f"{player}, please enter the correct answer (1-4): "))
            while not 1 <= player_answer <= 4:
                player_answer = int(input(f"{player}, please enter a valid answer (1-4): "))
            if player_answer == question['correct_answer']:
                players_dic[player] += 1


if game_level == "easy":
    ask_questions(easy)
elif game_level == "medium":
    ask_questions(medium)
elif game_level == "hard":
    ask_questions(hard)


high_score = max(players_dic.values())
winners = [key for key, value in players_dic.items() if value == high_score]
print(f"The winner(s) in this play is/are {winners}. Well done!")
print(players_dic)

