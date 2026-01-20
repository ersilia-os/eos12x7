# imports
import os
import sys
import numpy as np
from rdkit import Chem
from rdkit.Chem.SpacialScore import SPS
from ersilia_pack_utils.core import read_smiles, write_out

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# my model
def my_model(smiles_list):
    results = []
    for smi in smiles_list:
        if Chem.MolFromSmiles(smi) is None:
            results.append([None, None])
        else:
            sps_score = SPS(Chem.MolFromSmiles(smi), normalize=False)
            nsps_score = SPS(Chem.MolFromSmiles(smi), normalize=True)
            results.append([sps_score, nsps_score])
    return results

# read input
_, smiles_list = read_smiles(input_file)

# run model
outputs = my_model(smiles_list)

# check input and output have the same length
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

header = ["sps_score", "nsps_score"]

# write output in a .csv file
write_out(outputs, header, output_file, np.float32)
