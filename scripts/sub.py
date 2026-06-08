from rdkit import Chem
from rdkit.Chem import rdFMCS

# Create two example molecules
mol1 = Chem.MolFromSmiles('C=CC=C')
mol2 = Chem.MolFromSmiles('CC(=CCCC(=C)C=C)C')

# Find the maximum common substructure
mcs = rdFMCS.FindMCS([mol1, mol2])

# Convert the MCS query to a molecule
mcs_mol = Chem.MolFromSmarts(mcs.smartsString)

# Get the substructure matches
matches_mol1 = mol1.GetSubstructMatches(mcs_mol)
matches_mol2 = mol2.GetSubstructMatches(mcs_mol)

# Print the matches
print(f"Substructure matches in mol1: {matches_mol1}")
print(f"Substructure matches in mol2: {matches_mol2}")
