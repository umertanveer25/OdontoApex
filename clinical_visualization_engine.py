
import matplotlib.pyplot as plt
import numpy as np
import os

def create_clinical_plots():
    # Setup directory
    assets_dir = 'assets'
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)

    # Data for the 3 Patients
    patients = ['Patient A\n(Enamel)', 'Patient B\n(Restoration)', 'Patient C\n(Bone)']
    regrowth_improvement = [15, 32, 1720] # % improvement from baseline
    binding_affinities = [-8.2, -9.1, -10.4] # kcal/mol (Lower is better)

    # --- Plot 1: Regrowth Success (Log Scale for Patient C's huge recovery) ---
    plt.figure(figsize=(10, 6))
    plt.style.use('dark_background')
    
    colors = ['#4fc3f7', '#81c784', '#ffd54f'] # Blue, Green, Yellow
    bars = plt.bar(patients, regrowth_improvement, color=colors, alpha=0.8)
    
    plt.yscale('log') # Log scale because bone regrowth is a huge volume change
    plt.title('Clinical Odyssey: Regrowth Outcome Projections (5-Year)', fontsize=14, color='white', pad=20)
    plt.ylabel('Improvement over Baseline (%)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    
    # Adding value labels
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'+{int(yval)}%', 
                 va='bottom', ha='center', color='white', fontsize=10, fontweight='bold')

    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, 'validation_regrowth_chart.png'), dpi=300)
    plt.close()

    # --- Plot 2: Molecular Docking Affinities ---
    plt.figure(figsize=(10, 6))
    plt.style.use('dark_background')
    
    # Reversing for a "lower is better" visual
    plt.bar(patients, binding_affinities, color=['#0288d1', '#388e3c', '#fbc02d'], alpha=0.7)
    
    plt.axhline(0, color='white', linewidth=0.8)
    plt.title('Phase 8: Molecular Docking Binding Affinities', fontsize=14, color='white', pad=20)
    plt.ylabel('Binding Affinity (kcal/mol)', fontsize=12)
    plt.gca().invert_yaxis() # Invert because negative values are more stable
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    
    # Legend description
    plt.figtext(0.5, 0.01, "*Lower kcal/mol indicates stronger, more stable molecular bonding.", 
                ha="center", fontsize=9, color="#bdbdbd", style='italic')

    plt.tight_layout()
    plt.savefig(os.path.join(assets_dir, 'validation_molecular_docking.png'), dpi=300)
    plt.close()

    print(f"Success: Generated validation charts in {assets_dir}/")

if __name__ == "__main__":
    create_clinical_plots()
