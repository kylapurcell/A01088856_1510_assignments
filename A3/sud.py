def create_coordinates():
    list1 = []
    list2 = []
    list3 = []
    for i in range(0, 5):
        for j in range(0, 5):
            list1.append(i)
            list2.append(j)
    for i in list1:
        list3.append([i])
    for i in range(0, len(list3)):
        list3[i].insert(1, list2[i])
    return list3


def map(character):
    coord = create_coordinates()
    list2 = []
    for i in range(0, len(coord)):
        list2.append([coord[i][1]])
        list2[i].insert(1, coord[i][0])
    for i in range(0, len(coord)):
        if i % 5 == 0:
            print('\n')
        if character['Location'] == list2[i]:
            print('$' + '  ', end='')
        print('*' + '  ', end='')












def main():
    print("""          
   _  _      _                         _                
  / ___|__ _| |_ _ __   ___   ___ __ _| |_ __  ___  ___ 
 | |   / _` | __| '_ \ / _ \ / __/ _` | | '_ \/ __|/ _ 
 | |__| (_| | |_| |_) | (_) | (_| (_| | | |_) \__ \  __/
  \____\__,_|\__| .__/ \___/ \___\__,_|_| .__/|___/\___|
                |_|                     |_|                           """)
    print("""
    
                        _
                       | |
                       | |
                       | |
  |\                   | |                                      
 /, ~\                / /
X     `-.....-------./ /
 ~-. ~  ~              |
    \             /    |
     \  /_     ___\   /
     | /\ ~~~~~   \ |
     | | \        || |
     | |\ \       || )
    (_/ (_/      ((_/""")                   # Ascii art from https://textart.io/art/


