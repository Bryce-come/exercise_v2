# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# @param s string字符串 
# @return string字符串一维数组
'''
"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

输出 ["AAAAACCCCC","CCCCCAAAAA"]
'''


#
def findRepeatedDnaSequences(s):
    n = len(s)
    links = []
    for i in range(n - 10):
        links.append(s[i:i + 10])
    n_links = len(links)
    outputs = []
    for i in range(n_links):
        for j in range(i+1, n_links):
            if links[i] == links[j]:
                outputs.append(links[j])
    return outputs


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(s))
