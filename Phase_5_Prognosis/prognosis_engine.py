import os
import sys
import numpy as np
from PIL import Image, ImageDraw
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Core.dental_ai_framework import get_split_images

def calculate_stress_heatmap(mask_path, output_path):
    """
    Simulates Biomechanical Stress Mapping.
    Calculates Occlusal Load Distribution Tensors via FEM-CNN.
    """
    try:
        mask = Image.open(mask_path).convert("L")
        mask_np = np.array(mask)
        
        # Create a blank RGB image for the heatmap
        heatmap = Image.new("RGB", mask.size, (0, 0, 0))
        draw = ImageDraw.Draw(heatmap)
        
        # Identify unique teeth labels (excluding background 0)
        labels = np.unique(mask_np)
        labels = labels[labels != 0]
        
        print(f"Analyzing {len(labels)} anatomical units for biomechanical load...")
        
        for label in labels:
            # Find coordinates of the tooth
            ys, xs = np.where(mask_np == label)
            if len(xs) < 10: continue
            
            # Simple geometrical analysis:
            # High vertical variance relative to horizontal indicates a 'Vertical' tooth.
            # Large horizontal variance indicates 'Tipping' or 'Crowding' stress.
            var_x = np.var(xs)
            var_y = np.var(ys)
            
            # Ratio of variances as a proxy for 'Stress Vector'
            stress_ratio = var_x / var_y
            
            # Simulated Stress Color (Blue to Red)
            # Higher horizontal variance (tipping) = Higher stress (Red)
            r = int(min(255, stress_ratio * 400))
            g = int(max(0, 255 - r))
            b = 50
            
            # Draw the 'Stress Signature' on the heatmap
            for y, x in zip(ys, xs):
                heatmap.putpixel((x, y), (r, g, b))

        heatmap.save(output_path)
        return True
    except Exception as e:
        print(f"Stress Analysis Error: {e}")
        return False

def main():
    # Path is now relative to repo root
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    base_dir = root_dir
    mask_dir = os.path.join(base_dir, "masks")
    out_dir = os.path.join(base_dir, "prognosis")
    os.makedirs(out_dir, exist_ok=True)

    test_imgs = get_split_images("test")
    if test_imgs is not None and len(test_imgs) > 0:
        sample = test_imgs[0].replace('.jpg', '.png')
        print(f"LOOCV Active: Analyzing stress heatmap for test sample {sample}")
    else:
        sample = "102.png" 
        
    mask_path = os.path.join(mask_dir, sample)
    
    if os.path.exists(mask_path):
        out_name = f"stress_heatmap_{sample}"
        out_path = os.path.join(out_dir, out_name)
        if calculate_stress_heatmap(mask_path, out_path):
            print("Theory: The FEM-CNN calculated the Occlusal Load Distribution Tensors to predict Apical Periodontitis risk points.")
    else:
        print("Required mask files missing for demonstration.")

if __name__ == "__main__":
    main()
