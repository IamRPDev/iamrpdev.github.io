import mkdocs_gen_files
from pathlib import Path

# Path to the source profile
source_profile = Path("../.source/USERPROFILE_RPDev.md")

if source_profile.exists():
    with open(source_profile, "r") as f:
        content = f.read()
    
    # Create a virtual file in the wiki
    with mkdocs_gen_files.open("automated_profile.md", "w") as f:
        f.write(content)
        
    mkdocs_gen_files.set_edit_path("automated_profile.md", source_profile)
