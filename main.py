def love_calculator(name1, name2):
    combined_names = (name1 + name2).lower()
    # calculate for TRUE
    t = combined_names.count("t")
    r = combined_names.count("r")
    u = combined_names.count("u")
    e = combined_names.count("e")
    
    true_total = t + r + u + e
    
    # calculate for LOVE
    l = combined_names.count("l")
    o = combined_names.count("o")
    v = combined_names.count("v")
    e = combined_names.count("e")
    
    love_total = l + o + v + e
    
    score = int(str(true_total) + str(love_total))
    
    # conditional statements
    if score >= 80:
        print(f"Your love score is {score}. You're a perfect match")
    elif 60<= score < 80:
        print(f"Your love score is {score}. You guys can make it work.")
    elif 40 <= score < 60:
        print(f"Your love score is {score}. You have potential")
    else:
        print(f"Your love score is {score}. It's a rocky road ahead")

    
firstname = input("Enter first name: ")
secondname= input("Enter second name: ")   

love_calculator(firstname, secondname)
    