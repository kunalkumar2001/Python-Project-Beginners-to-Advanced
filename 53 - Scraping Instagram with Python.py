import instaloader

bot = instaloader.Instaloader()

profile = instaloader.Profile.from_username(bot.context, '__itskunalyaduvanshi__')

print(type(profile))
print("Username:", profile.username)
print("Full Name:", profile.full_name)
print("Followers:", profile.followers)
print("Following:", profile.followees)
print("Total Posts:", profile.mediacount)
print("Bio:", profile.biography)


#Get Recent Posts
for post in profile.get_posts():
    print(post.date)
    print(post.caption)
    print(post.likes)
    print("-" * 40)
    break 


