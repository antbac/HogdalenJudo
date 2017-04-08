import glob, re

def removeComment(html):
    depth = 1
    while depth > 0:
        start = html.find("<!--")
        end = html.find("-->")
        # Both start and end can not be -1 in syntactically correct code
        if start < end and start != -1:
            html = html[start + 4:]
            depth += 1
        else:
            html = html[end + 3:]
            depth -= 1
    return html


def minifier(html):
    # Double spaces are removed
    while True:
        tmp = html + " "
        html = re.sub(r'\s\s', r' ', html)
        if html == tmp[:-1]:
            break

    # Remove all comments
    tmp = ""
    while html.find("<!--") != -1:
        tmp += html[:html.find("<!--")]
        html = removeComment(html[html.find("<!--") + 4:])
    html = tmp + html

    # Remove all javascripts
    while html.find("<script") != -1:
        pre = html[:html.find("<script"):]
        html = html[html.find("<script") + 7:]
        post = html[html.find("/script>") + 8:]
        html = pre + post

    return html


def replaceLinks(html):
    html = re.sub(r'Index.html', r'http://idrottonline.se/HogdalensJK-Judo', html)
    html = re.sub(r'Information.html', r'http://idrottonline.se/HogdalensJK-Judo/Information', html)
    html = re.sub(r'Kalendarium.html', r'http://idrottonline.se/HogdalensJK-Judo/Kalendarium', html)
    html = re.sub(r'Arkiv.html', r'http://idrottonline.se/HogdalensJK-Judo/Arkiv', html)
    html = re.sub(r'Ledning.html', r'http://idrottonline.se/HogdalensJK-Judo/Ledning', html)
    return re.sub(r'./images/', r'http://idrottonline.se/HogdalensJK-Judo/globalassets/hogdalens-jk---judo/bilder/', html)


for inFile in glob.glob("*.html"):
    with open(inFile) as f:
        content = f.readlines()
    html = ""
    for line in content:
        html += line.strip()
    outFile = open("minified/" + inFile, "w", encoding='utf-8')
    outFile.write(replaceLinks(minifier(html))[len("<!DOCTYPE html><html>"):-len("</html>")])
    outFile.close()
