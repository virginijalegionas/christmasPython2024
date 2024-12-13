import re


def decodeFilename(filename):
    pattern = r"\d*\_(.*)[\.].*"
    match22222 = re.match(pattern, filename)
    if match22222:
        return match22222.group(1)
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
print(f"Decoded file is: {decodeFilename(
    "3_word.sqlite.work")}")
print(f"Decoded file is: {decodeFilename(
    "3_w dddd deee e 444 ord.sqlite.work")}")
