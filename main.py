from getpass import getpass
from auto_import import auto_import
auto_import("instaloader")


def fetch_instagram_follower_data():
    print("TRACK YOUR INSTAGRAM FOLLOWERS")

    print()
    username = input("Username: ")
    password = getpass()
    print()

    print("Verifying your account...", end='\r')
    L = instaloader.Instaloader()  # Get instance
    L.login(username, password)  # Login or load session
    profile = instaloader.Profile.from_username(
        L.context, username)  # Obtain profile metadata

    print("Fetching followee data...", end='\r')
    i_follow_them = []
    followee_count = 0
    for followee in profile.get_followees():
        i_follow_them.append(followee.username)
        followee_count = followee_count + 1

    print("Fetching follower data...", end='\r')
    they_follow_me = []
    follower_count = 0
    for follower in profile.get_followers():
        they_follow_me.append(follower.username)
        follower_count = follower_count + 1

    return i_follow_them, they_follow_me


mutual = []  # we mutually follow each other
betrayal = []  # i follow them but they don't follow me
sneaky = []  # they follow me but i don't follow them

i_follow_them, they_follow_me = fetch_instagram_follower_data()

for person in i_follow_them:
    if person in they_follow_me:
        mutual.append(person)
    else:
        betrayal.append(person)
for person in they_follow_me:
    if not person in i_follow_them:
        sneaky.append(person)

print(f"You have been betrayed by {len(betrayal)} people:")
for person in betrayal:
    print(f"    {betrayal.index(person)+1}. {person}")
print()

print(f"You have betrayed the trust of {len(sneaky)} people:")
for person in sneaky:
    print(f"    {sneaky.index(person)+1}. {person}")
print()
