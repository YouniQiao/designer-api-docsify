# DequeForEachCb

```TypeScript
export type DequeForEachCb<T> = (value: T, index: int, deque: Deque<T>) => void
```

The type of Deque forEach callback function.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |
| index | int | Yes |
| deque | [Deque](arkts-arkts-util-deque-deque-c.md)&lt;T&gt; | Yes |
