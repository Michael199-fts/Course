#Задание №6
def rps_game_winner(players_mass):
    if len(players_mass) > 2:
        raise Exception('WrongNumberOfPlayersError')
#исключение в случае, когда слишком много игроков
    if players_mass[0][1] != 'P' and players_mass[0][1] != 'S' and players_mass[0][1] != 'R' or players_mass[1][1] != 'P' and players_mass[1][1] != 'S' and players_mass[1][1] != 'R':
        raise Exception("NoSuchStrategyError")
#исключение в случае, когда подаются неверные значения
    if players_mass[0][1] == 'P' and players_mass[1][1] == 'R':
        return players_mass[0]
    if players_mass[0][1] == 'R' and players_mass[1][1] == 'S':
        return players_mass[0]
    if players_mass[0][1] == 'S' and players_mass[1][1] == 'P':
        return players_mass[0]
    if players_mass[0][1] == 'R' and players_mass[1][1] == 'P':
        return players_mass[1]
    if players_mass[0][1] == 'P' and players_mass[1][1] == 'S':
        return players_mass[1]
    if players_mass[0][1] == 'S' and players_mass[1][1] == 'R':
        return players_mass[1]
    if players_mass[0][1] == players_mass[1][1]:
        return players_mass[0]
#формирование ответа на вариант исхода игры
"""
print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))
"""