if __name__ == '__main__':
    from os import chdir, getcwd
    from xml.etree.ElementTree import parse
    if getcwd()[-1] == 's': chdir("players")
    players = parse('players.xml').getroot()
    print("The players of the CyberWater 2 Git basics challenge are…\n")
    for player in players.findall('player'):
        print(player.attrib["name"].title()+"! (https://github.com/%s/)"%player.text)
    print("\nThanks for playing!")