from termuxClipboard import Clipboard

clipboard = Clipboard()
text = repr(clipboard.get())
text = text.rsplit(r"\\n")
text = r"\\n".join([i.replace(r'\n', r"\n\t") for i in text])
text = text[1:-1]
text = r'\t' + text
print(text)
clipboard.set(text)