import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def generate_tooth_cloud(num_points=2000):
    """Generates a procedural 3D point cloud resembling a tooth."""
    theta = np.linspace(0, 2 * np.pi, num_points)
    z = np.linspace(-1, 1, num_points)
    
    # Simple crown shape (top)
    r_crown = 0.5 + 0.1 * np.cos(4 * theta)
    x = r_crown * np.cos(theta) * (z > 0)
    y = r_crown * np.sin(theta) * (z > 0)
    
    # Simple root shape (bottom)
    r_root = 0.3 * (1 - z) * (z <= 0)
    x += r_root * np.cos(theta) * (z <= 0)
    y += r_root * np.sin(theta) * (z <= 0)
    
    return x, y, z

def main():
    fig = plt.figure(figsize=(10, 8), facecolor='black')
    ax = fig.add_subplot(111, projection='3d', facecolor='black')
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
    ax.set_axis_off()

    x, y, z = generate_tooth_cloud()
    colors = np.array(['white'] * len(x), dtype=object)
    
    # Simulation Parameters
    num_frames = 200
    decay_start = 20
    regrow_start = 80
    
    # Scatter plot object
    scat = ax.scatter(x, y, z, c='white', s=5, alpha=0.6)
    
    # Title overlay
    title_text = ax.text2D(0.5, 0.95, "ODONTOAPEX: PHASE 11 - 3D TEMPORAL ENGINE", 
                           transform=ax.transAxes, color='cyan', fontsize=14, 
                           ha='center', fontweight='bold')
    phase_text = ax.text2D(0.5, 0.90, "INITIAL RADIOGRAPH", 
                            transform=ax.transAxes, color='white', fontsize=12, ha='center')

    def update(i):
        # Rotation
        ax.view_init(elev=20, azim=i*2)
        
        current_colors = np.array(['#FFFFFF'] * len(x), dtype=object)
        
        if i < decay_start:
            phase_text.set_text("PHASE 1-3: ANATOMICAL POSITIONING")
            phase_text.set_color('white')
        
        elif i < regrow_start:
            # Simulate Decay in the crown
            phase_text.set_text("PHASE 5-7: PATHOLOGICAL DECAY & MOLECULAR BREAK")
            phase_text.set_color('red')
            # Darken points in a "cavity" region
            decay_indices = np.where((y > 0.2) & (z > 0.3))[0]
            current_colors[decay_indices] = '#330000' # Deep dark red/brown
            
        else:
            # Simulate Regrowth (Phase 8-10)
            progress = (i - regrow_start) / (num_frames - regrow_start)
            phase_text.set_text(f"PHASE 8-10: BIOLOGICAL REGROWTH ({int(progress*100)}%)")
            phase_text.set_color('lime')
            
            decay_indices = np.where((y > 0.2) & (z > 0.3))[0]
            # Transition from dark back to glowing teal/white
            if progress > 0.5:
                current_colors[decay_indices] = '#00FFFF' # Healing Cyan
            else:
                current_colors[decay_indices] = '#552222'
                
        scat.set_offsets(np.vstack([x, y]).T) # Required for set_3d_properties
        scat.set_3d_properties(z, 'z')
        scat.set_color(current_colors)
        
        return scat, phase_text

    print("Launching Phase 11 3D Simulation...")
    ani = FuncAnimation(fig, update, frames=num_frames, interval=50, blit=False)
    plt.show()

if __name__ == "__main__":
    main()
