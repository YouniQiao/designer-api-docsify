# LinkedListForEachCb

```TypeScript
export type LinkedListForEachCb<T> = (value: T, index: int, linkedList: LinkedList<T>) => void
```

The type of LinkedList callback function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type LinkedListForEachCb<T> = (value: T, index: int, linkedList: LinkedList<T>) => void--><!--Device-unnamed-export type LinkedListForEachCb<T> = (value: T, index: int, linkedList: LinkedList<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The value of current element |
| index | int | Yes | The index of current element The value should be an integer. |
| linkedList | [LinkedList](arkts-arkts-util-linkedlist-linkedlist-c.md)&lt;T&gt; | Yes | The LinkedList instance being traversed |

