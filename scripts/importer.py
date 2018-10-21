import dendropy
import sys 

def get_file(read_file, schema, write_file):
    amphib = dendropy.DnaCharacterMatrix.get(
        read_file = sys.argv[1],
        schema= sys.argv[2], 
    )

amphib.write_to_path(sys.argv[3], schema="fasta")

return 

#get_file("../data/" plethodon.phy", "phylip")
