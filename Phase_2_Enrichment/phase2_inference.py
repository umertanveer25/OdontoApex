import os
import torch
from PIL import Image
from torchvision import transforms
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Core.dental_ai_framework import DentalUNet, get_split_images

def run_phase_2(data_dir, model_path):
    print("--- Phase 2: Generating Synthetic Masks for OPG Enrichment ---")
    
    img_dir = os.path.join(data_dir, "classification")
    out_dir = os.path.join(data_dir, "synthetic_masks")
    os.makedirs(out_dir, exist_ok=True)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = DentalUNet(n_channels=3, n_classes=256).to(device)
    
    if os.path.exists(model_path):
        model.load_state_dict(torch.load(model_path, map_location=device))
        print("Loaded Phase 1 model.")
    else:
        print("Warning: No trained model found. Using random initialized weights for pipeline demonstration.")
    
    model.eval()
    
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
    ])
    
    valid_imgs = get_split_images("train")
    if valid_imgs is not None:
        valid_basenames = [os.path.splitext(f)[0] for f in valid_imgs]
        images = [f for f in os.listdir(img_dir) if f.endswith('.jpg') and os.path.splitext(f)[0] in valid_basenames]
        print(f"LOOCV Active: Enriching {len(images)} train images...")
    else:
        images = [f for f in os.listdir(img_dir) if f.endswith('.jpg')]
        print(f"Enriching {len(images)} images...")
    
    with torch.no_grad():
        for img_name in images[:50]: # Process a subset for the prototype
            img_path = os.path.join(img_dir, img_name)
            img = Image.open(img_path).convert("RGB")
            x = transform(img).unsqueeze(0).to(device)
            
            output = model(x)
            pred_mask = torch.argmax(output, dim=1).squeeze(0).cpu().numpy()
            
            # Save as grayscale mask
            mask_img = Image.fromarray((pred_mask * 8).astype('uint8')) # Multiplication for visibility
            mask_img.save(os.path.join(out_dir, img_name.replace('.jpg', '.png')))
            
    print(f"Phase 2 Complete. Masks saved to {out_dir}")

if __name__ == "__main__":
    base_dir = r"c:\Users\umert\Downloads\Dental_AI_Research"
    model_weight = os.path.join(base_dir, "dental_segmenter_v1.pth")
    run_phase_2(base_dir, model_weight)
