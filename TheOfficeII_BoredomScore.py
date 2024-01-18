# Every now and then people in the office moves teams or departments. Depending what people are doing with their time they can become more or less boring. Time to assess the current team.

# You will be provided with an object(staff) containing the staff names as keys, 
# and the department they work in as values.

# Each department has a different boredom assessment score, as follows:

# accounts = 1
# finance = 2
# canteen = 10
# regulation = 3
# trading = 6
# change = 6
# IS = 8
# retail = 5
# cleaning = 4
# pissing about = 25

# Depending on the cumulative score of the team, return the appropriate sentiment:

# <=80: 'kill me now'
# < 100 & > 80: 'i can handle this'
# 100 or over: 'party time!!'

def boredom(staff):
    
    boredom = []
    for mood in staff.values():
        if mood == "accounts":
            boredom.append(1)
        elif mood == "finance":
            boredom.append(2)
        elif mood == "canteen":
            boredom.append(10)
        elif mood == "regulation":
            boredom.append(3)
        elif mood == "trading":        
            boredom.append(6)
        elif mood == "change":
            boredom.append(6)
        elif mood == "IS":
            boredom.append(8)
        elif mood == "retail":
            boredom.append(5)
        elif mood == "cleaning":
            boredom.append(4)
        elif mood == "pissing about":
            boredom.append(25)
    
    sentiment = sum(boredom)

    if sentiment  <= 80:
        return 'kill me now'
    elif sentiment < 100 and sentiment > 80:
        return 'i can handle this'
    elif sentiment >= 100:
        return 'party time!!'   



boredom({"tim": "change", "jim": "accounts",
      "randy": "canteen", "sandy": "change", "andy": "change", "katie": "IS",
      "laura": "change", "saajid": "IS", "alex": "trading", "john": "accounts",
      "mr": "finance" })
boredom({ "tim": "IS", "jim": "finance",
      "randy": "pissing about", "sandy": "cleaning", "andy": "cleaning",
      "katie": "cleaning", "laura": "pissing about", "saajid": "regulation",
      "alex": "regulation", "john": "accounts", "mr": "canteen" })
boredom({ "tim": "accounts", "jim": "accounts",
      "randy": "pissing about", "sandy": "finance", "andy": "change",
      "katie": "IS", "laura": "IS", "saajid": "canteen", "alex": "pissing about",
      "john": "retail", "mr": "pissing about" })