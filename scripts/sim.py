from rdkit import Chem
from rdkit import DataStructs

# Create two example fingerprints (Morgan fingerprints)
mol1 = Chem.MolFromSmiles('CC1C=CC=CCCC=CC=CC=CC=CC(CC2C(C(CC(O2)(CC(C(CCC(CC(CC(CC(=O)OC(C(C1O)C)C)O)O)O)O)O)O)O)C(=O)O)OC3C(C(C(C(O3)C)O)N)O')
mol2 = Chem.MolFromSmiles('CC(=CCCC(=C)C=C)C')

fp1 = Chem.RDKFingerprint(mol1)
fp2 = Chem.RDKFingerprint(mol2)

# Calculate Tanimoto similarity
similarity = DataStructs.TanimotoSimilarity(fp1, fp2)
print(f"Tanimoto similarity: {similarity}")
