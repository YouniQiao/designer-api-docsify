# HashSetCbFn

```TypeScript
export type HashSetCbFn<T> = (value: T, key: T, set: HashSet<T>) => void
```

The type of HashSet callback function.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type HashSetCbFn<T> = (value: T, key: T, set: HashSet<T>) => void--><!--Device-unnamed-export type HashSetCbFn<T> = (value: T, key: T, set: HashSet<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |
| key | T | Yes |
| set | [HashSet](arkts-arkts-util-hashset-hashset-c.md)&lt;T&gt; | Yes |
