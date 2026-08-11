# QueueForEachCb

```TypeScript
export type QueueForEachCb<T> = (value: T, index: int, queue: Queue<T>) => void
```

The type of Queue callback function.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type QueueForEachCb<T> = (value: T, index: int, queue: Queue<T>) => void--><!--Device-unnamed-export type QueueForEachCb<T> = (value: T, index: int, queue: Queue<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | T | Yes | The value of current element |
| index | int | Yes | The key of current element The value should be an integer. |
| queue | [Queue](arkts-arkts-util-queue-queue-c.md)&lt;T&gt; | Yes | The Queue instance being traversed |

