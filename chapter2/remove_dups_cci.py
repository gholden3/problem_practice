
from LinkedList import LinkedList


def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = set([current.data])
    print(current.next)
    while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next

    return ll


def remove_dups_followup(ll):
    if ll.head is None:
        return

    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return ll.head

ll = LinkedList([3, 4, 5, 6, 7, 7])
print(ll)
remove_dups(ll)
print(ll)

# ll.generate(100, 0, 9)
# print(ll)
# remove_dups_followup(ll)
# print(ll)