import sys
import json
from subprocess import call
import urllib
import os

class Slides():
	""" Class for processing audio of slides extracted from JSON file"""

	def write_audio(self, text_to_speak, language, on_slide, on_block):
		"""Use Google Text-to-Speech to create .mp3 files"""
		print "To .mp3: " + text_to_speak
		q = urllib.urlencode({"q":text_to_speak.encode('utf-8')})
		cmd = ["wget", "-q", "-U", "Mozilla", 
		       'http://www.translate.google.com/translate_tts?ie=UTF-8&tl=' + language + '&' + q, 
		       "-O", "audio/s" + str(on_slide) + "_" + str(on_block) + ".mp3"]
		call(cmd)
		return "s" + str(on_slide) + "_" + str(on_block) + ".mp3"

	def read_and_parse(self,file):
		"""Makes calls to output an .mp3 file for each block and one for the full slide"""
		d = {}
		with open(file) as json_data:
			d = json.load(json_data)
		on_slide = 0
		on_block = 0
		text_to_speak = ""
		for slide in d:
			for block in slide['slide']:
				if block['text']:
					text_to_speak += block['text'] + " "
					on_block += 1
					d[on_slide]['slide'][on_block-1]['audio'] = \
					 self.write_audio(block['text'], block['language'], on_slide, on_block)

			d[on_slide]['audio'] = self.write_audio(text_to_speak, d[on_slide]['slide'][0]['language'], on_slide, 0)
			with open('test_output.json', 'w') as outfile:
			    json.dump(d, outfile)
			on_slide += 1
			on_block = 0
			text_to_speak = ""


def main(argv):
	if len(argv) < 2:
		print "Usage: python json2mp3_google.py <json file>"
		print "Notes: language must be specified for each block"
		print "       .mp3 files output to audio folder"
	else:
		# Make sure audio folder exists
		if not os.path.exists("./audio"):
			os.makedirs("./audio")
		slides = Slides()
		slides.read_and_parse(argv[1])

if __name__ == "__main__":
    main(sys.argv)

