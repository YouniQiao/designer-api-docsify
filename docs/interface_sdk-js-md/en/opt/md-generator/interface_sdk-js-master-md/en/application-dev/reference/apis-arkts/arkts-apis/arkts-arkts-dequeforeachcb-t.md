# DequeForEachCb

```TypeScript
export type DequeForEachCb<T> = (value: T, index: number, deque: Deque<T>) => void
```

The type of Deque forEach callback function.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type DequeForEachCb<T> = (value: T, index: int, deque: Deque<T>) => void--><!--Device-unnamed-export type DequeForEachCb<T> = (value: T, index: int, deque: Deque<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |
| index | number | Yes |
| deque | [Deque](arkts-arkts-util-deque-deque-c.md)&lt;T&gt; | Yes |
