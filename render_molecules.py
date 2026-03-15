
from rdkit import Chem
from rdkit.Chem import Draw
import os

def render_patient_molecules():
    # Define the 3 SMILES strings for the specific patients
    molecules = {
        "A": {
            "name": "OdontoDox-A1 (Patient A)",
            "smiles": "CC(=O)N[C@@H](CC1=CC=CC=C1)C(=O)NCC(=O)O",
            "desc": "Peptide-based Enamel Stimulant"
        },
        "B": {
            "name": "BD-S2 Bond-Regen (Patient B)",
            "smiles": "C1=CC(=CC=C1C2=CC=CC=N2)S(=O)(=O)N",
            "desc": "Sulfonamide-Aromatic Enzyme Inhibitor"
        },
        "C": {
            "name": "OS-G3 OsteoStim (Patient C)",
            "smiles": "C1=CC=C(C=C1)C[C@@H](C(=O)O)N",
            "desc": "Growth-Factor Bone Regenerator"
        }
    }

    # Output directory (Artifacts directory as specified in metadata)
    artifact_dir = r"C:\Users\umert\.gemini\antigravity\brain\20ff8c49-4070-4dae-9c04-f7315651f0c6"
    if not os.path.exists(artifact_dir):
        os.makedirs(artifact_dir)

    for pid, data in molecules.items():
        mol = Chem.MolFromSmiles(data["smiles"])
        if mol:
            # Generate image
            img_path = os.path.join(artifact_dir, f"molecule_patient_{pid}.png")
            Draw.MolToFile(mol, img_path, size=(500, 500), legend=data["name"])
            print(f"Successfully rendered: {img_path}")
        else:
            print(f"Error: Invalid SMILES for Patient {pid}")

if __name__ == "__main__":
    render_patient_molecules()
