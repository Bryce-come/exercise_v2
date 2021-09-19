import sys

if __name__ == "__main__":
    yyyy, MM, dd, HH, mm, ss, n = sys.stdin.readline().split(", ")
    yyyy = int(yyyy)
    MM = int(MM)
    dd = int(dd)
    HH = int(HH)
    mm = int(mm)
    ss = int(ss)
    n = int(n)
    leap = 0
    if yyyy % 400 == 0 or yyyy % 100 != 0 and yyyy % 4 == 0:
        leap = 1

    def int_str(q1):
        n = len(q1)
        for i in range(n):
            if q1[i]>-1 and q1[i] < 10:
                q1[i] = "0" + str(q1[i])
            else:
                q1[i] = str(q1[i])
        return q1

    if leap == 1:
        md_dict1 = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30,
                    12: 31}
        ss = ss + n
        if ss > 59:
            ss = ss - 60
            mm += 1
            if mm > 59:
                mm = mm - 60
                HH += 1
                if HH > 23:
                    HH = HH - 24
                    dd += 1
                    if dd > md_dict1[MM]:
                        dd = dd - md_dict1[MM]
                        MM += 1
                        if MM > 12:
                            MM = MM - 12
                            yyyy += 1

        q1 = [MM, dd, HH, mm, ss]
        yyyy = str(yyyy)
        int_str(q1)
        print(yyyy + "-" + q1[0] + "-" + q1[1]+" "+q1[2] + ":" + q1[3] + ":" + q1[4])
    else:
        md_dict1 = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30,
                    12: 31}
        ss = ss + n
        if ss > 59:
            ss = ss - 60
            mm += 1
            if mm > 59:
                mm = mm - 60
                HH += 1
                if HH > 23:
                    HH = HH - 24
                    dd += 1
                    if dd > md_dict1[MM]:
                        dd = dd - md_dict1[MM]
                        MM += 1
                        if MM > 12:
                            MM = MM - 12
                            yyyy += 1
        q1 = [MM, dd, HH, mm, ss]
        yyyy = str(yyyy)
        int_str(q1)
        print(yyyy + "-" + q1[0] + "-" + q1[1]+" "+q1[2] + ":" + q1[3] + ":" + q1[4])

        '''
        2019, 12, 31, 23, 59, 59, 1
        '''