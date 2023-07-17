def create_youtube_video(title,description):
	video = {'title':title ,'description':description,'likes': 0,'dislikes': 0,'comments': {}} 
	return video


def like(video):
	if 'likes' in video:
		video['likes'] += 1
	return video


def dislike(video):
	if 'dislikes' in video:
		video['dislikes'] += 1
	return video

def add_comment(video, name, comment):
	video['comments'][name] = comment
	return video



vid = create_youtube_video('Mjd', 'FINISHED LAB')
like(vid)
dislike(vid)
add_comment(vid, 'Messi', ':)')
print(vid)
