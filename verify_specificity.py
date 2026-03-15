import cv2
import numpy as np
import os
from PIL import Image

def extract_clinical_features(img_path):
    img = Image.open(img_path).convert("L")
    arr = np.array(img)
    
    entropy_val = np.std(arr) / (np.mean(arr) + 1e-6)
    edges = cv2.Canny(arr, 100, 200)
    edge_density = np.sum(edges > 0) / edges.size
    local_contrast = np.mean(cv2.convertScaleAbs(cv2.Laplacian(arr, cv2.CV_64F)))
    
    return {
        "entropy": float(entropy_val),
        "edge_density": float(edge_density),
        "local_contrast": float(local_contrast)
    }

def main():
    img_dir = r"c:\Users\umert\Downloads\Dental_AI_Research\images"
    if not os.path.exists(img_dir):
        print(f"Error: Directory {img_dir} not found.")
        return
        
    images = [f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if len(images) < 2:
        print("Objective Verification: Need at least 2 images for comparison.")
        print(f"Current images in directory: {images}")
        return

    print("--- Clinical Specificity Audit ---")
    results = {}
    for img_name in images[:3]: # Compare first 3
        path = os.path.join(img_dir, img_name)
        features = extract_clinical_features(path)
        results[img_name] = features
        print(f"\n[Audit] Image: {img_name}")
        for k, v in features.items():
            print(f"  - {k}: {v:.4f}")

    # Calculate variance
    if len(results) >= 2:
        keys = ["entropy", "edge_density", "local_contrast"]
        print("\n[VERDICT] Variance Detection:")
        for k in keys:
            vals = [res[k] for res in results.values()]
            diff = max(vals) - min(vals)
            status = "PASS (Individualized)" if diff > 1e-5 else "FAIL (Static detected)"
            print(f"  - {k} variance: {diff:.6f} -> {status}")

if __name__ == "__main__":
    main()
