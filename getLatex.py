import json


def getProLatex(namelist,full=True):
    rs = ""
    d = {}
    for filename in ["ProjectJson/cloud.json","ProjectJson/ds.json","ProjectJson/searchengine.json","ProjectJson/other.json",]:
        print(filename)
        with open(filename, 'r') as f:
            obj = json.load(f)
        for i in obj:
            name = i["name"]
            date = i['date']
            place = i['place']
            title = i['title']
            tech = i['tech']
            bull = ""
            if name not in namelist:
                continue
            for s in i["bullet"]:
                bull += "\\item{{{0}}}\n".format(s)
            for t in tech:
                if t in bull:
                    bull = bull.replace(t, "\\textbf{{{0}}}".format(t))
            if full==False:
                template = "\\datedsubsection{{\\textbf{{{0}}}}}{{{1}}} \n\\begin{{itemize}}\n{2}\\end{{itemize}}\n".format(name, date,bull)
            else:
                template = "\\datedsubsection{{\\textbf{{{0}}}}}{{{1}}} \n\\role{{{2}}} {{\\hfill {3}}}\n\\begin{{itemize}}{4}\\end{{itemize}}\n".format(name, place,title,date,bull)
            d[name]=template
    for i in namelist:
        rs+=d[i]
    return rs


def getSkillLatex(name):
    with open("ProjectJson/skillset.json", 'r') as f:
        obj = json.load(f)
    rs = "\\begin{itemize}\n"
    for i in obj:
        if i["id"]==name:
            for k in i:
                if k=="id":
                    continue
                s2 = ", ".join(i[k])
                rs += "\\item \\textbf{{{0}}}: {{{1}}}\n".format(k,s2)
    rs+="\\end{itemize}\n"
    return rs


def getEductionLatex(ref):
    rs = ""
    for filename in ["ProjectJson/Education.json"]:
        with open(filename, 'r') as f:
            obj = json.load(f)
        for i in obj:
            name = i["name"]
            date = i['date']
            place = i['place']
            title = i['title']
            tech = i['tech']
            bull = ""
            if i["id"]!= ref:
                continue
            for s in i["bullet"]:
                bull += "\\item{{{0}}}\n".format(s)
            for t in tech:
                if t in bull:
                    bull = bull.replace(t, "\\textbf{{{0}}}".format(t))
            template = "\\datedsubsection{{\\textbf{{{0}}}}}{{{1}}} \n\\role{{{2}}} {{\\hfill {3}}}\n\\begin{{itemize}}\n{4}\\end{{itemize}}\n".format(name, place,title,date,bull)
            rs+= template
    return rs

def getExperience(ref):
    rs = ""
    for filename in ["ProjectJson/intern.json"]:
        with open(filename, 'r') as f:
            obj = json.load(f)
        for i in obj:
            name = i["name"]
            date = i['date']
            place = i['place']
            title = i['title']
            tech = i['tech']
            bull = ""
            if i["id"]!= ref:
                continue
            for s in i["bullet"]:
                bull += "\\item{{{0}}}\n".format(s)
            for t in tech:
                if t in bull:
                    bull = bull.replace(t, "\\textbf{{{0}}}".format(t))
            template = "\\datedsubsection{{\\textbf{{{0}}}}}{{{1}}} \n\\role{{{2}}} {{\\hfill   {3}}}\n\\begin{{itemize}}\n{4}\\end{{itemize}}\n".format(name, place,title,date,bull)
            rs+= template
    return rs
