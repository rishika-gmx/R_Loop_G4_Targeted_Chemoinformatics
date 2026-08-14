
# Virtual Screening of G-Quadruplex Stabilizers to Explore R-Loop-Associated Genomic Instability

**Academic Track Focus:** Chemoinformatics · Epitranscriptomics · Non-Canonical DNA Mechanics · Cancer Systems Biology  
**Execution Environment:** Local WSL2 Ubuntu Architecture  
**Scope:** Undergraduate Computational Research / CADD Exercise

---

## 1. Biological Foundation

### What is an R-Loop?

During cellular transcription, **RNA Polymerase II** unwinds a region of double-stranded DNA (dsDNA) to synthesize a nascent RNA transcript. Under normal conditions, the newly synthesized RNA separates from the DNA template as transcription proceeds.

However, in certain genomic regions, particularly those containing **G-rich sequences**, the newly synthesized RNA can rehybridize with the complementary DNA template strand behind the transcription machinery.

This creates a stable **three-stranded nucleic-acid structure known as an R-loop**.

An R-loop consists of:

| Component | Description |
|---|---|
| **RNA:DNA Hybrid** | The newly synthesized RNA remains hybridized to the complementary DNA template strand. |
| **Displaced DNA Strand** | The non-template DNA strand is displaced from the duplex and remains single-stranded. |
| **R-Loop Structure** | Together, these components form a three-stranded nucleic-acid structure. |

The basic structure can be represented as:

```text
                  [Displaced G-Rich Single-Strand DNA]
                /--------------------------------------\
=== DNA (Top)                                           \=== DNA (Top)
=== DNA (Bottom) ======== RNA:DNA Hybrid ================= DNA (Bottom)
````

R-loops are not inherently pathological and can occur as part of normal cellular processes. However, **persistent or improperly resolved R-loops can interfere with DNA replication and transcription and contribute to genomic instability**.

---

### G-Quadruplex Formation within G-Rich Regions

The displaced DNA strand of an R-loop can contain **guanine-rich sequences**. These single-stranded G-rich regions have the ability to fold into a specialized non-canonical DNA structure known as a **G-quadruplex (G4)**.

A G-quadruplex is formed when four guanine bases associate into a planar structure called a **G-quartet**.

The guanines interact through **Hoogsteen hydrogen bonding**, while monovalent cations such as **K⁺** or **Na⁺** can coordinate within the central channel of the structure.

Multiple G-quartets can then stack on top of one another:

```text
              G-Quartet
        ┌─────────────────┐
        │ G       G       │
        │      K⁺         │
        │ G       G       │
        └─────────────────┘
                │
                ▼
              G-Quartet
        ┌─────────────────┐
        │ G       G       │
        │      K⁺         │
        │ G       G       │
        └─────────────────┘
                │
                ▼
              G-Quartet
```

The resulting G-quadruplex can be highly stable and can influence the structural environment of the DNA region in which it forms.

---

## 2. R-Loop / G-Quadruplex Intersection

The relationship between R-loops and G-quadruplexes provides the biological basis for this computational project.

When a G-quadruplex forms on the **displaced G-rich DNA strand**, it can alter the structural properties of the R-loop region.

This creates an important connection between:

**G-rich DNA → G-quadruplex formation → R-loop structure → transcription-associated genomic instability**

G4 structures have been studied in genomic regions associated with transcription, replication, and oncogene regulation.

The **c-MYC promoter** is one well-characterized example of a genomic region capable of forming a G-quadruplex.

---

## 3. Computational Rationale

The objective of this project is to explore whether small molecules with suitable structural characteristics could potentially interact with a G-quadruplex target.

The computational workflow therefore uses a basic **Computer-Aided Drug Design (CADD)** approach.

The workflow consists of:

```text
Small-Molecule Structures
          │
          ▼
     SDF Structures
          │
          ▼
   Ligand Preparation
          │
          ├── 3D Structure Generation
          ├── Geometry Preparation
          ├── Protonation / H Handling
          └── Partial Charge Assignment
          │
          ▼
     PDBQT Structures
          │
          ▼
   Potential Docking Input
