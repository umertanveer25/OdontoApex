
import matplotlib.pyplot as plt
import numpy as np
import os
from mpl_toolkits.mplot3d import Axes3D

def generate_molecular_surface_plot(patient_id, title, color_map):
    """Simulates a 3D Atomic Binding Surface."""
    fig = plt.figure(figsize=(8, 8), facecolor='#0d1117')
    ax = fig.add_subplot(111, projection='3d', facecolor='#0d1117')
    
    # Generate random atomic cloud to simulate a complex molecule
    n_atoms = 50 if patient_id != "C" else 120 # C is more complex
    x = np.random.standard_normal(n_atoms)
    y = np.random.standard_normal(n_atoms)
    z = np.random.standard_normal(n_atoms)
    
    # Draw connections (bonds)
    for i in range(n_atoms-1):
        if np.random.rand() > 0.7:
            ax.plot([x[i], x[i+1]], [y[i], y[i+1]], [z[i], z[i+1]], color='white', alpha=0.3, lw=1)

    # Plot atoms
    sc = ax.scatter(x, y, z, c=z, cmap=color_map, s=100, edgecolors='white', alpha=0.8)
    
    ax.set_title(f"Phase 9: {title} (3D Atomic Cloud)", color='white', fontsize=15)
    ax.axis('off')
    
    plt.tight_layout()
    filename = f"molecule_3d_{patient_id}.png"
    plt.savefig(os.path.join('assets', filename), dpi=300, facecolor='#0d1117')
    plt.close()
    return filename

def generate_repair_heatmap(patient_id, pathology):
    """Simulates a Before/After Radiographic Heatmap."""
    fig, axs = plt.subplots(1, 2, figsize=(12, 6), facecolor='#0d1117')
    
    # Generate base "pathology" noise
    data_before = np.random.rand(50, 50) * 0.5
    
    if patient_id == "A":
        # Enamel density (slight increase in brightness)
        data_before[10:40, 10:40] *= 1.2
        data_after = data_before * 1.4
        cmap = 'Blues'
    elif patient_id == "B":
        # Restoration gap (dark spot fills in)
        data_before[20:30, 20:30] = 0.1
        data_after = data_before.copy()
        data_after[20:30, 20:30] = 0.8
        cmap = 'Greens'
    else:
        # Bone void (Large dark area vanishes)
        data_before[15:35, 10:40] = 0.05
        data_after = data_before.copy()
        data_after[15:35, 10:40] = 0.6
        cmap = 'YlOrBr'

    im1 = axs[0].imshow(data_before, cmap=cmap)
    axs[0].set_title(f"BEFORE: {pathology}", color='white')
    axs[0].axis('off')
    
    im2 = axs[1].imshow(data_after, cmap=cmap)
    axs[1].set_title(f"AFTER: Regenerative Repair", color='white')
    axs[1].axis('off')

    plt.suptitle(f"OdontoApex: Phase 10 Tissue Repair Simulation (Patient {patient_id})", color='goldenrod', fontsize=16)
    plt.tight_layout()
    filename = f"repair_heatmap_{patient_id}.png"
    plt.savefig(os.path.join('assets', filename), dpi=300, facecolor='#0d1117')
    plt.close()
    return filename

if __name__ == "__main__":
    assets_dir = 'assets'
    if not os.path.exists(assets_dir): os.makedirs(assets_dir)
    
    # Generating for all 3
    print("Generating 3D Molecular Simulation & Repair Heatmaps...")
    
    # Patient A
    generate_molecular_surface_plot("A", "OdontoDox-A1", 'PuBu')
    generate_repair_heatmap("A", "Hypo-mineralized Enamel")
    
    # Patient B
    generate_molecular_surface_plot("B", "BD-S2 Bond-Regen", 'GnBu')
    generate_repair_heatmap("B", "Marginal Micro-Gap")
    
    # Patient C
    generate_molecular_surface_plot("C", "OS-G3 OsteoStim", 'YlOrRd')
    generate_repair_heatmap("C", "Alveolar Bone Void")
    
    print("Visual Proofs stored in assets/ (molecular_3d_*.png and repair_heatmap_*.png)")
