
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Double-Six Dominoes")
root.geometry("850x650")
root.configure(bg="#176B45")

# Domino settings
TILE_WIDTH = 100
TILE_HEIGHT = 48
GAP = 12
DOT_RADIUS = 4

# Positions for dots on each half of a domino
DOT_POSITIONS = {
    0: [],
    1: [(0.5, 0.5)],
    2: [(0.25, 0.25), (0.75, 0.75)],
    3: [(0.25, 0.25), (0.5, 0.5), (0.75, 0.75)],
    4: [(0.25, 0.25), (0.75, 0.25),
        (0.25, 0.75), (0.75, 0.75)],
    5: [(0.25, 0.25), (0.75, 0.25),
        (0.5, 0.5),
        (0.25, 0.75), (0.75, 0.75)],
    6: [(0.25, 0.2), (0.75, 0.2),
        (0.25, 0.5), (0.75, 0.5),
        (0.25, 0.8), (0.75, 0.8)]
}

def draw_half(canvas, x, y, value, width, height):
    """Draw the dots for one half of a domino."""
    for px, py in DOT_POSITIONS[value]:
        cx = x + px * width
        cy = y + py * height
        r = DOT_RADIUS
        canvas.create_oval(
            cx-r, cy-r, cx+r, cy+r,
            fill="black", outline="black"
        )

def draw_domino(canvas, x, y, a, b):
    """Draw one domino tile."""
    w, h = TILE_WIDTH, TILE_HEIGHT

    canvas.create_rectangle(
        x, y, x+w, y+h,
        fill="white", outline="black", width=2
    )

    # Divider between the two halves
    canvas.create_line(
        x+w/2, y, x+w/2, y+h,
        fill="black", width=2
    )

    draw_half(canvas, x, y, a, w/2, h)
    draw_half(canvas, x+w/2, y, b, w/2, h)

# Heading
heading = tk.Label(
    root,
    text="DOUBLE-SIX DOMINOES",
    font=("Arial", 24, "bold"),
    bg="#176B45",
    fg="white"
)
heading.pack(pady=15)

subtitle = tk.Label(
    root,
    text="Complete set: 28 dominoes",
    font=("Arial", 12),
    bg="#176B45",
    fg="white"
)
subtitle.pack(pady=5)

# Scrollable canvas
container = tk.Frame(root, bg="#176B45")
container.pack(fill="both", expand=True, padx=15, pady=10)

canvas = tk.Canvas(
    container,
    bg="#176B45",
    highlightthickness=0
)
scrollbar = tk.Scrollbar(
    container, orient="vertical", command=canvas.yview
)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Generate every unique pair from 0-0 through 6-6
domino_set = [
    (a, b)
    for a in range(7)
    for b in range(a, 7)
]

# Arrange the 28 tiles in four columns
columns = 4
for index, (a, b) in enumerate(domino_set):
    row = index // columns
    col = index % columns

    x = 15 + col * (TILE_WIDTH + GAP)
    y = 15 + row * (TILE_HEIGHT + GAP)

    draw_domino(canvas, x, y, a, b)

# Update the scrollable area
canvas.configure(
    scrollregion=canvas.bbox("all")
)

# Start the application
root.mainloop()
