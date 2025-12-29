import os
import glob

def generate_readme_for_issuer(issuer_name, base_project_path):
    issuer_path = os.path.join(base_project_path, issuer_name)
    readme_path = os.path.join(issuer_path, "README.md")
    
    # Define patterns for image files
    patterns = [
        os.path.join(issuer_path, "**", "*.png"),
        os.path.join(issuer_path, "**", "*.jpeg"),
        os.path.join(issuer_path, "**", "*.jpg"),
        os.path.join(issuer_path, "**", "*.bmp")
    ]

    card_data = []
    for pattern in patterns:
        # Use os.path.normpath to handle mixed slashes in glob results
        for full_path in glob.glob(pattern, recursive=True):
            # Ensure paths are relative to the issuer's root for the README
            # and use forward slashes for markdown compatibility
            relative_to_issuer_path = os.path.relpath(full_path, issuer_path).replace("\\\\", "/")
            card_name = os.path.splitext(os.path.basename(full_path))[0]
            card_data.append((card_name, relative_to_issuer_path))
    
    # Sort by card name
    card_data.sort(key=lambda x: x[0].lower())

    readme_content = f"# {issuer_name} Cards\n\n"
    readme_content += "| | | |\n"
    readme_content += "|:---:|:---:|:---:|\n"
    
    # Group cards into rows of 3
    for i in range(0, len(card_data), 3):
        row_cards = card_data[i:i+3]
        row_cells = []
        for name, rel_path in row_cards:
            row_cells.append(f"![{name}](<{rel_path}>) {name}")
        
        # Fill empty cells if row_cards is less than 3
        while len(row_cells) < 3:
            row_cells.append("")

        readme_content += f"| { ' | '.join(row_cells) } |\n"


    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"Generated {readme_path}")

# List of all issuers (excluding 'Virtual ID' as per instruction)
issuers = [
    "American Express",
    "Bank of America",
    "Barclays",
    "Capital One",
    "Chase",
    "Citi",
    "Discover",
    "HSBC",
    "US Bank",
    "Penfed",
    "Synchrony",
    "Others", # 'Others' is treated as an issuer
    "Virtual ID"
]

base_project_path = os.getcwd() # Current working directory

for issuer in issuers:
    generate_readme_for_issuer(issuer, base_project_path)

print("All README.md files generated successfully.")
