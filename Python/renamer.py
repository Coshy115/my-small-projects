# Python 3.12.9
from pathlib import Path

season_num = input("Which season are you targeting?: ")
extension = input("Please type the extension. (mp4): ")
season_dir = Path(f"C:/Users/Admin/Desktop/Shows/My Name Is Earl/Season {season_num}")

Season1 = (
    "Pilot", "Quit Smoking", "Randy's Touchdown", "Faked My Own Death", "Teacher Earl",
    "Broke Joy's Fancy Figurine", "Stole Beer from a Golfer", "Joy's Wedding", "Cost Dad the Election",
    "White Lie Christmas", "Barn Burner", "O Karma, Where Art Thou", "Stole P's HD Cart",
    "Monkeys in Space", "Something to Live For", "The Professor", "Didn't Pay Taxes", "Dad's Car",
    "Y2K", "Boogeyman", "The Bounty Hunter", "Stole a Badge", "BB", "Number One"
)
Season2 = (
        "Very Bad Things", "Jump For Joy", "Sticks & Stones", "Larceny of a Kitty Cat", "Van Hickey",
        "Made a Lady Think I Was God", "Mailbox", "Robbed a Stoner Blind", "Born a Gamblin' Man",
        "South of the Border Part Uno", "South of the Border Part Dos", "Our 'Cops' Is On",
        "Buried Treasure", "Kept a Guy Locked in a Truck", "Foreign Exchange Student", "Blow",
        "The Birthday Party", "Guess Who's Coming Out of Joy", "Harassed a Reporter", "Two Balls, Two Strikes",
        "G.E.D.", "Get a Real Job", "The Trial"
)
Season3 = (
        "My Name Is Inmate #28301-016",
        "The Gangs of Camden County", "The Frank Factor", "Creative Writing", "Frank's Girl",
        "Our Other 'Cops' Is On", "Randy in Charge",
        "Midnight Bun", "Burn Victim", "Early Release", "Bad Earl",
        "I Won't Die with a Little Help from My Friends", "Stole a Motorcycle",
        "No Heads and a Duffel Bag", "Killerball", "Love Octagon", "Girl Earl",
        "Camdenites"
)
Season4 = (
        "The Magic Hour", "Monkeys Take a Bath", "Joy in a Bubble", "Stole an RV", "Sweet Johnny",
        "We've Got Spirit", "Quit Your Snitchin'", "Little Bad Voodoo Brother", "Sold a Guy a Lemon Car",
        "Earl and Joy's Anniversary", "Nature's Game Show", "Reading Is a Fundamental Case",
        "Orphan Earl", "Got the Babysitter Pregnant", "Darnell Outed Part 1", "Darnell Outed Part 2",
        "Randy's List Item", "Friends with Benefits", "My Name Is Alias", "Chaz Dalton's Space Academy",
        "Witch Lady", "Pinky", "Bullies", "Gospel", "Inside Probe Part 1", "Inside Probe Part 2", "Dodge's Dad"
)

season_var_name = f"Season{season_num}"
Target = globals().get(season_var_name)

if(season_dir.exists() and season_dir.is_dir()):
    files = sorted(season_dir.iterdir(), key=lambda f: f.name)
    
    for i, file in enumerate(files, start=1):
        old_path = file
        new_path = season_dir / f"{i:02d} - {Target[i-1]}.{extension}"
        old_path.rename(new_path)
else:
    print("Folder does not exist.")