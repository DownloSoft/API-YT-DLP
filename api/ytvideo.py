
from flask import Blueprint, jsonify, request
import yt_dlp

ytvideo = Blueprint('ytvideo', __name__)

@ytvideo.route('/api/ytvideo', methods=['POST'])

def main():
	data = request.get_json()
	dataURL = data.get('dataURL', '')

	videoOptions = {
	  'format': 'best',
	}

	audioOptions = {
		'format': 'bestaudio/best',
	}

	with yt_dlp.YoutubeDL(videoOptions) as ydlVideo:
		infoVideo = ydlVideo.extract_info(dataURL, download=False)
		video_url = infoVideo.get('url', None)

	with yt_dlp.YoutubeDL(audioOptions) as ydlAudio:
		infoAudio = ydlAudio.extract_info(dataURL, download=False)
		audio_url = infoAudio.get('url', None)
		
	response_data = {
			'videoURL': video_url,
			'audioURL' : audio_url 
	}

	return jsonify(response_data)