import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 한글 폰트 설정 (Windows: Malgun Gothic, macOS: AppleGothic, Linux: NanumGothic)
plt.rc('font', family='Malgun Gothic')   # 윈도우라면 'Malgun Gothic'
# plt.rc('font', family='AppleGothic')   # 맥이라면 'AppleGothic'
# plt.rc('font', family='NanumGothic')   # 리눅스라면 'NanumGothic'

# 마이너스 기호 깨짐 방지
matplotlib.rcParams['axes.unicode_minus'] = False

# 데이터 입력
years = list(range(1, 11))  # 1~10년차 데이터


marriage_husband_kor = [14677, 14822, 14869,
                        16608, 17687, 11100, 8985, 12007, 14710, 15624]
marriage_wife_kor = [6597, 5769, 5966, 6090,
                     5956, 4241, 4117, 4659, 5007, 5135]


divorce_husband_kor = [5743, 5610, 5206,
                       5174, 4917, 4378, 4315, 3961, 4175, 4218]
divorce_wife_kor = [2494, 2055, 1924, 1966, 1982, 1796, 1858, 1849, 1930, 1804]

# 비율 계산 (이혼수 / 혼인수)

ratio_husband_kor = [d/m for d,
                     m in zip(divorce_husband_kor, marriage_husband_kor)]
ratio_wife_kor = [d/m for d, m in zip(divorce_wife_kor, marriage_wife_kor)]

# 그래프 그리기
plt.figure(figsize=(10, 6))

plt.plot(years, ratio_husband_kor, marker='s', label='한국인 남편 + 외국인 아내')
plt.plot(years, ratio_wife_kor, marker='^', label='한국인 아내 + 외국인 남편')

plt.title('외국인 혼인 대비 이혼 비율')
plt.xlabel('연도(순차 데이터)')
plt.ylabel('이혼수 / 혼인수 비율')
plt.legend()
plt.grid(True)
plt.show()
print(ratio_husband_kor, ratio_wife_kor)

# 전체 혼인/이혼 데이터
marriage_total = [21274, 20591, 20835, 22698,
                  23643, 15341, 13102, 16666, 19717, 20759]
divorce_total = [8237, 7665, 7130, 7140, 6899, 6174, 6173, 5810, 6105, 6022]

# 비율 계산
ratio_total = [d/m for d, m in zip(divorce_total, marriage_total)]
ratio_husband_kor = [d/m for d,
                     m in zip(divorce_husband_kor, marriage_husband_kor)]
ratio_wife_kor = [d/m for d, m in zip(divorce_wife_kor, marriage_wife_kor)]

# 평균 계산
avg_total = np.mean(ratio_total)
avg_husband = np.mean(ratio_husband_kor)
avg_wife = np.mean(ratio_wife_kor)

print("전체 평균:", avg_total)
print("남편 한국인 평균:", avg_husband)
print("아내 한국인 평균:", avg_wife)
