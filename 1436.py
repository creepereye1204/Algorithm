N = int(input())

count = 0          # 현재까지 찾은 '666' 포함 숫자 개수
prefix = 0         # 앞자리 숫자
num_str = "666"    # 기본 패턴

while True:
    count += 1
    num_str = str(prefix) + "666"

    idx = num_str.find("6666")
    if idx >= 0:
        idx += 3
        total_len = len(num_str)
        right_len = total_len - idx
        skip = 10**right_len - 1  # 뒤쪽 자리수로 만들 수 있는 경우의 수

        if count + skip >= N:
            # 원하는 N번째가 이 구간 안에 있음 → 직접 생성
            num_str = num_str[:idx] + str(N - count).rjust(right_len, "0")
            break
        else:
            # 이 구간을 통째로 건너뛰기
            count += skip

    if count == N:
        break

    prefix += 1

print(int(num_str))
