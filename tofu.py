import fontforge

font = fontforge.font()
font.fontname = "TofuFont"
font.familyname = "Tofu Font"
font.fullname = "TofuFont"

# Load SVG tofu once
tofu_glyph = font.createChar(-1, "tofu")
tofu_glyph.importOutlines("paw-print.svg")
tofu_glyph.width = 1000

# Apply tofu glyph to many Unicode points
for code in range(0x0020, 0xFFFF):  # Basic Latin to BMP
    try:
        g = font.createChar(code)
        g.clear()
        g.addReference("tofu")  # Link to the tofu shape
        g.width = 1000
    except Exception as e:
        print(f"Error at {code:X}: {e}")

font.generate("PawFont.ttf")
print("Font generated: TofuFont.ttf")
