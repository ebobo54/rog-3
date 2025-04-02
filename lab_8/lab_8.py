def generate(count_psp, etalon, prefix, open, close):
    if count_psp == 0:
        print(prefix)
    else:
        if prefix == '':
            generate(count_psp-1, etalon, prefix+'(', open+1, close)
        else:
            if open == etalon:
                generate(count_psp-1, etalon, prefix+')', open, close+1)
            elif open == close:
                generate(count_psp-1, etalon, prefix+'(', open+1, close)
            else:
                generate(count_psp-1, etalon, prefix+'(', open+1, close)
                generate(count_psp-1, etalon, prefix+')', open, close+1)


count_psp = int(input())
prefix = ''
open = 0
close = 0

generate(count_psp*2, count_psp, prefix, open, close)