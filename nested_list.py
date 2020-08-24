if __name__ == '__main__':
    # parse from input
    records = []
    l = int(input())
    for _ in range(l):
        name = input()
        score = float(input())
        records.append([name, score])
    # sort it by scores non-decreasing order
    records = sorted(records, key=lambda record: record[1])

    got_second = False # found second flag
    sec_names = []
    for i in range(1,l):
        if records[i][1] == records[0][1]:
            # skip lowest
            continue
        if not got_second:
            # change flag and set second lowest
            sec_low =records[i][1]
            got_second = True
        if records[i][1] == sec_low:
            # add second lowests
            sec_names.append(records[i][0])
        else:
            # We passed second lowests, so no need to continue te loop
            break
    # sort names and output
    sort_names = sorted(sec_names)
    for name in sort_names:
        print(name)
