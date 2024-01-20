
from flask import Blueprint, jsonify, request
import yt_dlp

ytvideo = Blueprint('ytvideo', __name__)

@ytvideo.route('/api/ytvideo', methods=['POST'])

def main():
	data = request.get_json()
	video_url = data.get('video_url', '')

	# options = {
	#     'format': 'best',  # You can customize the format based on your needs
	# }

	options = {'extract_audio': True, 
	'format': 'bestaudio', 
	'outtmpl': '%(title)s.mp3'}

	# options = {
	# 	'format': 'bestaudio/best',
	# 	'postprocessors': [{
	# 		'key': 'FFmpegExtractAudio',
	# 		'preferredcodec': 'mp3',  # or 'm4a' or any other audio format
	# 		'preferredquality': '192',  # or another desired bitrate
	# 	}],
	# }

	with yt_dlp.YoutubeDL(options) as ydl:
		info_dict = ydl.extract_info(video_url, download=False)
		formats = info_dict.get('formats', [])
		video_url = info_dict.get('url', None)
		
	response_data = {
			'download_url': video_url,
			'formats': []
	}

	for format in formats:
		response_data['formats'].append({
			'id':format['format_id'],
			'Resolution': format['resolution'], 
			'Format': format['format'],
			'download_url': format['url']
		})

	return jsonify(response_data)