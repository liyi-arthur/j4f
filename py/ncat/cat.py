import requests
from lxml import etree
import sys

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

def cat(link, head, fname):
    fh = open(fname, "w", encoding="gb2312", errors='ignore')
    links = GetLinks(link)
    for l in links:
        print(l)
        c = GetContent(head+l)
        fh.write(c)
        fh.flush()
    fh.close()
    return


def main():
    if len(sys.argv) < 4:
        print("Usage: " + sys.argv[0] + " url head fname.")
        return
    cat(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__": main()