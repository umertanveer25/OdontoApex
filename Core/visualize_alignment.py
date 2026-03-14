import os
import glob
from PIL import Image, ImageChops

def create_overlap_visualization(img_path, mask_path, output_path):
    try:
        img = Image.open(img_path).convert("RGBA")
        mask = Image.open(mask_path).convert("RGBA")
        
        # Ensure they are the same size
        if img.size != mask.size:
            mask = mask.resize(img.size, Image.NEAREST)
        
        # Create a semi-transparent overlay
        # We'll make the mask 30% transparent
        blended = Image.blend(img, mask, alpha=0.3)
        blended.save(output_path)
        return True
    except Exception as e:
        print(f"Error creating visualization: {e}")
        return False

def main():
    base_dir = r"c:\Users\umert\Downloads\Dental_AI_Research"
    img_dir = os.path.join(base_dir, "classification")
    mask_dir = os.path.join(base_dir, "masks")
    out_dir = os.path.join(base_dir, "visualizations")
    os.makedirs(out_dir, exist_ok=True)

    # Pick top 5 samples
    samples = ["1.jpg", "10.jpg", "100.jpg", "101.jpg", "102.jpg"]
    
    for s in samples:
        img_path = os.path.join(img_dir, s)
        mask_name = s.replace(".jpg", ".png") # Based on previous list
        mask_path = os.path.join(mask_dir, mask_name)
        
        if os.path.exists(img_path) and os.path.exists(mask_path):
            out_name = f"overlay_{s.replace('.jpg', '.png')}"
            out_path = os.path.join(out_dir, out_name)
            if create_overlap_visualization(img_path, mask_path, out_path):
                print(f"Generated visualization: {out_path}")
        else:
            print(f"Skipping {s}: img or mask missing.")

if __name__ == "__main__":
    main()
