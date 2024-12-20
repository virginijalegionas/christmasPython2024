import re

def removeSnow(snow):    
    pattern = r"([a-zA-Z])\1"
    isMatch = re.search(pattern, snow)
    while isMatch:
        snow = re.sub(pattern, "", snow)        
        isMatch = re.search(pattern, snow)
    return snow





print(f"removed snow: {removeSnow('zxxzoz')}")
print(f"removed snow: {removeSnow('abcdd')}")
print(f"removed snow: {removeSnow('zzz')}")
print(f"removed snow: {removeSnow('a')}")