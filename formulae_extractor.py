#!/usr/bin/python
import os
import bz2
import argparse
import re
import gzip


def split_xml( filename, splitsize, dir, tag):

    # Check and create chunk diretory
    if not os.path.exists( dir ):
        os.mkdir( dir )
    # Counters
    pagecount = 0
    filecount = 1
    ismath=2    
    chunkname = lambda filecount: os.path.join( dir, "chunk-" + str(filecount) + ".xml.bz2")
    chunkfile = bz2.BZ2File( chunkname( filecount ), 'w')
    # Read line by line
    bzfile = bz2.BZ2File( filename )
    
     
    for line in bzfile:
        # the <page determines new wiki page
        if '<page' in line:
            
            ismath = 0
            mainarticle=0
            formula=0                     
        
        if '<title>' in line:
            title= re.sub(re.compile('<.*?>'),'', line)        
	
        if '<ns>0</ns>':
            mainarticle=1

        if '&lt;' + tag in line:
            ismath=1
            
        if((line.startswith(':&lt;' + 'math') or line.startswith('::&lt;' + 'math') or line.startswith(': &lt;' + 'math'))):            
                formula +=1                
                if(formula==1):                     
                    ismath=1                     
                    finalformula=line                    
                    

        if '</page>' in line:
            if (ismath==1 and mainarticle==1):                
                pagecount += 1
                print title
		print finalformula
                chunkfile.write(title)
                chunkfile.write(finalformula)
		
	if pagecount > splitsize:
                        
            chunkfile.close()
            pagecount = 0 # RESET pagecount
            filecount += 1 # increment filename
            chunkfile = bz2.BZ2File( chunkname( filecount ), 'w')
        
            
    try:        
        chunkfile.close()
    except:
        print 'Files already close'
        
if __name__ == '__main__': # When the script is self run
    parser = argparse.ArgumentParser(description='extract formulae from the wikipedia pages',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--filename', help='the bz2-file to be split and filtered',
        default='enwiki-latest-pages-articles.xml.bz2', dest='file')
    parser.add_argument('-s', '--splitsize', help='the number of pages contained in each split',
        default=1000000, type=int, dest='size')
    parser.add_argument('-d', '--outputdir', help='the directory name where the files go',
        default='wout', type=str, dest='dir')
    parser.add_argument('-t', '--tagname', help='the tag to search for',
        default='math', type=str, dest='tag')   
    args = parser.parse_args()
