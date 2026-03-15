import os
import subprocess
import sys
import json
import argparse

def write_split_state(train_imgs, test_imgs, root_dir):
    state_file = os.path.join(root_dir, "Core", "split_state.json")
    state = {
        "train_images": train_imgs,
        "test_images": test_imgs
    }
    with open(state_file, "w") as f:
        json.dump(state, f, indent=4)

def run_phase(script_path, cwd):
    print(f"\n>>> Executing: {os.path.basename(script_path)}...")
    try:
        result = subprocess.run([sys.executable, script_path], cwd=cwd, capture_output=False, text=True)
        if result.returncode == 0:
            print(f"--- {os.path.basename(script_path)} Completed Successfully ---")
        else:
            print(f"!!! Error in {os.path.basename(script_path)} (Exit Code: {result.returncode}) !!!")
    except Exception as e:
        print(f"Failed to execute {script_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="OdontoApex LOOCV Orchestrator")
    parser.add_argument("--max_folds", type=int, default=5, help="Maximum number of LOOCV folds to run. Set to 0 to run all datums.")
    args = parser.parse_args()

    root_dir = os.path.dirname(os.path.abspath(__file__))
    img_dir = os.path.join(root_dir, "images")
    
    # Discover all images
    all_images = [f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    all_images = sorted(all_images) # ensure determinism
    
    num_folds = min(args.max_folds, len(all_images)) if args.max_folds > 0 else len(all_images)
    
    print("="*60)
    print("ODONTOAPEX: LEAVE-ONE-OUT CROSS-VALIDATION (LOOCV)")
    print(f"Total Datums: {len(all_images)} | Running Folds: {num_folds}")
    print("="*60)
    
    phases = [
        ("Phase_0_GenerativeAugment/bidirectional_translator.py", "Phase_0_GenerativeAugment"),
        ("Phase_1_Segmentation/phase1_training.py", "Phase_1_Segmentation"),
        ("Phase_2_Enrichment/phase2_inference.py", "Phase_2_Enrichment"),
        ("Phase_3_Benchmarking/phase3_benchmark.py", "Phase_3_Benchmarking"),
        ("Phase_4_Restoration/anatomical_inpainter.py", "Phase_4_Restoration"),
        ("Phase_5_Prognosis/prognosis_engine.py", "Phase_5_Prognosis"),
        ("Phase_6_BioSimulation/enzyme_repair_simulator.py", "Phase_6_BioSimulation"),
        ("Phase_7_Molecular/molecular_diagnostic.py", "Phase_7_Molecular"),
        ("Phase_8_DrugDiscovery/drug_discovery_engine.py", "Phase_8_DrugDiscovery"),
        ("Phase_9_PersonalizedSynthesis/custom_drug_synthesizer.py", "Phase_9_PersonalizedSynthesis"),
        ("Phase_10_Outcome/outcome_simulator.py", "Phase_10_Outcome")
    ]
    
    for fold in range(num_folds):
        test_img = all_images[fold]
        train_imgs = [img for img in all_images if img != test_img]
        
        print("\n" + "*"*60)
        print(f"FOLD {fold + 1}/{num_folds} - TEST IMAGE: {test_img}")
        print("*"*60)
        
        write_split_state(train_imgs, [test_img], root_dir)
        
        for script_rel_path, phase_dir in phases:
            script_full_path = os.path.join(root_dir, script_rel_path)
            phase_full_path = os.path.join(root_dir, phase_dir)
            run_phase(script_full_path, phase_full_path)
            
    # Cleanup state
    state_file = os.path.join(root_dir, "Core", "split_state.json")
    if os.path.exists(state_file):
        os.remove(state_file)

    print("\n" + "="*60)
    print("ALL LOOCV FOLDS COMPLETE.")
    print("="*60)

if __name__ == "__main__":
    main()
