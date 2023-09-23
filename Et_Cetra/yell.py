def main ():
    yell ("This", "is", "CS50")
    
    
def yell(*words):
    # uppered_case = []
    # for word in words:
    #     uppered_case.append(word.upper())
    
    # uppered_case = map(str.upper, words)
    # print (*uppered_case)
    
    
    uppercase = [word.upper() for word in words]
    print (*uppercase)
    
if __name__ == "__main__":
    main()