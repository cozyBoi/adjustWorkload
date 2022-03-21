#
from nltk.tokenize import wordpunct_tokenize
i = 0
newEdges = 1
data = 'com-youtube.ungraph.txt' 
newData = 'com-youtube.ungraph' + str(4) + '.txt'
newf = open(newData, "w")
with open(data) as f:
    for line in f:
        g = wordpunct_tokenize(line)
        if g[1] == "Nodes" :
            print(g[3])
            print(g[6])
            newEdges = int(int(g[6]) / 4)
            print("Change Edges to " + str(newEdges))
            g[6] = str(newEdges)
            newf.write(g[0] + ' ' + g[1] + g[2] + ' ' + g[3] + ' ' + g[4] + g[5] + ' ' + g[6] + '\n')
            continue

        if g[0] != '#':
            i+=1

        newf.write(line) # write

        if i >= newEdges : # if exceed limit -> break
            break

print("Edge Num " + str(i))
