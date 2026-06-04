#hey
import time as t

def calcit(n_quarters,n_dimes,n_nickels,n_pennies):
    ans = 0.25*n_quarters + 0.1*n_dimes + 0.05*n_nickels + 0.01*n_pennies
    return ans

if __name__ == "__main__":

    while 1:
        
        n_quarterss = input("\nNumber of Quarters: ") or "0"
        n_dimess = input("Number of Dimes: ") or "0"
        n_nickelss = input("Number of Nickels: ") or "0"
        n_penniess = input("Number of Pennies: ") or "0"

        try:
            total = calcit(float(n_quarterss),float(n_dimess),float(n_nickelss),float(n_penniess))
        except ValueError:
            print("\nValueError, probably some non-numbers, try again or quit?")
            tryagain_bool = input("[t]ry again/[q]uit: ")
            if tryagain_bool != "t":
                break
        else:
            print(f"\nThat's ${format(total,'.2f')}... duh")
            t.sleep(0.96*2)
            replay_bool = input("Go again?\n[y]/[n]: ") or "n"
            if replay_bool != "y":
                break
        pass
    pass

else:
    pass
