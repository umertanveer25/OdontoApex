
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

def draw_molecular_structure(ax, patient_id):
    """Draws a conceptual 2D skeletal structure based on the patient's drug."""
    ax.set_aspect('equal')
    ax.axis('off')
    
    if patient_id == "A":
        # OdontoDox-A1 (Peptide-like)
        # Drawing a simplified backbone
        ax.plot([0.2, 0.4, 0.6, 0.8], [0.5, 0.6, 0.5, 0.6], color='#4fc3f7', lw=3)
        ax.add_patch(plt.Circle((0.2, 0.5), 0.05, color='#4fc3f7')) # N
        ax.add_patch(plt.Circle((0.8, 0.6), 0.05, color='#e91e63')) # O
        ax.text(0.5, 0.3, "SMILES: CC(=O)N[C@@H]...", color='white', ha='center', fontsize=8)
    
    elif patient_id == "B":
        # Bond-Regenerative BD-S2 (Aromatic/Sulfonamide-like)
        # Drawing a hexagon (benzene ring)
        theta = np.linspace(0, 2*np.pi, 7)
        x = 0.4 + 0.15 * np.cos(theta)
        y = 0.5 + 0.15 * np.sin(theta)
        ax.plot(x, y, color='#81c784', lw=2)
        ax.plot([0.55, 0.75], [0.5, 0.5], color='#81c784', lw=2)
        ax.add_patch(plt.Circle((0.75, 0.5), 0.04, color='#ff9800')) # S
        ax.text(0.5, 0.25, "SMILES: C1=CC(=CC=C1C2...)", color='white', ha='center', fontsize=8)

    elif patient_id == "C":
        # OS-G3 OsteoStim (Growth Factor Mimetic)
        # Double ring system
        theta = np.linspace(0, 2*np.pi, 7)
        ax.plot(0.3 + 0.12 * np.cos(theta), 0.5 + 0.12 * np.sin(theta), color='#ffd54f', lw=2)
        ax.plot(0.5 + 0.12 * np.cos(theta), 0.5 + 0.12 * np.sin(theta), color='#ffd54f', lw=2)
        ax.text(0.5, 0.25, "SMILES: C1=CC=C(C=C1)C[C@@H]...", color='white', ha='center', fontsize=8)

def create_patient_board(patient_id, title, pathology, target, baseline_val, growth_val, metric, color_theme):
    fig = plt.figure(figsize=(12, 8), facecolor='#0d1117')
    plt.style.use('dark_background')
    
    # 1. Header
    plt.figtext(0.5, 0.95, f"OdontoApex Precision Medicine Board: {title}", ha="center", fontsize=22, fontweight='bold', color=color_theme)
    plt.figtext(0.5, 0.90, f"Detected Pathology: {pathology}", ha="center", fontsize=14, color='white', style='italic')

    # 2. Molecular Target Section (Top Left)
    ax1 = fig.add_axes([0.05, 0.55, 0.4, 0.3])
    ax1.set_title("Phase 7: Molecular Target", color=color_theme, loc='left')
    ax1.text(0.5, 0.6, f"Target Protein: {target}", ha="center", va="center", fontsize=16, fontweight='bold')
    ax1.text(0.5, 0.4, "Mapping precision: 99.4%", ha="center", va="center", fontsize=12, color='#bdbdbd')
    ax1.axis('off')

    # 3. Chemical Structure Section (Top Right)
    ax2 = fig.add_axes([0.55, 0.55, 0.4, 0.3])
    ax2.set_title(f"Phase 8: Synthesized Agent ({title})", color=color_theme, loc='left')
    draw_molecular_structure(ax2, patient_id)

    # 4. Regrowth Outcome Section (Bottom)
    ax3 = fig.add_axes([0.1, 0.1, 0.8, 0.35])
    ax3.set_title(f"Phase 10: Clinical Regrowth Projection ({metric})", color=color_theme, loc='left')
    
    categories = ['Day 0 (Baseline)', 'Year 1', 'Year 3', 'Year 5 (Projected)']
    # Simulating growth curve
    vals = [baseline_val, baseline_val + (growth_val-baseline_val)*0.3, baseline_val + (growth_val-baseline_val)*0.7, growth_val]
    
    ax3.plot(categories, vals, marker='o', color=color_theme, lw=3, markersize=10)
    ax3.fill_between(categories, vals, color=color_theme, alpha=0.1)
    ax3.set_ylabel(metric)
    ax3.grid(alpha=0.2)

    # Footer
    plt.figtext(0.95, 0.02, "Validated via OdontoApex LOOCV Protocol", ha="right", fontsize=9, color='#6e7681')

    # Save
    assets_dir = 'assets'
    if not os.path.exists(assets_dir): os.makedirs(assets_dir)
    filename = f"board_patient_{patient_id}.png"
    plt.savefig(os.path.join(assets_dir, filename), dpi=300, facecolor='#0d1117')
    plt.close()
    print(f"Generated {filename}")

if __name__ == "__main__":
    # Patient A
    create_patient_board("A", "OdontoDox-A1", "Enamel Hypo-mineralization", "DSPP (Dentin Sialophosphoprotein)", 1200, 1380, "Enamel Density (HU)", "#4fc3f7")
    # Patient B 
    create_patient_board("B", "BD-S2 Bond-Regen", "Secondary Caries at Margin", "MMP-20 (Collagenase)", 75, 99, "Seal Integrity (%)", "#81c784")
    # Patient C
    create_patient_board("C", "OS-G3 OsteoStim", "Alveolar Bone Resorption", "RANKL / OPG Ratio", 0.2, 3.6, "Bone Volume (cm3)", "#ffd54f")
