from django.shortcuts import render

def generate_shades(base_color, steps):
    # base_color: "noir", "rouge", "bleu", "vert"
    # Here, we use a fixed RGB value and vary the brightness
    # noir: black -> 0, rouge: red, bleu: blue, vert: green
    color_map = {
        "noir": (0, 0, 0),
        "rouge": (255, 0, 0),
        "bleu": (0, 0, 255),
        "vert": (0, 128, 0)
    }
    base_rgb = color_map.get(base_color, (0,0,0))
    shades = []
    for i in range(steps):
        # Vary brightness between 0% and 100% (using simple linear interpolation)
        factor = (i+1) / steps  # from 1/steps to 1.0
        r = int(base_rgb[0] * factor)
        g = int(base_rgb[1] * factor)
        b = int(base_rgb[2] * factor)
        shades.append(f"rgb({r}, {g}, {b})")
    return shades

def table_view(request):
    steps = 50
    # Generate color shades for each of the 4 columns
    shades_noir = generate_shades("noir", steps)
    shades_rouge = generate_shades("rouge", steps)
    shades_bleu = generate_shades("bleu", steps)
    shades_vert = generate_shades("vert", steps)
    # Create a list combining background colors of 4 cells for each row
    rows = []
    for i in range(steps):
        rows.append([shades_noir[i], shades_rouge[i], shades_bleu[i], shades_vert[i]])
    context = {
        "headers": ["Noir", "Rouge", "Bleu", "Vert"],
        "rows": rows,
        "cell_width": 80,
        "cell_height": 40,
    }
    return render(request, "ex03/table.html", context)

