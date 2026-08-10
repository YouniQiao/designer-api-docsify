# QueueForEachCb

```TypeScript
export type QueueForEachCb<T> = (value: T, index: int, queue: Queue<T>) => void
```

Queue的回调函数类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type QueueForEachCb<T> = (value: T, index: int, queue: Queue<T>) => void--><!--Device-unnamed-export type QueueForEachCb<T> = (value: T, index: int, queue: Queue<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | 当前遍历到的元素。 |
| index | int | Yes | 当前遍历到的下标值。 该值为整数。 |
| queue | [Queue](arkts-arkts-util-queue-queue-c.md)&lt;T&gt; | Yes | 当前正在遍历的Queue实例。 |

