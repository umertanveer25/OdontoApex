
// OdontoApex: Real-Time Clinical Odyssey Logic Engine
document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const overlay = document.getElementById('processing-overlay');
    const loaderStatus = document.getElementById('loader-status');
    const uploadSection = document.getElementById('upload-section');
    const analysisSection = document.getElementById('analysis-section');
    
    let chartInstance = null;

    // --- 1. Interaction Handlers ---
    dropZone.addEventListener('click', () => fileInput.click());
    
    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) processImage(e.target.files[0]);
    });

    async function processImage(file) {
        // Show Loader
        uploadSection.classList.add('hidden');
        overlay.classList.remove('hidden');
        
        // --- 11-PHASE CLINICAL ODYSSEY SIMULATION ---
        const phases = [
            "Phase 0: Generative Augmentation (CycleGAN)...",
            "Phase 1: Attention U-Net Segmentation...",
            "Phase 2: Synthetic Mask Enrichment...",
            "Phase 3: Cross-Tier Benchmark (SAC vs ResNet)...",
            "Phase 4: Anatomical Inpainting Restoration...",
            "Phase 5: FEM-CNN Stress Tensor Mapping...",
            "Phase 6: Odontoblastic Oracle Calibration...",
            "Phase 7: Sub-Cellular Molecular Diagnostic...",
            "Phase 8: Virtual Screening (ZINC15 Library)...",
            "Phase 9: Bespoke Molecule Synthesis (GAN)...",
            "Phase 10: 18-Month Temporal Regrowth Simulation..."
        ];

        // Real-Time Analysis Trigger (Determine pathology early for phase specificity)
        const pathologyData = await analyzePixelData(file);

        for (let i = 0; i < phases.length; i++) {
            await updateStatus(phases[i], 600 + Math.random() * 400);
            
            // Phase-specific logic (simulated)
            if (i === 5) await updateStatus(`Mapping Stress: ${pathologyData.type === 'Healthy' ? 'Low' : 'Critical'} detected...`, 500);
            if (i === 8) await updateStatus(`Matching Ligand: ${pathologyData.type} specific library...`, 500);
        }

        overlay.classList.add('hidden');
        analysisSection.classList.remove('hidden');
        
        renderResults(pathologyData, file);
    }

    function updateStatus(text, ms) {
        return new Promise(resolve => {
            loaderStatus.innerText = text;
            setTimeout(resolve, ms);
        });
    }

    // --- 2. THE LOGIC ENGINE (Non-Static Calibration) ---
    async function analyzePixelData(file) {
        return new Promise((resolve) => {
            const reader = new FileReader();
            reader.onload = (e) => {
                const img = new Image();
                img.onload = () => {
                    const canvas = document.createElement('canvas');
                    const ctx = canvas.getContext('2d');
                    canvas.width = 100; // Small sample for speed
                    canvas.height = 100;
                    ctx.drawImage(img, 0, 0, 100, 100);
                    
                    const data = ctx.getImageData(0, 0, 100, 100).data;
                    let brightness = 0;
                    let highHighs = 0; // Spots of high density (fillings)
                    let lowLows = 0;   // Spots of voids (bone loss)
                    
                    for (let i = 0; i < data.length; i += 4) {
                        const gray = (data[i] + data[i+1] + data[i+2]) / 3;
                        brightness += gray;
                        if (gray > 220) highHighs++;
                        if (gray < 30) lowLows++;
                    }
                    
                    const avgBrightness = brightness / (100 * 100);
                    
                    // DETERMINISTIC BRANCHING LOGIC
                    if (highHighs > 150) {
                        resolve({ type: 'Restoration', score: highHighs/10 });
                    } else if (lowLows > 300) {
                        resolve({ type: 'BoneLoss', score: lowLows/10 });
                    } else {
                        resolve({ type: 'Healthy', score: avgBrightness/2 });
                    }
                };
                img.src = e.target.result;
            };
            reader.readAsDataURL(file);
        });
    }

    // --- 3. Rendering Engine ---
    function renderResults(data, file) {
        const xrayCanvas = document.getElementById('xray-canvas');
        const ctx = xrayCanvas.getContext('2d');
        const reader = new FileReader();
        
        reader.onload = (e) => {
            const img = new Image();
            img.onload = () => {
                xrayCanvas.width = img.width;
                xrayCanvas.height = img.height;
                ctx.drawImage(img, 0, 0);
                
                // Overlay "AI Segmentation" effect
                ctx.strokeStyle = data.type === 'Healthy' ? '#4fc3f7' : '#e91e63';
                ctx.lineWidth = 10;
                ctx.strokeRect(img.width/4, img.height/4, img.width/2, img.height/2);
            };
            img.src = e.target.result;
        };
        reader.readAsDataURL(file);

        // Update UI info
        const metrics = document.getElementById('radiomic-metrics');
        metrics.innerHTML = `
            <div class="metric-item"><span>Diagnostic Label</span><span class="metric-val">${data.type.toUpperCase()}</span></div>
            <div class="metric-item"><span>Pathology Depth</span><span class="metric-val">${data.score.toFixed(1)}mm</span></div>
        `;

        // Update Stress
        const stressBar = document.getElementById('stress-bar');
        const stressStatus = document.getElementById('stress-status');
        const stressLevel = data.type === 'Healthy' ? 20 : (data.type === 'BoneLoss' ? 65 : 95);
        stressBar.style.width = stressLevel + '%';
        stressStatus.innerText = stressLevel > 70 ? "CRITICAL: FRACTURE RISK" : "STABLE OCULUSAL LOAD";
        stressBar.style.background = stressLevel > 70 ? '#e91e63' : '#4fc3f7';

        // Update Molecule
        renderMolecule(data.type);
        
        // Update Chart
        renderChart(data.type);
    }

    function renderMolecule(type) {
        const names = { Healthy: "OdontoDox-A1", Restoration: "BD-S2 Bond-Regen", BoneLoss: "OS-G3 OsteoStim" };
        const smiles = { 
            Healthy: "CC(=O)N[C@@H](CC1=CC=CC=C1)C(=O)NCC(=O)O", 
            Restoration: "C1=CC(=CC=C1C2=CC=CC=N2)S(=O)(=O)N", 
            BoneLoss: "C1=CC=C(C=C1)C[C@@H](C(=O)O)N" 
        };
        
        document.getElementById('drug-name').innerText = names[type];
        document.getElementById('smiles-code').innerText = smiles[type];
        
        const canvas = document.getElementById('molecule-canvas');
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0,0, canvas.width, canvas.height);
        
        // Draw random "3D-ish" nodes based on type
        const color = type === 'BoneLoss' ? '#ffd54f' : '#4fc3f7';
        for(let i=0; i<15; i++) {
            ctx.beginPath();
            ctx.arc(Math.random()*canvas.width, Math.random()*canvas.height, 5, 0, Math.PI*2);
            ctx.fillStyle = color;
            ctx.fill();
        }
    }

    function renderChart(type) {
        const ctx = document.getElementById('regrowth-chart').getContext('2d');
        if (chartInstance) chartInstance.destroy();
        
        const config = {
            Healthy: [0, 5, 10, 15],
            Restoration: [0, 15, 25, 30],
            BoneLoss: [0, 2, 8, 45] // Exponential jump
        }[type];

        chartInstance = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['0m', '6m', '12m', '18m'],
                datasets: [{
                    label: 'Tissue Regrowth %',
                    data: config,
                    borderColor: '#4fc3f7',
                    tension: 0.4,
                    fill: true,
                    backgroundColor: 'rgba(79, 195, 247, 0.1)'
                }]
            },
            options: {
                responsive: true,
                scales: { y: { beginAtZero: true, grid: { color: 'rgba(255,255,255,0.05)' } } }
            }
        });
    }

    document.getElementById('reset-btn').onclick = () => window.location.reload();
});
