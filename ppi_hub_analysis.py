# In Silico Identification of Druggable Hub Proteins in Mycobacterium tuberculosis

This project identifies hub proteins among eight drug-resistance genes of M. tuberculosis (rpoB, katG, inhA, gyrA, gyrB, embB, pncA, rpsL) using a protein-protein interaction (PPI) network and molecular docking.

## Methods
- PPI network: STRING database
- Network analysis: Cytoscape v3.10.4, cytoHubba (degree centrality)
- Docking: AutoDock Vina, SwissDock (PDB: 5UHC, chain C)

## Results
- The network had 8 nodes and 28 edges.
- RpoB emerged as the central hub.
- Docking of aspirin (test ligand) at the RpoB site gave a best pose of -5.133 kcal/mol.

## Files
- ppi_hub_analysis.py : Python code for PPI network and hub ranking
- results/ : network figure and docking outputs
- poster : project poster
