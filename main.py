import os
import shutil

output_dir = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
os.makedirs(os.path.dirname(output_dir), exist_ok=True)

source_path = os.path.dirname(os.path.abspath(__file__)) + "/entry.png"
shutil.copy2(source_path, output_dir)