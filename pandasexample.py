import uproot
import matplotlib.pyplot as plot
def main():

    try:
        rootfile = uproot.open("~/higgs_merged_processed_Tight_VH.root")
    except FileNotFoundError:
        print("ERROR::File Not Found, link to a local root file")
        exit()

    try: 
        treename = rootfile.keys()[0]
        tree = rootfile[treename]
    except KeyError:
        print("ERROR::Tree not found")
        exit()
        
    pandasdf = tree.pandas.df(["*Pt", "*Eta", "*Phi"])
    print(pandasdf)

if __name__ == "__main__":
    main()
    
