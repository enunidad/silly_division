def divn(num, n=3, eps=1e-6):
    is_neg = num < 0
    to_return = num
    if n == 1:
        pass
    if n == 2:
        to_return = num/2
    else:
        import random
        left = random.random()*n
        right = n - left
        rem = divn(right, n-1, eps)
        while abs(rem - left) > eps:
            left = rem
            right = num - left
            rem = divn(right, n-1, eps)
        to_return = left
    return to_return
