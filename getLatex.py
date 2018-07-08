import json


def getProLatex(js):
    with open(js, 'r') as f:
        obj = json.load(f)
    rs = ""
    for i in obj:
        name = i["name"]
        date = i['date']
        place = i['place']
        title = i['title']
        tech = i['tech']
        bull = ""
        for s in i["bullet"]:
            bull += "\\item{{{0}}}\n".format(s)
        for t in tech:
            if t in bull:
                bull = bull.replace(t, "\\textbf{{{0}}}".format(t))
        template = "\\datedsubsection{{\\textbf{{{0}}}}}{{{1}}}\n\\begin{{itemize}}{2}\\end{{itemize}}\n".format(name, date, bull)
        rs+= template
    return rs
def getSkillLatex(js):
    with open(js, 'r') as f:
        obj = json.load(f)
    rs = ""
    for i in obj:
        for k in i:
            s2 = ", ".join(i[k])
            rs += "\\item \\textbf{{{0}}}: {{{1}}}\n".format(k,s2)
    return rs

#print(getProLatex("intern.json"))
print(getSkillLatex("skillset.json"))