import dendropy
import sys


amphib = dendropy.DnaCharacterMatrix.get(
    path=sys.argv[1],
    schema=sys.argv[2]
)

amphib.write_to_path(sys.argv[3], schema=sys.argv[4])