import argparse
import os
from subprocess import run

from sys import argv
from os import environ


def main(gitversion=argv[0]):
    os.environ['PATH'] = r"c:\Strawberry\perl\bin;" + os.environ['PATH']
    try:
        os.mkdir('.tmp')
    except FileExistsError:
        pass

    run(f"git --work-tree=./.tmp checkout {gitversion} -- .")
    
    with open("paper/main-diff.tex", "w") as f:
        run("latexdiff --flatten .tmp/main.tex paper/main.tex",
            stdout=f
        )
    run('pdflatex paper/main-diff.tex')
    
    
if __name__ == '__main__':
    main()