#!/usr/bin/python3
import genanki
import os

my_model = genanki.Model(
  6969696969,
  'Model',
  fields=[
    {'name': 'Object'},
    {'name': 'Image'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Object}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Image}}',
    },
  ])

note_index = 0
def create_note(filename):
    global note_index
    note_index += 1
    return genanki.Note(
            model=my_model,
            sort_field=note_index,
            fields=["".join(filename.replace("_", " ").split(".")[:-1]), f'<img src="{filename}" />'])


if __name__ == '__main__':
    my_deck = genanki.Deck(
      9696969696,
      'Serge Lang Basic Mathematics')
    
    filenames = []
    for filename in os.listdir("."):
        if filename.endswith(".png"): 
            filenames += [filename]
            my_deck.add_note(create_note(filename))

    my_package = genanki.Package(my_deck)
    my_package.media_files = filenames
    
    my_package.write_to_file('output.apkg')

