# build tex
# complie tex 
# xelatex -synctex=1 -interaction=nonstopmode "Tianchen Zhong_CMU_Data Scentist Internship".tex
# cp to dir with name+time

import json
import os
import sys
from GetLatex import *

def build(filename,js):
    with open(filename,'w') as f:
        with open("init.tex") as fin:
            for l in fin:
                if "Education" in l:
                    f.write(l)
                    f.write(getEductionLatex(js["education"]))
                elif "Skill" in l:
                    f.write(l)
                    f.write(getSkillLatex(js["skillset"]))
                elif "Internship" in l:
                    f.write(l)
                    f.write(getExperience(js["experience"]))
                elif "Projects" in l:
                    f.write(l)
                    f.write(getProLatex(js["project"],False))
                else:
                    f.write(l)

def main(f):
    j = json.load(open(f))
    build(j["filename"],j)
    os.system("mv "+j["filename"]+" template/")
    os.chdir("template")
    os.system("xelatex -synctex=1 -interaction=nonstopmode {0}".format(j['filename']))
    #os.system("cp {0} ../product/".format(j["filename"][:-4]+'.pdf'))

if __name__ == '__main__':
    main(sys.argv[1])
    