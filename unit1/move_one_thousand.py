#write code that moves 1000 times and then prints the 
#resulting probability distribution.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def get_moved_index(current, delta, total):
    actual = current + delta
    if actual < 0:
        actual = total + actual
    elif actual >= total:
        actual = actual - total
    return actual

def move(p, U):
    if U == 0:
        return p
    q = [x*0.0 for x in p]
    for i in range(len(p)):

        # Precompute indexes for inexact motions
        exact_index = get_moved_index(i, 1*U, len(p))
        undershoot_index = get_moved_index(exact_index, -1, len(p))
        overshoot_index = get_moved_index(exact_index, 1, len(p))

        final_q = [x*0.0 for x in p]
       
        # Factor inexact motion into distribution
        final_q[exact_index] = p[i]*pExact
        final_q[undershoot_index] = p[i]*pUndershoot
        final_q[overshoot_index] = p[i]*pOvershoot

        # Add result to overall distribution
        for j in range(len(final_q)):
            q[j] = q[j] + final_q[j]
    return q

def move_solution(p,U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q
    

times = 1000
for i in range(times):
  p = move(p,1)
print p