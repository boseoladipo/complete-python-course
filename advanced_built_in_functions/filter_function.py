def starts_with_r(friend):
    return friend.startswith('r')

friends = ['rolf', 'jose', 'randy', 'anna', 'mary']

# start_with_r = filter(starts_with_r, friends)
start_with_r = filter(lambda friend: friend.startswith('r'), friends)

print(list(start_with_r))
print(list(start_with_r))
# print(next(start_with_r))

friends_lower = map(lambda x: x.lower(), friends)
print(next(friends_lower))