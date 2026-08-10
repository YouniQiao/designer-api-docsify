# LinkedListForEachCb

```TypeScript
export type LinkedListForEachCb<T> = (value: T, index: int, linkedList: LinkedList<T>) => void
```

LinkedList的回调函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type LinkedListForEachCb<T> = (value: T, index: int, linkedList: LinkedList<T>) => void--><!--Device-unnamed-export type LinkedListForEachCb<T> = (value: T, index: int, linkedList: LinkedList<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 当前元素的值。 |
| index | int | Yes | 当前元素的下标。 该值为整数。 |
| linkedList | [LinkedList](arkts-arkts-util-linkedlist-linkedlist-c.md)&lt;T&gt; | Yes | 当前正在遍历的LinkedList实例。 |

