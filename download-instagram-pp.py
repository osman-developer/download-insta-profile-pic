import instaloader
ob=instaloader.Instaloader()
user=input("enter Username:")
ob.download_profile(user,profile_pic_only=True)