# DequeForEachCb

```TypeScript
export type DequeForEachCb<T> = (value: T, index: int, deque: Deque<T>) => void
```

The type of Deque forEach callback function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type DequeForEachCb<T> = (value: T, index: int, deque: Deque<T>) => void--><!--Device-unnamed-export type DequeForEachCb<T> = (value: T, index: int, deque: Deque<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The current element being processed  |
| index | int | Yes | The index of the current element  |
| deque | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;T&gt; | Yes | The Deque instance being traversed  |

