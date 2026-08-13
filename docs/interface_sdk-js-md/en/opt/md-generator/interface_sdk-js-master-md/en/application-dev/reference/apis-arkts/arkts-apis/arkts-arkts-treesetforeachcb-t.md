# TreeSetForEachCb

```TypeScript
export type TreeSetForEachCb<T> = (value: T, key: T, set: TreeSet<T>) => void
```

The type of TreeSet callback function.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type TreeSetForEachCb<T> = (value: T, key: T, set: TreeSet<T>) => void--><!--Device-unnamed-export type TreeSetForEachCb<T> = (value: T, key: T, set: TreeSet<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |
| key | T | Yes |
| set | [TreeSet](arkts-arkts-util-treeset-treeset-c.md)&lt;T&gt; | Yes |
