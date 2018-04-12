
COLOUR_CODES = {"CadetBlue2": "#8ee5ee", "CornflowerBlue": "#6495ed", "Chartreuse4": "#458600",
                "DarkOliveGreen3": "#a2cd5a", "DarkTurquoise": "#00ced1", "Gold1": "#ffd700",
                "IndianRed2": "#eeb363", "PaleVioletRed2": "#ee799f", "RosyBrown4": "#8b6969",
                "Snow2": "#eee9e9"}

colour = input("Enter the colour name:")
if colour in COLOUR_CODES:

    print("Colour: {} Hex Code: {}\n".format(colour, COLOUR_CODES[colour]))
else:
    print("Invalid Colour")
    colour = input("Enter the colour name:")


for key, value in COLOUR_CODES.items():
    print("Colour Name: {:<15} Hex Code: {:<7}".format(key, value))