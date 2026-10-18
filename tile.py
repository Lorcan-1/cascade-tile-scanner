import os
import time

TileNames = {
    73: "Glacial laboratory",
    78: "Laboratory",
    87: "Hall of legends",
    105: "Brig",
    119: "Agri-zone",
    120: "Serenity",
    142: "Habitat",
    144: "Lunaro",
    162: "Angel roost",
    164: "Amphitheatre",
    226: "Albrecht park",
    274: "Cargo bay",
    402: "Hangar",
    493: "Schoolyard",
}

ExoCount = {
    "Laboratory": 3,
    "Hall of legends": 3,
    "Brig": 3,
    "Agri-zone": 3,
    "Serenity": 4,
    "Habitat": 3,
    "Lunaro": 3,
    "Angel roost": 4,
    "Amphitheatre": 3,
    "Albrecht park": 4,
    "Cargo bay": 3,
    "Hangar": 5,
    "Schoolyard": 4,
    "Glacial laboratory": 3,
}

eelog = os.path.join(
    os.getenv("LOCALAPPDATA"),
    "Warframe",
    "EE.log"
)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


Totalvalue = 0
TileCount = 0
MissingRoomDeadline = None

with open(eelog, "r", encoding="utf-8", errors="ignore") as f:
    f.seek(0, os.SEEK_END)

    while True:
        if (
            TileCount == 2
            and MissingRoomDeadline is not None#the missing room deadline is ai i was losing my mind trying to find the new room id
            and time.time() >= MissingRoomDeadline
        ):
            TileName = "new room"
            TileValue = 3
            Color = "\033[91m"
            Reset = "\033[0m"

            print(f"{Color}Tile: {TileName} | Value: {TileValue}{Reset}")

            Totalvalue += TileValue
            TileCount += 1

            print(f"Total exos: {Totalvalue}")
            print("-" * 30)

            Totalvalue = 0
            TileCount = 0
            MissingRoomDeadline = None

        line = f.readline()

        if not line:
            time.sleep(0.1)
            continue

        if "HighLevelGraph setup" in line:
            try:
                TileId = int(line.split()[5])

                if TileId not in TileNames:
                    continue

                TileName = TileNames[TileId]
                TileValue = ExoCount.get(TileName, 0)

                if TileValue >= 4:
                    Color = "\033[92m"  #green 
                elif TileValue == 3:
                    Color = "\033[91m"  #red 
                else:
                    Color = "\033[97m"  #white 

                Reset = "\033[0m"

                print(f"{Color}Room: {TileName} | exos: {TileValue}{Reset}")

                Totalvalue += TileValue
                TileCount += 1

                if TileCount == 2:
                    MissingRoomDeadline = time.time() + 5

                if TileCount == 3:
                    if Totalvalue > 11:
                        print(f"\033[38;5;220mTotal exos: {Totalvalue}\033[0m")
                    elif Totalvalue < 12:
                        print(f"Total exos: {Totalvalue}")
                    print("-" * 30)

                    Totalvalue = 0
                    TileCount = 0
                    MissingRoomDeadline = None

            except (IndexError, ValueError):
                pass

#by fortnite 
