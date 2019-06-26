import matplotlib.pyplot as plt
from mido import MidiFile

acc = 0
times = []
notes = []
for msg in MidiFile('Claro de Luna Debussy.mid'):
    if msg.type in ['note_on', 'note_off']:
        acc += msg.time
        if msg.type == 'note_on':
            times.append(acc)
            notes.append(msg.note)

plt.scatter(times, notes)
plt.show()
