
print("로또 추첨 입니다")
import random
for i in range(5):
    lotto = random.sample(range(1, 46), 6)
    print(lotto)
