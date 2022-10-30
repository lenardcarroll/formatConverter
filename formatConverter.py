from openbabel import pybel
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-inp1", "--input1", dest = "input1", default = "xyz", help="Name of the input file's format (for allowed formats see http://openbabel.org/docs/2.3.0/FileFormats/Overview.html)")
parser.add_argument("-inp2", "--input2", dest = "input2", default = "Structure.xyz", help="Name of the input file with extension included (e.g. Structure.xyz)")
parser.add_argument("-out1", "--output1", dest = "output1", default = "pdb", help="Name of the output file's format (for allowed formats see http://openbabel.org/docs/2.3.0/FileFormats/Overview.html)")
parser.add_argument("-out2", "--output2", dest = "output2", default = "Structure.pdb", help="Name of the output file with extension included (e.g. Structure.xyz)")
print("Tip: Make sure that your files are single-framed")
args = parser.parse_args()

molecule = next(pybel.readfile(args.input1,args.input2)) #Read in file
molecule.write(args.output1,args.output2,overwrite=True) #Output file
print("Conversion complete!")
