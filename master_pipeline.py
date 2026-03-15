import os
import subprocess
import sys

def run_phase(script_path, cwd):
    print(f"\n>>> Executing: {os.path.basename(script_path)}...")
    try:
        # We run as a subprocess to ensure the sys.path changes in each script take effect correctly
        result = subprocess.run([sys.executable, script_path], cwd=cwd, capture_output=False, text=True)
        if result.returncode == 0:
            print(f"--- {os.path.basename(script_path)} Completed Successfully ---")
        else:
            print(f"!!! Error in {os.path.basename(script_path)} (Exit Code: {result.returncode}) !!!")
    except Exception as e:
        print(f"Failed to execute {script_path}: {e}")

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("="*60)
    print("DENTAL AI RESEARCH PIPELINE: MASTER ORCHESTRATOR")
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
    
    for script_rel_path, phase_dir in phases:
        script_full_path = os.path.join(root_dir, script_rel_path)
        phase_full_path = os.path.join(root_dir, phase_dir)
        run_phase(script_full_path, phase_full_path)

    print("\n" + "="*60)
    print("ALL PHASES COMPLETE. PROJECT REPOSITORY IS READY.")
    print("="*60)

if __name__ == "__main__":
    main()
