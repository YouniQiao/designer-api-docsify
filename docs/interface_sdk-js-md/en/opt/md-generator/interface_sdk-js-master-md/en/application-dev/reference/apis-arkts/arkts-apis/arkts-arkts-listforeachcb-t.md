# ListForEachCb

```TypeScript
export type ListForEachCb<T> = (value: T, index: number, list: List<T>) => void
```

The type of List callback function.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type ListForEachCb<T> = (value: T, index: int, list: List<T>) => void--><!--Device-unnamed-export type ListForEachCb<T> = (value: T, index: int, list: List<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |
| index | number | Yes |
| list | [List](arkts-arkts-util-list-list-c.md)&lt;T&gt; | Yes |
