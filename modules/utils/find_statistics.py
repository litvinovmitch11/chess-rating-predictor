import pandas as pd
import numpy as np

df_moves = pd.read_csv('../data/all_processed_moves.csv')


def percent_best_move(game_id, ost=0):
    # ost = 0 если смотрим ходы белых, иначе ost = 1
    move_in_game = df_moves[(df_moves['game_id'] == game_id) & (df_moves['move_number'] % 2 == ost)]
    matches = move_in_game[
        (move_in_game['move'] == move_in_game['best_line_1_move']) |
        (move_in_game['move'] == move_in_game['best_line_2_move']) |
        (move_in_game['move'] == move_in_game['best_line_3_move'])
        ]
    return matches.shape[0] / move_in_game.shape[0]


def min_max_delta_centipawns(game_id, ost=0, want=0):
    # ost = 0, если смотрим на ходы белых
    # want = 0, если интересуемся минимумом, want = 1, если нужен максимум и want = 2, если медиана
    last = 0
    _id = 0
    min_max_median_delta = (1000000, -1000000, 0)
    for centipawns in df_moves[df_moves['game_id'] == game_id].sort_values(by='move_number')['centipawns']:
        if _id % 2 == ost and not np.isnan(centipawns):
            min_max_median_delta = (
                min(min_max_median_delta[0], centipawns - last), max(min_max_median_delta[1], centipawns - last),
                min_max_median_delta[2] + centipawns)
        last = centipawns
        _id += 1
    min_max_median_delta = (
        min_max_median_delta[0] / 10000, min_max_median_delta[1] / 10000, (min_max_median_delta[2] / _id) / 10000)
    if want == 0:
        return min_max_median_delta[0]
    elif want == 1:
        return min_max_median_delta[1]
    return min_max_median_delta[2]


def min_centipawns_white(game_id):
    return min_max_delta_centipawns(game_id, ost=0, want=0)


def max_centipawns_white(game_id):
    return min_max_delta_centipawns(game_id, ost=0, want=1)


def median_centipawns_white(game_id):
    return min_max_delta_centipawns(game_id, ost=0, want=2)


def min_centipawns_black(game_id):
    return min_max_delta_centipawns(game_id, ost=1, want=0)


def max_centipawns_black(game_id):
    return min_max_delta_centipawns(game_id, ost=1, want=1)


def median_centipawns_black(game_id):
    return min_max_delta_centipawns(game_id, ost=1, want=2)


def win_mean(game_id, ost=0):
    # ost = 0 если смотрим ходы белых, иначе ost = 1
    move_in_game = df_moves[(df_moves['game_id'] == game_id)]
    if ost == 0:
        move_in_game['win'].mean()
    return move_in_game['lose'].mean()


def draw_mean(game_id, ost=0):
    move_in_game = df_moves[(df_moves['game_id'] == game_id)]
    return move_in_game['draw'].mean()
