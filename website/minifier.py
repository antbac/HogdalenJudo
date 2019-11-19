import glob
import re


def removeComments(html):
    return re.sub("(<!--.*?-->)", "", html, flags=re.DOTALL)


def extractHeadAndBody(html):
    start = html.find("<head>")
    end = html.find("</body>") + len("</body>")
    return html[start:end]


def removeScripts(html):
    return re.sub("(<script.*?</script>)", "", html, flags=re.DOTALL)


def replaceLinks(html):
    html = re.sub(
        r'Index.html', r'https://idrottonline.se/HogdalensJK-Judo', html)
    html = re.sub(r'Information.html',
                  r'https://idrottonline.se/HogdalensJK-Judo/Information', html)
    html = re.sub(r'Kalendarium.html',
                  r'https://idrottonline.se/HogdalensJK-Judo/Kalendarium', html)
    html = re.sub(
        r'Arkiv.html', r'https://idrottonline.se/HogdalensJK-Judo/Arkiv', html)
    html = re.sub(r'Ledning.html',
                  r'https://idrottonline.se/HogdalensJK-Judo/Ledning', html)
    return re.sub(r'./images/', r'https://idrottonline.se/HogdalensJK-Judo/globalassets/hogdalens-jk---judo/bilder/', html)


if __name__ == "__main__":
    for inFile in glob.glob("*.html"):
        with open(inFile, 'r', encoding='utf-8') as f:
            content = f.read()

        content = content.strip()
        content = removeComments(content)
        content = removeScripts(content)
        content = replaceLinks(content)
        content = extractHeadAndBody(content)
        content = re.sub(r"\s+", " ", content)
        content = re.sub("> <", "><", content)
        content = re.sub("\"", "'", content)

        outFile = open(
            "minified/" + inFile[:-5] + ".min.html", "w", encoding='utf-8')
        outFile.write(content)
        outFile.close()
