#!/usr/bin/env python3
"""
Script to:
1. Correct game names in the CSV
2. Generate game-docs folders with manifest.json files
"""

import csv
import json
import os
import re
from pathlib import Path

# Corrections for known games (original -> corrected official name)
NAME_CORRECTIONS = {
    "ArmA": "ARMA: Armed Assault",
    "ArmA 2": "ARMA 2",
    "ArmA 3": "ARMA 3",
    "DCS": "DCS World",
    "Colin McRae DiRT 2": "DiRT 2",
    "DiRT": "Colin McRae: DiRT",
    "GRID": "GRID",
    "DiRT 3": "DiRT 3",
    "F1 2011": "F1 2011",
    "F1 2015": "F1 2015",
    "F1 2016": "F1 2016",
    "F1 2017": "F1 2017",
    "F1 2018": "F1 2018",
    "IL-2 Forgotten Battles ACE Pacific Fighters": "IL-2 Sturmovik: Forgotten Battles",
    "IL-2 Sturmovik: Battle of Stalingrad": "IL-2 Sturmovik: Battle of Stalingrad",
    "Euro Truck Simulator": "Euro Truck Simulator",
    "American Truck Simulator": "American Truck Simulator",
    "Falcon BMS": "Falcon BMS",
    "Free Falcon 4.0: Allied Force": "Falcon 4.0: Allied Force",
    "Free Falcon 5": "FreeFalcon 5",
    "Flight Simulator 2002": "Microsoft Flight Simulator 2002",
    "Flight Simulator 2004": "Microsoft Flight Simulator 2004: A Century of Flight",
    "Flight Simulator X": "Microsoft Flight Simulator X",
    "MS Flight Simulator 2020": "Microsoft Flight Simulator (2020)",
    "MS Flight Simulator 2024": "Microsoft Flight Simulator 2024",
    "FSX Steam Edition": "Microsoft Flight Simulator X: Steam Edition",
    "Microsoft Flight": "Microsoft Flight",
    "X-Plane (32 and 64 bit)": "X-Plane",
    "X-Plane Pilot View (32 and 64 bit)": "X-Plane (Pilot View Plugin)",
    "Lock-On: Modern Air Combat": "Lock On: Modern Air Combat",
    "LockOn: Flaming Cliffs 2": "Lock On: Flaming Cliffs 2",
    "rFactor": "rFactor",
    "rFactor2": "rFactor 2",
    "rFactor Pro": "rFactor Pro",
    "rFPro": "rFactor Pro (rFpro)",
    "iRacing": "iRacing",
    "Live For Speed": "Live for Speed",
    "Live for Speed S2": "Live for Speed S2",
    "RACE (the WTCC game)": "RACE: The WTCC Game",
    "RACE 07 RACE GTR 2": "RACE 07",
    "GTR": "GTR - FIA GT Racing Game",
    "GT Legends": "GT Legends",
    "Richard Burns Rally": "Richard Burns Rally",
    "Assetto Corsa Competizione": "Assetto Corsa Competizione",
    "Project CARS 2": "Project CARS 2",
    "C.A.R.S.": "Project CARS",
    "RaceRoom Racing Experience": "RaceRoom Racing Experience",
    "Beamng.drive": "BeamNG.drive",
    "Elite: Dangerous": "Elite Dangerous",
    "Star Citizen": "Star Citizen",
    "EVE Online": "EVE Online",
    "EVE Valkyrie": "EVE: Valkyrie",
    "Star Wars: Squadrons": "Star Wars: Squadrons",
    "X2: The Threat": "X2: The Threat",
    "X3: Albion Prelude": "X3: Albion Prelude",
    "X-Rebirth": "X Rebirth",
    "Combat Flight Simulator 3": "Microsoft Combat Flight Simulator 3: Battle for Europe",
    "Orbiter 2005 Plug-In": "Orbiter 2005",
    "Orbiter 2006": "Orbiter 2006",
    "Orbiter 2006 Plug-In": "Orbiter 2006",
    "Prepar3D": "Prepar3D",
    "Rise of Flight": "Rise of Flight",
    "Wings of Prey": "Wings of Prey",
    "Birds of Prey": "IL-2 Sturmovik: Birds of Prey",
    "Birds of Steel": "Birds of Steel",
    "War Thunder": "War Thunder",
    "Take On Helicopters": "Take On Helicopters",
    "Take on Mars": "Take On Mars",
    "DayZ": "DayZ",
    "Operation Flashpoint 2 (inactive)": "Operation Flashpoint 2",
    "Operation Flashpoint(r): Dragon Rising(tm)": "Operation Flashpoint: Dragon Rising",
    "VBS2": "VBS2",
    "VBS2 2.0": "VBS2",
    "VBS3 IG": "VBS3",
    "Enemy Engaged: Commanche vs Hokum": "Enemy Engaged: Comanche vs. Hokum",
    "Enemy Engaged 2": "Enemy Engaged 2",
    "Steel Beasts 2": "Steel Beasts II",
    "Steel Beasts Pro": "Steel Beasts Pro",
    "Steel Beasts Pro Personal": "Steel Beasts Pro PE",
    "Steel Beasts Professional": "Steel Beasts Pro",
    "Mechwarrior Online": "MechWarrior Online",
    "MechWarrior Online": "MechWarrior Online",
    "Half Life 2": "Half-Life 2",
    "Source Engine (Half-Life 2)": "Source Engine (Half-Life 2)",
    "Counter Strike": "Counter-Strike",
    "CS GO MOD": "Counter-Strike: Global Offensive",
    "Garry's Mod": "Garry's Mod",
    "Halo": "Halo: Combat Evolved",
    "America's Army": "America's Army",
    "America's Army 3": "America's Army 3",
    "Battlefield 2": "Battlefield 2",
    "Battlefield 2 Trauma Studios": "Battlefield 2",
    "Battlefield 2142": "Battlefield 2142",
    "BF2 (Unsupported Demo)": "Battlefield 2 (Demo)",
    "Tom Clancy's H.A.W.X.": "Tom Clancy's H.A.W.X.",
    "Tom Clancy's H.A.W.X. 2": "Tom Clancy's H.A.W.X. 2",
    "Farming Simulator 17": "Farming Simulator 17",
    "Farmer Simulator 2009": "Farming Simulator 2009",
    "Ship Simulator 2006": "Ship Simulator 2006",
    "Ship Simulator 2008": "Ship Simulator 2008",
    "Sail Simulator 5": "Sail Simulator 5",
    "Rail Simulator 1": "Rail Simulator",
    "RailWorks 2": "RailWorks 2: Train Simulator",
    "RailWorks 5 (TS2014)": "Train Simulator 2014",
    "Train Sim World": "Train Sim World",
    "Train Sim World 2": "Train Sim World 2",
    "Dovetail Train Simulator 2015": "Train Simulator 2015",
    "Dovetail Flight School": "Dovetail Flight School",
    "Microsoft Train Simulator": "Microsoft Train Simulator",
    "OMSI Bus Simulator": "OMSI - The Bus Simulator",
    "Bus Simulator 16": "Bus Simulator 16",
    "Bussim 18": "Bus Simulator 18",
    "Tourist Bus Simulator": "Tourist Bus Simulator",
    "Fernbus Simulator": "Fernbus Simulator",
    "Subnautica": "Subnautica",
    "Rust": "Rust",
    "H1Z1": "H1Z1",
    "The Crew": "The Crew",
    "PlanetSide 2": "PlanetSide 2",
    "PlanetSide 2 M.E.": "PlanetSide 2",
    "Dungeons and Dragons Online": "Dungeons & Dragons Online",
    "Gothic 3": "Gothic 3",
    "FreeSpace2": "FreeSpace 2",
    "Beyond The Red Line": "Beyond the Red Line",
    "Descent: Underground": "Descent: Underground",
    "D2x-XL": "D2X-XL",
    "Overload": "Overload",
    "Evochron Mercenary": "Evochron Mercenary",
    "Evochron Legacy": "Evochron Legacy",
    "Evochron Legends": "Evochron Legends",
    "Evochron Renegades": "Evochron Renegades",
    "Evochron Alliance 2.0": "Evochron Alliance",
    "Grand Prix Legends": "Grand Prix Legends",
    "Grand Theft Auto: San Andreas": "Grand Theft Auto: San Andreas",
    "NecroVisioN": "NecroVisioN",
    "Crysis Mod": "Crysis",
    "Aces High II": "Aces High II",
    "NetKar Pro": "netKar PRO",
    "Kart Racing Pro": "KartKraft",
    "KartKraft": "KartKraft",
    "Condor: The Competitive Soaring Simulator": "Condor: The Competition Soaring Simulator",
    "Silent Wings": "Silent Wings",
    "RealFlight": "RealFlight",
    "Phoenix R/C": "Phoenix R/C",
    "Micro Flight": "Micro Flight",
    "Future Pinball": "Future Pinball",
    "Rowan's Battle Of Britain": "Rowan's Battle of Britain",
    "Battle of Britain II - Wings of Victory": "Battle of Britain II: Wings of Victory",
    "Battle of Britain (iENT)": "Battle of Britain",
    "Over Flanders Fields": "Over Flanders Fields",
    "Wings: Over Flanders Fields": "Wings Over Flanders Fields",
    "First Eagles Wings Over Europe Strike Fighters": "First Eagles: The Great War",
    "Red Baron 3D": "Red Baron 3D",
    "Dawn of Aces II": "Dawn of Aces",
    "Dawn of Aces/Red Baron": "Dawn of Aces",
    "Flyboys / Warbirds": "WarBirds",
    "Apache: Air Assault": "Apache: Air Assault",
    "Combat Helo": "Combat Helo",
    "Comanche": "Comanche",
    "Escape from Tarkov": "Escape from Tarkov",
    "Squad": "Squad",
    "Insurgency": "Insurgency",
    "Rising Storm 2: Vietnam": "Rising Storm 2: Vietnam",
    "Red Orchestra: Ostfront": "Red Orchestra: Ostfront 41-45",
    "Red Orchestra: Heroes of Stalingrad": "Red Orchestra 2: Heroes of Stalingrad",
    "Arma Reforger": "Arma Reforger",
    "theHunter": "theHunter",
    "Miscreated": "Miscreated",
    "Space Shuttle Mission 2007": "Space Shuttle Mission 2007",
    "Reentry - An Orbital Simulator": "Reentry - An Orbital Simulator",
    "Kerbal Space Program": "Kerbal Space Program",
    "Eagle Lander 3D": "Eagle Lander 3D",
    "Tacview": "Tacview",
    "Trainz": "Trainz",
    "Fractured Space": "Fractured Space",
    "Strike Suit Zero": "Strike Suit Zero",
    "Starshatter": "Starshatter",
    "Vox Machinae": "Vox Machinae",
    "Stormworks: Build and Rescue": "Stormworks: Build and Rescue",
    "SnowRunner": "SnowRunner",
    "Rig N Roll": "Rig 'n' Roll",
    "18 Wheels of Steel: Haulin'": "18 Wheels of Steel: Haulin'",
    "Infinity: Battlescape": "Infinity: Battlescape",
    "Project Wingman": "Project Wingman",
    "Combat Air Patrol 2": "Combat Air Patrol 2: Military Flight Simulator",
    "Tiny Combat Arena": "Tiny Combat Arena",
    "Nuclear Option": "Nuclear Option",
    "VTOL VR": "VTOL VR",
    "Aerofly FS": "Aerofly FS",
    "Aerofly": "Aerofly RC",
    "FlyInside Flight Simulator": "FlyInside Flight Simulator",
    "FlightGear": "FlightGear",
    "Flight Gear": "FlightGear",
    "Interstellar Rift": "Interstellar Rift",
    "PULSAR: Lost Colony": "PULSAR: Lost Colony",
    "Objects in Space": "Objects in Space",
    "Everspace 2": "EVERSPACE 2",
    "Le Mans Ultimate": "Le Mans Ultimate",
    "Construction Simulator": "Construction Simulator",
    "Heavy Duty Challenge": "Heavy Duty Challenge: The Off-Road Truck Simulator",
    "The Bus": "The Bus",
    "On the Road": "On The Road - Truck Simulator",
    "Truck and Logistics Simulator": "Truck and Logistics Simulator",
    "World of Aircraft": "World of Aircraft: Glider Simulator",
    "DiRT 4": "DiRT 4",
    "gRally": "gRally",
    "Radial-G : Racing Revolved": "Radial-G: Racing Revolved",
    "Vector 36": "Vector 36",
    "Air Missions: HIND": "Air Missions: HIND",
    "Flying Tigers: Shadows Over China": "Flying Tigers: Shadows Over China",
    "Combat Pilot": "Combat Pilot",
    "Burning Lands": "Burning Lands",
    "AIRWARS": "Airwars",
    "Earth Analog": "Earth Analog",
    "Frontier Pilot Simulator": "Frontier Pilot Simulator",
    "Frontiers Reach": "Frontiers Reach",
    "Helicopter Gunship D.E.X": "Helicopter Gunship DEX",
    "Sub Level Zero": "Sublevel Zero",
    "Cypher City": "Cipher City",
    "Space Hulk: Deathwing": "Space Hulk: Deathwing",
    "End Space": "End Space",
    "Go For Launch: Mercury": "Go For Launch: Mercury",
    "Starfighter Inc.": "Starfighter Inc.",
    "Enemy Starfighter": "Enemy Starfighter",
    "GoD Factory: Wingmen": "GoD Factory: Wingmen",
    "The Battle of Sol": "The Battle of Sol",
    "World of Diving": "World of Diving",
    "CDF Ghostship": "CDF Ghostship",
    "Ghostship Aftermath": "CDF Ghostship",
    "CDF Starfighter": "CDF Starfighter",
    "Miner Wars": "Miner Wars 2081",
    "X Motor Racing": "X Motor Racing",
    "Solitude": "Solitude",
    "Sir You Are Being Hunted": "Sir, You Are Being Hunted",
    "Police 1013": "Police 1013",
    "Stride": "STRIDE",
    "Into the Dungeon": "Into the Dungeon",
    "Rift's Cave": "Rift's Cave",
    "World Racing 2": "World Racing 2",
    "Ford Racing 3": "Ford Racing 3",
    "NASCAR Heat": "NASCAR Heat",
    "NASCAR Racing 2003 season": "NASCAR Racing 2003 Season",
    "NASCAR SimRacing": "NASCAR SimRacing",
    "F-22 Total Air War": "F-22 Total Air War",
    "Janes F18": "Jane's F/A-18",
    "Jet Thunder": "Jet Thunder",
    "Jetfighter V": "JetFighter V: Homeland Protector",
    "Whirlwind of Vietnam": "Whirlwind of Vietnam: UH-1",
    "Battleground Europe : World War II Online": "Battleground Europe: World War II Online",
    "Battleground Europe : WWII Online": "Battleground Europe: World War II Online",
    "Brothers In Arms": "Brothers in Arms",
    "Commandos Strike Force": "Commandos: Strike Force",
    "Test Drive Unlimited": "Test Drive Unlimited",
    "Mig Alley": "MiG Alley",
    "M4 Tank Platoon": "M1 Tank Platoon II",
    "M4 Tank Brigade": "M1 Tank Platoon",
    "WWII Battle Tanks: T-34 vs. Tiger": "WWII Battle Tanks: T-34 vs. Tiger",
    "Down In Flames": "Down in Flames",
    "Jumpgate": "Jumpgate: The Reconstruction Initiative",
    "Jumpgate Evolution": "Jumpgate Evolution",
    "Jump to Lightspeed": "Star Wars Galaxies: Jump to Lightspeed",
    "Rogue Warrior": "Rogue Warrior",
    "Total War": "Total War",
    "Crashday": "Crashday",
    "Cross Racing Championship": "Cross Racing Championship Extreme",
    "Full Out": "Full Auto",
    "Nitro Stunt Racing": "Nitro Stunt Racing",
    "Superkarting": "Super 1 Karting",
    "Sirocco Racing": "Sirocco Racing",
    "Big Scale Racing": "Big Scale Racing",
    "Stoked Rider": "Stoked Rider",
    "RidingStar": "Riding Star",
    "Concept RS": "Concept RS",
    "Harrier Attack II": "Harrier Attack II",
    "Fighter Ace": "Fighter Ace",
    "Fighter Ops": "Fighter Ops",
    "Fighter Squadron: Screamin Demons Over Europe": "Fighter Squadron: The Screamin' Demons Over Europe",
    "Flying Tigers": "Flying Tigers",
    "FlyingGuns": "Flying Guns",
    "Target: Korea": "Target: Korea",
    "Target: Rabaul": "Target: Rabaul",
    "Storm of War: the Battle of Britain": "Storm of War: Battle of Britain",
    "Bomber Squadron": "Bomber Squadron",
    "Conflict Taiwan": "Conflict: Taiwan",
    "Arvoch Alliance": "Arvoch Alliance",
    "Arvoch Conflict": "Arvoch Conflict",
    "Void War": "Void War",
    "Lore (Dark Horizons)": "Dark Horizons: Lore",
    "Dark Horizons Lore": "Dark Horizons: Lore",
    "HoverAssault": "HoverAssault",
    "Viper Arena": "Viper Racing",
    "Meteor Maze": "Meteoroid Maze",
    "Starfighter": "Starfighter",
    "Sailors of the Sky": "Sailors of the Sky",
    "Virtual Sailor": "Virtual Sailor",
    "TrackIR SDK": "TrackIR SDK",
    "X-Wing Alliance": "Star Wars: X-Wing Alliance",
    "Demon Core": "Demon Core",
    "Love": "LOVE",
    "Illumina": "Illumina",
    "Gamma": "Gamma",
    "Wallbusters": "Wallbusters",
    "Chopper": "Chopper",
    "Paraworld": "ParaWorld",
}

