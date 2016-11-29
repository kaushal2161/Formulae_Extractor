# Formulae_Extractor
##Extract the formulae from Wikipedia articles with the title

To extract the formulae from all pages that contain math from enwiki you can do the following
```
git clone https://kaushal2161/Formulae_Extractor/
cd Formulae_Extractor
mkdir wout
wget https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
./formulae_extractor.py
```

All options of formula_extractor can be seen via
```
./formula_extractor --help
usage: formula_extractor.py [-h] [-f FILE] [-s SIZE] [-d DIR] [-t TAG]

extract wikipages that contain the math tag

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --filename FILE
                        the bz2-file to be split and filtered (default:
                        enwiki-latest-pages-articles.xml.bz2)
  -s SIZE, --splitsize SIZE
                        the number of pages contained in each split (default:
                        1000000)
  -d DIR, --outputdir DIR
                        the directory name where the files go (default: wout)
  -t TAG, --tagname TAG
                        the tag to search for (default: math)
  
```

