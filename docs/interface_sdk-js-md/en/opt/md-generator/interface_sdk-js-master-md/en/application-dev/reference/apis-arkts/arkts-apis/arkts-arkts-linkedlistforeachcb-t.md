# LinkedListForEachCb

```TypeScript
export type LinkedListForEachCb<T> = (value: T, index: number, linkedList: LinkedList<T>) => void
```

The type of LinkedList callback function.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type LinkedListForEachCb<T> = (value: T, index: int, linkedList: LinkedList<T>) => void--><!--Device-unnamed-export type LinkedListForEachCb<T> = (value: T, index: int, linkedList: LinkedList<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |
| index | number | Yes |
| linkedList | [LinkedList](arkts-arkts-util-linkedlist-linkedlist-c.md)&lt;T&gt; | Yes |
