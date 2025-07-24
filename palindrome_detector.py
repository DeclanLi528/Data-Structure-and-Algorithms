from pythonds3.basic import Deque

def pal_checker(a_string):
    char_deque = Deque()

    for ch in a_string:
        char_deque.add_rear(ch)

    while char_deque.size()>1:
#Don't forget the parentheses() to actually invoke them.
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            return False
    
    return True

result = pal_checker("radar")
print(result)