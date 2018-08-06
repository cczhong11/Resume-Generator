'''
This file will write and compile resume latex file.
'''
import json
import os
import sys
from GetLatex import *

'''
Read init tex file and add content from pre-defined json 
args:
    filename:  filename defined your resume file
    js: resume json object 
'''
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

'''
main program

Read resume object, copy to template folder, use latex to build and compile it. Then delete some temp files and move your tex and pdf to root folder.

args:
    file:  json file defines your resume.
'''
def main(file):
    jobj = json.load(open(file))
    build(jobj["filename"],jobj)
    os.system("mv "+jobj["filename"]+" template/")
    os.chdir("template")
    os.system("xelatex -synctex=1 -interaction=nonstopmode {0}".format(jobj['filename']))
    os.system("mv {0} ..".format(jobj["filename"][:-4]+'.pdf'))
    os.system("mv {0} ..".format(jobj["filename"][:-4]+'.tex'))
    os.system("rm {0}".format(jobj["filename"][:-4]+'.*'))

if __name__ == '__main__':
    main(sys.argv[1])
    