# QueueForEachCb

```TypeScript
export type QueueForEachCb<T> = (value: T, index: number, queue: Queue<T>) => void
```

The type of Queue callback function.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type QueueForEachCb<T> = (value: T, index: int, queue: Queue<T>) => void--><!--Device-unnamed-export type QueueForEachCb<T> = (value: T, index: int, queue: Queue<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |
| index | number | Yes |
| queue | [Queue](arkts-arkts-util-queue-queue-c.md)&lt;T&gt; | Yes |
