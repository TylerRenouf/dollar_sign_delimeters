from .math_parser import convert_obsidian_math, convert_mathjax_math
from anki import hooks
from aqt import gui_hooks
from aqt.editor import Editor




def preprocess_note_if_enabled(collection, note, deckId):
	for field in note.keys():
		note[field] = convert_obsidian_math(note[field])

   
def on_latex_math_toggle(editor: Editor) -> None:
	note = editor.note
		
	for field in note.keys():
		note[field] = convert_obsidian_math(note[field])

	editor.loadNoteKeepingFocus()

def on_mathjax_math_toggle(editor: Editor) -> None:
	note = editor.note

	for field in note.keys():
		note[field] = convert_mathjax_math(note[field])
 
	editor.loadNoteKeepingFocus()


def add_toggle_button(buttons, editor: Editor) -> None:
	latex_button = editor.addButton(None,'latex_math', on_latex_math_toggle,label = "Convert LaTeX to MathJax")
	mathjax_button = editor.addButton(None,'mathjax_math', on_mathjax_math_toggle,label = "Convert MathJax to LaTeX")
 
	buttons.append(latex_button)
	buttons.append(mathjax_button)


def setup_hooks():
	gui_hooks.editor_did_init_buttons.append(add_toggle_button)
	hooks.note_will_be_added.append(preprocess_note_if_enabled)
