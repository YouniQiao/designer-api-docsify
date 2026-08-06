# @ohos.util.LinkedList

LinkedList is implemented based on the doubly linked list. Each node of the doubly linked list has references
 pointing to the previous element and the next element. When querying an element, the system traverses the list from
 the beginning or end. LinkedList offers efficient insertion and removal operations but supports low query efficiency.
 LinkedList allows null elements.
 Unlike [List](arkts-util-list.md), which is a singly linked list, LinkedList is a doubly linked list that supports
 insertion and removal at both ends.
 LinkedList is more efficient in data insertion than [ArrayList](arkts-util-arraylist.md), but less efficient in
 data access.
 > **NOTE**
 >
 > Accessing elements in a LinkedList using the \[index\] syntax may lead to undefined results. You are advised to use
 > **get()** instead.
 > **Recommended use case**: Use LinkedList for frequent insertion and removal operations when a doubly linked list is
 > required.
 > This topic uses the following to identify the use of generics:
 - T: Type
 > **NOTE**
 >
 > - Container classes, implemented in static languages, have restrictions on storage locations and properties, and do
 > not support custom properties or methods.


## Summary

### Classes

| Name | Description |
| --- | --- |
| [LinkedList](arkts-arkts-util-linkedlist-linkedlist-c.md) | LinkedList is implemented based on the doubly linked list. Each node of the doubly linked list has references pointing to the previous element and the next element. When querying an element,the system traverses the list from the beginning or end. |

### Types

| Name | Description |
| --- | --- |
| [LinkedListForEachCb](arkts-arkts-linkedlistforeachcb-t.md) | The type of LinkedList callback function. |

