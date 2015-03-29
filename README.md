# words_and_pictures
Python and Javascript to make and play talking pictures.

Create simple, interactive reading lessons with words and pictures by creating three things:

- pictures
- words
- audio files of/from the words

The pictures are grouped on *slides*.

The words are separated into *blocks*.

See [demo](http://jg1141.github.io/) with 6 slides in English, German and Chinese.

##JSON Format for Linking Pictures (img) to Words (text)

Example input (test.json):

```json
 [
  {
    "slide" : [
      {
        "img" : "Raining.jpg",
        "text" : "First rain,"
      },
      {
        "img" : "Rainbow.jpg",
        "text" : "then rainbow."
      }
    ]
  },
  {
    "slide" : [
      {
        "img" : "Land.jpg",
        "text" : "Sea"
      },
      {
        "img" : "Clouds.jpg",
        "text" : "and clouds"
      },
      {
        "img" : "Sunshine.jpg",
        "text" : "make a sunny day."
      }
    ]
  }
]
```

On a Mac, use 

> $ python json2mp3.py test.json

to use the *say* utility to create .mp3 files from the words and add the file names (with key of "audio") to each block. Output goes into *test_output.json*.

Don't have a Mac? Use

> $ python json2mp3_google.py test_google.json

to use the *Google Translate Text-to-Speech API* to create .mp3 files into the audio folder.

Prefer your own voice? Use a sound file editor to create .mp3 files with names following the pattern of s + slide_block + .mp3:

- s0_0.mp3 for full audio of first slide
- s0_1.mp3 for audio of first block of words on first slide
- s0_2.mp3 for audio of second block of words on first slide
- ...
- s1_0.mp3 for full audio of second slide
- s1_1.mp3 for audio of first block of words on second slide
- s1_2.mp3 for audio of second block of words on second slide


##Playing with Cloned Repo

```
$ git clone https://github.com/jg1141/words_and_pictures.git
$ cd words_and_pictures
$ python -m SimpleHTTPServer
```

Open your web browser to [http://localhost:8000/](http://localhost:8000/).
