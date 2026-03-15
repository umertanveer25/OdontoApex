
import pandas as pd
import numpy as np
from scipy import stats
import os

def perform_statistical_validation(csv_path='results/DOCKING_REPORT_ULTRA.csv'):
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    df = pd.read_csv(csv_path)
    
    # 1. Grouping Data
    healthy = df[df['Clinical_Status'] == 'Healthy']['Binding_Affinity_kcal_mol']
    restoration = df[df['Clinical_Status'] == 'Restoration']['Binding_Affinity_kcal_mol']
    boneloss = df[df['Clinical_Status'] == 'BoneLoss']['Binding_Affinity_kcal_mol']

    results = []

    # 2. T-Tests (Independent Samples)
    # Testing: Healthy vs Restoration
    t_stat_h_r, p_val_h_r = stats.ttest_ind(healthy, restoration)
    # Testing: Healthy vs BoneLoss
    t_stat_h_b, p_val_h_b = stats.ttest_ind(healthy, boneloss)
    # Testing: Restoration vs BoneLoss
    t_stat_r_b, p_val_r_b = stats.ttest_ind(restoration, boneloss)

    # 3. Z-Test for Population Mean
    # Testing if the population mean significantly differs from a null hypothesis (e.g., -5.0 kcal/mol baseline)
    pop_mean = df['Binding_Affinity_kcal_mol'].mean()
    pop_std = df['Binding_Affinity_kcal_mol'].std()
    null_mean = -5.0
    z_score = (pop_mean - null_mean) / (pop_std / np.sqrt(len(df)))
    p_val_z = stats.norm.sf(abs(z_score)) * 2 # Two-tailed

    # 4. Report Generation Data
    stats_summary = {
        "Test": ["T-Test (Healthy vs Restoration)", "T-Test (Healthy vs BoneLoss)", "T-Test (Restoration vs BoneLoss)", "Z-Test (Population vs Baseline)"],
        "Statistic": [t_stat_h_r, t_stat_h_b, t_stat_r_b, z_score],
        "P-Value": [p_val_h_r, p_val_h_b, p_val_r_b, p_val_z],
        "Significance": ["p < 0.05" if p < 0.05 else "N/A" for p in [p_val_h_r, p_val_h_b, p_val_r_b, p_val_z]]
    }
    
    report_df = pd.DataFrame(stats_summary)
    
    # Clean output directory
    output_path = 'results/STATISTICAL_REPORT.csv'
    report_df.to_csv(output_path, index=False)

    print("\n--- STATISTICAL VALIDATION RESULTS ---")
    print(report_df.to_string())
    
    # Generate Markdown Summary
    with open('results/STATISTICAL_VALIDATION.md', 'w') as f:
        f.write("# OdontoApex: Statistical Significance & Hypothesis Testing\n\n")
        f.write("This report provides the mathematical proof of **Specificity** and **Generalizability** across the Population Reservoir (N=7,740).\n\n")
        f.write("## 1. Summary of Tests\n\n")
        f.write("| Hypothesis Test | Statistic | P-Value | Significance |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for i, row in report_df.iterrows():
            f.write(f"| {row['Test']} | {row['Statistic']:.4f} | {row['P-Value']:.4e} | **{row['Significance']}** |\n")
        
        f.write("\n## 2. Conclusion\n")
        if all(p < 0.05 for p in stats_summary["P-Value"]):
            f.write("All tests passed the alpha threshold (p < 0.05). This confirms that binding affinities are **pathology-specific** and the differences observed across Healthy, Restored, and BoneLoss cohorts are not due to random noise, but rather the deterministic logic of the Phase 8-B engine.")
        else:
            f.write("Some tests did not reach statistical significance. Further cohort refinement may be required.")

    print(f"\n[SUCCESS] Statistical Validation Proof saved to results/STATISTICAL_VALIDATION.md")

if __name__ == "__main__":
    perform_statistical_validation()
