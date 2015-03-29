import sys
import json
from subprocess import call
import os

class Slides():
	""" Class for processing audio of slides extracted from JSON file"""

	def write_audio(self, text_to_speak, on_slide, on_block):
		"""Use Mac say command to create .m4a files and ffmpeg to convert them to .mp3"""
		cmd = ["say", '\"' + text_to_speak + '\"', "-o", "s" + 
		        str(on_slide) + "_" + str(on_block) + ".m4a", "--file-format=m4af"]
		call(cmd)
		output_file = "audio/s" + str(on_slide) + "_" + str(on_block) + ".mp3"
		cmd = ["ffmpeg", "-y", "-i", "s" + 
		        str(on_slide) + "_" + str(on_block) + ".m4a", output_file]
		call(cmd)
		cmd = ["rm", "s" + 
		        str(on_slide) + "_" + str(on_block) + ".m4a"]
		call(cmd)
		return output_file

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
					 self.write_audio(block['text'], on_slide, on_block)

			d[on_slide]['audio'] = self.write_audio(text_to_speak, on_slide, 0)
			with open('test_output.json', 'w') as outfile:
			    json.dump(d, outfile)
			on_slide += 1
			on_block = 0
			text_to_speak = ""


def main(argv):
	if len(argv) < 2:
		print "Usage: python json2mp3.py <json file>"
		print "       .mp3 files output to audio folder"
	else:
		# Make sure audio folder exists
		if not os.path.exists("./audio"):
			os.makedirs("./audio")
		slides = Slides()
		slides.read_and_parse(argv[1])

if __name__ == "__main__":
    main(sys.argv)

