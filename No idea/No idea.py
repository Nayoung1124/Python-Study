# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_my_score (q, like, dislike):
    my_score = 0
    for i in q:
        if i in like:
            my_score += 1
        if i in dislike:
            my_score -= 1
    print(my_score)




if __name__ == '__main__':
    a = input().split()
    q = input().split()
    like = set(input().split())
    dislike = set(input().split())
    find_my_score(q, like, dislike)


