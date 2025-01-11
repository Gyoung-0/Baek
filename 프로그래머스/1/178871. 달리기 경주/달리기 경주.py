def solution(players, callings):
    dict_player = {key: i for i, key in enumerate(players)}


    for run in callings:
        c = dict_player[run]
        dict_player[run] -= 1
        dict_player[ players[c-1] ] += 1
        players[c-1], players[c] = players[c], players[c-1]
        
        
    return players
    
    return 0