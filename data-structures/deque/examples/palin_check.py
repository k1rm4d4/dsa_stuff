from deque import Deque

def pal_checker(text: str):
    if len(text) == 0:
        return False 
    
    d = Deque()

    for t in text: 
        d.add_rear(t)

    print(d)

    while d.size() > 1:
        left = d.remove_rear()
        right = d.remove_front()
        print(d)
        if left != right:
            return False
    
    return True


if __name__ == "__main__":
    print(pal_checker("nitin"))
    print(pal_checker("apple"))
    print(pal_checker("a"))
    print(pal_checker(""))
    print(pal_checker("lsdkjfskf"))
    print(pal_checker("radar"))
