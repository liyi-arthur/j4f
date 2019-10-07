import requests
from lxml import etree
import sys
import os

g_curdir = os.path.split(os.path.abspath(__file__))[0]
g_outDir = os.path.join(g_curdir, "out")

def GetRequest(link, to, retries):
    for i in range(0, retries):
        try:
            return requests.get(url=link, timeout=to)
        except requests.exceptions.Timeout:
            print("Failed to get " + link + ", and retry...")

# /html/body/div[5]/div/div[2]/div[2]/ul
def GetLinks(link):
    r = requests.get(url=link)
    print(r.encoding)
    print(r.status_code)
    tree = etree.HTML(str(r.content, encoding='utf-8', errors='ignore'))
    links = tree.xpath('/html/body/div[5]/div/div[2]/div[2]/ul/li/a')
    res = []
    for link in links:
        # print(link.text, link.attrib['href'])
        res.append(link.attrib['href'])
    return res

def GetContent(link):
    r = GetRequest(link, 3, 3)
    print(r.encoding, r.status_code)
    beginStr = "<div class=\"content\">"
    begin = r.text.find(beginStr)
    end = r.text.find("</div>", begin)
    content = r.text[(begin+len(beginStr)):end].replace("<br/><br/>", "\n")
    # print(content)
    return content

def SaveLinks(links):
    fh = open(os.path.join(g_outDir, "links.txt"), "w")
    for l in links:
        fh.write(l + "\n")
    fh.close()

def GetLinksLocal():
    if os.path.exists(g_outDir) == False:
        os.mkdir(g_outDir)
    linksFile = os.path.join(g_outDir, "links.txt")
    if os.path.exists(linksFile) == False:
        return None
    links = []
    fh = open(linksFile, "r")
    for l in fh.readlines():
        links.append(l)
    fh.close()
    return links

def SaveContent(link, content):
    fname = os.path.join(g_outDir, link.split("/")[-1])
    fh = open(fname, "w", encoding="gb2312", errors='ignore')
    fh.write(content)
    fh.close()

def IsLinkFetched(link):
    fname = os.path.join(g_outDir, link.split("/")[-1])
    return os.path.exists(fname)

def cat(weburl, head, fname):
    links = GetLinksLocal()
    if links == None:
        links = GetLinks(weburl)
        SaveLinks(links)
    for l in links:
        if IsLinkFetched(l.strip()): continue
        link = head+l.strip()
        print(link)
        c = GetContent(link)
        SaveContent(l.strip(), c)
    return


def main():
    if len(sys.argv) < 4:
        print("Usage: " + sys.argv[0] + " url head fname.")
        return
    cat(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__": main()