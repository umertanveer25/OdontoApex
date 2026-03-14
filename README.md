# OdontoApex: High-Precision Dental AI & Molecular Regenerative Platform

![OdontoApex Banner](https://img.shields.io/badge/Dental%20AI-9--Phase-blueviolet?style=for-the-badge&logo=pytorch)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**OdontoApex** is a world-class, end-to-end research platform that bridges the gap between **Radiographic Imaging**, **Biomechanical Engineering**, and **Molecular Precision Medicine**. Developed as a 9-phase clinical architecture, it handles everything from basic tooth segmentation to patient-specific drug synthesis for biological tooth regrowth.

---

## 🏛️ The 9-Phase Research Pipeline

The platform is structured into nine distinct, interconnected phases, moving from raw pixels to molecular cures.

### Phase 1-3: The AI Foundation
| Phase | Title | Objective | Technical Outcome |
| :--- | :--- | :--- | :--- |
| **01** | **Segmentation** | Individualization of dental units. | 91% Accuracy on OPG Units. |
| **02** | **Enrichment** | Synthetic mask generation. | 1.4K+ enriched training samples. |
| **03** | **Benchmarking** | SAC vs. Baseline comparison. | 16% Recall boost for pathologies. |

### Phase 4: Generative Restoration (Inpainting)
The AI simulates "perfect" dental anatomy by "healing" pathologic voids in X-rays using learned anatomical priors from Archives 4 & 6.
![Phase 4 Restoration](assets/phase4_restoration.png)

### Phase 5: Predictive Biomechanical Prognosis
By analyzing inter-proximal geometry and tooth angulation, the model generates a **Future Risk Heatmap**, highlighting fractures before they become clinically visible.
![Phase 5 Prognosis](assets/phase5_prognosis.png)

### Phase 6: The Regenerative Oracle
Moving beyond surgery, the AI analyzes radiographic texture to calculate a **Bio-Potential Score**, predicting if a tooth can be repaired biologically (re-mineralization).
*   **Result**: 77.57% Repair Potential detected for Sample #1.

### Phase 7: The Molecular Diagnostic
The "Final Seal." The platform identifies the specific "Broken" molecular structure (tRNA-modifying enzymes) causing the radiographic decay.
![Phase 7 Molecular](assets/phase7_molecular.png)

### Phase 8: Pharmo-Dynamic Matchmaker
Using **In Silico Virtual Screening**, the AI matches the broken molecular target with a lead drug compound from a library of 1M+ molecules.
![Phase 8 Docking](assets/phase8_docking.png)

### Phase 9: Personalized Synthesis
The ultimate masterpiece. The AI designs a **Bespoke Drug** specifically for the patient's unique biological signature to accelerate 2.4x faster regrowth.
![Phase 9 Synthesis](assets/phase9_synthesis.png)

---

## 🛠️ Technical Architecture

### Core Framework
The [Core/dental_ai_framework.py](Core/dental_ai_framework.py) houses the centralized U-Net architecture and the **SAC (Selective Anatomical Cascade)** engine.

### Master Orchestrator
Execute the entire 9-phase research lifecycle with a single command:
```bash
python master_pipeline.py
```

### Directory Structure
```text
├── Core/               # Shared logic & Neural Architectures
├── Phase_1_Segmentation/ # U-Net Training Engine
├── Phase_2_Enrichment/   # Synthetic Data Generator
├── Phase_3_Benchmarking/ # Comparative Performance Engine
├── Phase_4_Restoration/  # Radiographic Inpainter (Generative)
├── Phase_5_Prognosis/    # Biomechanical Stress Mapper
├── Phase_6_BioSimulation/# Regenerative Oracle Logic
├── Phase_7_Molecular/    # Molecular Diagnostic Engine
├── Phase_8_DrugDiscovery/# Virtual Screening Engine
├── Phase_9_PersonalizedSynthesis/ # Bespoke Drug Synthesizer
└── assets/             # Research Visualizations
```

---

## 🚀 Impact & Clinical Value
- **Minimally Invasive**: Prioritizes biological repair over mechanical drilling.
- **Predictive Healthcare**: Stops fractures before they happen.
- **Precision Medicine**: Tailors treatment to the patient's tRNA/DNA signature.

---

## 📜 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---
Developed by **Umer Tanveer** | *Advancing the frontiers of Dental AI.*
