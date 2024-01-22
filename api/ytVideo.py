
from flask import Blueprint, jsonify, request
import yt_dlp

ytvideo = Blueprint('ytvideo', __name__)

@ytvideo.route('/api/ytvideo', methods=['POST'])

def main():
	data = request.get_json()
	video_url = data.get('video_url', '')

	videoOptions = {
	  'format': '22',
	}

	audioOptions = {
		'format' : '251',
	}

	with yt_dlp.YoutubeDL(videoOptions) as ydlVideo:
		infoVideo = ydlVideo.extract_info(video_url, download=False)
		# videoFormats = infoVideo.get('formats', [])
		video_url = infoVideo.get('url', None)

	with yt_dlp.YoutubeDL(audioOptions) as ydlAudio:
		infoAudio = ydlAudio.extract_info(video_url, download=False)
		# audioFormats = infoAudio.get('formats', [])
		audio_url = infoAudio.get('url', None)
		
	response_data = {
			'videoURL': video_url,
			'audioURL' : audio_url 
	}

	# options = {'extract_audio': True, 
	# 'format': 'bestaudio', 
	# 'outtmpl': '%(title)s.mp3'}

	# options = {
	# 	'format': 'bestaudio/best',
	# 	'postprocessors': [{
	# 		'key': 'FFmpegExtractAudio',
	# 		'preferredcodec': 'mp3',  # or 'm4a' or any other audio format
	# 		'preferredquality': '192',  # or another desired bitrate
	# 	}],
	# 

	# for format in formats:
	# 	response_data['formats'].append({
	# 		'id':format['format_id'],
	# 		'Resolution': format['resolution'], 
	# 		'Format': format['format'],
	# 		'download_url': format['url']
	# 	})

	return jsonify(response_data)