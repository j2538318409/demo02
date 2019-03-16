if __name__ == '__main__':
    vlist = [1,2,3,4]
    klist = ['a','b','c','d']
    klist1 = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]
    wlist = [k.strip() for k in klist1]
    lset = set(wlist)
    vas = {l: l for l in lset}
    print(vas)
    vas = {}
    for l in lset:
        vas[l] = l
    print(vas)

    kos1 ={k:v for k in klist for v in vlist}
    print(kos1)


