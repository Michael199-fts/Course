#Задание №6

class WrongNumberOfPlayersError(Exception):
    pass
class NoSuchStrategyError(Exception):
    pass
def rps_game_winner(players_mass=None):
    if players_mass == None:
        return None
    if len(players_mass) != 2:
        raise WrongNumberOfPlayersError('WrongNumberOfPlayersError')
#исключение в случае, когда слишком много игроков
    if players_mass[0][1] != 'P' and players_mass[0][1] != 'S' and players_mass[0][1] != 'R' or players_mass[1][1] != 'P' and players_mass[1][1] != 'S' and players_mass[1][1] != 'R':
        raise NoSuchStrategyError("NoSuchStrategyError")
#исключение в случае, когда подаются неверные значения
    if players_mass[0][1] == 'P' and players_mass[1][1] == 'R':
        return str(players_mass[0][0]) + ' ' + str(players_mass[0][1])
    if players_mass[0][1] == 'R' and players_mass[1][1] == 'S':
        return str(players_mass[0][0]) + ' '+ str(players_mass[0][1])
    if players_mass[0][1] == 'S' and players_mass[1][1] == 'P':
        return str(players_mass[0][0]) + ' '+ str(players_mass[0][1])
    if players_mass[0][1] == 'R' and players_mass[1][1] == 'P':
        return str(players_mass[1][0]) + ' '+ str(players_mass[1][1])
    if players_mass[0][1] == 'P' and players_mass[1][1] == 'S':
        return str(players_mass[1][0]) + ' '+ str(players_mass[1][1])
    if players_mass[0][1] == 'S' and players_mass[1][1] == 'R':
        return str(players_mass[1][0]) + ' '+ str(players_mass[1][1])
    if players_mass[0][1] == players_mass[1][1]:
        return str(players_mass[0][0]) + ' '+ str(players_mass[0][1])
#формирование ответа на вариант исхода игры

#print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
#print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))
print(rps_game_winner())