# @ohos.util.ArrayList

ArrayList is a linear data structure that is implemented based on arrays. ArrayList can dynamically adjust the
 capacity based on project requirements. It increases the capacity by 50% each time.
 When compared with [LinkedList](arkts-util-linkedlist.md), ArrayList is more efficient in random access but less
 efficient in the addition or removal operation, because its addition or removal operation affects the position of
 other elements in the container.
 **Recommended use case**: Use ArrayList when elements in a container need to be frequently read.
 This topic uses the following to identify the use of generics:
 - T: Type
 > **NOTE**
 >
 > - Container classes, implemented in static languages, have restrictions on storage locations and properties, and do
 > not support custom properties or methods.


## Summary

### Classes

| Name | Description |
| --- | --- |
| [ArrayList](arkts-arkts-util-arraylist-arraylist-c.md) | ArrayList is a linear data structure that is implemented based on arrays.ArrayList can dynamically adjust the capacity based on project requirements.It increases the capacity by 50% each time. |

### Types

| Name | Description |
| --- | --- |
| [ArrayListComparatorFn](arkts-arkts-arraylistcomparatorfn-t.md) | This type specifies the comparator of sort in comparation. |
| [ArrayListForEachCb](arkts-arkts-arraylistforeachcb-t.md) | The type of ArrayList callback function. |
| [ArrayListReplaceCb](arkts-arkts-arraylistreplacecb-t.md) | The type of ArrayList callback function. |

