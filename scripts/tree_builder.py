import dendropy
from dendropy.interop import raxml
pleth = dendropy.DnaCharacterMatrix.get(
    path="../data/full_plethodon_alignment.phy",
    schema="fasta"
)
rx = raxml.RaxmlRunner(raxml_path="/bin/raxmlHPC")
tree = rx.estimate_tree(
        char_matrix=pleth)
tree.write_to_path("../data_output/tree.phy", schema="newick")