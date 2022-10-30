# formatConverter

This script converts typical MD/QM file formats from one format to another using Openbabel. To use the script make sure that you have installed conda, check here for example https://docs.conda.io/en/latest/miniconda.html

Next, make sure that you run the following:

```
conda install -c conda-forge openbabel
pip install argparse
```

To use the script, here is the help guideline:

```
Tip: Make sure that your files are single-framed
usage: formatConversion.py [-h] [-inp1 INPUT1] [-inp2 INPUT2] [-out1 OUTPUT1]
                           [-out2 OUTPUT2]

optional arguments:
  -h, --help            show this help message and exit
  -inp1 INPUT1, --input1 INPUT1
                        Name of the input file's format (for allowed formats
                        see http://openbabel.org/docs/2.3.0/FileFormats/Overvi
                        ew.html)
  -inp2 INPUT2, --input2 INPUT2
                        Name of the input file with extension included (e.g.
                        Structure.xyz)
  -out1 OUTPUT1, --output1 OUTPUT1
                        Name of the output file's format (for allowed formats
                        see http://openbabel.org/docs/2.3.0/FileFormats/Overvi
                        ew.html)
  -out2 OUTPUT2, --output2 OUTPUT2
                        Name of the output file with extension included (e.g.
                        Structure.xyz)
 ```
 
 For example use:
 ```
 python -i formatConversion.py -inp1 xyz -inp2 Structure.xyz -out1 pdb -out2 Structure.pdb
 ```
