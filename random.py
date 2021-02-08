from itertools import combinations

def MaximizeCodeChef():
    T = int(input())
    if 1 <= T <= 5:

        for _ in range(T):
            N = int(input())
            if 3 <= N <= 10**5:
                N_l = list(map(int, input().split()))
                comb = combinations(N_l, 3)
                out_f = 0
                for var in comb:
                    if var[0] <= 10 ** 9 and var[1] <= 10 ** 9 and var[2] <= 10 ** 9:
                        out = abs(var[0] - var[1]) + abs(var[1] - var[2]) + abs(var[2] - var[0])
                        if out > out_f:
                            out_f = out
                        else:
                            pass
    #             out_f = 0
    #             for var in range(N - 2):
    #                 index = var
    #                 if N_l[index] <= 10**9 and N_l[index+1] <= 10**9 and N_l[index+2] <= 10**9:
    #                     out = abs(N_l[index] - N_l[index + 1]) + abs(N_l[index + 1] - N_l[index + 2]) + abs(
    #                         N_l[index + 2] - N_l[index])
    #                     if out > out_f:
    #                         out_f = out
    #                     else:
    #                         pass
                    else:
                        raise Exception("A_i: Out of Constraints")
                print(out_f)
            else:
                raise Exception("N: Out of Constraints")
    else:
        raise Exception("T: Out of Constraints")


if __name__ == '__main__':
    MaximizeCodeChef()
