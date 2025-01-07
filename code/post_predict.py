import os
from datetime import datetime

# Team logos mapping
team_logos = {
    "Arsenal": "logos/Arsenal.svg",
    "Tottenham Hotspur": "logos/TottenhamHotspur.svg",
    "Chelsea": "logos/Chelsea.svg",
    "Bournemouth": "logos/Bournemouth.svg",
    "Newcastle United": "logos/NewcastleUnited.svg",
    "Wolverhampton Wanderers": "logos/WolverhamptonWanderers.svg",
    "Brentford": "logos/Brentford.svg",
    "Manchester City": "logos/ManchesterCity.svg",
    "Manchester United": "logos/ManchesterUnited.svg",
    "Southampton": "logos/Southampton.svg",
    "West Ham United": "logos/WestHamUnited.svg",
    "Fulham": "logos/Fulham.svg",
    "Everton": "logos/Everton.svg",
    "Aston Villa": "logos/AstonVilla.svg",
    "Nottingham Forest": "logos/NottinghamForest.svg",
    "Ipswich Town": "logos/IpswichTown.svg",
    "Brighton and Hove Albion": "logos/BrightonHoveAlbion.svg",
    "Leicester City": "logos/LeicesterCity.svg",
    "Crystal Palace": "logos/CrystalPalace.svg"
}

def update_ui():
    # Input and output file paths
    input_file = "./fixtures_predictions.txt"
    output_file = "README.md"

    # Read predictions from the .txt file
    with open(input_file, "r") as f:
        lines = f.readlines()

    # Start writing the Markdown content
    with open(output_file, "w") as md:
        md.write("# Football Game Predictions\n\n")
        md.write("Here are the latest predictions for upcoming football matches:\n\n")
        md.write("<table>\n")
        md.write("  <tr>\n")
        md.write("    <th>Date</th>\n")
        md.write("    <th>Home Team</th>\n")
        md.write("    <th>Away Team</th>\n")
        md.write("    <th>Predicted Result for Home</th>\n")
        md.write("  </tr>\n")
        
        for line in lines[1:]:  # Skip the header row
            date, home, away, result = line.strip().split("\t")
            home_logo = team_logos.get(home, "")
            away_logo = team_logos.get(away, "")

            # Add a row to the table
            md.write("  <tr>\n")
            md.write(f"    <td>{date}</td>\n")
            md.write(f"    <td><img src='{home_logo}' alt='{home}' width='50'> {home}</td>\n")
            md.write(f"    <td><img src='{away_logo}' alt='{away}' width='50'> {away}</td>\n")
            md.write(f"    <td>{result}</td>\n")
            md.write("  </tr>\n")
        
        md.write("</table>\n")
        md.write(f"*Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")

