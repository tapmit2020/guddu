player={'name': 'Tapas', 'attack': 10, 'heal': 16, 'health': 100}
monster = {'name': 'rawan', 'attack': 12, 'health': 100}
game_running = True

while game_running == True:


    print('please select action')
    print('1) Attack')
    print('2) Heal')

    player_choice = input()


    if player_choice == '1':
    
        monster['health'] =  monster['health'] - player['attack']
        player['health'] = player['health'] - monster['attack']
        print(monster['health'])
        print(player['health'])

    elif player_choice == '2':
        print('Heal player')


    else:
        print('Invalid input')  
    if player['health'] <= 0:
        game_running = False