```

The current repository focuses specifically on the **ligand-preparation stage** of this workflow.

---

## 4. Computational Working Model

The selected G-quadruplex structure provides a non-canonical nucleic-acid target for exploring structure-based molecular interactions.

Unlike conventional protein targets, G-quadruplexes contain **planar guanine tetrads, grooves, loops, and exposed aromatic surfaces** that can provide potential interaction sites for small molecules.

Potential ligand interactions can include:

| Interaction                    | Description                                                                 |
| ------------------------------ | --------------------------------------------------------------------------- |
| **π–π stacking**               | Aromatic ligand systems may interact with exposed nucleobase surfaces.      |
| **Hydrogen bonding**           | Functional groups on ligands may interact with nucleobases or loop regions. |
| **Electrostatic interactions** | Charged or polar groups can contribute to ligand–DNA interactions.          |
| **Groove interactions**        | Ligands may occupy grooves or loop-associated regions of the G4 structure.  |
| **Van der Waals interactions** | Close molecular contact can contribute to predicted binding affinity.       |

These interactions are the basis for computationally evaluating how small molecules may interact with non-canonical DNA structures.

> **Important:** Molecular docking or ligand preparation alone cannot demonstrate that a compound stabilizes a G-quadruplex, increases R-loop persistence, causes DNA damage, or produces anticancer effects. Those biological conclusions require experimental validation.

---

# 5. Structural Target

### Human *c-MYC* Promoter G-Quadruplex

The selected receptor is the **G-quadruplex structure formed within the human *c-MYC* promoter**.

| Parameter          | Value                                      |
| ------------------ | ------------------------------------------ |
| **Target**         | Human *c-MYC* promoter G-quadruplex        |
| **PDB ID**         | `1XAV`                                     |
| **Structure Type** | NMR                                        |
| **Target Class**   | Non-canonical DNA                          |
| **Application**    | Structure-based CADD / docking exploration |

The `1XAV` structure provides a structurally defined G-quadruplex target for investigating potential interactions with small molecules.

---

# 6. Selected Ligand Library

Three small molecules were selected for the initial computational workflow:

| Compound        | Chemical Class             | General Structural Feature                                        |
| --------------- | -------------------------- | ----------------------------------------------------------------- |
| **Resveratrol** | Stilbene polyphenol        | Aromatic conjugated scaffold with hydroxyl groups                 |
| **Curcumin**    | Diarylheptanoid polyphenol | Extended conjugated system with multiple oxygen-containing groups |
| **Quercetin**   | Flavonol                   | Polycyclic flavonoid scaffold with multiple hydroxyl groups       |

These compounds were selected as **representative small-molecule scaffolds** for exploring ligand preparation and potential interactions with G-quadruplex DNA.

The current library is intentionally small and serves as a **proof-of-concept computational exercise rather than a large-scale drug-screening campaign**.

---

# 7. Ligand Preparation Workflow

The main computational script in this repository is:

```text
g4_library_prep.py
```

The script uses **Python 3** to automate Open Babel command-line operations within a **WSL2 Ubuntu environment**.

The preparation workflow is:

```text
Raw SDF Structures
        │
        ▼
  Library Discovery
        │
        ▼
  3D Structure Generation
        │
        ▼
 Geometry Preparation
        │
        ▼
Protonation / H Handling
        │
        ▼
 Gasteiger Charges
        │
        ▼
   PDBQT Conversion
        │
        ▼
Prepared Ligand Library
```

---

## 7.1 Automated Library Discovery

Instead of manually specifying every compound in the Python script, the workflow automatically searches the input directory for `.sdf` files.

For example:

```text
raw_compounds/
├── resveratrol.sdf
├── curcumin.sdf
└── quercetin.sdf
```

Additional `.sdf` files can be added to the directory without modifying the main Python script.

---

## 7.2 3D Structure Generation

Open Babel is used to generate three-dimensional molecular coordinates from the input structures.

The workflow uses:

```text
--gen3d
```

to generate the initial 3D representation required for subsequent docking preparation.

---

## 7.3 Protonation and Hydrogen Handling

The preparation workflow applies protonation/hydrogen handling using a specified pH.

The current default is:

```text
pH = 7.0
```

Protonation state can influence molecular interactions, particularly for compounds containing ionizable functional groups.

---

## 7.4 Partial Charge Assignment

The workflow assigns **Gasteiger partial charges** to the prepared ligand structures.

These charges provide the electrostatic information required by AutoDock-compatible PDBQT structures.

---

## 7.5 PDBQT Conversion

The final structures are converted from SDF format into:

```text
.pdbqt
```

PDBQT structures contain information including:

* Atomic coordinates
* Partial charges
* AutoDock atom types
* Rotatable-bond information

These files can subsequently be used as ligand inputs for AutoDock-compatible molecular docking workflows.

---

# 8. Repository Structure

```text
R_Loop_G4_Targeted_Chemoinformatics/
│
├── README.md
├── g4_library_prep.py
│
├── raw_compounds/
│   ├── resveratrol.sdf
│   ├── curcumin.sdf
│   └── quercetin.sdf
│
└── prepared_ligands_pdbqt/
    ├── resveratrol.pdbqt
    ├── curcumin.pdbqt
    └── quercetin.pdbqt
