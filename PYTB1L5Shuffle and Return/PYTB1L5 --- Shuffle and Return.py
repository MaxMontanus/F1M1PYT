import random

original = "Hallo"
originalrandom = 'Hallo'.join(random.sample(original, len(original)))
print(originalrandom)