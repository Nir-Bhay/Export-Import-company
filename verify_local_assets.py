import os
import re

def verify_images():
    workspace_root = "/workspaces/Export-Import-company"
    html_file = os.path.join(workspace_root, "index.html")
    
    with open(html_file, 'r') as f:
        content = f.read()

    # Regex to find src attributes starting with assets/ or similar local paths
    # We look for src="assets/..." specifically as that's what we used
    matches = re.findall(r'src="(assets/[^"]+)"', content)
    
    missing_files = []
    
    print(f"Checking {len(matches)} local image references...")
    
    for relative_path in matches:
        full_path = os.path.join(workspace_root, relative_path)
        
        if not os.path.exists(full_path):
            missing_files.append(relative_path)
            print(f"MISSING: {relative_path}")
            
    if missing_files:
        print(f"\nFound {len(missing_files)} missing files.")
    else:
        print("\nAll local image references matched existing files.")

if __name__ == "__main__":
    verify_images()
