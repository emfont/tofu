import fontforge

font = fontforge.font()
font.fontname = "TofuFont"
font.familyname = "Tofu Font"
font.fullname = "TofuFont"

# Create only the .notdef glyph
notdef = font.createChar(0, ".notdef")
notdef.importOutlines("tofu.svg")
notdef.width = 1000

# Don't define any other glyphs

font.generate("TofuFont-Minimal.ttf")
print("Done. Minimal tofu font generated.")
