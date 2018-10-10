import dendropy

amphib = dendropy.DnaCharacterMatrix.get(
    path="../data/plethodon.phy",
    schema="phylip"
)

amphib.write_to_path("../data/plethodon.fa", schema="fasta")