def slugify(name):
    """Convert game name to folder-friendly slug."""
    # Convert to lowercase
    slug = name.lower()
    # Replace special characters and spaces with hyphens
    slug = re.sub(r"[':.,!?&®™()\/]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    # Remove multiple consecutive hyphens
    slug = re.sub(r"-+", "-", slug)
    # Remove leading/trailing hyphens
    slug = slug.strip("-")
    return slug

def correct_name(name):
    """Apply name corrections if available."""
    return NAME_CORRECTIONS.get(name, name)

def parse_csv(filepath):
    """Parse the CSV file and return list of game entries."""
    games = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            if not row.get('Game Name'):
                continue
            games.append({
                'number': int(row['No']) if row.get('No') else None,
                'original_name': row['Game Name'],
                'name': correct_name(row['Game Name']),
                'game_protocol': row.get('Game protocol', ''),
                'supported_since': row.get('Supported since', ''),
                'verified': True if row.get('Verified') == 'V' else None,
                'by': row.get('By') if row.get('By') else None,
                'international_id': row.get('INTERNATIONAL_ID', ''),
                'ftn_id': row.get('FTN_ID', ''),
            })
    return games

def update_csv(filepath, games):
    """Update CSV with corrected names."""
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['No', 'Game Name', 'Game protocol', 'Supported since', 'Verified', 'By', 'INTERNATIONAL_ID', 'FTN_ID']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        for game in games:
            writer.writerow({
                'No': game['number'],
                'Game Name': game['name'],
                'Game protocol': game['game_protocol'],
                'Supported since': game['supported_since'],
                'Verified': 'V' if game['verified'] else '',
                'By': game['by'] if game['by'] else '',
                'INTERNATIONAL_ID': game['international_id'],
                'FTN_ID': game['ftn_id'],
            })

def create_manifest(game):
    """Create manifest dict for a game."""
    return {
        'name': game['name'],
        'number': game['number'],
        'game_protocol': game['game_protocol'],
        'supported_since': game['supported_since'],
        'verified': game['verified'],
        'by': game['by'],
        'international_id': game['international_id'],
        'ftn_id': game['ftn_id'],
    }

def generate_game_docs(games, output_dir):
    """Generate game-docs folders with manifest.json files."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    created = 0
    skipped = 0
    
    for game in games:
        slug = slugify(game['name'])
        game_dir = output_path / slug
        
        # Create directory
        game_dir.mkdir(exist_ok=True)
        
        # Create manifest.json
        manifest_path = game_dir / 'manifest.json'
        manifest = create_manifest(game)
        
        with open(manifest_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        
        created += 1
        print(f"Created: {slug}/manifest.json")
    
    return created, skipped

def main():
    # Paths
    csv_path = 'facetracknoir supported games.csv'
    output_dir = 'docs/game-docs'
    
    # Parse CSV
    print(f"Reading CSV: {csv_path}")
    games = parse_csv(csv_path)
    print(f"Found {len(games)} games")
    
    # Count corrections
    corrections = sum(1 for g in games if g['original_name'] != g['name'])
    print(f"Applied {corrections} name corrections")
    
    # Update CSV with corrections
    print(f"\nUpdating CSV with corrections...")
    update_csv(csv_path, games)
    print("CSV updated!")
    
    # Generate game-docs
    print(f"\nGenerating game-docs in: {output_dir}")
    created, skipped = generate_game_docs(games, output_dir)
    print(f"\nDone! Created {created} game folders")

if __name__ == '__main__':
    main()






