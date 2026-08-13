# ListReplaceCb

```TypeScript
export type ListReplaceCb<T> = (value: T, index: number, list: List<T>) => T
```

The type of List callback function.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type ListReplaceCb<T> = (value: T, index: int, list: List<T>) => T--><!--Device-unnamed-export type ListReplaceCb<T> = (value: T, index: int, list: List<T>) => T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |
| index | number | Yes |
| list | [List](arkts-arkts-util-list-list-c.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |
