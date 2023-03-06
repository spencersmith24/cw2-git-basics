if __name__ == '__main__':
    from os import chdir
    from os.path import dirname, realpath
    from xml.etree.ElementTree import parse
    chdir(dirname(realpath(__file__)))
    players = parse('players.xml').getroot()
    print("The players of the CyberWater 2 Git basics challenge are…\n")
    for player in players.findall('player'):
        print(player.attrib["name"].title()+"! (https://github.com/%s/)"%player.text.replace('\n','').rstrip())
        if favorites := player.findall('favorite'):
            for thing in favorites:
                try: print('\t• Their favorite %s is %s!'%(thing.attrib["type"], thing.text))
                except KeyError: raise KeyError("No “type” attribute was provided! (Add it by adding “type=\"something\"” to your item's tag!)")
        else: raise KeyError("Either no “favorite” keys were added, or they weren't added as child keys to “player!”")
    print("\nThanks for playing!")