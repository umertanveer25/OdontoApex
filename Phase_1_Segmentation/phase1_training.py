import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Core.dental_ai_framework import DentalSegmentationDataset, DentalUNet, get_split_images

def train_phase_1(data_dir, epochs=10, batch_size=4, lr=0.001):
    print("--- Phase 1: Training PDL Boundary Delineation Engine ---")
    print("Strategy: Enamel-Dentin Junction Gradient Mapping via Attention U-Net")
    
    img_dir = os.path.join(data_dir, "images")
    mask_dir = os.path.join(data_dir, "masks")
    
    # Get LOOCV train split
    valid_imgs = get_split_images("train")
    if valid_imgs is not None:
        print(f"LOOCV Active: Training on {len(valid_imgs)} images.")

    # Preprocessing
    transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
    ])
    
    dataset = DentalSegmentationDataset(img_dir, mask_dir, transform=transform, valid_images=valid_imgs)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    model = DentalUNet(n_channels=3, n_classes=256).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        for images, masks in dataloader:
            images = images.to(device)
            masks = masks.long().to(device) # Masks are already indices [N, H, W]
            
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, masks)
            loss.backward()
            optimizer.step()
            
            running_loss += loss.item()
            
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {running_loss/len(dataloader):.4f}")
        
    model_path = os.path.join(data_dir, "dental_segmenter_v1.pth")
    torch.save(model.state_dict(), model_path)
    print(f"Phase 1 Complete. Model saved to {model_path}")

if __name__ == "__main__":
    base_dir = r"c:\Users\umert\Downloads\Dental_AI_Research"
    # Note: This is set to 1 epoch for prototype demonstration.
    # Increase to 50+ for real research.
    train_phase_1(base_dir, epochs=1)
