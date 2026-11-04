posts = [    
    "New campus coffee shop opens",
    "Python workshop this Friday",
    "Robotics club builds a drone",
    "Students launch a weather app",
    "Hackathon registration is open",
    "New library study spaces",
    "Campus Wi-Fi gets upgraded",
    "CS students build a game",
]

PAGE_SIZE = 3


def fetch_page(page):
    start = page * PAGE_SIZE
    end = start + PAGE_SIZE
    return posts[start:end]


page = 0
feed = []
tempVar = True

while True:

    #added if to fix infinite scroll 
    #added an equal sign to fix empty list bug
    if page*PAGE_SIZE >= len(posts):
        print("no more posts")
        break
    if tempVar == True:
        new_posts = fetch_page(page)

        for post in new_posts:
            feed.append(post)

        print("\nYour Feed:")
        for post in feed:
            print("-", post)

        print(f"\nLoaded {len(feed)} posts")




        #no yes case, going to swap to match case
        #added .strip and .lower`
        #fixe
    action = input("\nScroll? (y/n): ")
    match action.strip().lower():
        case "y":
            tempVar = True
            #moved page declaration to case y and changed to += to correctly load more posts
            page += 1
            #removed continue statement because it is un-needed
        case "n":
            break
        case _:
            tempVar = False
            print("Please enter y or n")
            
            #removed continue statement because it is 
            

    


print("Session ended.")
