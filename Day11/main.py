import re


def decodeFilename(filename):
    pattern = r"\_([^.])*\.(\w{3})"
    match = re.search(pattern, filename)
    if match:
        return filename[match.start()+1:match.end()]
    return "nothing is decoded, empty or incorect filename was passed "


print(f"Decoded file is: {decodeFilename(
    "202_312_25123$45678_4slei-ghD123_123esign.png.grinchwa")}")
print(f"Decoded file is: {decodeFilename(
    "2023122512345678_sleighDesign.png.grinchwa")}")
print(f"Decoded file is: {decodeFilename(
    "42_chimney_dimensions.pdf.hack2023")}")
print(f"Decoded file is: {decodeFilename(
    "987654321_elf-roster.csv.tempfile")}")
print(f"Decoded file is: {decodeFilename(
    "")}")
print(f"Decoded file is: {decodeFilename(
    "987654321_elf-rostercsvtempfile")}")
