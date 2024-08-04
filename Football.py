#ie seri team darim...
#to har khat nataiej bazi ro midim be barname
#bad ie seri etelaat midim be karbar
# iran - spain
# iran - portugal
# iran morocco
# spain - portugal
# spain - morocco
# portugal - morocco
#emtiaz team haro be tartib bala midim


#nemoone vooroodi:   
#                   2-2
#                   2-1
#                   1-2
#                   2-2
#                   3-1
#                   2-1

#nemoone khoorooji:
#                   Spain  wins:1 , loses:0 , draws:2 , goal difference:2 , points:5
#                   Iran  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
#                   Portugal  wins:1 , loses:1 , draws:1 , goal difference:0 , points:4
#                   Morocco  wins:1 , loses:2 , draws:0 , goal difference:-2 , points:3

#bar asas emtiaz sort beshe
#age mosavi bud tedad win
#age unam mosavi bud hooroof alefba




d = {'Iran': {'name': 'Iran', 'wins': 0, 'loses': 0, 'draws': 0},
      'Spain': {'name': 'Spain', 'wins': 0, 'loses': 0, 'draws': 0},
        'Portugal': {'name': 'Portugal', 'wins': 0, 'loses': 0, 'draws': 0},
          'Morocco': {'name': 'Morocco', 'wins': 0, 'loses': 0, 'draws': 0}}



def whoWins(team1, team2, score1, score2):
    if score1 > score2:
        d[team1]['wins'] += 1
        d[team2]['loses'] += 1
    
      
    elif score1 == score2:
        d[team1]['draws'] += 1
        d[team2]['draws'] += 1

    else:
        d[team1]['loses'] += 1
        d[team2]['wins'] += 1

    d[team1]['goaldifference'] = d[team1].get('goaldifference', 0) + (score1 - score2)
    d[team2]['goaldifference'] = d[team2].get('goaldifference', 0) + (score2 - score1)
    d[team1]['points'] = (d[team1].get('wins', 0) * 3) + d[team1].get('draws', 0)
    d[team2]['points'] = (d[team2].get('wins', 0) * 3) + d[team2].get('draws', 0)


iran, spain = input().split('-')
whoWins('Iran', 'Spain', int(iran), int(spain))

iran, portugal = input().split('-')
whoWins('Iran', 'Portugal', int(iran), int(portugal))

iran, morocco = input().split('-')
whoWins('Iran', 'Morocco', int(iran), int(morocco))

spain, portugal = input().split('-')
whoWins('Spain', 'Portugal', int(spain), int(portugal))

spain, morocco = input().split('-')
whoWins('Spain', 'Morocco', int(spain), int(morocco))

portugal, morocco = input().split('-')
whoWins('Portugal', 'Morocco', int(portugal), int(morocco))

l = list(d.values())
l.sort(key = lambda x: (-x['points'], -x['wins'], x['name']))

for i in l:
    print('%s  wins:%s , loses:%s , draws:%s , goal difference:%s , points:%s' %(i['name'], i['wins'], i['loses'], i['draws'], i['goaldifference'], i['points']))