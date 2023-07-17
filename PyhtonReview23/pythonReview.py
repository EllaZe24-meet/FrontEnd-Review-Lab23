#percentage = 0
counter = 0
def create_youtube_video(title,description):
    youtube = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}}
    return youtube
    
def like(youtube):
    if "likes" in youtube:
       youtube["likes"]+=1
       
def dislike(youtube):
    if "dislikes" in youtube:
        youtube["dislikes"]+=1

def add_comment(youtubevideo,username,comment_text):
    youtubevideo["comments"][username] = comment_text

youtube = create_youtube_video("Ella","abcde")
print(youtube)
# def similarity_to_video(youtube,youtube2):
#     youtubelist = list(youtube.items())
#     for item in items:
#         if youtubelist[i] == youtube2[counter]:
#             percentage+=16.6
#         counter ++
    
#     print(" the videos are" , percentage, "% similiar")
like(youtube)
dislike(youtube)                
add_comment(youtube, "ella", "hi")
print(youtube)