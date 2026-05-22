import mkdocs_gen_files

def generate_matrix():
    # Define skills and levels (1-5)
    skills = {
        "Enterprise Security": 5,
        "Network Engineering": 5,
        "Automation (PS/Bash)": 4,
        "Virtualization": 4,
        "RF / SDR": 3,
        "Low-level Systems": 4,
        "Compliance / BIA": 5
    }

    svg_width = 400
    svg_height = 200
    bar_height = 20
    spacing = 5
    max_level = 5

    svg = f'<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg" style="background: #000; border: 1px solid #333; padding: 10px;">'
    svg += '<style>.label { fill: #0f0; font-family: monospace; font-size: 12px; } .bar { fill: #0f0; opacity: 0.3; } .fill { fill: #0f0; }</style>'

    for i, (skill, level) in enumerate(skills.items()):
        y = i * (bar_height + spacing) + 20
        # Label
        svg += f'<text x="5" y="{y + 14}" class="label">{skill}</text>'
        
        # Background Bar
        svg += f'<rect x="160" y="{y}" width="{svg_width - 180}" height="{bar_height}" class="bar" />'
        
        # Filled Bar
        fill_width = (svg_width - 180) * (level / max_level)
        svg += f'<rect x="160" y="{y}" width="{fill_width}" height="{bar_height}" class="fill" />'

    svg += '</svg>'

    with mkdocs_gen_files.open("assets/skill_matrix.svg", "w") as f:
        f.write(svg)

if __name__ == "__main__":
    generate_matrix()
