import matplotlib.pyplot as plt

# Dictionary of colors with hex codes
colors_with_hex = {
    "rouge": "#FF0000", "bleu": "#0000FF", "vert": "#008000",
    "jaune": "#FFFF00", "orange": "#FFA500", "noir": "#000000",
    "blanc": "#FFFFFF", "gris": "#808080", "rose": "#FFC0CB",
    "violet": "#800080", "marron": "#8B4513", "beige": "#F5F5DC",
    "turquoise": "#40E0D0", "argent": "#C0C0C0", "or": "#FFD700",
    "bordeaux": "#800000", "cyan": "#00FFFF", "émeraude": "#50C878",
    "indigo": "#4B0082", "lavande": "#E6E6FA", "magenta": "#FF00FF",
    "olive": "#808000", "sable": "#C2B280", "saumon": "#FA8072",
    "crème": "#FFFDD0", "corail": "#FF7F50", "aubergine": "#61006d",
    "ivoire": "#FFFFF0", "chocolat": "#5a3a22", "cerise": "#DE3163"
}

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, len(colors_with_hex) * 0.4))

# Plot each color as a row
for i, (color_name, hex_code) in enumerate(colors_with_hex.items()):
    ax.add_patch(plt.Rectangle((0, i), 1, 1, color=hex_code))
    ax.text(1.05, i + 0.5, f"{color_name} ({hex_code})", va="center", fontsize=12)

# Set axis limits and remove ticks
ax.set_xlim(0, 2)
ax.set_ylim(0, len(colors_with_hex))
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)

# Show the color palette
plt.show()
