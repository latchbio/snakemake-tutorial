import sys
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pysam import VariantFile

quals = [record.qual for record in VariantFile(sys.argv[1])]
plt.hist(quals)

plt.savefig(sys.argv[2])

