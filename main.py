from .math_parser import convert_obsidian_math
from anki import hooks
from aqt import mw

def preprocess_note_if_enabled(collection, note, deckId):
    for field in note.keys():
        note[field] = convert_obsidian_math(note[field])

def setup_hook():
    hooks.note_will_be_added.append(preprocess_note_if_enabled)
    mw.form.menuTools
    