```

---

# 9. Execution Environment

The workflow was designed for a local **WSL2 Ubuntu environment**.

### Software Used

| Software / Tool   | Purpose                                        |
| ----------------- | ---------------------------------------------- |
| **Python 3**      | Pipeline automation                            |
| **Open Babel**    | Molecular structure conversion and preparation |
| **WSL2 Ubuntu**   | Linux-based execution environment              |
| **AutoDock Vina** | Planned downstream docking environment         |

---

# 10. Running the Pipeline

## Requirements

Verify Python and Open Babel:

```bash
python3 --version
obabel -V
```

---

## Default Execution

From the repository directory:

```bash
python3 g4_library_prep.py
```

The script searches:

```text
raw_compounds/
```

and writes prepared ligand structures to:

```text
prepared_ligands_pdbqt/
```

---

# 11. AutoDock Vina Search Parameters

The project also documents an example docking search region selected for the `1XAV` G-quadruplex structure.

| Parameter          |      Value |
| ------------------ | ---------: |
| **Receptor**       |     `1XAV` |
| **Center X**       |  `14.85 Å` |
| **Center Y**       |   `2.30 Å` |
| **Center Z**       | `-11.40 Å` |
| **Size X**         |     `22 Å` |
| **Size Y**         |     `22 Å` |
| **Size Z**         |     `22 Å` |
| **Exhaustiveness** |       `32` |

The search region was selected to encompass the targeted G-quadruplex surface and surrounding structural features relevant to potential ligand interactions.

These parameters document the **planned CADD/docking configuration** associated with the project.

---

# 12. Current Output

The current ligand-preparation stage generates:

```text
prepared_ligands_pdbqt/
├── resveratrol.pdbqt
├── curcumin.pdbqt
└── quercetin.pdbqt
```

The resulting PDBQT structures represent the prepared ligand inputs for a potential AutoDock Vina docking workflow.

The repository does **not** currently claim experimentally validated binding affinities or biological activity for these compounds.

---

# 13. Scope and Limitations

This project is intentionally focused on **exploring a computational workflow for G-quadruplex-targeted ligand preparation**.

The workflow does not establish:

* Experimental G-quadruplex stabilization
* R-loop formation or persistence
* Transcription-replication conflicts
* DNA damage
* Cancer-cell selectivity
* Experimental binding affinity
* Anticancer activity

Computational docking, when used, provides **predicted molecular interactions and relative scoring estimates**, rather than experimental measurements.

Additional biochemical, biophysical, and cellular experiments would be required to establish the proposed biological mechanism.

---

## 14. Peer-Reviewed Academic Literature Sources / References

This pipeline design and structural code base are strictly guided by these primary peer-reviewed scientific citations:

1.  **The G4-R Loop Link:** *G-quadruplexes associated with R-loops promote CTCF binding* (Cell Press: Molecular Cell, 2023). This study proved that R-loops co-localize directly with G-quadruplex structures across oncogenic genomic tracks, changing localized chromatin architecture.
2.  **The CADD Screening Protocol:** *G-quadruplex Virtual Drug Screening: A Review* (Molecules / PMC, 2018). This methodology standard provides the exact mathematical guidelines used to center grid box structures and establish exhaustiveness parameters for non-canonical DNA docking campaigns.
3.  **The Structural Mapping Baseline:** *Major G-quadruplex structure formed in the human c-MYC promoter...* (Biochemistry, 2004). The foundational structural paper that originally resolved the 3D NMR coordinate landscape of the `1XAV` asset, validating its loop matrices as elite targets for drug design.
---

## 15. How to Cite or Reference
Pandey, R. (2026). *Virtual Screening of G-Quadruplex Stabilizers to Explore R-Loop-Associated Genomic Instability.*

