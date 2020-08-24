# Difference between using out buffer and joining keys are subtle
def merge(string):
    chars = {}
    # out = ""
    for c in string:
        if c not in chars:
            # out += c
            chars[c] = 1
    # print(out)
    print("".join([c for c in chars.keys()]))
def merge_the_tools(string, k):
    l = len(string)
    for i in range(0,l,k):
        t = string[i:i+k]
        merge(t)

if __name__ == '__main__':
