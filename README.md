# In Silico Identification of Druggable Hub Proteins in Mycobacterium tuberculosis Drug Resistance Pathways via Protein-Protein Interaction Network and Molecular Docking Analysis

**Author:** Salmoli Kangsabanik
**Affiliation:** Department of Biotechnology, University of Engineering and Management, Kolkata

## 1. Introduction
- Tuberculosis (TB), caused by Mycobacterium tuberculosis, caused about 1.23 million deaths and an estimated 10.7 million new cases worldwide in 2024, and remains the leading cause of death from a single infectious agent (WHO, 2025).
- India accounts for about 32% of the global MDR/rifampicin-resistant TB burden (WHO, 2025).
- Multi-drug-resistant (MDR) and extensively drug-resistant (XDR) strains are a major challenge to global TB control.
- Resistance to first-line drugs mainly arises from mutations in rpoB, katG, inhA, gyrA, gyrB, embB, pncA and rpsL, which alter drug targets or drug-activating enzymes.
- These proteins do not act in isolation, so a network-level view can reveal key therapeutic targets.

## Objective
- To construct a protein-protein interaction (PPI) network of eight resistance-associated genes (rpoB, katG, inhA, gyrA, gyrB, embB, pncA and rpsL) using the STRING database.
- To analyse the topology of the network using Cytoscape v3.10.4.
- To identify and rank hub proteins by degree centrality using the cytoHubba plugin.
- To assess whether the top-ranked hub, RpoB, the established rifampicin target, is biologically consistent with a central position in the network.
- To retrieve the RpoB β-subunit structure (PDB ID: 5UHC, chain C) and perform preliminary molecular docking using AutoDock Vina via SwissDock.
- To provide a rational basis for future virtual screening of FDA-approved drugs as repurposing candidates against drug-resistant tuberculosis.

## 3. Methodology
- Eight resistance genes (rpoB, katG, inhA, gyrA, gyrB, embB, pncA, rpsL) were selected.
- The PPI network was built using the STRING database.
- The network was analysed in Cytoscape v3.10.4.
- Hub proteins were ranked by degree centrality using cytoHubba.
- The RpoB structure (PDB ID: 5UHC, chain C) was retrieved from RCSB PDB.
- Preliminary docking was performed using AutoDock Vina via SwissDock.

## 4. Result
- **PPI network:** The network had 8 nodes and 28 edges, with a PPI enrichment p-value of 3.33 × 10^-16.
- **Hub proteins:** The top five hubs by degree centrality were RpoB, GyrB, EmbB, RpsL and PncA. RpoB emerged as the central node.
- **Molecular docking (preliminary):** RpoB (PDB: 5UHC, chain C) was docked with aspirin as a test ligand (exhaustiveness = 1). The best binding affinity was -5.13 kcal/mol, and the top three poses were -5.13, -4.79 and -4.65 kcal/mol.
- The network was fully connected: all 28 of the 28 possible edges among the 8 proteins were present, so each protein interacted with all 7 others (degree = 7). cytoHubba ranked RpoB, GyrB, EmbB, RpsL and PncA as the top five hubs, with RpoB as the central node.

### Network stats
| Metric | Value |
|---|---|
| Number of nodes | 8 |
| Number of edges | 28 |
| Average node degree | 7 |
| Avg. local clustering coefficient | 1 |
| Expected number of edges | 4 |
| PPI enrichment p-value | 3.33e-16 |

### Docking affinities (aspirin at RpoB site, SwissDock)
| Model | Calculated affinity (kcal/mol) |
|---|---|
| 1 | -5.133 |
| 2 | -4.794 |
| 3 | -4.653 |
| 4 | -4.421 |
| 5 | -3.711 |
| 6 | -3.473 |
| 7 | -3.297 |
| 8 | -2.691 |
| 9 | -2.688 |
| 10 | -2.586 |

## 5. Discussion
- A hub protein is connected to many other proteins, so targeting it may affect the network more broadly.
- RpoB, the established target of rifampicin, emerged as the central node, supporting the biological validity of this network-based prioritization.
- In preliminary docking, the RpoB pocket accommodated a test ligand (aspirin) with a best affinity of -5.13 kcal/mol, suggesting a structurally accessible site.
- Limitations: only a test ligand was used, exhaustiveness was low (1), and there is no experimental validation yet.

## 7. Conclusion
- Network analysis identified RpoB as a central, highly connected hub among TB drug-resistance proteins.
- RpoB's prominent network position aligns with its known clinical role as the rifampicin target, validating this network-based approach.
- Docking at the RpoB rifampicin-binding pocket confirmed it is structurally accessible and druggable (binding affinity ≈ -5.1 kcal/mol).
- This validated pipeline provides a foundation for future large-scale virtual screening of FDA-approved drugs for TB repurposing.

## Significance and Applications
- Helps prioritize drug targets in MDR/XDR TB before experimental work.
- Supports drug repurposing with FDA-approved compounds.
- Gives a network-level view of interacting resistance genes.
- Narrows many compounds to a few candidates for laboratory testing.

## 8. References
- World Health Organization (2025). Global Tuberculosis Report 2025. Geneva: WHO.
- Szklarczyk, D., et al. (2023). The STRING database in 2023. Nucleic Acids Res., 51(D1), D638-D646.
- Bugnon, M., et al. (2024). SwissDock 2024: major enhancements for small-molecule docking with Attracting Cavities and AutoDock Vina. Nucleic Acids Res.
- Eberhardt, J., et al. (2021). AutoDock Vina 1.2.0: new docking methods, expanded force field, and Python bindings. J. Chem. Inf. Model., 61(8), 3891-3898.

## Files
- `ppi_hub_analysis.py` : Python code for PPI network and hub ranking
- `results/` : network figure and docking outputs
- poster image : project poster
- ![Poster](poster.png)

