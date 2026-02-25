def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery=0
    pickup=0
    for i in range(n-1,-1,-1):
        delivery+=deliveries[i]
        pickup+=pickups[i]
        cycle,mod=divmod(max(delivery,pickup),cap)
        if mod:
            cycle+=1
        answer+=cycle*2*(i+1)
        delivery-=cap*cycle
        pickup-=cap*cycle
    return answer