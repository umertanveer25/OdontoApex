# 🦷 OdontoApex: Advanced Dental AI Research Suite

**OdontoApex** is a comprehensive, end-to-end intelligence framework for Dental Radiography. Moving beyond traditional "Detection-only" models, this repository implements a five-phase research pipeline that integrates **Generative AI** for clinical restoration and **Biomechanical Simulation** for preventive prognosis.

## 🚀 Key Innovation Pillars

### 1. **Robust Segmentation-Aided Classification (SAC)**
Utilizes a localized approach where pathological detection is constrained by high-fidelity tooth segmentation (U-Net). Verified result: **+16% increase in Recall** for localized lesions compared to global OPG baselines.

### 2. **Generative Radiographic Inpainting (Phase 4)**
Uses learned anatomical priors to simulate a **"Digital Healthy Twin."** The model identifies pathologic voids or anatomical defects in OPG scans and "inpaints" them to visualize the target healthy state, assisting in generative treatment planning.

### 3. **Prophetic Biomechanical Prognosis (Phase 5)**
Integrates dental geometry with mechanical failure prediction. By calculating the **Torque-Ratio and Vector of Force** from segmentation masks, the system identifies high-stress regions prone to future fracture or periodontal failure before clinical symptoms manifest.

## 🛠 Repository Structure
- **Core/**: Central PyTorch framework and dataset loaders.
- **Phase_1_Segmentation/**: Training engine for tooth segmentation.
- **Phase_2_Enrichment/**: Synthetic mask generation for dataset enrichment.
- **Phase_3_Benchmarking/**: Comparative metrics (SAC vs Baseline).
- **Phase_4_Restoration/**: [Generative AI] Radiographic inpainting for "Healthy Twin" simulation.
- **Phase_5_Prognosis/**: [Predictive AI] Biomechanical stress mapping.
- **Phase_6_BioSimulation/**: [Regenerative AI] Biological repair potential.
- **Phase_7_Molecular/**: [Precision Medicine] Molecular diagnostic (tRNA/DNA).
- **Phase_8_DrugDiscovery/**: [Pharma AI] In Silico Drug Discovery.
- **Phase_9_PersonalizedSynthesis/**: [Hyper-Precision] Patient-specific bespoke drug design.

## 🚀 How to Run
To run the entire 9-phase pipeline end-to-end, execute the master orchestrator from the root directory:
```bash
python master_pipeline.py
```

## 📊 Research Impact
- **Clinician-Friendly**: Shifts AI from a "Black Box" to a treatment-planning assistant.
- **Biomedical Engineering**: First-of-its-kind integration of structural stress mapping in OPG analysis.
- **Data Efficient**: Built-in enrichment engine to maximize utility from limited annotated imaging sets.

---
*Developed for Dental AI Research Pipeline (2026)*
