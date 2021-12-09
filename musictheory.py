from flask import Flask, render_template

notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#'
,'G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#','A','A#','B','C','C#','D','D#','E','F','F#','G','G#']

modes = ['ionian','dorian','phrygian','lydian','myxolydian','aeolian','locrian','ionian','dorian','phrygian','lydian','myxolydian','aeolian','locrian',"ionian","dorian"
,'ionian','dorian','phrygian','lydian','myxolydian','aeolian','locrian','ionian','dorian','phrygian','lydian','myxolydian','aeolian','locrian',"ionian","dorian"]

sl_key = notes.index(input(str('input key:',)))
sl_mode = modes.index(input(str('input mode:',)))

print(sl_key,sl_mode)

x = len(notes)
y = len(modes)

notes_range = notes[sl_key:x]
modes_range = modes[sl_mode:y]
print(notes_range[0:7])

listo = [0,2,4,5,7,9,11,12,14,16]
 

mode_formula = listo[sl_mode:y]
print(mode_formula[0:7])

new_range = notes_range[0+12-mode_formula[0]:30]
print(new_range[0:7])


i = 0
k = 0
mode_letters = []
while i < len(mode_formula):
    i = i + 1
    while k < len(mode_formula):
        if k not in mode_letters:
            mode_letters.append(new_range[mode_formula[k]])
            k = k + 1
print(f'{modes[sl_mode]} in the key of {notes[sl_key]} is: {str(mode_letters[0:7])[1:-1]}')



app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return f'{modes[sl_mode]} in the key of {notes[sl_key]} is: {str(mode_letters[0:7])[1:-1]}'

if __name__ == '__main__':
    app.run(debug=True,port=5001)

